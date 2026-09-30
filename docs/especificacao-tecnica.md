# Especificação técnica inicial

## Objetivo

Definir os requisitos que precisam estar estáveis antes da implementação do gerador e do validador.

## Requisitos funcionais

- **RF-01 — Criar trabalho:** iniciar um projeto a partir de um exemplo ou CLI.
- **RF-02 — Metadados:** informar instituição, centro, curso, autor, orientação, título, tipo, datas e demais metadados da modalidade.
- **RF-03 — Pré-textuais:** gerar a estrutura pré-textual compatível com a base MDT adotada, respeitando elementos opcionais.
- **RF-04 — Conteúdo separado:** permitir capítulos/seções em arquivos separados.
- **RF-05 — Referências:** aceitar base `.bib` e preservar o fluxo de citações do template.
- **RF-06 — Elementos gráficos:** suportar figuras, tabelas, quadros, gráficos, ilustrações e indicação de fonte.
- **RF-07 — Build:** fornecer comando único para validar e compilar.
- **RF-08 — Validação:** emitir `ERROR`, `WARNING` e `INFO`.
- **RF-09 — Rastreabilidade:** cada regra automatizada terá ID e referência normativa.
- **RF-10 — CI:** Pull Request que quebra build, testes ou regra `ERROR` deve falhar.

## Requisitos não funcionais

- **RNF-01 — Reprodutibilidade:** mesma entrada deve produzir resultado equivalente.
- **RNF-02 — Portabilidade:** funcionar localmente e no Overleaf quando as dependências forem compatíveis.
- **RNF-03 — Manutenibilidade:** conteúdo, configuração, layout e validação desacoplados.
- **RNF-04 — Testabilidade:** regras importantes testáveis sem compilar um trabalho completo.
- **RNF-05 — Versionamento:** versão do MDT explicitamente registrada.
- **RNF-06 — Transparência:** separar regra institucional de decisão de implementação.
- **RNF-07 — Segurança:** configuração não pode executar comandos arbitrários.

## Dependências previstas

### LaTeX

- TeX Live;
- XeLaTeX;
- BibTeX;
- MakeIndex quando necessário;
- classe `ufsm_2021` ou derivação controlada;
- `tocstyle.sty`/equivalente;
- pacotes exigidos pela classe.

### Python

Python será usado para validação, configuração, geração, testes e CLI.

### GitHub Actions

A CI deverá usar ambiente versionado e registrar a versão do TeX Live.

## Modelo de configuração

```text
document
├── version
├── type
├── language
├── institution
├── work
├── author
├── advisor
├── committee
├── dates
└── options
```

O conteúdo textual longo permanece em arquivos `.tex`, não no YAML/TOML.

## Modelo de regra

```yaml
id: MDT-XXXX-NNN
severity: error | warning | info
source:
  name: "MDT UFSM"
  version: "2021"
  section: ""
  page: ""
description: ""
check: ""
message: ""
```

## Códigos de saída da CLI

- `0`: sucesso;
- `1`: erro de validação;
- `2`: erro de configuração;
- `3`: erro de build;
- `4`: erro interno.

## Primeira versão implementável

Não tentar validar todo o MDT de uma vez:

1. configuração;
2. template LaTeX;
3. TCC mínimo;
4. relatório mínimo;
5. build local;
6. build CI;
7. metadados obrigatórios;
8. resumo/palavras-chave;
9. referências básicas;
10. documentação.

Regras avançadas e validação visual entram incrementalmente.
