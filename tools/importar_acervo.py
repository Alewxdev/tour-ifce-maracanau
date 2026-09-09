#!/usr/bin/env python3
"""Importação retomável do vocabulário do roteiro: Signbank, INES e fontes complementares documentadas.

Uso: python3 tools/importar_acervo.py --catalogos /tmp/acervo-libras --baixar
Os catálogos são JSON de dados, nunca código JavaScript executado.
"""
import argparse
import collections
import concurrent.futures
import json
import re
import shutil
import subprocess
import tempfile
import unicodedata
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'videos/libras/sinais'
INES_PUBLICO = 'http://www.acessibilidadebrasil.org.br/libras_3/public/'


def normalizar(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.upper())
                   if unicodedata.category(c) != 'Mn').strip()


# Homógrafos ou acepções que exigem seleção por contexto, não só pelo nome.
IGNORAR = set('A AS C DA DAS DE DO DOS E EM I LA NA NAS NO NOS O OS PELO PELOS POR UM UMA X'.split())
AMBIGUOS = set('ANDAR ARQUITETURA BANCO CAMPO CHAVE COLA CONTA DADOS DEVER FEIRA FUNCAO INSTANTE JUIZ LACO MEMORIA MODELAR MOVIMENTO PASSAGEM PASSAR PASSO PONTO PRESENTE REPRESENTAR SO FINAL FORMAR TRANCA LIBERAR'.split())
INES_SELECIONADOS = {
    'ACERTAR': 89, 'APONTAR': 472, 'DEVER': 1900,
    'EXERCICIO': 2380, 'EXISTIR': 2386,
    'ANDAR': 360, 'MENOS': 3575, 'QUANDO': 4610, 'QUEM': 4650, 'SO': 5138, 'VEZ': 5703,
    'ACESSO': 91, 'ANTECEDENCIA': 397, 'APARECER': 435, 'ATRAS': 631,
    'CALCULO': 1060, 'CATRACA': 1203, 'CAUDA': 1205, 'COLA': 1392,
    'DEVOLVER': 1904, 'DIZER': 1990, 'DOIS': 2006, 'EDUCACAO': 2051,
    'FICHA': 2521, 'INTERIOR': 3034, 'OBSERVAR': 3842, 'OFICIAL': 3873,
    'OLHAR': 3890, 'PILHA': 4267, 'RECADO': 4738, 'SEM': 5071, 'TESTE': 5328,
}
INES_INCOMPATIVEIS = set('BAIXO BOTAO CHAVE COMPLETO CONSTRUIR LIGAR VARIAVEL DIVISAO ENTRADA FONTE FORCA JUIZ METRO PORTUGUES RECEBER RECOLHER RECONHECER RESERVADO SAIDA VIVA VISITA SALGADO'.split())


def ler_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def salvar(path, data):
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)


def palavras():
    script = (ROOT / 'script.rpy').read_text(encoding='utf-8')
    chars = re.findall(r'^define (\w+) = Character', script, re.M)
    falas = re.findall(r'^\s*(?:' + '|'.join(chars) + r') "((?:[^"\\]|\\.)*)"', script, re.M)
    contagem = collections.Counter()
    for fala in falas:
        fala = re.sub(r'\{[^}]*\}|\[[^]]*\]', '', fala)
        contagem.update(normalizar(w) for w in re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ]+', fala))
    glosas = re.findall(r'^\s+".*?":\s*"([^"]+)",$', (ROOT / 'acessibilidade.rpy').read_text(), re.M)
    return contagem, {normalizar(t) for g in glosas for t in g.split()}, len(falas)


