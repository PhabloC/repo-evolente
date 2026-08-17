# Handoff — Task 400

- Task: 400 — Preservar trail_items ao regravar trilha com FKs
- Slice: 033 — Integridade referencial Postgres
- Status final: done

## Decisões preservadas

- `replaceItems` deixa de delete+recreate total
- Reaproveita IDs por `contentId` (+ weekday quando possível)
- Remover item já concluído → `ConflictException`
- Plano compartilhado em `utils/replace-trail-items.util.ts`

## Contexto usado

- Task 399 handoff, módulo trails

## Arquivos alterados

- util + typeorm + in-memory + specs trails
- task/index/handoff 400

## Validações

- jest trails: 9 passed

## Pendências

- nenhuma

## Próximo contexto recomendado

- nenhum

## Não carregar

- design-system, front-end, mobile
