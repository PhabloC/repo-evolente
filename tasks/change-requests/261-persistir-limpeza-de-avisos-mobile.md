# Task 261 - Persistir limpeza de avisos no mobile

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

correção incremental sobre UI existente

### Fonte primaria visual

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Objetivo

Fazer a limpeza dos avisos persistir ao sair e voltar para a tela, evitando que avisos já limpos reapareçam por remontagem da aba ou refetch da query.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-260.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Correção da limpeza anterior | `tasks/change-requests/260-limpar-avisos-na-tela-mobile.md` | entender a implementação volátil anterior | sim |
| Tela de avisos | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | substituir estado local por persistência | sim |
| Persistência local | `mobile/src/shared/storage/appStorage.ts` | reaproveitar storage local do app | sim |
| Padrão de storage | `mobile/src/features/auth/storage/biometricPreferenceStorage.ts` | seguir convenção de leitura/escrita resiliente | sim |
| Cobertura de teste | `mobile/src/features/auth/storage/biometricPreferenceStorage.test.ts` | espelhar padrão de testes de AsyncStorage | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`, `mobile/docs/ai/QA.md` | manter organização, reuso e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: corrigir apenas a persistência da limpeza e adicionar teste focado de storage

## Criterios de conclusao

- [x] avisos limpos continuam ocultos após sair e voltar para a tela
- [x] a tela usa persistência local em vez de estado efêmero para a lista dispensada
- [x] existe teste cobrindo serialização, leitura inválida e falhas de storage
- [x] validações do escopo alterado executadas

## Dependencias

- Task 024 - done
- Task 248 - done
- Task 260 - done

## Resultado da execucao

- A lista de avisos dispensados passou a ser persistida em `AsyncStorage` via storage dedicado de notificações
- `ResponsavelNotificationsScreen` deixou de depender de `useState` local para a limpeza e passou a carregar/escrever os ids dispensados via query local
- A correção cobre o cenário em que a aba é remontada ou a query de notificações é recarregada

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-260.md`

### Sob demanda

- `tasks/change-requests/260-limpar-avisos-na-tela-mobile.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/shared/storage/appStorage.ts`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.test.ts`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/QA.md`

### Fontes evitadas

- `contracts/openapi.yaml`: sem mudança de contrato ou endpoint
- `design-system/mobile/`: correção de persistência sem alteração visual estrutural

## Handoff

- `.agents/state/handoffs/TASK-261.md`

## Arquivos alterados

- `tasks/change-requests/261-persistir-limpeza-de-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-261.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/notifications/storage/dismissedNotificationsStorage.ts`
- `mobile/src/features/notifications/storage/dismissedNotificationsStorage.test.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/notifications/storage/dismissedNotificationsStorage.ts src/features/notifications/storage/dismissedNotificationsStorage.test.ts` - ok
- `cd mobile && npm run typecheck` - ok
- `cd mobile && npx jest src/features/notifications/storage/dismissedNotificationsStorage.test.ts --runInBand` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo, conforme registrado na Task 260

## Status final

done
