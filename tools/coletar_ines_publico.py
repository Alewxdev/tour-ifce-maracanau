#!/usr/bin/env python3
"""Consulta somente dados públicos do INES/Acessibilidade Brasil, sem executar JS."""
import argparse
import concurrent.futures
import json
import re
import string
import subprocess
import unicodedata
from pathlib import Path

BASE = 'http://www.acessibilidadebrasil.org.br/libras_3/'


def normalizar(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto.upper())
                   if unicodedata.category(c) != 'Mn')


def buscar(caminho):
    resultado = subprocess.run(['curl', '-fLSs', '--retry', '2', '--max-time', '30',
                               BASE + caminho], check=True, capture_output=True, text=True)
    dados = json.loads(resultado.stdout)
    if not dados.get('success'):
        raise ValueError('Consulta sem sucesso: ' + caminho)
    return dados['data']


def coletar(saida, alvos):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        paginas = list(pool.map(lambda letra: buscar('ajax/getWordsByLetter/' + letra), string.ascii_uppercase))
    indice = {int(i['id']): i for pagina in paginas for i in pagina}
    selecionados = [ident for ident, i in indice.items()
                   if normalizar(re.sub(r'\d+$', '', i['palavra'])) in alvos]
    registros = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for dados in pool.map(lambda ident: buscar('ajax/getWordById/' + str(ident)), selecionados):
            if not isinstance(dados, dict):
                print('Verbete público sem dados; ignorado.', flush=True)
                continue
            dados['id'] = int(dados['id'])
            dados['descricao'] = dados['acepcao']
            dados['status'] = bool(dados.get('video'))
            registros.append(dados)
    saida.parent.mkdir(parents=True, exist_ok=True)
    temporario = saida.with_suffix('.tmp')
    temporario.write_text(json.dumps(registros, ensure_ascii=False, indent=2) + '\n')
    temporario.replace(saida)
    print(f'{len(indice)} verbetes indexados; {len(registros)} acepções consultadas.', flush=True)
    return registros


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--saida', type=Path, required=True)
    parser.add_argument('--alvos', type=Path, required=True, help='JSON com lista de termos normalizados')
    args = parser.parse_args()
    coletar(args.saida, set(json.loads(args.alvos.read_text())))
