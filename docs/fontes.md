# Fontes e rastreabilidade

## Política

O projeto usa somente fontes diretamente relacionadas ao objeto que estamos implementando.

### Hierarquia

1. **UFSM:** fonte normativa institucional.
2. **Modelo LaTeX publicado/referenciado pela UFSM:** fonte técnica de implementação.
3. **Overleaf:** distribuição do modelo indicada pela UFSM.
4. **GitHub do modelo:** código-fonte e histórico técnico da implementação.

Fontes secundárias não devem substituir essas fontes.

## 1. UFSM — Normas MDT

Página oficial das Bibliotecas UFSM:

https://www.ufsm.br/orgaos-suplementares/biblioteca/mdt

A página identifica a MDT 2021 como o Manual de Dissertações e Teses da UFSM e informa que ela também orienta TCCs de graduação e pós-graduação e trabalhos de iniciação científica. Também informa a obrigatoriedade da versão 2021 a partir de 2022.2.

## 2. UFSM — Normas ABNT/MDT

https://www.ufsm.br/orgaos-suplementares/biblioteca/normas-abnt-mdt

Esta página é especialmente importante para o projeto porque informa que o modelo LaTeX MDT 2021 foi desenvolvido por Eugênio Piveta Pozzobon, atualizado conforme o MDT 2021 e revisado/aprovado por unidades de biblioteca da UFSM.

A própria página disponibiliza:

- código-fonte no GitHub;
- modelo no Overleaf.

## 3. UFSM — notícia de disponibilização

https://www.ufsm.br/?p=61308

A notícia da Biblioteca Central informa que o modelo foi desenvolvido para refletir as mudanças da MDT 2021, foi revisado/aprovado por unidades da Biblioteca e foi disponibilizado tanto no GitHub quanto no Overleaf.

## 4. MDT UFSM 2021 — documento

https://www.ufsm.br/app/uploads/sites/538/2021/12/MDT_UFSM_2021.pdf

Esta é a fonte normativa documental que deve ser usada para extrair regras.

## 5. Repositório técnico do template

https://github.com/Eugenio-Pozzobon/mdt-ufsm-2021-latex

O README do repositório informa duas distribuições do template, uma para desktop e outra para Overleaf. Também documenta a configuração de XeLaTeX e o fluxo XeLaTeX + MakeIndex + BibTeX.

O repositório lista versões do template e descreve alterações feitas em relação à MDT 2015, incluindo mudanças de elementos pré-textuais, referências, listas e ambientes.

## 6. Overleaf — MDT UFSM 2021

https://www.overleaf.com/latex/templates/mdt-ufsm-2021/wbmqyzfngtgv

A página identifica:

- título: MDT UFSM 2021;
- autor: Eugênio Pozzobon;
- licença indicada: Creative Commons CC BY 4.0;
- referência ao GitHub como fonte atualizada;
- observação de que o template foi revisado por bibliotecários da UFSM.

## 7. O que cada fonte pode afirmar

| Fonte | Pode definir regra institucional? | Pode definir implementação? |
|---|---:|---:|
| UFSM / MDT 2021 | Sim | Parcialmente |
| UFSM / Normas ABNT/MDT | Sim | Sim, quando descreve o modelo |
| UFSM / notícia | Contexto e procedência | Sim, para origem/distribuição |
| GitHub do template | Não sozinho | Sim |
| Overleaf do template | Não sozinho | Sim, como distribuição do modelo |

## 8. Regra de rastreabilidade

Uma regra do sistema deve apontar, sempre que possível, para:

- documento;
- versão;
- seção;
- página;
- implementação correspondente;
- teste correspondente.

Se a fonte normativa e a implementação divergirem, isso deve ser registrado como problema/decisão e não resolvido silenciosamente.

## 9. Licenciamento

A distribuição do modelo no Overleaf informa CC BY 4.0. O código do GitHub deve ser verificado arquivo a arquivo antes de redistribuir ou modificar componentes.

O `ufsm-mdt` não deve assumir automaticamente que toda a base do novo projeto possui a mesma licença sem concluir essa verificação.
