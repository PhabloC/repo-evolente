# Handoff - Task 256

## Task

- identificador: 256
- título: Hardening da troca de avatar no bucket backend
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 027
- objetivo de negócio: evitar perda do avatar anterior quando a troca falhar em algum ponto intermediário

## Decisões preservadas

- O upload do novo avatar acontece antes da remoção do objeto antigo
- A remoção do avatar antigo passou a ser pós-persistência e best-effort
- Falhas após upload acionam limpeza compensatória do novo objeto

## Contexto efetivamente usado

- task 256, índice, slice 027
- handoffs `TASK-162` e `TASK-243`
- `profile-avatar-storage.service`
- serviços `users`, `patients` e `guardians`
- specs de avatar correspondentes

## Arquivos alterados

- `backend/src/modules/storage/profile-avatar-storage.service.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`

## Validacoes executadas

- `cd backend && npm run test -- users.service.spec.ts patients.service.spec.ts guardians.service.spec.ts` — ok
- lint focado nos arquivos alterados — ok

## Pendencias ou bloqueios

- Falta smoke test contra bucket real em cenário de indisponibilidade/intermitência
- `typecheck` global do backend continua com falhas antigas fora do escopo

## Próximo contexto recomendado

- `tasks/change-requests/257-hardening-caca-palavras-assets-e-bootstrap-backend.md`
- `backend/src/modules/contents/word-search-game-assets.ts`
- `backend/scripts/upload-caca-palavras-cover.mjs`