def candidatos(catalogos, necessarios):
    resultado = collections.defaultdict(list)
    for i in ler_json(catalogos / 'signbank.json'):
        url = ((i.get('json') or {}).get('video') or {}).get('url')
        if not url:
            continue
        for nome in {i.get('id_sinais') or '', i.get('sign_lemma') or ''}:
            alvo = normalizar(nome)
            if alvo not in necessarios or alvo in IGNORAR | AMBIGUOS:
                continue
            resultado[alvo].append({
                'glosa': i['id_sinais'], 'id': i['id'], 'fonte': url,
                'credito': 'Signbank da Libras — Universidade Federal de Santa Catarina',
                'licenca': 'CC BY-NC-SA 4.0',
                'acepcao': i.get('traducao_portgues'),
            })
    for entries in resultado.values():
        entries.sort(key=lambda i: ('-' in i['glosa'], i['id']))
    for i in ler_json(catalogos / 'ines.json'):
        alvo = normalizar(i['palavra'])
        selecionado = next((t for t, ident in INES_SELECIONADOS.items() if ident == i['id']), None)
        if selecionado:
            alvo = selecionado
        if (alvo not in necessarios or (alvo in IGNORAR | AMBIGUOS | INES_INCOMPATIVEIS and not selecionado)
                or not i.get('video', '').endswith('.mp4') or not i.get('status')):
            continue
        resultado[alvo].append({
            'glosa': i['palavra'], 'id': i['id'],
            'fonte': INES_PUBLICO + 'media/palavras/videos/' + i['video'],
            'credito': 'Dicionário da Língua Brasileira de Sinais — INES / Acessibilidade Brasil',
            'licenca': 'Não informada no catálogo consultado; não abrangida pela licença UFSC',
            'acepcao': i['descricao'],
        })
    complementares = ROOT / 'tools/dados/fontes_complementares.json'
    if complementares.exists():
        for alvo, entries in ler_json(complementares).items():
            if alvo in necessarios:
                resultado[alvo] = entries + resultado[alvo]
    for alvo, entries in resultado.items():
        resultado[alvo] = list({i['fonte']: i for i in entries}.values())
    return resultado


def baixar(item, ffmpeg):
    token, opcoes = item
    falhas = []
    for dados in opcoes:
        try:
            with tempfile.TemporaryDirectory(prefix='libras-') as temp:
                original = Path(temp) / 'original.mp4'
                webm = Path(temp) / 'sinal.webm'
                url = urllib.parse.quote(dados['fonte'], safe=':/?=&%')
                subprocess.run(['curl', '-fLSs', '--retry', '2', '--max-time', '60', url, '-o', str(original)], check=True, capture_output=True, timeout=190)
                subprocess.run([ffmpeg, '-y', '-v', 'error', '-i', str(original), '-an',
                    '-vf', 'format=yuv444p,scale=400:225:force_original_aspect_ratio=decrease,pad=400:225:(ow-iw)/2:(oh-ih)/2,setsar=1',
                    '-c:v', 'libvpx-vp9', '-threads', '1', '-cpu-used', '4', '-crf', '38', '-b:v', '0', str(webm)], check=True, capture_output=True, timeout=120)
                subprocess.run([ffmpeg, '-v', 'error', '-xerror', '-i', str(webm), '-f', 'null', '-'], check=True, capture_output=True, timeout=60)
                if webm.stat().st_size < 1024:
                    raise ValueError('Vídeo vazio ou pequeno demais')
                destino = OUT / (token.lower().replace(' ', '_') + '.webm')
                shutil.copy2(webm, destino)
            return token, dict(dados, arquivo='videos/libras/sinais/' + destino.name), falhas
        except (subprocess.SubprocessError, OSError, ValueError) as erro:
            stderr = getattr(erro, 'stderr', b'') or b''
            falhas.append({'fonte': dados['fonte'], 'erro': str(erro) + ' ' + stderr.decode(errors='replace')[-400:]})
    return token, None, falhas


