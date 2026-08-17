# Handoff - Task 501

## Task

- identificador: 501
- título: Backend: trilha self-serve do responsável
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 047-trilha-self-serve-responsavel-mobile
- objetivo de negócio: API permite create/suggest/replace para guardian sem link
- entrega verificável: testes guardian com/sem vínculo

## Decisões preservadas

- decisão: com link `active`, guardian só lê (`canManage: false`); sem link, `professionalUserId` null
- motivo: evita conflito clínico com trilha do profissional
- impacto: mobile usa `canManage` para UI dono vs execução

## Contexto utilizado

### Contexto mínimo lido

- Task 500 / openapi
- `backend/src/modules/trails/*`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| patients link status | ownership | bloquear manage |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile UI | task só backend |

## Resultado por stack

- backend: migration 186… + TrailsService ownership + roles

## Arquivos alterados

- `backend/src/database/migrations/1860000000000-MakeWeeklyTrailsProfessionalUserIdNullable.ts`
- `backend/src/modules/trails/trails.service.ts`
- `backend/src/modules/trails/trails.controller.ts`
- `backend/src/modules/trails/entities/weekly-trail.entity.ts`
- `backend/src/modules/trails/trails.service.spec.ts`

## Validações executadas

- `npx jest src/modules/trails/trails.service.spec.ts` — 8 passed

## Pendências ou bloqueios

- aplicar migration no ambiente local/prod antes de usar create guardian

## Próxima ação sugerida

- Task 502 (UI mobile) — concluída

## Próximo contexto recomendado

- handoff 502 / TrailTodayScreen

## Contexto que não deve ser carregado na próxima etapa

- front-end web trilhas
