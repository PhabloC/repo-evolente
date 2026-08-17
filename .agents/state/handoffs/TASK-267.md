# Handoff - Task 267

## Status

done

## Decisões

- a borda das imagens foi removida no estilo compartilhado `IconPill`
- a mudança vale para qualquer asset renderizado pela pastilha, sem alterar o fallback vetorial

## Contexto utilizado

- `tasks/change-requests/267-remover-borda-das-imagens-na-icon-pill-mobile.md`
- `.agents/state/handoffs/TASK-124.md`
- `mobile/src/shared/components/IconPill/styles.ts`
- `mobile/src/shared/components/IconPill/index.tsx`

## Arquivos alterados

- `tasks/change-requests/267-remover-borda-das-imagens-na-icon-pill-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-267.md`
- `mobile/src/shared/components/IconPill/styles.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/shared/components/IconPill/styles.ts src/shared/components/IconPill/index.tsx`
- `cd mobile && npm run typecheck`

## Pendencias

- `npm run lint` global do mobile continua com débitos antigos fora deste escopo

## Proximo contexto recomendado

- reutilizar esta task se a `IconPill` voltar a ganhar tratamento visual específico para assets raster
