# Tipos de trabalhos — MDT UFSM 2021

## Implementação

Todas as 11 tipologias catalogadas estão representadas por perfis declarativos em `profiles/`.

| ID | Tipo | Perfil | Comando/base |
|---|---|---|---|
| MDT-TYPE-001 | Projeto de Pesquisa | `research-project` | `generico` |
| MDT-TYPE-002 | Trabalho de Conclusão de Curso | `tcc` | `tcc` |
| MDT-TYPE-003 | Relatório de Estágio | `internship-report` | `relatorio` |
| MDT-TYPE-004 | Dissertação | `dissertation` | `dissertacao` |
| MDT-TYPE-005 | Tese | `thesis` | `tese` |
| MDT-TYPE-006 | Artigo Científico | `article` | `generico` |
| MDT-TYPE-007 | Relatório Técnico-Científico | `technical-report` | `generico` |
| MDT-TYPE-008 | Monografia | `monograph` | `monografia` |
| MDT-TYPE-009 | Material Didático | `didactic-material` | `generico` |
| MDT-TYPE-010 | Recurso Pedagógico | `pedagogical-resource` | `generico` |
| MDT-TYPE-011 | Projeto de aplicação/adequação/inovação | `professional-project` | `generico` |

### Interpretação

A implementação técnica não transforma automaticamente `generico` em equivalência normativa. Nesses casos, o perfil preserva a tipologia do catálogo e permite que a aplicação apresente os campos específicos do tipo.

O projeto seguirá a regra de completude: quando a MDT não exigir determinado elemento, ele pode ser omitido pelo usuário; quando houver informação útil e suportada pelo modelo, a interface deve favorecer o preenchimento completo.

### Fonte

MDT UFSM 2021, seção 2.2, pp. 14–16 do documento eletrônico.
