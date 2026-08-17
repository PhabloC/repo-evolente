# Task 281 - Remover bg trilha e mover sombra para o card de avisos home mobile

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

## Objetivo

Remover a imagem de background do card "Avisos da trilha" e aplicar o box-shadow no próprio card, não no pai.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-280.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Card e sombra | `HomeActionCard/*`, `ResponsavelHomeScreen.tsx` | remover bg e mover shadow | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] sem `trilha.webp` no card de avisos
- [x] sombra aplicada no card, não no wrapper pai

## Dependencias

- Task 280 - done

## Resultado da execucao

- removidos props/camada de background image do `HomeActionCard`
- removido `trilha.webp` do card de avisos na home
- sombra aplicada diretamente no `Pressable`/`View` do card; wrapper pai eliminado

## Contexto utilizado

### Mínimo

- task 281, handoff 280, slice 010, índice

### Sob demanda

- `HomeActionCard/index.tsx`, `styles.ts`
- `ResponsavelHomeScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-281.md`

## Arquivos alterados

- `tasks/change-requests/281-remover-bg-trilha-e-mover-sombra-para-card-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-281.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- validação visual dependente de reload no Expo Go

## Pendencias pos-task

- nenhuma

## Status final

done
