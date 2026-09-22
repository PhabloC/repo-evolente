# Handoff Task 719

- Slice: `tasks/slices/002-autenticacao.md`
- Status final: done
- Decisão: sessão permanece no SecureStore em Android/iOS; no web, onde o módulo não é implementado, fica somente em memória para permitir o login sem gravar tokens em localStorage/AsyncStorage. Durante o boot nativo, uma falha de validação protegida dispara refresh explícito antes de limpar a sessão, e o papel retornado pelo refresh é validado antes de persistir/retornar.
- Contexto usado: contrato `/auth/refresh`, segurança mobile, authService, SecureStore, AppGate, apiClient e testes relacionados.
- Arquivos alterados: `mobile/src/features/auth/services/authService.ts`, `mobile/src/features/auth/services/authService.test.ts`, `mobile/src/shared/storage/secureStorage.ts`, `mobile/src/shared/storage/secureStorage.test.ts` e rastreabilidade da Task 719.
- Validações: testes direcionados do storage e auth passaram 7/7 cada; ESLint dos arquivos alterados e `git -C mobile diff --check` passaram; typecheck permanece bloqueado por erros preexistentes fora do storage/auth.
- Pendência: validar reabertura após expiração do access token em dispositivo real.
- Próximo contexto: teste manual de persistência e refresh no app instalado.
