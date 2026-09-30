# Snapshot técnico do template MDT UFSM 2021

## Referência adotada

- Repositório: `Eugenio-Pozzobon/mdt-ufsm-2021-latex`
- Branch observada: `main`
- Commit observado em 2026-09-30: `3be37b6bb04d1561423aa95619bc9c37632cf1b3`
- Classe principal: `ufsm_2021.cls`
- SHA do blob observado na branch `main`: `716baf9f12990ceb82b798ee5e995e6cf3d4c85c`
- Arquivo de apoio: `tocstyle.sty`
- SHA do blob observado: `617ce686fd27a061bc42fe108812e23375c69465`
- Exemplo principal: `arquivo_2021.tex`
- SHA do blob observado: `35bc0cf9258bf52be58e34dfb73330074088d109`
- Referências de exemplo: `referencias.bib`
- SHA do blob observado: `5ffab8e237538ba12bd9be1198800882e481bb39`

## Versão declarada pelo próprio template

O README do repositório declara a classe como versão 1.1.1 no cabeçalho de `ufsm_2021.cls`, enquanto o histórico do projeto registra a versão 1.1.2 como a alteração de numeração das páginas de início de capítulo. Por isso, o projeto não tratará o número de versão isoladamente como identidade suficiente: a identidade reprodutível será o commit fixado.

## Capacidades técnicas observadas

A classe de referência expõe comandos específicos para:

- tese;
- exame de qualificação;
- dissertação;
- monografia;
- monografia de graduação;
- trabalho final;
- trabalho final de graduação;
- TCC;
- TCC de graduação;
- relatório;
- tipo genérico configurável.

A classe também define estruturas para listas, resumo/abstract, ficha catalográfica, errata, banca/orientação, referências e ambientes de tabela, quadro, gráfico e ilustração.

## Compilação declarada pelo repositório

O README do template orienta:

- XeLaTeX no TeXstudio;
- XeLaTeX + MakeIndex + BibTeX no TeXworks;
- XeLaTeX no Overleaf;
- o fluxo Overleaf documentado pelo repositório menciona TeX Live 2020 (legacy).

Isso é evidência de compatibilidade histórica, não uma decisão definitiva do ambiente do `ufsm-mdt`. O ambiente do novo projeto será fixado somente após teste reproduzível.

## Higienização necessária

O repositório upstream contém artefatos gerados de compilação (por exemplo `.aux`, `.log`, `.pdf`, `.synctex.gz`, `.bcf`, `.blg`, `.bbl`, `.run.xml`). Esses artefatos não devem ser incorporados como parte da base do produto.

Também existe conteúdo de exemplo e um arquivo `backup2015.zip`; nenhum desses itens deve ser tratado automaticamente como componente do produto.

## Licença

A distribuição no Overleaf informa CC BY 4.0. Antes de redistribuir/modificar a base dentro do `ufsm-mdt`, a licença e os avisos de cada componente efetivamente incorporado devem ser verificados e preservados.

## Regra de manutenção

O `ufsm-mdt` deve registrar:

1. commit upstream utilizado;
2. hashes dos arquivos incorporados;
3. alterações locais;
4. versão do ambiente de compilação;
5. teste de compilação associado.

Atualizações do upstream não devem ser aplicadas silenciosamente.
