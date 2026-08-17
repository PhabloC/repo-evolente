# Task 551 - PATCH da trilha para responsável com canManage

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts

## Contrato

- `contracts/openapi.yaml#/paths/~1trails~1{trailId}` (PATCH)

## Modo de execucao

cross-stack

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (UI fora de escopo)

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- autorização de API; sem UI

## Origem da solicitacao

Code review em `ajustes_backend.md` item 1: `canManage` é true para o responsável, mas PATCH `/trails/:trailId` fica em `@Roles('profissional')` e `update()` exige profissional.

## Objetivo

Alinhar inativação da trilha à mesma regra de `assertCanManagePatientTrail()` usada em create/replace.

## Escopo

- Incluir `responsavel` no PATCH do controller
- `update()` usa `assertCanManagePatientTrail` em vez de `assertProfessional`
- Atualizar descrição do contrato
- Teste: responsável inativa a trilha que criou

## Fora de escopo

- UI web/mobile de inativar
- Mudar a regra de `canManage` da Task 506

## Slice vertical

### Identificador do slice

Slice 047 - Trilha self-serve do responsável no mobile

### Arquivo do slice

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

### Objetivo de negocio

Responsável monta e gerencia a trilha da criança.

### Entrega verificavel do slice

PATCH de status permitido quando `canManage` é true.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 047

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API | `contracts/openapi.yaml#/paths/~1trails~1{trailId}` | alinhar papéis do PATCH | sim |
| Implementação | `trails.controller.ts`, `trails.service.ts`, spec | autorização | sim |
| Segurança | `backend/docs/ai/SECURITY.md` | papéis no endpoint | sim |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 3
- Risco: baixo
- Estratégia: só PATCH de trilha

## Dependencias

- Task 501, Task 506 (done)

## Criterios de conclusao

- Responsável autenticado dono da criança consegue PATCH `status: inactive`
- Profissional continua podendo PATCH da trilha do paciente vinculado
- Outro responsável recebe 403
- Contrato descreve os mesmos atores do PUT items

## Instrucoes de implementacao

- `@Roles('profissional', 'responsavel')` no PATCH
- Remover `assertProfessional` de `update()`
- Reusar `assertCanManagePatientTrail(user, trail.childId)`

## Validacao esperada

- Jest `trails.service.spec.ts`
- Lint dos arquivos alterados

## Entregaveis esperados

- Controller, service, contrato, teste, handoff

## Resultado da execucao

- PATCH `/trails/:trailId` aceita `profissional` e `responsavel`
- `update()` autoriza com `assertCanManagePatientTrail` (mesma regra de create/replace)
- Contrato descreve os mesmos atores de `canManage`
- Teste: responsável sem vínculo cria a trilha e PATCH `status: inactive`
- Slice 047 permanece done

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 047

### Contexto sob demanda carregado

- `contracts/openapi.yaml#/paths/~1trails~1{trailId}` (PATCH) — alinhar papéis
- `trails.controller.ts`, `trails.service.ts`, `trails.service.spec.ts` — autorização
- `backend/docs/ai/SECURITY.md` — papéis no endpoint (reuso de `canManage`)

### Contexto não carregado

- `design-system/`, `front-end/`, `mobile/` — sem UI nesta CR

## Handoff

- `.agents/state/handoffs/TASK-551.md`
- Próximo contexto: smoke PATCH inactive como responsável dono da criança

## Arquivos alterados

- `backend/src/modules/trails/trails.controller.ts`
- `backend/src/modules/trails/trails.service.ts`
- `backend/src/modules/trails/trails.service.spec.ts`
- `contracts/openapi.yaml`
- `tasks/change-requests/551-patch-trilha-responsavel-canmanage.md`
- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest `trails.service.spec.ts` (filtro guardian without professional): PASS
- eslint dos arquivos de trilha alterados: 0 erros

## Pendencias pos-task

- Smoke HTTP: responsável autenticado PATCH `status: inactive` na trilha que criou

## Status final

done