def atualizar_catalogos(pasta):
    """Busca todas as páginas anunciadas pela API e extrai JSON estático do INES."""
    pasta.mkdir(parents=True, exist_ok=True)
    def buscar_pagina(numero):
        destino = pasta / f'signbank-{numero}.json'
        subprocess.run(['curl', '-fLSs', '--retry', '2', '--max-time', '40',
            'https://api-signbank.levantelab.com.br/api/tabela_sinais/sinais?page=' + str(numero),
            '-o', str(destino)], check=True)
        return ler_json(destino)
    primeira = buscar_pagina(1)
    sinais = primeira['data']
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for pagina in pool.map(buscar_pagina, range(2, int(primeira['last_page']) + 1)):
            sinais.extend(pagina['data'])
    salvar(pasta / 'signbank.json', sinais)
    destino = pasta / 'ines.js'
    try:
        subprocess.run(['curl', '-fLSs', '--retry', '2', '--max-time', '40',
            INES_PUBLICO + 'site/js/palavras.js', '-o', str(destino)], check=True)
        conteudo = destino.read_text()
        dados = json.loads(conteudo[conteudo.index('['):].strip().rstrip(';'))
        if not isinstance(dados, list):
            raise ValueError('Catálogo INES não é uma lista')
    except (ValueError, subprocess.CalledProcessError):
        # O endereço antigo pode retornar HTML com status 200.
        from coletar_ines_publico import coletar
        contagem, glosas, _ = palavras()
        formas = ler_json(ROOT / 'tools/dados/formas_libras.json')
        equivalencias = ler_json(ROOT / 'tools/dados/equivalencias_contextuais.json')
        alvos = set(contagem) | glosas | {normalizar(k) for k in formas}
        alvos |= {normalizar(v['base']) for v in equivalencias.values()}
        print('Catálogo estático INES indisponível; consultando verbetes públicos.', flush=True)
        coletar(pasta / 'ines.json', alvos)
    else:
        salvar(pasta / 'ines.json', dados)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalogos', type=Path, required=True)
    parser.add_argument('--baixar', action='store_true')
    parser.add_argument('--atualizar-catalogos', action='store_true')
    parser.add_argument('--ffmpeg', default='ffmpeg')
    parser.add_argument('--tokens', nargs='*', help='Restringe o download, mantendo a auditoria completa')
    args = parser.parse_args()
    if args.atualizar_catalogos:
        atualizar_catalogos(args.catalogos)
    manifesto = ler_json(OUT / 'manifesto.json')
    manifesto['nota_licenca'] = 'Licença padrão apenas dos vídeos Signbank/UFSC; consultar credito e licenca de cada fonte alternativa.'
    registros = manifesto['sinais']
    contagem, glosas, n_falas = palavras()
    formas = ler_json(ROOT / 'tools/dados/formas_libras.json')
    arquivo_equivalencias = ROOT / 'tools/dados/equivalencias_contextuais.json'
    equivalencias = ler_json(arquivo_equivalencias) if arquivo_equivalencias.exists() else {}
    alvos = {normalizar(v['base']) for v in equivalencias.values()} | set(contagem) | glosas | {normalizar(k) for k in formas}
    disponiveis = {normalizar(k): v for k, v in registros.items() if (ROOT / v['arquivo']).is_file() and (ROOT / v['arquivo']).stat().st_size > 1024}
    opcoes = candidatos(args.catalogos, alvos - set(disponiveis))
    if args.tokens is not None:
        selecionados = {normalizar(t) for t in args.tokens}
        opcoes = {t: v for t, v in opcoes.items() if t in selecionados}
    salvar(ROOT / 'tools/dados/candidatos_acervo.json', opcoes)
    print(f'{len(opcoes)} termos com vídeos candidatos; {len(disponiveis)} entradas locais.', flush=True)
    if not args.baixar:
        return
    logpath = ROOT / 'tools/dados/resultado_importacao.json'
    log = ler_json(logpath) if logpath.exists() else {'adicionados': {}, 'erros': {}}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futuros = [pool.submit(baixar, item, args.ffmpeg) for item in opcoes.items()]
        for n, futuro in enumerate(concurrent.futures.as_completed(futuros), 1):
            token, dados, erros = futuro.result()
            if dados:
                registros[token] = dados
                disponiveis[token] = dados
                log['adicionados'][token] = dados
                log['erros'].pop(token, None)
            else:
                log['erros'][token] = erros
            salvar(OUT / 'manifesto.json', manifesto)
            salvar(logpath, log)
            print(f'{n}/{len(opcoes)} {token}: {"OK" if dados else "FALHOU"}', flush=True)
    aliases = {}
    for lema, variacoes in formas.items():
        termos = [normalizar(lema)] + [normalizar(t) for t in variacoes.split()]
        base = next((t for t in termos if t in disponiveis), None)
        if not base:
            continue
        for token in termos:
            if token in alvos and token not in disponiveis:
                dados = dict(disponiveis[base], forma_base=base, tipo_correspondencia='forma lexical; não traduz a frase')
                registros[token] = dados
                disponiveis[token] = dados
                aliases[token] = base
    log.setdefault('formas_reutilizadas', {}).update(aliases)
    for token, regra in equivalencias.items():
        token, base = normalizar(token), normalizar(regra['base'])
        if token in alvos and token not in disponiveis and base in disponiveis:
            dados = dict(disponiveis[base], forma_base=base, tipo_correspondencia='equivalência contextual de vocabulário', justificativa=regra['justificativa'])
            registros[token] = disponiveis[token] = dados
            log.setdefault('equivalencias_contextuais', {})[token] = regra
    salvar(logpath, log)
    manifesto['ausentes'] = sorted(glosas - set(disponiveis))
    manifesto['ausentes_roteiro'] = sorted(set(contagem) - set(disponiveis))
    salvar(OUT / 'manifesto.json', manifesto)
    texto = f'# Palavras do roteiro sem correspondência no acervo\n\nAuditoria de {n_falas} falas e narrações: {len(manifesto["ausentes_roteiro"])} formas textuais sem correspondência.\n\nA lista considera também as formas lexicais cadastradas (por exemplo, MÃOS → MÃO). Inclui artigos, preposições, nomes próprios e sentidos ambíguos; não equivale ao número de sinais necessários.\n\n| Forma textual normalizada | Ocorrências |\n| --- | ---: |\n'
    texto += ''.join(f'| {t} | {contagem[t]} |\n' for t in manifesto['ausentes_roteiro'])
    (ROOT / 'PALAVRAS_SEM_VIDEO.md').write_text(texto)
    arquivos = {v['arquivo'] for v in registros.values()}
    relatorio = f"# Importação ampliada do acervo de Libras\n\n{len(log['adicionados'])} vídeos novos, {len(log['formas_reutilizadas'])} formas lexicais reutilizando vídeos e {len(arquivos)} arquivos distintos no acervo.\n\n"
    relatorio += f"Restam {len(manifesto['ausentes_roteiro'])} formas textuais sem correspondência; consulte `PALAVRAS_SEM_VIDEO.md`. Artigos, nomes próprios, flexões não mapeadas e termos ambíguos estão incluídos nesse número.\n\n"
    relatorio += "## Vídeos adicionados\n\n| Termo | Fonte | Arquivo |\n| --- | --- | --- |\n"
    for token, v in sorted(log['adicionados'].items()):
        fonte = v['credito']
        relatorio += f"| {token} | [{fonte}]({v['fonte']}) | {v['arquivo']} |\n"
    relatorio += "\n## Formas que reutilizam vídeos\n\n| Forma | Base |\n| --- | --- |\n"
    relatorio += ''.join(f"| {t} | {b} |\n" for t, b in sorted(log['formas_reutilizadas'].items()))
    relatorio += '\n## Equivalências contextuais de vocabulário\n\nNão são flexões automáticas nem tradução de frases; a justificativa de cada correspondência está no manifesto.\n\n| Palavra | Base | Justificativa |\n| --- | --- | --- |\n'
    relatorio += ''.join(f"| {t} | {v['base']} | {v['justificativa']} |\n" for t, v in sorted(log.get('equivalencias_contextuais', {}).items()))
    relatorio += "\n## Validação e reprodução\n\nTodos os vídeos novos foram convertidos para WebM/VP9 e decodificados integralmente com FFmpeg antes de entrar no manifesto. Não foi feita validação linguística por intérprete nem teste visual dentro do Ren’Py.\n\n"
    relatorio += "As fontes e acepções constam no manifesto. O INES disponibiliza consultas públicas de verbetes em JSON; o importador usa essas consultas quando o catálogo estático antigo não contém dados válidos. Sua licença de reutilização não foi informada no catálogo consultado; a licença CC BY-NC-SA 4.0 refere-se aos vídeos Signbank/UFSC. O Glossário Letras Libras/UFSC é uma fonte separada, com condições registradas por vídeo.\n\n"
    relatorio += "Para atualizar e retomar a importação: `python3 tools/importar_acervo.py --catalogos /tmp/acervo-libras --atualizar-catalogos --baixar --ffmpeg /caminho/ffmpeg`. Downloads concluídos são preservados; falhas ficam em `tools/dados/resultado_importacao.json`.\n"
    (ROOT / 'RELATORIO_IMPORTACAO.md').write_text(relatorio)
    print(f"Concluído: {len(log['adicionados'])} novos vídeos; {len(log['formas_reutilizadas'])} formas reutilizadas; {len(manifesto['ausentes_roteiro'])} formas pendentes.", flush=True)


if __name__ == '__main__':
    main()
