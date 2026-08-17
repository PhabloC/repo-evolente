# Handoff - Task 208

## Task

- identificador: 208
- título: Header da home: Olá, avatar à esquerda, lupa e sino
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010 - App do responsavel: home, perfil e notificacoes
- objetivo de negócio: Completar mobile do responsavel com home, perfil e base de notificacoes
- entrega verificável: Header da home com Olá, avatar à esquerda, lupa e sino à direita

## Decisões preservadas

- decisão: saudação superior = "Olá"; nome sem prefixo "Olá,"
- motivo: pedido explícito de produto
- impacto: copy do `HomeHeader` alterada

- decisão: avatar/foto à esquerda; lupa e sino à direita
- motivo: pedido explícito de layout
- impacto: reorganização do `HomeHeader`; sino abre avisos; lupa sem tela dedicada nesta task

- decisão: mapear `avatarUrl` na sessão mobile a partir do `AuthResponse`
- motivo: exibir foto real quando o login já a devolve
- impacto: `Session.user.avatarUrl` + fallback para inicial

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/208-header-home-ola-avatar-lupa-sino-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `HomeHeader/` | layout do header | reorganizar UI |
| `ResponsavelHomeScreen.tsx` | wire de props | avatar, unread, callbacks |
| `session.ts` / `adaptSession.ts` | foto de perfil | mapear `avatarUrl` |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `front-end/` | task mobile only |
| `backend/` | sem mudança de API |
| tela de busca | fora de escopo |

## Resultado por stack

- front-end ou next-js: nao se aplica
- backend: nao se aplica
- mobile: header da home atualizado

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

## Validações executadas

- validação: `npm run typecheck` (mobile) — ok
- validação: `npm test -- --testPathPattern=adaptSession` — ok (3 testes)

## Pendências ou bloqueios

- item: fluxo/tela de busca ao tocar na lupa ainda não existe

## Próxima ação sugerida

- se desejado: criar task para tela/fluxo de pesquisa no app do responsável

## Próximo contexto recomendado

- `HomeHeader/` e `ResponsavelHomeScreen.tsx` se for conectar a lupa

## Contexto que não deve ser carregado na próxima etapa

- fonte: `contracts/openapi.yaml` completo
- motivo: avatar já coberto pelo AuthResponse existente
