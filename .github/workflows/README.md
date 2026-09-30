# GitHub Actions

A CI validará tanto o software quanto os documentos de exemplo.

## Pipeline

1. checkout;
2. instalar Python;
3. instalar TeX Live compatível;
4. instalar dependências;
5. testes unitários;
6. validar configurações;
7. compilar exemplos;
8. executar validador;
9. armazenar PDFs/logs como artefatos quando útil.

## Regras

- erro de build => falha;
- teste quebrado => falha;
- regra `ERROR` => falha;
- `WARNING` não bloqueia por padrão;
- registrar versão do TeX Live.

A CI valida tecnicamente o projeto; não representa aprovação institucional da UFSM.
