#!/usr/bin/env python3
"""Consulta somente verbetes públicos da API SENAI Libras, sem autenticação."""
import argparse
import json
import subprocess
from pathlib import Path

QUERY = '''query($cursor: String) {
  sinals(first: 100, after: $cursor) {
    totalCount
    edges { node { _id titulo descricao descricaoMovimento isVideo
      arquivos { edges { node { caminho } } }
      areaTecnologica { _id nome }
    } }
    pageInfo { endCursor hasNextPage }
  }
}'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--saida', type=Path, required=True)
    args = parser.parse_args()
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    items, cursor = [], None
    while True:
        body = json.dumps({'query': QUERY, 'variables': {'cursor': cursor}})
        proc = subprocess.run(['curl', '-fLSs', '--retry', '2', '--max-time', '40',
            '-H', 'Content-Type: application/json', '--data-binary', '@-',
            'https://api-senai-libras.senai.br/graphql'], input=body,
            check=True, text=True, capture_output=True)
        response = json.loads(proc.stdout)
        if response.get('errors'):
            raise ValueError(response['errors'])
        page = response['data']['sinals']
        items.extend(row['node'] for row in page['edges'])
        print(f"{len(items)}/{page['totalCount']}", flush=True)
        if not page['pageInfo']['hasNextPage']:
            break
        next_cursor = page['pageInfo']['endCursor']
        if next_cursor == cursor:
            raise ValueError('Cursor repetido na API')
        cursor = next_cursor
    args.saida.write_text(json.dumps(items, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
