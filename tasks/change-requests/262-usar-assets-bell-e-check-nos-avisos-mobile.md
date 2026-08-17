# Task 262 - Usar assets bell e check nos avisos mobile

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
- `mobile/assets/bell.webp`
- `mobile/assets/check.webp`

## Objetivo

Substituir, na página de avisos, os ícones vetoriais de sino e check da lista pelos assets locais `bell.webp` e `check.webp`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-261.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Lista de avisos | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | aplicar assets no sino/check da lista | sim |
| Reuso da pastilha | `mobile/src/shared/components/IconPill/index.tsx` | aceitar asset local mantendo fallback do ícone | sim |
| Assets locais | `mobile/assets/bell.webp`, `mobile/assets/check.webp` | usar as imagens fornecidas | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`, `mobile/docs/ai/QA.md` | manter organização e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar somente a pastilha de ícone reutilizável e a tela de avisos

## Criterios de conclusao

- [x] a lista de avisos usa `bell.webp` para avisos não lidos
- [x] a lista de avisos usa `check.webp` para avisos lidos
- [x] `IconPill` suporta asset local sem quebrar o fallback vetorial
- [x] validações do escopo alterado executadas

## Dependencias

- Task 248 - done
- Task 260 - done
- Task 261 - done

## Resultado da execucao

- `IconPill` passou a aceitar `imageSource` com asset local além de `imageUri`
- A lista de avisos passou a renderizar `bell.webp` e `check.webp` no lugar dos ícones vetoriais correspondentes
- Hero, estado vazio e demais ícones da página permaneceram inalterados

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-261.md`

### Sob demanda

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/assets/bell.webp`
- `mobile/assets/check.webp`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/QA.md`

### Fontes evitadas

- `contracts/openapi.yaml`: sem mudança de API
- `design-system/mobile/`: troca pontual de assets sem revisão estrutural de layout

## Handoff

- `.agents/state/handoffs/TASK-262.md`

## Arquivos alterados

- `tasks/change-requests/262-usar-assets-bell-e-check-nos-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-262.md`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/shared/components/IconPill/index.tsx src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/trail/screens/TrailTodayScreen.tsx` - ok
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo, conforme registrado nas tasks anteriores

## Status final

done
