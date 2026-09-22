# Handoff Task 719

- Slice: `tasks/slices/002-autenticacao.md`
- Status final: done
- Decisão: sessão permanece no SecureStore; durante o boot, uma falha de validação protegida dispara refresh explícito antes de limpar a sessão.
- Contexto usado: contrato `/auth/refresh`, segurança mobile, authService, SecureStore, AppGate, apiClient e testes relacionados.
- Arquivos alterados: `mobile/src/features/auth/services/authService.ts`, `mobile/src/features/auth/services/authService.test.ts`, `mobile/src/shared/storage/secureStorage.ts` e rastreabilidade da Task 719.
- Validações: 12 testes direcionados passaram e `git -C mobile diff --check` passou.
- Pendência: validar reabertura após expiração do access token em dispositivo real.
- Próximo contexto: teste manual de persistência e refresh no app instalado.
