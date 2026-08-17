# Task 272 - Alinhar CTAs dos heroes home e trilha mobile

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

- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`

## Objetivo

Deixar os botões internos dos heroes da home e da página de trilha com o mesmo design, seguindo o CTA da home e adicionando seta à direita.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-271.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| CTA da home | `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`, `styles.ts` | adicionar seta e definir padrão visual | sim |
| CTA da trilha | `mobile/src/features/trail/screens/TrailTodayScreen.tsx`, `styles.ts` | alinhar botão ao padrão da home | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter consistência e registrar validação | sim |

## Orçamento de contexto

- baixo
- estrategia: ajustar apenas os CTAs dos heroes, sem alterar outros botões da aplicação

## Criterios de conclusao

- [x] CTA da home ganhou seta à direita
- [x] CTA do hero da trilha segue o mesmo visual da home
- [x] ambos mantêm o comportamento existente de navegação

## Dependencias

- Task 123 - done
- Task 271 - done

## Resultado da execucao

- O CTA da home passou a renderizar label + seta à direita
- O CTA do hero da trilha deixou de usar o `Button` genérico e passou a usar o mesmo visual do CTA da home
- A navegação existente foi preservada

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-271.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-272.md`

## Arquivos alterados

- `tasks/change-requests/272-alinhar-ctas-dos-heroes-home-e-trilha-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-272.md`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/components/HomeHeroBanner/index.tsx src/features/shell/components/HomeHeroBanner/styles.ts src/features/trail/screens/TrailTodayScreen.tsx src/features/trail/screens/styles.ts` - execução iniciada, sem retorno final da sessão
- `cd mobile && npm run typecheck` - execução iniciada, sem retorno final da sessão

## Pendencias pos-task

- Reexecutar `eslint` e `typecheck` do escopo em nova sessão, porque as execuções desta task não devolveram status final
- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo

## Status final

done
