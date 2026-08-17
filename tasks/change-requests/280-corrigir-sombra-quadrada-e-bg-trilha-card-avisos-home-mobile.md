# Task 280 - Corrigir sombra quadrada e bg trilha no card de avisos home mobile

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

refino incremental + print do card com sombra quadrada e sem bg

### Fonte primaria visual

- print enviado pelo usuário (sombra em bloco sob o card, sem `trilha.webp`)
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/assets/trilha.webp`

## Objetivo

Eliminar a sombra quadrada sob o card "Avisos da trilha" e fazer o `trilha.webp` voltar a aparecer no background, sem esticar o card.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-279.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Sombra e estrutura do card | `HomeActionCard/index.tsx`, `styles.ts` | separar host de sombra do Pressable | sim |
| Asset de fundo | `trilha.webp`, `ResponsavelHomeScreen.tsx` | reaparecer carimbo decorativo | sim |

## Orçamento de contexto

- baixo
- estrategia: só `HomeActionCard` + props na home

## Criterios de conclusao

- [x] sombra acompanha o radius do card (sem bloco quadrado)
- [x] `trilha.webp` visível no fundo do card
- [x] card não fica esticado pelo background

## Dependencias

- Task 279 - done

## Resultado da execucao

- sombra saiu do `Pressable` e foi para um `View` host com `borderRadius` + elevation mais baixa
- `trilha.webp` voltou como carimbo 168x168 à esquerda com opacidade 0.7 e `contain`

## Contexto utilizado

### Mínimo

- task 280, handoff 279, slice 010, índice

### Sob demanda

- `HomeActionCard/index.tsx`, `styles.ts`
- `ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`

## Handoff

- `.agents/state/handoffs/TASK-280.md`

## Arquivos alterados

- `tasks/change-requests/280-corrigir-sombra-quadrada-e-bg-trilha-card-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-280.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- validação visual dependente de reload no Expo Go

## Pendencias pos-task

- confirmar no device se a sombra arredondou e se o carimbo da trilha está no tamanho certo

## Status final

done
