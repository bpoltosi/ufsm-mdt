# UFSM-MDT

Ferramenta open source em desenvolvimento para facilitar a criação, estruturação, validação e geração de trabalhos acadêmicos conforme o **Manual de Dissertações e Teses da UFSM (MDT 2021)**.

> **Status:** 🟡 Fundação / especificação do núcleo.

## Comece pelo Pages

A interface estática em `site/` é a porta de entrada visual do projeto:

1. **Criar** — abra o [criador guiado](site/creator.html) para selecionar um perfil e montar um documento.
2. **Explorar perfis** — consulte o [catálogo de perfis](site/profiles.html).
3. **Consultar regras** — veja o [catálogo de regras e evidências](site/rules.html).
4. **Desenvolver localmente** — use o núcleo Python para validar e gerar o projeto LaTeX.

O criador do navegador produz o mesmo contrato estrutural usado pelo núcleo (`type`, `metadata`, `sections`, `references` e `assets`). A interface não é a autoridade normativa: a validação oficial do documento permanece no Python.

## Fluxo técnico

```
Pages / criador
    ↓
Documento estruturado (JSON)
    ↓
ufsm-mdt validate
    ↓
ufsm-mdt generate
    ↓
Projeto LaTeX
    ├── compilação local
    └── Overleaf, quando compatível
```

A interface web é deliberadamente estática: não há login, banco de dados ou armazenamento permanente dos trabalhos.

## Desenvolvimento local

Instale o projeto em ambiente Python e consulte a ajuda da CLI:

```bash
python -m ufsm_mdt --help
```

Com um documento JSON:

```bash
python -m ufsm_mdt validate documento.json
python -m ufsm_mdt generate documento.json ./saida
```

Os comandos exatos e opções disponíveis devem ser conferidos na CLI da versão em uso; o README não replica regras do validador.

## Arquitetura resumida

- `src/ufsm_mdt/` — modelo, perfis, validação, geração e CLI.
- `profiles/` — perfis declarativos; a interface web consome uma representação derivada deles.
- `template/upstream/` — base LaTeX versionada quando incorporada ao projeto.
- `docs/mdt/` — documentação normativa e matriz de regras.
- `site/` — GitHub Pages, sem backend.
- `scripts/build_site_data.py` — gera dados derivados para o Pages durante o deploy.

## Estendendo perfis e regras

### Novo perfil

1. Verifique a fonte normativa e registre-a em `docs/mdt/`.
2. Crie ou atualize o JSON correspondente em `profiles/`.
3. Defina somente metadados e comandos respaldados pelo contrato existente.
4. Adicione fixture quando o fluxo do núcleo exigir.
5. Rode a validação/testes locais.
6. Verifique a representação gerada no Pages; `site/data/profiles.json` é artefato de deploy e não deve ser editado manualmente.

### Nova regra

1. Identifique a fonte e o contexto.
2. Diferencie evidência, regra planejada e regra automatizada.
3. Implemente a regra no núcleo Python quando houver contrato verificável.
4. Atualize `docs/mdt/regras.md`.
5. Não copie a regra para JavaScript apenas para reproduzir a validação.

## Contribuição

Consulte [CONTRIBUTING.md](CONTRIBUTING.md). Em especial:

- documentação em português do Brasil;
- fonte explícita para regras institucionais;
- alterações pequenas e verificáveis;
- nenhuma exigência normativa inventada;
- sem dados pessoais ou trabalhos reais;
- validação local antes de abrir PR, para reduzir execuções desnecessárias de Actions.

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