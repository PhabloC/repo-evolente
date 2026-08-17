# Handoff - Task 387

## Task

- identificador: 387
- título: Preservar renovação de token no download de relatórios mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao

## Decisões preservadas

- `refreshAccessToken` virou exportação pública do `apiClient` para que o download reaproveite o mesmo refresh single-flight do interceptor de 401 em vez de duplicar a lógica
- o download de relatório continua usando `downloadAsync` (streaming direto para o arquivo) e trata o 401 manualmente, com uma única retentativa
- status HTTP fora de 2xx passa a ser erro explícito, e o arquivo gravado nesse caso é descartado antes de qualquer tentativa de abertura
- mensagens diferenciadas para sessão expirada, 403 e 404; demais status usam mensagem genérica com sugestão de nova tentativa

## Contexto utilizado

- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/shared/network/apiClient.ts`
- `mobile/src/shared/network/createAppError.ts`

## Arquivos alterados

- serviço de relatórios, teste do serviço, `apiClient`, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npm run lint`
- `cd mobile && npm run test`

## Pendências ou bloqueios

- erros preexistentes de typecheck no app mobile (`MemoryGameRenderer`, `TrailActivityScreen`) seguem fora do escopo

## Próximo contexto recomendado

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`, se a tela precisar diferenciar visualmente o erro de sessão expirada
