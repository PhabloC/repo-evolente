# Task 260 - Limpar avisos na tela mobile

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

ajuste incremental sobre UI existente

### Fonte primaria visual

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Objetivo

Adicionar uma opção de limpar todos os avisos visíveis ao lado da seção "Últimos avisos" na tela de avisos do app mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-248.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI atual de avisos | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | incluir ação no cabeçalho e estado vazio | sim |
| Estilos da tela | `mobile/src/features/shell/screens/styles.ts` | manter consistência visual da nova ação | sim |
| Hooks de notificações | `mobile/src/features/notifications/hooks/useNotifications.ts` | preservar leitura/contagem após limpeza local | sim |
| Serviço de notificações | `mobile/src/features/notifications/services/notificationsService.ts` | confirmar ausência de endpoint batch para não inferir API nova | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`, `mobile/docs/ai/QA.md` | manter organização, reuso e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a mudança à tela de avisos, sem reabrir contrato, backend ou design system amplo

## Criterios de conclusao

- [x] seção "Últimos avisos" exibe ação de limpar avisos quando houver itens visíveis
- [x] tocar em limpar remove todos os avisos visíveis da tela atual
- [x] resumo e estado vazio passam a refletir a lista limpa sem criar endpoint novo
- [x] validações do mobile executadas

## Dependencias

- Task 024 - done
- Task 219 - done
- Task 248 - done

## Resultado da execucao

- A seção "Últimos avisos" ganhou a ação "Limpar avisos" no cabeçalho
- A limpeza foi implementada como estado local da tela, removendo os avisos visíveis sem alterar contrato ou backend
- O resumo rápido, a hero e o estado vazio passaram a refletir a lista após a limpeza local

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-248.md`

### Sob demanda

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/notifications/hooks/useNotifications.ts`
- `mobile/src/features/notifications/services/notificationsService.ts`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/QA.md`

### Fontes evitadas

- `contracts/openapi.yaml`: sem endpoint novo ou integração nova
- `design-system/mobile/`: ajuste incremental sobre composição já consolidada
- `mobile/docs/ai/ACCESSIBILITY.md`: arquivo não existe no repositório; mantidos os padrões acessíveis já usados na tela

## Handoff

- `.agents/state/handoffs/TASK-260.md`

## Arquivos alterados

- `tasks/change-requests/260-limpar-avisos-na-tela-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-260.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`

## Validacoes executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo em `WordSearchGameRenderer`, `HomeHeader`, `AppBackgroundBubbles`, `EditChildProfileScreen`, `EditGuardianProfileScreen` e `Screen`
- `cd mobile && npx eslint src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/shell/screens/styles.ts` - ok
- `cd mobile && npm run typecheck` - ok
- `cd mobile && npm run test -- --runInBand` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue bloqueado por erros preexistentes fora do escopo desta task

## Status final

done
