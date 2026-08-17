# Task 208 - Header da home: Olá, avatar à esquerda, lupa e sino

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

- reuso: `AuthResponse.user.avatarUrl` (já no OpenAPI) para exibir foto quando existir
- sem endpoint novo; busca (lupa) sem tela dedicada nesta task

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 010 - App do responsavel: home, perfil e notificacoes

### Arquivo do slice

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system + pedido explícito de UI

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- pedido do produto: saudação "Olá", nome sem "Olá,", foto à esquerda, lupa e sino à direita

## Contexto de negocio

### Por que

O cabeçalho da home do responsável ainda usa "Bem-vindo de volta" / "Olá, {nome}" com avatar à direita, fora do padrão pedido agora.

### O que

Reorganizar o `HomeHeader` da home do responsável.

### Comportamento esperado

- texto superior: `Olá` (não "Bem-vindo de volta")
- nome sem prefixo "Olá,"
- foto/avatar de perfil à esquerda (fallback para inicial se sem `avatarUrl`)
- à direita: ícone de lupa (pesquisa) e ícone de sino (notificações)
- sino abre a aba/tela de avisos já existente
- lupa fica no header; fluxo de busca completo fora de escopo se não houver tela

### Fora de escopo

- implementar tela/fluxo completo de busca
- upload de avatar
- mudanças no design-system documental
- alterações web/backend

## Dependencias

- Task 122
- Task 123
- Slice 027 (avatar no contrato/bucket)

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Header home | `mobile/src/features/shell/components/HomeHeader/` | reorganizar layout e copy | sim |
| Home responsável | `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx` | passar props (avatar, callbacks, badge) | sim |
| Sessão / avatar | `mobile/src/features/auth/types/session.ts`, `adaptSession.ts` | mapear `avatarUrl` do login | sim |
| Ícones | lucide-react-native (`Search`, `Bell`) | lupa e sino | sim |
| Notificações | hooks/navigator existentes | wire do sino | sim |

## Orcamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a `HomeHeader`, home do responsável e mapeamento mínimo de `avatarUrl` na sessão

## Criterios de conclusao

- header mostra "Olá" + nome sem "Olá,"
- avatar à esquerda; lupa e sino à direita
- sino navega para avisos
- foto usa `avatarUrl` quando disponível; senão inicial
- lint/typecheck mobile ok no escopo alterado

## Resultado da execucao

- `HomeHeader` agora exibe: avatar (foto ou inicial) à esquerda, "Olá" + nome no centro, lupa e sino à direita.
- Sino abre avisos (`onOpenNotifications`) e mostra ponto de não lidos.
- Avatar abre perfil quando `onOpenProfile` é passado.
- Sessão mobile passou a mapear `avatarUrl` do `AuthResponse` (fallback `null` → inicial).
- Lupa presente no header; fluxo de busca completo permanece fora de escopo.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 208, slice 010
- contexto sob demanda: `HomeHeader/`, `ResponsavelHomeScreen.tsx`, `session.ts`, `adaptSession.ts`
- contexto evitado: `front-end/`, `backend/`, tela de busca

## Handoff

- `.agents/state/handoffs/TASK-208.md`

## Arquivos alterados

- `mobile/src/features/shell/components/HomeHeader/index.tsx`
- `mobile/src/features/shell/components/HomeHeader/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/auth/types/session.ts`
- `mobile/src/features/auth/adapters/adaptSession.ts`
- `mobile/src/features/auth/adapters/adaptSession.test.ts`
- `tasks/change-requests/208-header-home-ola-avatar-lupa-sino-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-208.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm test -- --testPathPattern=adaptSession` — ok (3 testes)
- `cd mobile && npm run lint` — ok (2 warnings antigos em `alphabetWritingGame.ts`)

## Pendencias pos-task

- fluxo/tela de busca ao tocar na lupa ainda não existe

## Status final

done
