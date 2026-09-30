# Arquitetura técnica

## 1. Objetivo

O `ufsm-mdt` será um **gerador e validador de trabalhos acadêmicos baseado no MDT UFSM 2021**.

A arquitetura deve preservar a apresentação do modelo LaTeX de referência e, ao mesmo tempo, separar:

- fontes e regras;
- perfis de tipos de trabalho;
- modelo interno;
- conteúdo;
- template LaTeX;
- geração;
- validação;
- testes;
- interface;
- compilação online opcional.

A arquitetura foi deliberadamente simplificada: **não haverá VM, backend permanente, banco de dados ou microserviços na primeira versão**.

## 2. Fluxo principal

```text
Fontes oficiais
      ↓
Regras documentadas
      ↓
Perfil do trabalho
      ↓
Modelo interno
      ↓
Gerador
      ↓
Projeto LaTeX
      ├──────────────→ Download / compilação local / Overleaf
      │
      └──────────────→ PDF sob demanda via GitHub Actions
```

A validação acompanha o fluxo:

```text
Modelo interno
      ↓
Validador
      ↓
ERROR / WARNING / INFO
```

## 3. Princípio fundamental

O sistema não deve tentar descobrir a regra acadêmica na interface ou no gerador.

A cadeia é:

```text
MDT/UFSM
   ↓
regra documentada
   ↓
perfil
   ↓
implementação
   ↓
teste
```

## 4. Fontes técnicas utilizadas

A UFSM disponibiliza o modelo LaTeX MDT 2021 e aponta tanto o GitHub quanto o Overleaf como formas de acesso ao modelo. O Overleaf identifica o template como `MDT UFSM 2021`, autoria de Eugênio Pozzobon, e informa CC BY 4.0.

O repositório técnico informa:

- existência de uma implementação para desktop e outra para Overleaf;
- uso de XeLaTeX;
- configuração de XeLaTeX + MakeIndex + BibTeX em uma das rotinas desktop;
- necessidade de selecionar XeLaTeX no Overleaf;
- versão de TeX Live 2020 (legacy) no fluxo descrito pelo repositório.

Essas informações são referência de compatibilidade; a versão definitiva do ambiente do `ufsm-mdt` deverá ser registrada e testada separadamente.

## 5. Camadas

### 5.1 Fontes e regras

Documenta o MDT e transforma requisitos verificáveis em regras rastreáveis.

### 5.2 Perfis

Representa cada tipo de trabalho suportado.

### 5.3 Modelo interno

Representa o trabalho sem depender diretamente da sintaxe LaTeX.

### 5.4 Template

Contém a implementação LaTeX de apresentação.

### 5.5 Gerador

Converte o modelo interno em um projeto LaTeX.

### 5.6 Validador

Executa regras objetivas e produz relatório.

### 5.7 Testes

Testa perfis, geração, build e regras.

### 5.8 Interface

Permite criar/preencher/validar/baixar o projeto.

### 5.9 Build online

Executa somente quando o usuário solicita um PDF.

## 6. Modelo interno

Modelo conceitual:

```text
Document
├── type
├── metadata
├── pretextual
├── textual
├── posttextual
├── references
└── assets
```

O modelo não deve conter detalhes de apresentação que pertençam ao template.

## 7. Geração

```text
Document
   ↓
perfil do tipo
   ↓
gerador
   ↓
main.tex + conteúdo + referências + assets
   ↓
template MDT
```

A saída deve ser um projeto independente o suficiente para compilação local ou no Overleaf, respeitando as dependências e licenças utilizadas.

## 8. Compilação online

A compilação online é opcional.

```text
Usuário
  ↓
"Gerar PDF"
  ↓
GitHub Actions
  ↓
ambiente de build
  ↓
XeLaTeX / ferramentas auxiliares
  ↓
PDF
```

Não haverá workflow obrigatório para cada edição.

## 9. O que não faz parte da primeira arquitetura

- VM;
- backend 24/7;
- banco de dados;
- contas de usuários;
- armazenamento permanente de documentos;
- colaboração;
- IA;
- editor visual semelhante a Word;
- importação de PDF;
- microserviços;
- filas distribuídas.

## 10. Critério de sucesso arquitetural

A arquitetura será considerada adequada quando conseguirmos:

1. selecionar um tipo suportado;
2. representar seus metadados e estrutura;
3. gerar um projeto LaTeX;
4. compilar o projeto;
5. validar regras objetivas;
6. baixar o projeto;
7. solicitar o PDF online somente quando desejado;
8. reproduzir o resultado sem depender da aplicação web.
