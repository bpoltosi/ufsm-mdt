# Contribuindo

Obrigado por contribuir com o UFSM-MDT.

## Antes de alterar

1. Leia o [README](README.md) e a documentação em `docs/`.
2. Identifique se a mudança é normativa, de núcleo, de template ou de interface.
3. Para requisitos institucionais, registre a fonte antes de automatizar.
4. Prefira a issue/bloco correspondente e mantenha o escopo pequeno.

## Desenvolvimento

### Núcleo

O núcleo Python é a autoridade para o modelo, validação e geração. Alterações em regras devem ser implementadas ali e acompanhadas da documentação de rastreabilidade.

### Perfis

Perfis em `profiles/*.json` são declarativos. Não coloque no JavaScript uma cópia dos requisitos do perfil. O Pages recebe uma representação derivada por `scripts/build_site_data.py`.

### Pages

O site em `site/` é estático e não possui backend. Preserve:

- HTML semântico;
- navegação por teclado;
- foco visível;
- responsividade;
- dependências mínimas;
- identidade visual minimalista;
- ausência de regras normativas duplicadas.

Quando possível, valide HTML/CSS/JS localmente antes do PR. O workflow do Pages gera dados derivados durante o deploy; não edite `site/data/profiles.json` manualmente.

## Regras e evidências

Não trate uma regra como oficial sem indicar sua fonte. Diferencie explicitamente:

- **evidência** — informação documentada na fonte;
- **planejada** — candidata a automação ainda não implementada;
- **automatizada** — regra implementada e verificável pelo núcleo.

Se a evidência for insuficiente, documente a lacuna em vez de inventar uma exigência.

## Pull Requests

Use uma branch por bloco e, quando possível, um único PR por etapa. O PR deve informar:

- objetivo;
- arquivos principais alterados;
- validações executadas;
- impactos no Pages, núcleo ou template;
- eventuais limitações ou bloqueios.

Evite pushes exploratórios e execuções desnecessárias de GitHub Actions.

## Dados

Não inclua dados pessoais, documentos acadêmicos reais, credenciais ou materiais que não possam ser redistribuídos. Fixtures devem usar dados fictícios.

## Licenciamento

Não incorpore arquivos de terceiros sem verificar sua licença e registrar a origem.

## Idioma

A documentação do projeto deve permanecer em português do Brasil, mantendo nomes técnicos e comandos originais quando necessário.

Fluxo sugerido: **branch → alteração → validação local → Pull Request → revisão → merge**.