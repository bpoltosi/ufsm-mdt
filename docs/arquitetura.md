# Arquitetura técnica implementada

## Camadas

```text
Perfis JSON / fontes
        ↓
Modelo interno (Document)
        ↓
Gerador Python
        ↓
Projeto LaTeX independente
        ↓
UFSM 2021 class + tocstyle
        ↓
XeLaTeX/latexmk no GitHub Actions
```

A interface futura consumirá o mesmo núcleo; regras acadêmicas não devem ser duplicadas na interface.

## Tipologias

As 11 tipologias documentadas em `docs/mdt/tipos.md` estão implementadas como perfis:

- `research-project`
- `tcc`
- `internship-report`
- `dissertation`
- `thesis`
- `article`
- `technical-report`
- `monograph`
- `didactic-material`
- `pedagogical-resource`
- `professional-project`

Quando a classe upstream possui comando próprio, o perfil o utiliza. Para tipologias sem comando dedicado, o perfil usa `generico` e fornece seus metadados de tipo. Isso resolve a representação técnica sem declarar equivalência normativa automática.

## Princípio de completude

A UX pode informar que um campo ou elemento é opcional, mas a configuração padrão deve privilegiar o trabalho mais completo quando a informação estiver disponível e isso não contradizer a MDT. O sistema não deve remover elementos apenas para simplificar a interface.

## Build

- Testes Python: GitHub Actions em push/PR.
- Compilação das fixtures: workflow manual.
- PDF para usuário: workflow manual, somente sob solicitação.
- Engine: XeLaTeX via `latexmk`.
- TeX Live: 2026 no CI atual; o número é explícito e deve ser atualizado de forma controlada.

## Rastreabilidade

O template incorporado mantém o commit upstream `3be37b6bb04d1561423aa95619bc9c37632cf1b3`. Cada perfil aponta para a seção 2.2 da MDT como fonte normativa, enquanto o comando LaTeX é tratado como evidência técnica.
