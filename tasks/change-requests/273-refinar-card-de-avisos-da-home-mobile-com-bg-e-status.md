# Task 273 - Refinar card de avisos da home mobile com bg e status

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

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`

## Objetivo

Refinar o card "Avisos da trilha" da home com shadow, sem barra azul lateral, pill de status com ícone de carta, pastilha do sino arredondada e background `trilha.webp` alinhado à esquerda e apagado.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-268.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Componente do card da home | `mobile/src/features/shell/components/HomeActionCard/index.tsx`, `styles.ts` | suportar shadow, background ilustrado, pill com ícone e variações visuais | sim |
| Uso no card de avisos | `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx` | aplicar props visuais só no card de avisos | sim |
| Asset local | `mobile/assets/trilha.webp` | usar background apagado à esquerda | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter organização e registrar validação | sim |

## Orçamento de contexto

- baixo
- estrategia: concentrar o refino no `HomeActionCard` e no uso do card de avisos da home

## Criterios de conclusao

- [x] card de avisos da home ganhou shadow
- [x] barra azul lateral foi removida desse card
- [x] pill "Não lidos" ganhou ícone de carta e largura baseada no conteúdo
- [x] pastilha do sino ficou redonda
- [x] card usa `trilha.webp` apagado e alinhado à esquerda no background

## Dependencias

- Task 246 - done
- Task 268 - done

## Resultado da execucao

- `HomeActionCard` passou a suportar background ilustrado, shadow, status com ícone, pastilha principal circular e opção de ocultar a barra lateral
- O card "Avisos da trilha" passou a usar `trilha.webp` no fundo, `Mail` na pill "Não lidos", sino em pastilha circular e sem a barra azul à esquerda
- A busca da home também passou a reutilizar `bell.webp` nos resultados de avisos

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-268.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-273.md`

## Arquivos alterados

- `tasks/change-requests/273-refinar-card-de-avisos-da-home-mobile-com-bg-e-status.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-273.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/components/HomeActionCard/index.tsx src/features/shell/components/HomeActionCard/styles.ts src/features/shell/screens/ResponsavelHomeScreen.tsx` - execução iniciada, sem retorno final da sessão
- `cd mobile && npm run typecheck` - execução iniciada, sem retorno final da sessão

## Pendencias pos-task

- Reexecutar as validações do escopo em nova sessão, porque as execuções desta task não devolveram status final
- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo

## Status final

done
