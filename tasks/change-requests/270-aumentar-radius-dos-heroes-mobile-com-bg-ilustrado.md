# Task 270 - Aumentar radius dos heroes mobile com bg ilustrado

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

- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`

## Objetivo

Deixar mais arredondadas as bordas dos cards iniciais com background ilustrado nas páginas mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-269.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Hero da home | `mobile/src/features/shell/components/HomeHeroBanner/styles.ts` | aumentar radius do banner inicial | sim |
| Heroes de avisos/perfil | `mobile/src/features/shell/screens/styles.ts` | aumentar radius dos cards com bg ilustrado | sim |
| Hero de atividades | `mobile/src/features/trail/screens/styles.ts` | aumentar radius do card inicial da trilha | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter consistência e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar somente os estilos dos heroes com background ilustrado, sem tocar nos demais cards

## Criterios de conclusao

- [x] home, avisos, perfil e atividades usam hero com radius mais arredondado
- [x] cards comuns do app permanecem inalterados
- [x] `eslint` e `typecheck` passam no escopo alterado

## Dependencias

- Task 123 - done
- Task 124 - done

## Resultado da execucao

- Os heroes com background ilustrado passaram de `radius.card` para `radius.lg`
- A mudança foi aplicada no banner da home, nos heroes das telas de shell e no hero da tela de atividades
- Cards funcionais e listas permaneceram com o radius anterior

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-269.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-270.md`

## Arquivos alterados

- `tasks/change-requests/270-aumentar-radius-dos-heroes-mobile-com-bg-ilustrado.md`
- `tasks/000-index.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-270.md`
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/components/HomeHeroBanner/styles.ts src/features/shell/screens/styles.ts src/features/trail/screens/styles.ts` - ok
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo

## Status final

done
