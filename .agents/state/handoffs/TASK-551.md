# Handoff - Task 551

## Task

- identificador: TASK-551
- título: PATCH da trilha para responsável com canManage
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 047
- objetivo de negócio: responsável monta e gerencia a trilha da criança
- entrega verificável: PATCH de status permitido quando `canManage` é true

## Decisões preservadas

- decisão: `@Roles('profissional', 'responsavel')` no PATCH
- motivo: create/replace já aceitavam responsável; só o PATCH ficava em profissional
- impacto: responsável dono da criança inativa a trilha que criou

- decisão: `update()` usa `assertCanManagePatientTrail`
- motivo: mesma regra de `canManage` da Task 506; não reabrir essa regra
- impacto: profissional vinculado continua podendo PATCH; outro responsável recebe 403

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 551, slice 047

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `openapi.yaml` PATCH `/trails/{trailId}` | contrato | papéis alinhados ao PUT items |
| `trails.controller.ts` / `trails.service.ts` | autorização | Roles + assertCanManage |
| `trails.service.spec.ts` | regressão | guardian PATCH inactive |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| UI web/mobile | CR só de API |

## Resultado por stack

- backend: PATCH alinhado a canManage
- contracts: description do PATCH atualizada
- front-end / mobile: fora de escopo

## Arquivos alterados

- `backend/src/modules/trails/trails.controller.ts`
- `backend/src/modules/trails/trails.service.ts`
- `backend/src/modules/trails/trails.service.spec.ts`
- `contracts/openapi.yaml`

## Validações executadas

- validação: Jest guardian create/replace/update inactive — PASS
- validação: eslint arquivos de trilha — 0 erros

## Pendências ou bloqueios

- smoke HTTP PATCH inactive como responsável

## Próxima ação sugerida

- Task 552 (bootstrap word-spell) já no mesmo review

## Próximo contexto recomendado

- `trails.controller.ts` PATCH
- `trails.service.ts` `update()`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `design-system/`
- motivo: sem UI
