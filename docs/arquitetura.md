# Arquitetura técnica

## 1. Objetivo

O `ufsm-mdt` será uma camada de engenharia sobre o modelo LaTeX MDT UFSM 2021: preservar a compatibilidade visual e estrutural do template revisado, mas separar **conteúdo, configuração, regras acadêmicas, implementação LaTeX, validação e automação**.

O projeto não deve substituir o MDT institucional. Ele deve transformar as regras verificáveis do MDT em uma implementação reproduzível e testável.

## 2. O que aprendemos com o template de referência

O template analisado usa uma classe própria, `ufsm_2021.cls`, baseada em `report`, com grande parte da lógica de apresentação concentrada na classe. O arquivo principal `arquivo_2021.tex` funciona como um arquivo de configuração + conteúdo + exemplos.

Características importantes:

- compilação indicada pelo autor com **XeLaTeX**;
- A4 e fonte base de 12 pt;
- opções `oneside`/`twoside` e `openright`;
- geração das páginas pré-textuais por um comando central (`\\pretextual`);
- metadados fornecidos por comandos como `\\centroensino`, `\\curso`, `\\author`, `\\orientador`, `\\titulo`, `\\data`, etc.;
- tipos de trabalho selecionados por comandos como `\\tese`, `\\dissertacao`, `\\tcc`, `\\relatorio`;
- elementos opcionais ativados/desativados por comandos;
- listas específicas para figuras, gráficos, ilustrações, tabelas e quadros;
- ambiente próprio `quadro`;
- comando `\\fonte` para indicar fonte de elementos gráficos;
- citações e referências baseadas em `abntex2cite`/BibTeX;
- suporte a `\\cite`, `\\citeonline`, `\\apud` e `\\apudonline`;
- tratamento específico de folha de rosto, aprovação, ficha catalográfica, errata, resumo, abstract, siglas, abreviaturas e símbolos;
- `tocstyle.sty` auxilia na formatação do sumário/listas;
- o repositório de referência contém também arquivos auxiliares gerados pela compilação, que não devem fazer parte da base limpa do nosso projeto.

A conclusão arquitetural é importante: **não devemos transformar o novo projeto em um único `.tex` gigante**. Devemos manter a classe/layout isolados do conteúdo e tornar a configuração declarativa.

## 3. Arquitetura em camadas

```text
                 +-----------------------------+
                 |       Usuário / Autor       |
                 +--------------+--------------+
                                |
                                v
                 +-----------------------------+
                 |      config/work.yaml       |
                 |   metadados + preferências |
                 +--------------+--------------+
                                |
                 +--------------v--------------+
                 |       Template LaTeX        |
                 | classe + estilos + macros   |
                 +--------------+--------------+
                                |
                                v
                 +-----------------------------+
                 |        Documento.tex        |
                 | pre-textuais + conteúdo     |
                 +--------------+--------------+
                                |
                 +--------------v--------------+
                 |      Pipeline de build      |
                 | XeLaTeX + BibTeX + MakeIndex|
                 +--------------+--------------+
                                |
                                v
                 +-----------------------------+
                 |          trabalho.pdf       |
                 +-----------------------------+

       Paralelamente:

       regras/MDT -> especificações -> validator -> CI -> relatório
```

## 4. Estrutura física proposta

```text
ufsm-mdt/
├── .github/
│   └── workflows/
│       ├── build.yml
│       └── validate.yml
│
├── config/
│   ├── schema.yaml
│   ├── README.md
│   └── examples/
│       ├── tcc.yaml
│       ├── relatorio.yaml
│       └── monografia.yaml
│
├── docs/
│   ├── arquitetura.md
│   ├── especificacao-tecnica.md
│   ├── visao-geral.md
│   ├── roadmap.md
│   ├── fontes.md
│   └── guia-rapido.md
│
├── examples/
│   ├── tcc-minimo/
│   ├── relatorio-minimo/
│   └── monografia-minima/
│
├── scripts/
│   ├── ufsm_mdt/
│   │   ├── config.py
│   │   ├── validate.py
│   │   ├── generate.py
│   │   └── cli.py
│   └── README.md
│
├── template/
│   ├── ufsm_2021.cls
│   ├── tocstyle.sty
│   ├── ufsm-macros.sty
│   └── README.md
│
├── tests/
│   ├── fixtures/
│   ├── test_config.py
│   ├── test_validator.py
│   └── test_generation.py
│
├── Makefile
├── pyproject.toml
├── README.md
├── CONTRIBUTING.md
└── LICENSE.md
```

## 5. Responsabilidade de cada camada

### `template/`

Contém somente a infraestrutura LaTeX necessária para reproduzir a apresentação.

Não deve conter capítulos, texto pessoal ou dados do autor.

Regra: mudanças visuais devem ser feitas aqui, não espalhadas pelos documentos de exemplo.

### `config/`

Contém a representação declarativa dos metadados.

Exemplo:

```yaml
mdt_version: "2021"
document_type: "tcc"
language: "pt-BR"

institution:
  name: "Universidade Federal de Santa Maria"
  center: ""
  center_acronym: ""
  course: ""
  course_level: "Graduação"
  city: "Santa Maria"
  state: "RS"

work:
  title: ""
  subtitle: ""
  english_title: ""
  english_subtitle: ""
  area: ""

author:
  name: ""
  sex: ""
  email: ""

advisor:
  name: ""
  title: ""
  institution: ""
  sex: ""

options:
  dedication: false
  acknowledgements: false
  epigraph: false
  errata: false
  catalog_card: false
  abbreviations: false
  acronyms: false
  symbols: false
```

