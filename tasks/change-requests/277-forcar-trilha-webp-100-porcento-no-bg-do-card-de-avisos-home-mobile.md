# Task 277 - Forcar trilha.webp 100 porcento no bg do card de avisos home mobile

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

Fazer o `trilha.webp` aparecer 100% como background do card "Avisos da trilha".

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-276.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Camada de background do card | `mobile/src/features/shell/components/HomeActionCard/index.tsx`, `styles.ts` | forçar preenchimento total do asset | sim |
| Uso na home | `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx` | remover fade do fundo só no card de avisos | sim |
| Asset local | `mobile/assets/trilha.webp` | manter o mesmo background solicitado | sim |

## Orçamento de contexto

- baixo
- estrategia: mexer só na composição do background do card

## Criterios de conclusao

- [x] `trilha.webp` passa a ocupar 100% do fundo do card de avisos
- [x] opacidade do background do card de avisos fica em 1

## Dependencias

- Task 276 - done

## Resultado da execucao

- o fundo do card passou a ocupar toda a área disponível com largura e altura em `100%`
- o `resizeMode` foi alterado para `stretch` para forçar presença visual integral do asset
- o uso na home passou a aplicar `backgroundImageOpacity={1}`

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-276.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`

## Handoff

- `.agents/state/handoffs/TASK-277.md`

## Arquivos alterados

- `tasks/change-requests/277-forcar-trilha-webp-100-porcento-no-bg-do-card-de-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-277.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- validação visual dependente de execução do app

## Pendencias pos-task

- confirmar no app se o `stretch` preserva a leitura visual esperada da arte

## Status final

done
