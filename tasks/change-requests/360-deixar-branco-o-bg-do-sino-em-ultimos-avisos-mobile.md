# Task 360 - Deixar branco o bg do sino em Ultimos avisos mobile

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
- `mobile/src/features/shell/screens/styles.ts`

## Objetivo

Deixar branco o fundo da pastilha do sino no item não lido de "Ultimos avisos".

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-359.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Refino visual da pastilha | `mobile/src/features/shell/screens/styles.ts` | trocar apenas a cor de fundo da pastilha do sino | sim |
| Componente consumidor | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | confirmar que o ajuste afeta só o item não lido de "Ultimos avisos" | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter organização e registrar validações | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar o ajuste à cor de fundo da pastilha, sem reabrir estrutura, assets ou estados da tela

## Criterios de conclusao

- [x] o sino do item não lido em "Ultimos avisos" mantém o `bell.webp`
- [x] a pastilha do sino passa a ter fundo branco
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 359 - done

## Resultado da execucao

- a pastilha do sino no item não lido de "Ultimos avisos" passou de `orangeSoft` para fundo branco
- o restante do tratamento visual do item foi preservado

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-359.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-360.md`

## Arquivos alterados

- `tasks/change-requests/360-deixar-branco-o-bg-do-sino-em-ultimos-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-360.md`
- `mobile/src/features/shell/screens/styles.ts`

## Validacoes executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo em `WordSearchGameRenderer`, `EditChildProfileScreen`, `EditGuardianProfileScreen`, `HomeHeader`, `AppBackgroundBubbles` e `Screen`
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` - ok (`26` suites, `90` testes)

## Pendencias pos-task

- `npm run lint` do mobile segue com débitos preexistentes fora do escopo desta mudança
- `npm run typecheck` do mobile segue com débitos preexistentes fora do escopo desta mudança

## Status final

done
