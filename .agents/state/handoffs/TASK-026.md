# Handoff - Task 026

## Task

- identificador: 026
- título: Login visual e acesso livre web
- tipo: front
- modo de execução: single-stack
- status final: done
- arquivo: `tasks/change-requests/026-login-visual-acesso-livre-web.md`

## Slice vertical

- identificador: Slice 012 - Login visual e acesso livre (web)
- objetivo de negócio: login aderente ao print + exploração sem auth
- entrega verificável: UI login + bypass guards
- status do slice: done

## Decisões preservadas

- decisão: layout dedicado na LoginPage (sem alterar AuthLayout)
- motivo: outras telas auth não devem herdar a landing do print
- impacto: AuthLayout permanece para recovery/reset/cadastros

- decisão: assets renomeados para `logo-wordmark.webp` e `logo-seal.webp`
- motivo: nomes com espaço quebram ergonomia de import
- impacto: imports estáveis via `@/assets/`

- decisão: "Criar conta" → `/cadastro/profissional` + link "Cadastro responsável"
- motivo: print tem um CTA; produto tem dois fluxos
- impacto: profissional como default do CTA outline

- decisão: bypass em PrivateRoutes/RoleGuard quando `!isAuthenticated`
- motivo: pedido de acesso livre sem login
- impacto: área principal navegável; sidebar guest = itens profissional
- reversão: remover early-returns e restaurar redirect para `/login`

- decisão: mascote do print omitido
- motivo: sem asset dedicado
- impacto: apenas formas CSS decorativas

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, CR-026, slice 012

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/prints/login-desktop.png` | UI | layout |
| DS Desktop | tokens | cores |
| assets logos | branding | wordmark/selo |
| docs/ai ARCHITECTURE + CODE_STYLE | front | padrões |
| Login/guards/nav | código | implementação |

### Evitado

- mobile/, backend/, openapi, requirements

## Arquivos alterados

- `front-end/src/pages/Auth/Login/**`
- `front-end/src/routes/PrivateRoutes.tsx`
- `front-end/src/routes/RoleGuard.tsx`
- `front-end/src/constants/navigation.ts`
- `front-end/src/assets/logo-*.webp`
- governança: slice 012, CR-026, index, print, este handoff

## Validações executadas

- lint ok
- test Login ok
- build ok

## Pendências

- Reverter bypass antes de produção
- Asset do mascote (opcional)

## Próxima ação sugerida

- Revisar visualmente `/login` no browser; se ok, seguir próxima CR ou reativar guards quando auth for obrigatória

## Próximo contexto recomendado

- Handoff desta task + CR futura de hardening de auth, se houver
- Não carregar mobile/backend para ajustes só de login web

## Contexto que não deve ser carregado

- `mobile/`, `backend/`, `contracts/openapi.yaml`, requirements inteiros
