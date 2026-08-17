# Task 279 - Reduzir tamanho do bg trilha no card de avisos home mobile

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
- `mobile/assets/trilha.webp`

## Objetivo

Diminuir o tamanho do `trilha.webp` no card "Avisos da trilha" para o fundo deixar de esticar/distorcer a composição do card.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-278.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Tamanho/posição do bg | `HomeActionCard/styles.ts`, `index.tsx` | reduzir asset e evitar fill total | sim |

## Orçamento de contexto

- baixo
- estrategia: só ajustar tamanho/posição do background no `HomeActionCard`

## Criterios de conclusao

- [x] `trilha.webp` fica menor e sem esticar o card
- [x] sombra e conteúdo do card permanecem intactos

## Dependencias

- Task 278 - done

## Resultado da execucao

- o `trilha.webp` deixou de preencher 100% do card e passou a um carimbo 112x112 à esquerda
- `resizeMode` voltou para `contain` para evitar distorção
- scrim full-bleed removido; opacidade do bg na home ajustada para 0.45

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 010, handoff 278

### Sob demanda

- `HomeActionCard/index.tsx`, `styles.ts`
- `ResponsavelHomeScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-279.md`

## Arquivos alterados

- `tasks/change-requests/279-reduzir-tamanho-bg-trilha-card-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-279.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- validação visual dependente de reload no Expo Go

## Pendencias pos-task

- confirmar se 112px está no tamanho desejado

## Status final

done
