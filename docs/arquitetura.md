# Arquitetura proposta

ufsm-mdt/
- .github/workflows/
- docs/
- examples/
- scripts/
- template/
- config/
- README.md

## Camadas

Template: implementação LaTeX e arquivos do documento.

Configuração: metadados do trabalho.

Exemplos: trabalhos mínimos sem dados pessoais.

Scripts: validação, geração e automação.

CI: compilação e validações automatizadas.

Princípio central: separar regra acadêmica de detalhe técnico. Cada regra implementada deve ser rastreável à sua fonte.