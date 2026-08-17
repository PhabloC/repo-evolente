# Task 271 - Aumentar ainda mais o radius dos heroes mobile

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

refino incremental solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`

## Objetivo

Aumentar ainda mais o border radius dos cards iniciais com background ilustrado nas páginas mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-270.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Hero da home | `mobile/src/features/shell/components/HomeHeroBanner/styles.ts` | elevar radius do banner | sim |
| Heroes de shell | `mobile/src/features/shell/screens/styles.ts` | elevar radius dos cards iniciais | sim |
| Hero da trilha | `mobile/src/features/trail/screens/styles.ts` | elevar radius do hero da página de atividades | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter consistência e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: ajustar apenas o raio dos heroes ilustrados, sem tocar nos demais cards

## Criterios de conclusao

- [x] heroes ilustrados usam radius maior que o ajuste anterior
- [x] cards comuns permanecem inalterados
- [x] `eslint` e `typecheck` passam no escopo alterado

## Dependencias

- Task 270 - done

## Resultado da execucao

- Os heroes ilustrados passaram a usar `borderRadius: 32`
- O ajuste foi aplicado no banner da home, nos heroes de shell e no hero da trilha
- Os demais cards do app permaneceram com o radius anterior

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-270.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-271.md`

## Arquivos alterados

- `tasks/change-requests/271-aumentar-ainda-mais-o-radius-dos-heroes-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-271.md`
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
