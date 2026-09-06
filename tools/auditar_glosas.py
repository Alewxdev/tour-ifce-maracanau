#!/usr/bin/env python3
"""Lista glossas pedagógicas sem arquivo local; não confunde falas com glossas."""
import argparse
import json
import re
import unicodedata
from pathlib import Path


def normalizar(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto.upper())
                   if unicodedata.category(c) != 'Mn')


def auditar(root, roteiro=False):
    manifesto = json.loads((root / 'videos/libras/sinais/manifesto.json').read_text())
    source = (root / 'acessibilidade.rpy').read_text()
    glosas = re.findall(r'^\s+".*?":\s*"([^"]+)",$', source, re.M)
    necessarios = {normalizar(t) for g in glosas for t in g.split()}
    if roteiro:
        texto = (root / 'script.rpy').read_text()
        personagens = re.findall(r'^define (\w+) = Character', texto, re.M)
        falas = re.findall(r'^\s*(?:' + '|'.join(personagens) + r') "((?:[^"\\]|\\.)*)"', texto, re.M)
        necessarios = {
            normalizar(t) for fala in falas
            for t in re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ]+', re.sub(r'\{[^}]*\}|\[[^]]*\]', '', fala))
        }
    disponiveis = {normalizar(t) for t, v in manifesto['sinais'].items()
                   if (root / v['arquivo']).is_file()
                   and (root / v['arquivo']).stat().st_size > 1024}
    return sorted(necessarios - disponiveis)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--roteiro', action='store_true', help='Confere todas as falas e narrações')
    args = parser.parse_args()
    print(json.dumps(auditar(Path(__file__).resolve().parents[1], args.roteiro), ensure_ascii=False, indent=2))
