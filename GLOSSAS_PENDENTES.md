# Cobertura das glossas e do roteiro

A auditoria inicial verificava apenas as glossas pedagógicas cadastradas em
`acessibilidade.rpy`. Essa verificação permanece separada da auditoria completa
das falas e narrações.

As glossas cadastradas ainda sem correspondência são **FINAL** e **MOVIMENTO**.
Isso não significa que sejam as únicas palavras sem vídeo no roteiro.

A lista completa e atualizada está em [PALAVRAS_SEM_VIDEO.md](PALAVRAS_SEM_VIDEO.md).
Os vídeos adicionados, fontes e formas reutilizadas estão em
[RELATORIO_IMPORTACAO.md](RELATORIO_IMPORTACAO.md).

Para conferir offline:

```sh
python3 tools/auditar_glosas.py
python3 tools/auditar_glosas.py --roteiro
```

Não foram substituídos termos por homônimos incompatíveis: FINAL de campeonato,
MOVIMENTO de pessoas, ANDAR no sentido de caminhar (o roteiro usa pavimento),
BANCO financeiro para banco de dados, ou LIGAR ao telefone para conexão entre
conceitos. As correspondências por forma lexical estão documentadas em
`tools/dados/formas_libras.json` e no campo `forma_base` do manifesto.
