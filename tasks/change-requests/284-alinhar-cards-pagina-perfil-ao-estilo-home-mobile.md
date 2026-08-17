# Task 284 - Alinhar cards da pagina de perfil ao estilo do card da home mobile

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

refino incremental — card da home como referencia

### Fonte primaria visual

- `HomeActionCard` (card Avisos da trilha da home)
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Objetivo

Colocar os dois cards da página de perfil (dados do responsável e criança) no mesmo estilo visual do card da home.

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-283.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Cards do perfil | `ResponsavelProfileScreen.tsx`, `screens/styles.ts` | trocar para HomeActionCard | sim |
| Estilo | `HomeActionCard/*` | reutilizar | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] card do responsável no estilo HomeActionCard
- [x] card da criança no estilo HomeActionCard

## Dependencias

- Task 283 - done

## Resultado da execucao

- card do responsável e card da criança passaram a usar `HomeActionCard` com sombra, pastilha, status e CTA no padrão da home
- lista de crianças ficou como conteúdo interno do segundo card
- estilos locais antigos do layout de perfil (avatar tile / status pills) removidos

## Contexto utilizado

- task 284, handoff 283, `ResponsavelProfileScreen.tsx`, `HomeActionCard`, `screens/styles.ts`

## Handoff

- `.agents/state/handoffs/TASK-284.md`

## Arquivos alterados

- `tasks/change-requests/284-alinhar-cards-pagina-perfil-ao-estilo-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-284.md`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`

## Validacoes executadas

- validação visual dependente de reload no Expo Go

## Pendencias pos-task

- nenhuma

## Status final

done
