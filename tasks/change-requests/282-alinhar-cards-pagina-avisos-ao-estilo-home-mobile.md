# Task 282 - Alinhar cards da pagina de avisos ao estilo do card da home mobile

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

- card "Avisos da trilha" da home (`HomeActionCard`)
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/components/HomeActionCard/`

## Objetivo

Colocar os dois cards da página de avisos (resumo rápido e estado vazio) no mesmo estilo visual do card da home.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-281.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Cards da página de avisos | `ResponsavelNotificationsScreen.tsx`, `screens/styles.ts` | substituir pelos HomeActionCard | sim |
| Estilo de referencia | `HomeActionCard/*` | reutilizar componente | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] card de resumo rápido usa o mesmo estilo do card da home
- [x] card de estado vazio usa o mesmo estilo do card da home

## Dependencias

- Task 281 - done

## Resultado da execucao

- resumo rápido e estado vazio passaram a usar `HomeActionCard` com `withShadow`, pastilha circular e tipografia/status no padrão da home
- estilos locais `noticeSummary*` e `noticeEmptyCard` removidos

## Contexto utilizado

### Mínimo

- task 282, handoff 281, slice 010, índice

### Sob demanda

- `ResponsavelNotificationsScreen.tsx`
- `screens/styles.ts`
- `HomeActionCard/*`

## Handoff

- `.agents/state/handoffs/TASK-282.md`

## Arquivos alterados

- `tasks/change-requests/282-alinhar-cards-pagina-avisos-ao-estilo-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-282.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`

## Validacoes executadas

- validação visual dependente de reload no Expo Go

## Pendencias pos-task

- nenhuma

## Status final

done
