# Task 274 - Refinar tipografia e profundidade do card de avisos home mobile

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

refino incremental solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- print enviado pelo usuário do card "Avisos da trilha"

## Objetivo

Deixar menor o texto descritivo do card "Avisos da trilha" e reforçar a sombra para transmitir mais profundidade visual.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-273.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste tipográfico e sombra do card | `mobile/src/features/shell/components/HomeActionCard/styles.ts` | reduzir texto descritivo e aprofundar shadow | sim |
| Estrutura do card | `mobile/src/features/shell/components/HomeActionCard/index.tsx` | confirmar o alvo visual sem abrir outros cards | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter organização e registrar validação | sim |

## Orçamento de contexto

- baixo
- estrategia: mexer apenas no estilo compartilhado já aberto pela Task 273

## Criterios de conclusao

- [x] texto "Há 1 aviso esperando..." ficou visualmente menor
- [x] shadow do card ficou mais profunda e evidente

## Dependencias

- Task 273 - done

## Resultado da execucao

- a tipografia da descrição do `HomeActionCard` foi reduzida para 14/20
- a sombra do card foi reforçada com maior offset, blur, opacidade e elevation

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-273.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-274.md`

## Arquivos alterados

- `tasks/change-requests/274-refinar-tipografia-e-profundidade-do-card-de-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-274.md`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/components/HomeActionCard/styles.ts`

## Pendencias pos-task

- `npm run lint` e `npm run typecheck` globais do mobile seguem pendentes fora do escopo desta microtask

## Status final

done
