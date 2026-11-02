# UFSM-MDT

Ferramenta open source em desenvolvimento para estruturar, validar e gerar documentos acadêmicos com base nas diretrizes do **Manual de Dissertações e Teses da Universidade Federal de Santa Maria (MDT/UFSM 2021)**.

> O projeto é independente e não representa aprovação ou certificação institucional da UFSM. Regras automatizadas devem estar vinculadas a fontes documentadas.

## O que existe no repositório

- Núcleo Python para modelar documentos, listar perfis, validar dados e gerar projetos LaTeX.
- Perfis declarativos para diferentes tipos de documentos acadêmicos.
- Fixtures e testes automatizados.
- Template LaTeX incorporado.
- Interface web estática em GitHub Pages para explorar perfis, regras e montar documentos estruturados.
- Documentação de arquitetura, decisões, regras, fontes e roadmap.
- Workflows GitHub Actions para testes, geração de artefatos e publicação do site.

## Fluxo geral

```text
Interface web ou JSON
        ↓
Documento estruturado
        ↓
Validação pelo núcleo Python
        ↓
Geração de projeto LaTeX
        ↓
Compilação pelo ambiente escolhido
```

A interface do navegador não substitui o validador Python, que é a autoridade técnica do projeto. O site é estático e não mantém contas ou armazenamento permanente de trabalhos.

## Estrutura

- `src/ufsm_mdt/` — modelo, perfis, validador, gerador e CLI.
- `profiles/` — perfis de documentos.
- `template/` — base LaTeX e referência upstream.
- `site/` — interface web estática.
- `docs/` — especificação, arquitetura, regras e decisões.
- `tests/` — testes e documentos de fixture.
- `scripts/` — geração de dados derivados para o site.

## Requisitos

- Python 3.11 ou superior.
- XeLaTeX/TeX Live quando for necessário compilar os arquivos LaTeX gerados.

O pacote Python não declara dependências de runtime externas na configuração atual.

## Instalação e comandos

Na raiz do repositório:

```bash
python -m pip install -e .
ufsm-mdt --help
ufsm-mdt types
ufsm-mdt validate documento.json
ufsm-mdt generate documento.json ./saida
```

Também é possível utilizar `python -m ufsm_mdt` se o pacote estiver disponível no ambiente.

## Testes

```bash
python -m pytest
```

Consulte os workflows e a documentação de contribuição para as verificações específicas de cada alteração.

## Fontes e contribuição

As regras devem ser sustentadas por fontes institucionais identificadas em `docs/fontes.md` e `docs/mdt/`. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) antes de propor alterações.

## Status

Projeto em desenvolvimento. Consulte [docs/roadmap.md](docs/roadmap.md) e [docs/visao-geral.md](docs/visao-geral.md) para escopo e evolução.