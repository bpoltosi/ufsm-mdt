# Blocos de construção do projeto

Este documento transforma as decisões do projeto em blocos independentes de implementação.

## Visão geral

```text
[1] Fontes e regras
       ↓
[2] Perfis de trabalho
       ↓
[3] Modelo interno
       ↓
[4] Template LaTeX
       ↓
[5] Gerador
       ↓
[6] Validador
       ↓
[7] Testes
       ↓
[8] Interface
       ↓
[9] PDF sob demanda
```

A ordem é intencional: primeiro definimos o que o documento deve ser; depois construímos a interface.

---

## Bloco 1 — Fontes e rastreabilidade

**Objetivo:** estabelecer uma base confiável para todas as decisões do sistema.

### Fontes aceitas

1. UFSM — página oficial de Normas MDT.
2. UFSM — página oficial de Normas ABNT/MDT.
3. MDT UFSM 2021 publicado pela UFSM.
4. Modelo LaTeX publicado pela UFSM e seu repositório GitHub.
5. Modelo MDT UFSM 2021 publicado no Overleaf e apontado pela UFSM.

Não usar blogs, tutoriais aleatórios, fóruns ou templates não relacionados como autoridade normativa.

### Entregáveis

- catálogo de fontes;
- versão da fonte;
- seção/página;
- regra extraída;
- grau de certeza;
- eventual ambiguidade.

---

## Bloco 2 — Catálogo de tipos de trabalho

**Objetivo:** descobrir quais tipos realmente precisam ser suportados.

O template de referência possui comandos para vários tipos, incluindo tese, qualificação, dissertação, monografia, trabalho final, TCC, relatório e tipo genérico.

Isso é um indício técnico, não uma autorização automática de escopo.

### Entregáveis

Uma matriz:

| ID | Tipo | Comando do template | Abrangência no MDT | Suportado pelo produto | Observação |
|---|---|---|---|---|---|
| TYPE-001 | Tese | `\\tese` | a confirmar | não definido | |
| TYPE-002 | Qualificação | `\\qualificacao` | a confirmar | não definido | |
| TYPE-003 | Dissertação | `\\dissertacao` | a confirmar | não definido | |
| TYPE-004 | Monografia | `\\monografia` | a confirmar | não definido | |
| TYPE-005 | Monografia graduação | `\\monografiag` | a confirmar | não definido | |
| TYPE-006 | Trabalho Final | `\\tf` | a confirmar | não definido | |
| TYPE-007 | Trabalho Final de Graduação | `\\tfg` | a confirmar | não definido | |
| TYPE-008 | TCC | `\\tcc` | a confirmar | não definido | |
| TYPE-009 | TCC graduação | `\\tccg` | a confirmar | não definido | |
| TYPE-010 | Relatório | `\\relatorio` | a confirmar | não definido | |
| TYPE-011 | Genérico | `\\generico` | a confirmar | não definido | |

---

## Bloco 3 — Perfis e estrutura dos documentos

**Objetivo:** transformar cada tipo em uma especificação declarativa.

Cada perfil deverá definir:

- metadados obrigatórios;
- elementos pré-textuais;
- elementos textuais;
- elementos pós-textuais;
- elementos opcionais;
- regras específicas;
- comandos necessários do template.

Saída esperada:

```text
document-types/
├── tese.yaml
├── qualificacao.yaml
├── dissertacao.yaml
├── monografia.yaml
├── tcc.yaml
├── relatorio.yaml
└── ...
```

Os nomes finais só serão criados após o Bloco 2.

---

## Bloco 4 — Modelo interno

**Objetivo:** representar o trabalho sem depender diretamente de LaTeX.

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

O modelo deve ser suficiente para representar todos os perfis suportados sem criar campos específicos de LaTeX quando isso não for necessário.

---

## Bloco 5 — Template LaTeX

**Objetivo:** incorporar e organizar a implementação de referência sem perder sua compatibilidade.

Componentes observados no repositório de referência:

- `ufsm_2021.cls`;
- `tocstyle.sty`;
- arquivo principal de exemplo;
- arquivos de apoio do template.

O repositório de referência informa uso de XeLaTeX e apresenta configuração específica para Overleaf e compiladores desktop.

### Entregáveis

- base incorporada;
- origem registrada;
- versão/commit registrado;
- arquivos auxiliares separados;
- documentação de compilação.

---

## Bloco 6 — Gerador

**Objetivo:** converter o modelo interno em projeto LaTeX.

Entrada:

```text
Document
```

Saída:

```text
project/
├── main.tex
├── template/
├── content/
├── references.bib
└── assets/
```

O gerador não deve decidir regras acadêmicas. Ele deve executar o perfil e a estrutura já definidos.

---

## Bloco 7 — Validador

**Objetivo:** detectar problemas objetivos antes ou depois da geração.

Categorias:

- configuração;
- estrutura;
- conteúdo;
- referências;
- elementos gráficos;
- build.

Resultado:

```text
ERROR
WARNING
INFO
```

Cada regra deve ser rastreável.

---

## Bloco 8 — Testes

**Objetivo:** impedir regressões.

Cada tipo suportado deverá ter pelo menos:

1. fixture mínimo;
2. geração;
3. build;
4. validação;
5. verificação dos arquivos esperados.

A validação visual será tratada separadamente e de forma incremental.

---

## Bloco 9 — Interface web

**Objetivo:** tornar o gerador utilizável sem transformar o projeto em uma plataforma complexa.

Fluxo mínimo:

```text
Escolher tipo
   ↓
Preencher dados
   ↓
Escrever conteúdo
   ↓
Validar
   ↓
Baixar projeto
        ou
   ↓
Solicitar PDF
```

A interface é consumidora do núcleo; não deve conter as regras do MDT espalhadas pelo código.

---

## Bloco 10 — PDF sob demanda

**Objetivo:** oferecer compilação online somente quando solicitada.

Fluxo:

```text
Usuário solicita PDF
       ↓
Workflow GitHub Actions
       ↓
Build
       ↓
Validação
       ↓
PDF
       ↓
Download
```

Não haverá build online automático para cada alteração do usuário.

---

## Bloco 11 — Distribuição e documentação

**Objetivo:** permitir que o projeto seja utilizado de forma independente.

Entregáveis:

- README;
- guia local;
- guia Overleaf;
- exemplos;
- instruções de compilação;
- registro de versão do MDT;
- registro das fontes;
- limitações conhecidas.

---

## Relação entre blocos

| Bloco | Depende de | Produz |
|---|---|---|
| Fontes | MDT/UFSM/template | regras documentadas |
| Tipos | Fontes + template | catálogo de tipos |
| Perfis | Tipos + MDT | especificações |
| Modelo | Perfis | contrato interno |
| Template | Fonte técnica | base LaTeX |
| Gerador | Modelo + Perfis + Template | projeto LaTeX |
| Validador | Perfis + Regras | relatório |
| Testes | Todos os anteriores | garantia de regressão |
| Interface | Modelo + Gerador + Validador | UX |
| PDF online | Gerador + build | PDF |
| Documentação | Todos | uso e manutenção |

## Regra de dependência

Nenhum bloco posterior deve inventar regras que deveriam ter sido definidas em blocos anteriores.

Exemplo:

```text
Interface NÃO define:
"resumo é obrigatório"

Perfil/regra define isso.
Interface apenas apresenta a informação.
```
