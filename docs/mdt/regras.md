# Catálogo de regras automatizáveis — MDT UFSM 2021

> Status: catálogo inicial. Regras marcadas como **automatizada** já possuem implementação no validador; regras **planejada** foram identificadas na fonte, mas ainda não devem ser aplicadas automaticamente.

## Princípios

1. Toda regra automatizada deve possuir um identificador estável.
2. Toda regra deve indicar a fonte normativa e a versão da MDT.
3. A ausência de uma regra no catálogo não autoriza o validador a inferi-la.
4. Quando a MDT delegar a definição ao curso/PPG/orientador, a regra não será transformada em exigência institucional global sem fonte adicional.
5. Severidades: ERROR, WARNING e INFO.

## Regras atualmente automatizadas

| ID | Categoria | Severidade | Regra | Implementação | Fonte |
|---|---|---|---|---|---|
| `MDT-CONFIG-<FIELD>` | configuração | ERROR | Cada campo listado em `required_metadata` do perfil deve estar preenchido. | `src/ufsm_mdt/validator.py` | Perfil do tipo; referência normativa do perfil: MDT 2021 §2.2 |
| `MDT-STRUCT-001` | estrutura | WARNING | A ausência de seções textuais é sinalizada; o gerador cria uma estrutura mínima para permitir a execução técnica. | `src/ufsm_mdt/validator.py` | Regra operacional do produto; não é apresentada como exigência normativa |
| `MDT-REF-001` | referências | INFO | A ausência de referências é informada; o gerador cria um registro bibliográfico mínimo para permitir o build técnico. | `src/ufsm_mdt/validator.py` | Regra operacional do produto; não é apresentada como exigência normativa |

### Sobre `MDT-CONFIG-<FIELD>`

O identificador é parametrizado pelo nome do campo, por exemplo `MDT-CONFIG-AUTHOR`. A lista efetiva de campos pertence ao perfil declarativo. Isso evita duplicar a lista de metadados no validador.

Os perfis atuais apontam para a MDT UFSM 2021, seção 2.2, para a identificação da tipologia. A existência do tipo no manual não significa que todos os metadados usados pelo template sejam, individualmente, requisitos normativos universais. Portanto, nesta fase, o catálogo distingue a origem do perfil da origem de cada exigência de campo.

## Regras identificadas e ainda não automatizadas

| ID proposto | Categoria | Situação | Fonte |
|---|---|---|---|
| `MDT-FORMAT-001` | formatação | validar margens, tipografia e demais parâmetros somente após mapear a seção normativa correspondente e confirmar a representação no template | MDT 2021; Anexo Q contém exemplos explícitos de margens e tipografia |
| `MDT-PRE-001` | pré-textuais | mapear ordem e obrigatoriedade por tipologia antes de automatizar | MDT 2021; estrutura documental |
| `MDT-SUMMARY-001` | resumos | mapear requisitos de resumo/abstract e palavras-chave por tipo | MDT 2021 |
| `MDT-CIT-001` | citações | mapear regras de citação e referências com a versão normativa aplicável | MDT 2021 / ABNT referenciada pelo manual |
| `MDT-GRAPHIC-001` | elementos gráficos | mapear figuras, tabelas, quadros, fórmulas e respectivas fontes | MDT 2021 |
| `MDT-POST-001` | pós-textuais | mapear referências, glossário, apêndices e anexos por contexto | MDT 2021 |

## Limites normativos importantes

A UFSM informa que a MDT 2021 passou a ser a versão obrigatória a partir de 2022.2. A página oficial também descreve a MDT como abrangendo trabalhos de conclusão e outras produções acadêmicas.

Para Projeto de Pesquisa, o próprio manual registra que a estrutura e apresentação são descritas pela NBR 15287 e que cada PPG pode determinar seu modelo, desde que aprovado e regulamentado. Portanto, não devemos criar uma regra institucional rígida apenas a partir da existência do tipo na MDT.

## Próxima etapa

1. mapear cada regra diretamente para seção/página da MDT;
2. separar regras universais de regras dependentes da tipologia;
3. separar regras institucionais de decisões do curso/PPG;
4. verificar se o template `ufsm_2021.cls` expõe a informação necessária para validação;
5. criar teste positivo e negativo para cada regra automatizada;
6. só então promover regras planejadas para execução no validador.

## Fontes primárias

- UFSM — MDT 2021
- UFSM — página oficial das Normas MDT
- UFSM — página oficial Normas ABNT/MDT e referência ao modelo LaTeX 2021
