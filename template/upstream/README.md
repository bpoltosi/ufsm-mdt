# Base LaTeX MDT UFSM 2021

## Proveniência

- Repositório de origem: https://github.com/Eugenio-Pozzobon/mdt-ufsm-2021-latex
- Snapshot upstream inspecionado: `3be37b6bb04d1561423aa95619bc9c37632cf1b3`
- O README upstream identifica o template como MDT UFSM 2021 e documenta o uso de XeLaTeX; também registra versões históricas 1.0.0, 1.0.1, 1.1.0, 1.1.1 e 1.1.2.
- A classe atualmente incorporada em `template/upstream/ufsm_2021.cls` declara `ver. 1.1.1`.

## Arquivos incorporados

Somente os arquivos necessários ao gerador atualmente estão versionados nesta pasta:

- `ufsm_2021.cls`
- `tocstyle.sty`

Arquivos auxiliares de compilação (`.aux`, `.log`, `.pdf`, `.toc`, `.synctex`, entre outros) não fazem parte da base incorporada.

## Compilador e dependências

A documentação upstream orienta XeLaTeX. A classe depende de pacotes do ecossistema LaTeX/abnTeX2, além de `tocstyle.sty` incorporado localmente.

A versão exata do TeX Live compatível com a base deste projeto ainda precisa ser fixada por teste reprodutível.

## Licenciamento

**Pendente de verificação.** Não foi localizado um arquivo `LICENSE` no repositório upstream consultado. Os cabeçalhos dos arquivos incorporados identificam autoria/origem, mas isso não constitui por si só uma licença de redistribuição.

Por esse motivo, esta documentação registra a proveniência sem declarar uma licença para os arquivos upstream. A incorporação definitiva e qualquer relicenciamento dependem de confirmação apropriada.

## Critério de fechamento

Antes de fechar a tarefa de consolidação, é necessário:

1. confirmar a permissão/licença para redistribuir os dois arquivos;
2. executar uma compilação mínima com XeLaTeX em ambiente suportado;
3. verificar o fluxo de referências;
4. registrar a versão do ambiente utilizado.
