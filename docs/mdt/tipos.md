# Tipos de trabalhos — MDT UFSM 2021

## Fonte normativa

A seção 2.2 da MDT UFSM 2021 apresenta como tipos frequentes no contexto da UFSM:

- Monografia;
- Dissertação;
- Tese;
- Artigo científico;
- Material didático;
- Recurso pedagógico;
- Relatório de estágio;
- Relatório técnico-científico;
- Projeto de aplicação, adequação ou inovação tecnológica ou artística (Mestrado profissional).

O manual também descreve especificamente Projeto de Pesquisa e Trabalho de Conclusão de Curso.

### Observação importante

A existência de uma tipologia no manual **não significa automaticamente que ela terá um perfil independente no gerador**. O produto precisa cruzar:

1. tipologia normativa;
2. forma de apresentação exigida;
3. suporte existente no template LaTeX;
4. necessidade real de configuração diferente.

## Tipos descritos pela MDT

| ID | Tipo | Fonte | Perfil independente inicialmente? |
|---|---|---|---|
| MDT-TYPE-001 | Projeto de Pesquisa | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-002 | Trabalho de Conclusão de Curso | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-003 | Relatório de Estágio | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-004 | Dissertação | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-005 | Tese | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-006 | Artigo Científico | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-007 | Relatório Técnico-Científico | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-008 | Monografia | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-009 | Material Didático | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-010 | Recurso Pedagógico | MDT 2021, seção 2.2 | A definir |
| MDT-TYPE-011 | Projeto de aplicação/adequação/inovação | MDT 2021, seção 2.2 | A definir |

## Template LaTeX

O repositório técnico do template possui comandos específicos para diversas modalidades, incluindo:

- tese;
- qualificação;
- dissertação;
- monografia;
- monografia de graduação;
- trabalho final;
- trabalho final de graduação;
- TCC;
- TCC de graduação;
- relatório;
- genérico.

Esses comandos são **evidência técnica do template**, não uma lista normativa independente.

## Regra para o produto

Antes de criar um perfil, devemos responder:

> O tipo possui uma estrutura de apresentação suficientemente distinta para exigir regras/configuração próprias?

Se não, ele pode ser representado como uma variante de um perfil estrutural existente.

## Fonte

MDT UFSM 2021, seção 2.2, especialmente pp. 14–16 do documento eletrônico.

Fonte oficial:
https://www.ufsm.br/app/uploads/sites/538/2021/12/MDT_UFSM_2021.pdf


## Matriz de cruzamento normativa × implementação

| Tipologia normativa MDT | Evidência no template | Identificador técnico no produto | Situação |
|---|---|---|---|
| Projeto de Pesquisa | Não identificado como comando dedicado na classe | `research-project` (proposto) | requer decisão de perfil |
| Trabalho de Conclusão de Curso | `\\tcc`, `\\tccg`, `\\tf`, `\\tfg`, `\\monografia`, `\\monografiag` | `tcc` / variantes estruturais | requer consolidação de perfis |
| Relatório de Estágio | `\\relatorio` | `internship-report` | candidato |
| Dissertação | `\\dissertacao` | `dissertation` | candidato |
| Tese | `\\tese` | `thesis` | candidato |
| Artigo Científico | não há comando dedicado identificado | `article` (proposto) | requer decisão de perfil |
| Relatório Técnico-Científico | `\\relatorio` pode ser tecnicamente reutilizado, mas não prova equivalência normativa | `technical-report` | requer decisão de perfil |
| Monografia | `\\monografia`, `\\monografiag` | `monograph` | candidato |
| Material Didático | não há comando dedicado identificado | `didactic-material` (proposto) | requer decisão de perfil |
| Recurso Pedagógico | não há comando dedicado identificado | `pedagogical-resource` (proposto) | requer decisão de perfil |
| Projeto de aplicação/adequação/inovação | não há comando dedicado identificado | `professional-project` (proposto) | requer decisão de perfil |

### Regra de interpretação

O cruzamento acima não declara que duas tipologias são equivalentes. Ele registra apenas a evidência disponível para orientar a próxima etapa. Um perfil só poderá ser considerado suportado depois de:

1. confirmar a estrutura exigida na MDT;
2. confirmar que o template consegue expressá-la;
3. definir os metadados necessários;
4. criar fixture mínimo;
5. validar e compilar o fixture.


## Implementação dos perfis

Todas as 11 tipologias desta matriz agora possuem perfil declarativo e fixture de integração. Tipologias sem comando dedicado utilizam `generico` para preservar o tipo solicitado sem afirmar equivalência normativa.

| ID | Perfil | Base LaTeX |
|---|---|---|
| MDT-TYPE-001 | `research-project` | `generico` |
| MDT-TYPE-002 | `tcc` | `tcc` |
| MDT-TYPE-003 | `internship-report` | `relatorio` |
| MDT-TYPE-004 | `dissertation` | `dissertacao` |
| MDT-TYPE-005 | `thesis` | `tese` |
| MDT-TYPE-006 | `article` | `generico` |
| MDT-TYPE-007 | `technical-report` | `generico` |
| MDT-TYPE-008 | `monograph` | `monografia` |
| MDT-TYPE-009 | `didactic-material` | `generico` |
| MDT-TYPE-010 | `pedagogical-resource` | `generico` |
| MDT-TYPE-011 | `professional-project` | `generico` |
