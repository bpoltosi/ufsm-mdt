# Especificação técnica

## Objetivo

Definir os contratos técnicos mínimos do `ufsm-mdt` sem antecipar funcionalidades que não são necessárias ao núcleo do projeto.

## Escopo da primeira versão

A primeira versão deve:

1. suportar tipos de trabalho definidos após o mapeamento do MDT 2021;
2. representar os dados e a estrutura desses tipos;
3. gerar projetos LaTeX;
4. validar regras objetivas;
5. permitir compilação local/Overleaf;
6. oferecer PDF online apenas sob solicitação;
7. manter rastreabilidade entre regra, implementação e teste.

## Fora do escopo inicial

- contas;
- banco de dados;
- colaboração;
- armazenamento permanente;
- IA;
- importação de PDF;
- editor visual complexo;
- backend permanente;
- VM;
- microserviços.

## Requisitos funcionais

- **RF-01 — Selecionar tipo:** selecionar um perfil de trabalho suportado.
- **RF-02 — Metadados:** preencher os campos definidos pelo perfil.
- **RF-03 — Estrutura:** criar os elementos previstos pelo perfil.
- **RF-04 — Conteúdo:** escrever/organizar o conteúdo do trabalho.
- **RF-05 — Referências:** utilizar referências conforme o fluxo suportado pelo template.
- **RF-06 — Elementos gráficos:** representar os elementos gráficos suportados pelo perfil/template.
- **RF-07 — Validar:** executar regras aplicáveis ao perfil.
- **RF-08 — Gerar projeto:** produzir um projeto LaTeX completo.
- **RF-09 — Download:** permitir baixar o projeto para compilação manual.
- **RF-10 — PDF sob demanda:** permitir solicitar a compilação online somente quando desejado.
- **RF-11 — Rastreabilidade:** cada regra automatizada possui ID e fonte.
- **RF-12 — Testabilidade:** cada tipo suportado possui fixture de integração.

## Requisitos não funcionais

- **RNF-01 — Reprodutibilidade:** mesma entrada deve gerar estrutura equivalente.
- **RNF-02 — Portabilidade:** projeto gerado deve ser utilizável localmente e, quando compatível, no Overleaf.
- **RNF-03 — Manutenibilidade:** regras, perfis, conteúdo e apresentação desacoplados.
- **RNF-04 — Testabilidade:** regras devem ser testáveis independentemente do PDF sempre que possível.
- **RNF-05 — Versionamento:** versão do MDT usada pelo projeto deve ser explícita.
- **RNF-06 — Transparência:** decisão institucional e decisão de implementação devem ser diferenciadas.
- **RNF-07 — Segurança:** arquivos/configuração não devem permitir execução arbitrária pelo gerador.
- **RNF-08 — Independência:** a compilação online é conveniência, não requisito para utilização do projeto.

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

## Severidades

- **ERROR:** impede considerar o documento validado segundo aquela regra.
- **WARNING:** problema ou situação que merece revisão, mas não necessariamente impede a geração.
- **INFO:** informação ou observação.

Essas severidades são do sistema e não representam classificação oficial da UFSM.

## Saídas

### Projeto

```text
project/
├── main.tex
├── template/
├── content/
├── references.bib
├── assets/
└── README.md
```

### Validação

```text
ERROR
WARNING
INFO
```

### PDF

Gerado apenas quando solicitado.

## Ambiente de build

O ambiente de compilação deverá ser versionado/documentado.

A implementação de referência indica XeLaTeX como compilador principal e menciona BibTeX/MakeIndex no fluxo desktop. O ambiente definitivo do projeto será estabelecido em uma issue própria após os testes do template.
