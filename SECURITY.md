# Política de segurança

## Escopo

Este repositório contém código-fonte, automações de CI e uma base LaTeX incorporada.

## Reporte

Não publique segredos, tokens, credenciais ou detalhes exploráveis em issue pública. Use o mecanismo de Private vulnerability reporting / Security Advisories do GitHub quando disponível; caso contrário, contate o mantenedor por canal privado.

## Regras

1. Nunca armazenar segredos no Git.
2. Nunca imprimir tokens ou credenciais nos logs do Actions.
3. Workflows devem declarar o menor conjunto possível de `permissions`.
4. Não usar `pull_request_target` para executar código do PR.
5. Fixar ações de terceiros por SHA completo e registrar a versão em comentário.
6. Dependências devem ser atualizadas por PR revisável.
7. Artefatos temporários devem ter retenção curta.
8. PDF para usuário só deve ser gerado sob solicitação.
9. Alterações em `.github/`, `src/`, `profiles/` e `template/` exigem revisão do mantenedor.
10. Não usar secrets em jobs que executem conteúdo não confiável.

## Proteção de main

A branch `main` deve exigir PR, checks obrigatórios, revisão antes do merge, resolução de conversas e bloquear push direto. Essas são configurações administrativas do GitHub e precisam ser habilitadas nas configurações do repositório.
