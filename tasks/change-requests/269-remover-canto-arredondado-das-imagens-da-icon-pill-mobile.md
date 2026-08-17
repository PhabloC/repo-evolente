# Task 269 - Remover canto arredondado das imagens da IconPill mobile

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

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

ajuste incremental solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/shared/components/IconPill/styles.ts`

## Objetivo

Remover o canto arredondado das imagens renderizadas pela `IconPill`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-267.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Estilo compartilhado da pastilha | `mobile/src/shared/components/IconPill/styles.ts` | remover arredondamento residual das imagens | sim |
| Implementação da pastilha | `mobile/src/shared/components/IconPill/index.tsx` | garantir que só imagens percam o raio extra | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter organização e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a alteração ao estilo `pillWithImage`

## Criterios de conclusao

- [x] imagens da `IconPill` não ficam mais com canto arredondado
- [x] `eslint` e `typecheck` passam no escopo compartilhado da pastilha

## Dependencias

- Task 267 - done

## Resultado da execucao

- `pillWithImage` passou a zerar `borderRadius`
- os assets visuais de avisos e atividades agora renderizam sem borda e sem canto arredondado

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-267.md`

### Sob demanda

- `mobile/src/shared/components/IconPill/styles.ts`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-269.md`

## Arquivos alterados

- `tasks/change-requests/269-remover-canto-arredondado-das-imagens-da-icon-pill-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-269.md`
- `mobile/src/shared/components/IconPill/styles.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/shared/components/IconPill/styles.ts src/shared/components/IconPill/index.tsx src/features/shell/components/HomeHeader/index.tsx` - falhou por débitos preexistentes em `HomeHeader`; `IconPill` ficou sem novos erros no escopo alterado
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `HomeHeader` já tinha débitos de lint locais (`react-hooks/refs`) fora do escopo desta mudança
- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo

## Status final

done
