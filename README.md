# UFSM-MDT

Ferramenta open source em desenvolvimento para facilitar a criação, estruturação, validação e geração de trabalhos acadêmicos conforme o **Manual de Dissertações e Teses da UFSM (MDT 2021)**.

> **Status:** 🟡 Fundação / especificação do núcleo.

## Objetivo

O foco do projeto é **gerar corretamente os diferentes tipos de trabalhos acadêmicos suportados**, preservando a implementação LaTeX do modelo MDT UFSM 2021 e transformando regras verificáveis do manual em validações automatizadas.

O projeto não substitui o MDT, regulamentos, editais ou orientação de professores da UFSM.

## Fluxo planejado

```
Escolher tipo
    ↓
Preencher dados e conteúdo
    ↓
Validar
    ↓
Gerar projeto LaTeX
    ├── baixar e compilar manualmente
    └── solicitar PDF online
              ↓
       GitHub Actions
```

A compilação online é opcional. O usuário sempre deverá poder baixar o projeto LaTeX e compilá-lo localmente ou no Overleaf, quando as dependências forem compatíveis.

## Escopo inicial

O projeto **não** terá inicialmente:

- VM ou backend permanente;
- banco de dados;
- contas de usuários;
- colaboração;
- IA;
- editor visual complexo;
- importação de PDF;
- armazenamento permanente dos trabalhos.

A prioridade é a correção do gerador e das regras do MDT.

## Documentação

- [Decisões do projeto](docs/decisoes.md)
- [Blocos de construção](docs/blocos.md)
- [Arquitetura](docs/arquitetura.md)
- [Especificação técnica](docs/especificacao-tecnica.md)
- [Fontes e rastreabilidade](docs/fontes.md)
- [Roadmap](docs/roadmap.md)
- [Documentação geral](docs/README.md)

## Fontes principais

- UFSM — Normas MDT: https://www.ufsm.br/orgaos-suplementares/biblioteca/mdt
- UFSM — Normas ABNT/MDT: https://www.ufsm.br/orgaos-suplementares/biblioteca/normas-abnt-mdt
- MDT UFSM 2021: https://www.ufsm.br/app/uploads/sites/538/2021/12/MDT_UFSM_2021.pdf
- Template LaTeX: https://github.com/Eugenio-Pozzobon/mdt-ufsm-2021-latex
- Template Overleaf: https://www.overleaf.com/latex/templates/mdt-ufsm-2021/wbmqyzfngtgv

## Tecnologias

O núcleo está implementado em Python e mantém o modelo de documento independente da apresentação. A base LaTeX incorporada usa XeLaTeX. GitHub Actions é o ambiente oficial de testes e build controlado. O PDF para usuário é compilado somente sob solicitação explícita.

## Licença

A licença definitiva do `ufsm-mdt` será definida após a verificação das licenças dos componentes incorporados.

## Autor

Desenvolvido por [bpoltosi](https://github.com/bpoltosi).
