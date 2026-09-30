# Fontes e referências

## 1. Fonte normativa principal

**Universidade Federal de Santa Maria — Manual de Dissertações e Teses da UFSM: Estrutura e Apresentação Documental para Trabalhos Acadêmicos — 2021.**

A página oficial de Normas MDT informa que a MDT 2021 passou a ser obrigatória para os trabalhos a partir de 2022.2 e que o manual também orienta TCCs, trabalhos de pós-graduação e iniciação científica.

## 2. Modelo LaTeX adotado como referência

**Eugênio Piveta Pozzobon — mdt-ufsm-2021-latex.**

O portal da UFSM informa que o modelo foi desenvolvido por Eugênio Piveta Pozzobon, atualizado conforme a MDT 2021 e revisado/aprovado por unidades de biblioteca da UFSM.

## 3. Overleaf

O modelo **MDT UFSM 2021** está publicado no Overleaf com autoria de Eugênio Pozzobon. A página informa **Creative Commons CC BY 4.0** e aponta o GitHub como fonte atualizada.

O GitHub analisado não possui arquivo LICENSE explícito. Portanto, antes de redistribuir arquivos derivados, devemos registrar origem, atribuição e licença indicada pela distribuição.

## 4. Implementação técnica observada

A referência utiliza:

- `ufsm_2021.cls`;
- `report` como classe base;
- `abntex2cite` para citações;
- BibTeX com `abntex2-alf`;
- `babel` em português;
- `fontenc`;
- `setspace`;
- `hyperref`;
- `caption`;
- `tocloft`;
- `tocstyle.sty`;
- comandos e ambientes próprios da MDT.

O README recomenda XeLaTeX e, no desktop, XeLaTeX + MakeIndex + BibTeX.

## 5. Rastreabilidade

Cada regra implementada deve registrar:

| Campo | Obrigatório |
|---|---|
| ID | Sim |
| Fonte | Sim |
| Versão | Sim |
| Seção/página | Sim, quando disponível |
| Descrição | Sim |
| Implementação | Sim |
| Teste | Sim |
| Data da verificação | Sim |
| Ambiguidade | Quando aplicável |

## 6. Papel de cada fonte

- **UFSM:** regra institucional.
- **Overleaf:** publicação/distribuição do modelo.
- **GitHub:** implementação concreta do modelo.

O código do template não deve ser tratado sozinho como fonte normativa.
