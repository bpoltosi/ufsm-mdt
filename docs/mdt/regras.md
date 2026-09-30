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


## Mapeamento normativo inicial — MDT 2021

A leitura direta do documento oficial permite fixar alguns pontos de rastreabilidade antes de automatizar regras:

| ID | Evidência normativa | Localização | Tratamento no produto |
|---|---|---|---|
| MDT-SCOPE-001 | O manual define um padrão institucional de apresentação e esclarece que não determina a qualidade ou o teor científico do texto; regulamentos de curso/PPG também devem ser observados. | §1, pp. 10–11 | Não automatizar qualidade/conteúdo científico. |
| MDT-LANG-001 | Português é a língua oficial para trabalhos de conclusão; outros idiomas podem ser usados quando previstos em Regimento do Curso/Programa. A versão final deve conter título, resumo e palavras-chave em português. | §2, pp. 12–13 | Planejada; depende de metadado sobre idioma/regulamento. |
| MDT-TYPE-001 | A seção 2.2 lista, entre as tipologias frequentes, monografia, dissertação, tese, artigo científico, material didático, recurso pedagógico, relatório de estágio, relatório técnico-científico e projeto de aplicação/adequação/inovação. | §2.2, p. 14 | Já refletida em `docs/mdt/tipos.md`; não implica equivalência entre perfis. |
| MDT-RESEARCH-001 | Projeto de Pesquisa segue a NBR 15287 vigente; cada PPG pode determinar modelo de apresentação/estrutura se aprovado e regulamentado. | §2.2, p. 15 | Não impor estrutura institucional global sem configuração do PPG. |
| MDT-PRE-001 | A estrutura do manual identifica folha de rosto, ficha catalográfica, folha de aprovação, resumo em língua vernácula, resumo em língua estrangeira e sumário como obrigatórios; errata, dedicatória, agradecimentos, epígrafe e listas são opcionais no escopo geral descrito. | §3.2, pp. 25–47 | Planejada; a obrigatoriedade precisa ser cruzada com o contexto/tipologia antes de virar regra de perfil. |
| MDT-MARGIN-001 | O manual possui seção específica para configuração geral de margens. | §3.2.12, p. 47 | Planejada; extrair parâmetros e verificar se o template já os garante. |
| MDT-CIT-001 | O manual dedica seção própria a citações diretas, indiretas, citação de citação, regras gerais e sistemas autor-data/numérico. | §4.2, pp. 56–68 | Planejada; exige modelagem da referência/citação antes da validação. |
| MDT-GRAPHIC-001 | O manual trata equações/fórmulas, ilustrações, quadros e tabelas em seções próprias. | §4.3–4.5, pp. 69–72 | Planejada; validação deve operar sobre elementos estruturados, não sobre texto LaTeX arbitrário. |
| MDT-POST-001 | O manual define apêndice e anexo como elementos pós-textuais e mantém referências em seção própria. | §5–6, pp. 74–114 | Planejada; mapear cardinalidade/ordem por contexto antes de automatizar. |

> **Fonte primária:** Universidade Federal de Santa Maria, *Manual de Dissertações e Teses da UFSM: Estrutura e Apresentação Documental para Trabalhos Acadêmicos*, Santa Maria, 2021. PDF oficial consultado em 30/09/2026. A numeração de páginas acima segue a paginação impressa indicada no próprio manual.

### Regra de interpretação

Esses itens são um **mapa de evidências**, não uma lista de novas exigências já ativadas. Antes de transformar qualquer item em ERROR/WARNING, devemos cruzar a norma com a tipologia, o regulamento aplicável e a capacidade do template de representar a informação.
