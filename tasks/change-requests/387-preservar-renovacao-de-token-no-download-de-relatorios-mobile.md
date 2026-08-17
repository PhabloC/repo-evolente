# Task 387 - Preservar renovação de token no download de relatórios mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1reports~1{reportId}~1download/get`

## Modo de execução

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referência visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

correção funcional sem mudança de UI

### Fonte primaria visual

- não se aplica

## Objetivo

Fazer o download de relatórios do responsável respeitar o mesmo fluxo de refresh de token usado pelo `apiClient` e validar o status HTTP antes de abrir o arquivo baixado.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Download autenticado | `mobile/src/features/reports/services/reportsService.ts` | corrigir o fluxo de token e a validação de status | sim |
| Fluxo de refresh | `mobile/src/shared/network/apiClient.ts` | reaproveitar o refresh single-flight já existente | sim |
| Tratamento de erro | `mobile/src/shared/network/createAppError.ts` | confirmar como a mensagem chega na tela | não |

## Orçamento de contexto

- baixo
- estratégia: manter a mudança no serviço de relatórios e na exportação do refresh do cliente HTTP

## Critérios de conclusão

- [x] download com token expirado tenta renovar a sessão antes de falhar
- [x] status HTTP não-2xx deixa de ser tratado como download bem-sucedido
- [x] arquivo parcial/erro é descartado em vez de ser aberto
- [x] `npm run lint` executado
- [x] `npm run test` executado

## Origem

- comentário de code review (`P1 ALTO`) apontando que `downloadAsync` usava o token antigo e ignorava o interceptor de 401/refresh do `apiClient`

## Resultado da execucao

- `refreshAccessToken` passou a ser exportado pelo `apiClient`, preservando o refresh single-flight e a limpeza de sessão já usados pelo interceptor de 401
- `reportsService.downloadAndOpen` passou a delegar o download para `downloadReportFile`, que renova o token e repete a requisição uma vez quando a API responde 401
- o status HTTP do download passou a ser validado antes de abrir o arquivo, com mensagens específicas para sessão expirada, 403 e 404
- arquivos gravados em respostas de erro são removidos com `deleteAsync({ idempotent: true })` para não abrir conteúdo inválido

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 011
- contexto sob demanda: `mobile/src/features/reports/services/reportsService.ts`, `mobile/src/shared/network/apiClient.ts`, `mobile/src/shared/network/createAppError.ts`
- contexto evitado: backend, front-end web e design system, porque a correção é local ao cliente mobile e não altera o contrato

## Handoff

- `.agents/state/handoffs/TASK-387.md`

## Arquivos alterados

- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/features/reports/services/reportsService.test.ts`
- `mobile/src/shared/network/apiClient.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run lint`
- `cd mobile && npm run test`

## Pendencias pos-task

- erros preexistentes de typecheck no app mobile seguem fora do escopo desta task

## Status final

done
