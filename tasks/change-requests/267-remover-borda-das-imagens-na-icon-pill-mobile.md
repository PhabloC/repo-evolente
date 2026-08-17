# Task 267 - Remover borda das imagens na IconPill mobile

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

Remover a borda aplicada ao redor das imagens renderizadas pela `IconPill`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-124.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Estilo compartilhado da pastilha | `mobile/src/shared/components/IconPill/styles.ts` | remover contorno das imagens | sim |
| Implementação da pastilha | `mobile/src/shared/components/IconPill/index.tsx` | validar impacto no uso com assets locais | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`, `mobile/docs/ai/QA.md` | manter organização e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a mudança ao estilo compartilhado da `IconPill`

## Criterios de conclusao

- [x] imagens renderizadas pela `IconPill` não exibem mais borda
- [x] `eslint` e `typecheck` passam no escopo alterado

## Dependencias

- Task 124 - done
- Task 262 - done
- Task 263 - done
- Task 264 - done

## Resultado da execucao

- Removidos `borderColor` e `borderWidth` do estilo `pillWithImage`
- Assets locais usados em avisos e atividades agora aparecem sem contorno extra

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-124.md`

### Sob demanda

- `mobile/src/shared/components/IconPill/styles.ts`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-267.md`

## Arquivos alterados

- `tasks/change-requests/267-remover-borda-das-imagens-na-icon-pill-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-267.md`
- `mobile/src/shared/components/IconPill/styles.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/shared/components/IconPill/styles.ts src/shared/components/IconPill/index.tsx` - ok
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo

## Status final

done
