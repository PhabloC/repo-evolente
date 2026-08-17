# Task 256 - Hardening da troca de avatar no bucket backend

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Dependencias

- Task 162
- Task 243

## Objetivo

Tornar a substituição de avatar resiliente a falhas de upload e persistência, evitando perda da imagem anterior e limpando uploads órfãos quando necessário.

## Entrega verificavel

- Upload do novo avatar acontece antes da remoção do objeto antigo
- Se a persistência falhar após o upload, o novo objeto é compensado/removido
- O avatar antigo só é apagado após a atualização bem-sucedida no banco
- Testes cobrindo falha no upload, falha na persistência e limpeza compensatória

## Fora de escopo

- Mudança no contrato público de avatar
- Crop, remoção manual ou novos formatos de imagem
- Ajustes em UI web ou mobile

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-162.md`
- `.agents/state/handoffs/TASK-243.md`

## Contexto sob demanda

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `backend/src/modules/storage/profile-avatar-storage.service.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- testes/specs que exercitam upload de avatar

## Orcamento de contexto

baixo

## Estrategia de reducao

Conter a mudança ao fluxo backend de troca de avatar e aos testes relacionados, sem reabrir front-end, mobile ou migrações.

## Referencia visual

- nao se aplica

## Resultado da execucao

- O `ProfileAvatarStorageService` deixou de apagar o avatar antigo antes do upload do novo
- `UsersService`, `PatientsService` e `GuardiansService` passaram a remover o avatar antigo apenas após persistência bem-sucedida
- Em falha de persistência após upload, o novo objeto é removido de forma compensatória
- Foram adicionados testes cobrindo troca bem-sucedida e compensação no fluxo de usuário, mantendo as suítes de paciente e guardian verdes

## Contexto utilizado

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `backend/src/modules/storage/profile-avatar-storage.service.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `backend/src/modules/patients/patients.service.spec.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `.agents/state/handoffs/TASK-162.md`
- `.agents/state/handoffs/TASK-243.md`

## Handoff

- `.agents/state/handoffs/TASK-256.md`

## Arquivos alterados

- `backend/src/modules/storage/profile-avatar-storage.service.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`

## Validacoes executadas

- `cd backend && npm run test -- users.service.spec.ts patients.service.spec.ts guardians.service.spec.ts` — ok
- `cd backend && npx eslint src/modules/storage/profile-avatar-storage.service.ts src/modules/users/users.service.ts src/modules/users/users.service.spec.ts src/modules/patients/patients.service.ts src/modules/guardians/guardians.service.ts src/modules/guardians/guardians.service.spec.ts` — ok

## Pendencias pos-task

- Validar em ambiente real o comportamento quando o bucket estiver indisponível durante uma troca de avatar
- `typecheck` global do backend continua com falhas pré-existentes fora deste escopo

## Status final

done
