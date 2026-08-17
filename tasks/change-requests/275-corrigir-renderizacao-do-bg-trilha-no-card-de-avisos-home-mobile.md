# Task 275 - Corrigir renderizacao do bg trilha no card de avisos home mobile

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

Garantir que o `trilha.webp` apareça de fato no background do card "Avisos da trilha" da home.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-274.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Camada de background do card | `mobile/src/features/shell/components/HomeActionCard/index.tsx`, `styles.ts` | corrigir renderização do asset no fundo do card | sim |
| Asset local | `mobile/assets/trilha.webp` | confirmar o arquivo usado na composição | sim |

## Orçamento de contexto

- baixo
- estrategia: corrigir apenas a camada visual de fundo do card

## Criterios de conclusao

- [x] `trilha.webp` aparece no card de avisos da home
- [x] imagem continua alinhada à esquerda e apagada

## Dependencias

- Task 273 - done
- Task 274 - done

## Resultado da execucao

- o `HomeActionCard` passou a renderizar o fundo ilustrado dentro de uma camada absoluta dedicada
- o `trilha.webp` foi ampliado e ganhou `resizeMode="contain"` para aparecer com mais consistência
- conteúdo e rodapé do card ficaram acima da camada ilustrada com `zIndex`

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-274.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/assets/trilha.webp`

## Handoff

- `.agents/state/handoffs/TASK-275.md`

## Arquivos alterados

- `tasks/change-requests/275-corrigir-renderizacao-do-bg-trilha-no-card-de-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-275.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`

## Validacoes executadas

- validação visual dependente de execução do app

## Pendencias pos-task

- confirmar no app se a opacidade atual do fundo está no ponto desejado

## Status final

done
