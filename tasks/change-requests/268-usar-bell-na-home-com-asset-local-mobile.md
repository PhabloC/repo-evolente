# Task 268 - Usar bell na home com asset local mobile

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

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

ajuste incremental solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/bell.webp`

## Objetivo

Trocar pelo asset local `bell.webp` o ícone do quadro "Avisos da trilha" na home.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-265.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Card de avisos da home | `mobile/src/features/shell/components/HomeActionCard/index.tsx`, `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx` | aplicar asset local no quadro de avisos | sim |
| Asset local | `mobile/assets/bell.webp` | usar imagem fornecida na home | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter organização e registrar validação | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas o ícone do quadro de avisos da home e reverter o header ao estado anterior

## Criterios de conclusao

- [x] o quadro "Avisos da trilha" da home usa `bell.webp`
- [x] o sino do header volta ao ícone vetorial anterior
- [x] `typecheck` passa

## Dependencias

- Task 262 - done
- Task 265 - done

## Resultado da execucao

- O quadro "Avisos da trilha" passou a renderizar `bell.webp` via `HomeActionCard`
- O sino do header foi revertido para o ícone vetorial anterior

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-265.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/bell.webp`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-268.md`

## Arquivos alterados

- `tasks/change-requests/268-usar-bell-na-home-com-asset-local-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-268.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeHeader/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/components/HomeHeader/index.tsx src/features/shell/components/HomeActionCard/index.tsx src/features/shell/screens/ResponsavelHomeScreen.tsx` - falhou por débitos preexistentes em `HomeHeader` na regra `react-hooks/refs`
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `HomeHeader` já tinha débitos de lint locais (`react-hooks/refs`) fora do escopo desta mudança
- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo

## Status final

done
