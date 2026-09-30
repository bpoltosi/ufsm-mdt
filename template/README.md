# Template LaTeX

Esta pasta contém a infraestrutura de composição do documento.

## Base analisada

A referência é o modelo **MDT UFSM 2021** desenvolvido por Eugênio Pozzobon e disponibilizado no GitHub/Overleaf, cuja adoção é indicada pelo portal da UFSM.

Arquivos relevantes:

- `ufsm_2021.cls`: classe principal;
- `tocstyle.sty`: suporte ao sumário;
- arquivo `.tex`: exemplo/configuração;
- `.bib`: referências;
- figuras de exemplo.

## Não colocar aqui

- capítulos de trabalhos reais;
- dados pessoais;
- PDFs gerados;
- `.aux`, `.log`, `.toc`, `.bbl`, `.bcf`, `.synctex.gz` ou equivalentes.

## Incorporação

Antes de copiar/modificar a classe:

1. registrar versão/commit de origem;
2. registrar licença indicada pela distribuição;
3. registrar diferenças introduzidas;
4. preservar atribuição;
5. criar teste de compilação;
6. evitar mudanças visuais sem regra ou justificativa documentada.

## Estratégia

Não reescrever a classe do zero.

```text
template de referência
        ↓
base limpa
        ↓
TCC mínimo
        ↓
build reproduzível
        ↓
testes
        ↓
refatoração incremental
```

Só considerar substituições internas depois de existir cobertura suficiente.
