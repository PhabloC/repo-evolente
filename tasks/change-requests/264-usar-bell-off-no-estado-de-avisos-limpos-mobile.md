# Task 264 - Usar bell-off no estado de avisos limpos mobile

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

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/assets/bell-off.webp`

## Objetivo

Usar o asset `bell-off.webp` no estado em que os avisos foram limpos da tela, em vez do ícone vetorial de sino riscado.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-262.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Estado vazio após limpeza | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | aplicar asset apenas no estado de avisos limpos | sim |
| Asset local | `mobile/assets/bell-off.webp` | usar a imagem fornecida | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`, `mobile/docs/ai/QA.md` | manter organização e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas o estado visual de avisos limpos na tela de notificações

## Criterios de conclusao

- [x] o estado “Avisos limpos da tela” usa `bell-off.webp`
- [x] o estado “Nenhum aviso ainda” mantém o comportamento anterior
- [x] validações do escopo alterado executadas

## Dependencias

- Task 260 - done
- Task 261 - done
- Task 262 - done

## Resultado da execucao

- O card de estado vazio após limpar avisos passou a usar `bell-off.webp`
- O estado vazio padrão sem avisos iniciais segue usando o fallback vetorial anterior
- A mudança ficou restrita à tela de avisos, sem impacto em outras telas

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-262.md`

### Sob demanda

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/assets/bell-off.webp`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/QA.md`

### Fontes evitadas

- `contracts/openapi.yaml`: sem mudança de API
- `design-system/mobile/`: troca pontual de asset sem revisão estrutural

## Handoff

- `.agents/state/handoffs/TASK-264.md`

## Arquivos alterados

- `tasks/change-requests/264-usar-bell-off-no-estado-de-avisos-limpos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-264.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/screens/ResponsavelNotificationsScreen.tsx` - ok
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo, conforme registrado nas tasks anteriores

## Status final

done
