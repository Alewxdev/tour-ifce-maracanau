#!/usr/bin/env python3
"""Baixa sinais públicos do Signbank e converte para WebM/VP9."""

import argparse
import concurrent.futures
import json
import re
import ssl
import subprocess
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api-signbank.levantelab.com.br/api/tabela_sinais/sinais"
SOURCE = Path(__file__).resolve().parents[1] / "acessibilidade.rpy"
SCRIPT = Path(__file__).resolve().parents[1] / "script.rpy"
OUTPUT = Path(__file__).resolve().parents[1] / "videos" / "libras" / "sinais"
CERTIFICATE = Path(__file__).resolve().parents[1] / "certs" / "cacert.pem"
SSL_CONTEXT = ssl.create_default_context(cafile=str(CERTIFICATE))


def sem_acento(texto):
    return "".join(
        c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn"
    ).upper()


def limpar_token(token):
    token = re.sub(r"\[[^]]+\]", "", token).strip()
    token = token.split("&", 1)[0]
    token = re.sub(r"^[123][SP]_", "", token)
    token = re.sub(r"_[123][SP]$", "", token)
    token = token.replace("_", " ")
    return token.strip(" .,!?;:")


def tokens_do_cache():
    conteudo = SOURCE.read_text(encoding="utf-8")
    glosas = re.findall(r'^\s+".*?":\s*"([A-ZÁÉÍÓÚÂÊÔÃÕÇ0-9_& \[\]]+)",$', conteudo, re.M)
    tokens = {
        limpar_token(alternativa)
        for glosa in glosas
        for bruto in glosa.split()
        for alternativa in bruto.split("&")
        if limpar_token(alternativa)
    }

    roteiro = SCRIPT.read_text(encoding="utf-8")
    falas = re.findall(r'^\s*[ejm] "([^"]+)"', roteiro, re.M)
    for fala in falas:
        for palavra in re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", fala):
            if len(palavra) > 2:
                tokens.add(palavra.upper())

    return sorted(tokens)


def buscar_sinal(token):
    query = urllib.parse.urlencode(
        {"page": 1, "search": token.lower(), "search_type": "general"}
    )
    req = urllib.request.Request(
        API + "?" + query,
        headers={
            "User-Agent": "IFCE-Jogo-Libras/1.0",
            "Accept": "application/json",
            "Referer": "https://signbank.libras.ufsc.br/pt/",
        },
    )
    with urllib.request.urlopen(req, timeout=30, context=SSL_CONTEXT) as resposta:
        itens = json.load(resposta).get("data", [])

    alvo = sem_acento(token)
    for item in itens:
        candidatos = [item.get("id_sinais", ""), item.get("sign_lemma", "")]
        if alvo in {sem_acento(c) for c in candidatos}:
            return item
    return None


def baixar(url, destino):
    url = urllib.parse.quote(url, safe=":/?=&%")
    subprocess.run(
        [
            "curl", "-fL", "--retry", "2", "--max-time", "120",
            "-A", "IFCE-Jogo-Libras/1.0", "-o", str(destino), url,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ffmpeg", required=True)
    parser.add_argument("--tokens", nargs="*", help="Importa somente os sinais informados")
    args = parser.parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    manifesto = {}
    ausentes = []

    tokens = sorted(set(args.tokens)) if args.tokens else tokens_do_cache()

    manifesto_anterior = OUTPUT / "manifesto.json"
    if manifesto_anterior.exists():
        try:
            manifesto.update(
                json.loads(manifesto_anterior.read_text(encoding="utf-8")).get("sinais", {})
            )
        except Exception:
            pass

    def importar(item_numerado):
        numero, token = item_numerado
        slug = sem_acento(token).lower().replace(" ", "_")
        webm = OUTPUT / (slug + ".webm")
        print(f"[{numero}] {token}", flush=True)
        try:
            item = buscar_sinal(token)
            video = ((item or {}).get("json") or {}).get("video") or {}
            url = video.get("url")
            if not url:
                return token, None, None

            if not webm.exists() or webm.stat().st_size < 1024:
                temporario = OUTPUT / (slug + ".mp4")
                baixar(url, temporario)
                subprocess.run(
                    [
                        args.ffmpeg, "-y", "-loglevel", "error", "-i", str(temporario),
                        "-an", "-vf", "scale=400:225,setsar=1",
                        "-c:v", "libvpx-vp9", "-crf", "38", "-b:v", "0", str(webm),
                    ],
                    check=True,
                )
                temporario.unlink(missing_ok=True)

            dados_sinal = {
                "arquivo": "videos/libras/sinais/" + webm.name,
                "fonte": url,
                "id": item.get("id"),
                "glosa": item.get("id_sinais"),
            }
            return token, dados_sinal, None
        except Exception as erro:
            print(f"  ERRO: {erro}", flush=True)
            return token, None, str(erro)

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for token, dados_sinal, erro in executor.map(
            importar, enumerate(tokens, 1)
        ):
            if dados_sinal:
                manifesto[token] = dados_sinal
            else:
                ausentes.append(token)

    dados = {
        "licenca": "CC BY-NC-SA 4.0",
        "credito": "Signbank da Libras — Universidade Federal de Santa Catarina",
        "url": "https://signbank.libras.ufsc.br/pt",
        "sinais": manifesto,
        "ausentes": sorted(set(ausentes)),
    }
    (OUTPUT / "manifesto.json").write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Prontos: {len(manifesto)} | Ausentes: {len(set(ausentes))}")


if __name__ == "__main__":
    main()
