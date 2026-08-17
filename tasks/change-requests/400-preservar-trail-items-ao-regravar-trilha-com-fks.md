# Task 400 - Preservar trail_items ao regravar trilha com FKs

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem alteração de OpenAPI; mesmo `PUT`/`replace` de itens da trilha

## Modo de execução

single-stack

## Slice vertical

- Slice 033 - Integridade referencial Postgres (follow-up da Task 399)
- `tasks/slices/033-integridade-referencial-postgres.md`

## Objetivo

Ajustar `replaceItems` para atualizar/criar/remover seletivamente os `trail_items`, preservando IDs com evolução, para não quebrar na FK `RESTRICT` ao regravar a trilha.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/033-integridade-referencial-postgres.md`
- `.agents/state/handoffs/TASK-399.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Implementação atual | `backend/src/modules/trails/` | ajustar replace |
| Regressão | `trails.service.spec.ts` | cobrir preservação pós-conclusão |

## Orçamento de contexto

- baixo

## Critérios de conclusão

- [x] `replaceItems` não apaga itens que têm `evolution_records`
- [x] itens reaproveitados por `contentId` mantêm o mesmo `id`
- [x] remoção de item já concluído retorna conflito claro
- [x] teste de regressão cobrindo o fluxo
- [x] `npm test` do módulo trails (ou suite relevante) passa

## Resultado da execucao

- Extraído `planTrailItemsReplace` para emparelhar por `contentId`(+weekday), atualizar in-place, criar novos e deletar só itens sem evolução.
- TypeORM e in-memory usam o mesmo plano; remoção de item concluído → `ConflictException`.
- Testes util + service passando (9).

## Contexto utilizado

- handoff Task 399, módulo trails, Slice 033

## Handoff

- `.agents/state/handoffs/TASK-400.md`

## Arquivos alterados

- `backend/src/modules/trails/utils/replace-trail-items.util.ts`
- `backend/src/modules/trails/utils/replace-trail-items.util.spec.ts`
- `backend/src/modules/trails/trails.typeorm.repository.ts`
- `backend/src/modules/trails/trails.in-memory.repository.ts`
- `backend/src/modules/trails/trails.service.spec.ts`
- `tasks/change-requests/400-preservar-trail-items-ao-regravar-trilha-com-fks.md`
- `tasks/000-index.md`
- `tasks/slices/033-integridade-referencial-postgres.md`
- `.agents/state/handoffs/TASK-400.md`

## Validacoes executadas

- `npx jest src/modules/trails --runInBand` — 2 suites, 9 testes OK

## Pendencias pos-task

- nenhuma

## Status final

done
