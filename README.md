# UFSM-MDT

Ferramenta open source em desenvolvimento para facilitar a criação, organização, formatação e validação técnica de trabalhos acadêmicos baseados nas diretrizes do Manual de Dissertações e Teses (MDT) da Universidade Federal de Santa Maria (UFSM).

> **Status:** 🟡 Fundação do projeto.

## Objetivo

Reduzir o trabalho manual necessário para iniciar e manter trabalhos acadêmicos da UFSM, oferecendo uma estrutura versionável, documentada e preparada para automação.

O projeto pretende evoluir de um template LaTeX organizado para uma ferramenta capaz de centralizar metadados, estruturar documentos, facilitar a compilação, verificar regras técnicas e integrar validações ao GitHub Actions.

## Estrutura

- `template/` — base LaTeX
- `config/` — metadados e configurações
- `examples/` — exemplos mínimos
- `scripts/` — automação e validação
- `docs/` — documentação, arquitetura, fontes e roadmap
- `.github/workflows/` — futura integração contínua

## Fluxo planejado

1. Iniciar um trabalho a partir do template.
2. Preencher os dados básicos.
3. Escrever o conteúdo.
4. Compilar localmente ou no Overleaf.
5. Executar as validações.
6. Corrigir erros e avisos.
7. Manter o histórico com Git.

## Importante

O projeto não substitui o MDT, regulamentos, editais ou orientação de professores da UFSM. Regras institucionais deverão ser verificadas contra fontes oficiais e registradas com sua versão/data. Uma validação automatizada não será tratada como aprovação institucional.

## Documentação

- [Visão geral](docs/visao-geral.md)
- [Arquitetura](docs/arquitetura.md)
- [Fontes e referências](docs/fontes.md)
- [Roadmap](docs/roadmap.md)
- [Contribuição](CONTRIBUTING.md)

## Tecnologias previstas

LaTeX · Python · Git/GitHub · GitHub Actions · Overleaf

## Licença

A licença definitiva será definida após a verificação das licenças das fontes e templates utilizados.

## Autor

Desenvolvido por [bpoltosi](https://github.com/bpoltosi).