O formato pode mudar durante a implementação, mas a ideia é manter um contrato estável entre configuração e gerador.

### `examples/`

Cada exemplo deve ser um projeto compilável isolado.

Os exemplos serão nossos **fixtures de integração**: se uma alteração quebrar um TCC mínimo, a CI deve detectar.

### `scripts/`

Responsável por operações que não pertencem ao LaTeX:

- carregar e validar configuração;
- verificar regras estruturais;
- gerar arquivos;
- executar o build;
- produzir relatório de erros/avisos;
- futuramente oferecer CLI.

### `tests/`

Testes unitários e de integração do software.

O PDF também será validado como artefato de integração, mas testes visuais completos serão tratados separadamente.

### `.github/workflows/`

Automação:

1. instalar dependências;
2. validar configuração;
3. compilar exemplos;
4. executar testes Python;
5. executar validador;
6. publicar artefatos de build quando apropriado.

## 6. Separação fundamental: regra x implementação

Toda regra deve existir em três níveis:

```text
MDT / fonte oficial
       |
       v
regra documentada
       |
       v
implementação técnica
       |
       v
teste automatizado
```

Exemplo:

```text
Fonte: MDT 2021, seção/página X
        |
        v
Regra: resumo obrigatório para determinado tipo
        |
        v
Validator: required_when(document_type, "resumo")
        |
        v
Teste: TCC sem resumo => ERROR
```

Isso evita que uma decisão acidental no código seja confundida com uma regra institucional.

## 7. Pipeline de geração

O fluxo pretendido é:

```text
config/*.yaml
     |
     v
schema validation
     |
     v
normalização
     |
     v
gerador
     |
     +----> documento.tex
     |
     +----> arquivos de conteúdo
     |
     v
XeLaTeX
     |
     +----> BibTeX
     |
     +----> XeLaTeX
     |
     +----> MakeIndex, se necessário
     |
     +----> XeLaTeX
     |
     v
PDF
     |
     v
validator pós-build
```

A sequência exata deverá ser confirmada durante a implementação, porque o template de referência mistura recursos LaTeX e ferramentas auxiliares.

## 8. Tipos de validação

### 8.1 Estrutural

Verifica presença/ausência de arquivos e elementos.

Exemplos:

- configuração existe;
- tipo de trabalho é válido;
- autor existe;
- título existe;
- orientador existe quando obrigatório;
- resumo/abstract existem quando obrigatórios.

### 8.2 Configuração

Verifica valores permitidos.

Exemplos:

- sexo com domínio conhecido;
- tipo de trabalho em enumeração;
- campos incompatíveis não preenchidos;
- campos obrigatórios por modalidade.

### 8.3 Conteúdo

Quando tecnicamente possível:

- número de palavras do resumo;
- quantidade mínima de palavras-chave;
- existência de referências citadas;
- referências sem uso;
- figuras sem legenda;
- tabelas/quadros sem fonte quando aplicável.

### 8.4 Build

Verifica:

- compilação sem erro;
- referências resolvidas;
- citações resolvidas;
- arquivos auxiliares esperados;
- ausência de erros LaTeX.

### 8.5 Visual

Não deve ser o primeiro validador.

No futuro, podemos gerar PDF de referência e comparar páginas/renderizações para detectar regressões de layout.

## 9. Contratos técnicos

O projeto deve estabelecer contratos claros:

### Config -> Gerador

Entrada válida segundo `schema.yaml`.

### Gerador -> LaTeX

Arquivos gerados devem ser determinísticos: mesma configuração + mesmo conteúdo = mesma estrutura de saída.

### LaTeX -> PDF

Build deve ser reproduzível com versões de ferramentas registradas.

### Regras -> Validator

Cada regra deve possuir identificador único, severidade, descrição, fonte e teste.

Exemplo conceitual:

```yaml
id: MDT-RESUMO-001
severity: error
source:
  document: "MDT UFSM 2021"
  section: ""
  page: ""
rule: "Resumo obrigatório para TCC."
check: "metadata.summary.required"
```

## 10. Princípios para facilitar o desenvolvimento

1. **Não editar a classe sem necessidade.**
2. **Não colocar regra institucional diretamente no gerador sem documentação.**
3. **Não usar o exemplo completo como base de produção.**
4. **Não versionar arquivos auxiliares de compilação.**
5. **Manter exemplos pequenos e compiláveis.**
6. **Uma regra nova deve ter documentação e teste.**
7. **Uma mudança visual deve ter PDF de comparação quando possível.**
8. **Não acoplar o validator ao LaTeX mais do que o necessário.**
9. **Não depender de Overleaf para CI.**
10. **Registrar versões do MDT, TeX Live e ferramentas de build.**

## 11. Decisões ainda abertas

- versão exata da base LaTeX que será incorporada;
- estratégia de distribuição da classe;
- versão de TeX Live suportada;
- uso de YAML ou TOML como configuração principal;
- geração automática de `.tex` ou template parametrizado;
- escopo do validator na primeira versão;
- estratégia de testes visuais;
- compatibilidade com Overleaf;
- suporte a trabalhos de graduação, pós-graduação, iniciação científica e relatórios;
- política de atualização quando o MDT institucional mudar.
