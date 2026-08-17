# Task 028 - Template do login em criar conta e recuperar senha

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

prints de telas

### Fonte primaria visual

- `design-system/front/prints/login-desktop.png` (shell visual)
- apoio: layout ja implementado em Login (Task 026)

## Origem da solicitacao

Pedido do usuario: criar conta e recuperar senha devem usar o template do login.

## Objetivo

Extrair o shell visual do login para layout compartilhado e aplicar em cadastro e recuperacao de senha.

## Escopo

- Extrair template (branding + card + trust) para `AuthLayout`
- Refatorar Login para usar o layout compartilhado
- Aplicar em: RegisterProfessional, RegisterGuardian, PasswordRecovery, PasswordReset
- Manter formularios/logica existentes
- Card `wide` para cadastros longos
- Atualizar testes afetados
- Validar lint/test/build

## Fora de escopo

- Mobile
- API
- Mudar fluxos de negocio

## Dependencias

- Task 026, 027 — done

## Slice vertical

### Identificador do slice

Slice 014 - Template auth unificado

### Arquivo do slice

- `tasks/slices/014-template-auth-unificado.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/014-template-auth-unificado.md`

## Contexto sob demanda

| Gatilho | Fonte | Obrigatorio? |
|---|---|---|
| Shell login | Login/** | sim |
| Layout | AuthLayout/** | sim |
| Telas alvo | Register*, Password* | sim |

## Orçamento de contexto

- Risco: baixo

## Criterios de conclusao

- [x] Layout compartilhado com visual do login
- [x] Cadastros e recovery/reset no template
- [x] Login sem duplicar shell
- [x] Testes/lint/build ok

## Resultado da execucao

### Resumo por stack

- **front-end**: `AuthLayout` virou o template marketing do login (branding + card + footer). Login, cadastros, recovery/reset e SubscriptionGate (herdado) usam o mesmo shell. Cadastros mantêm `wide`.

### Relação com o slice

- Slice 014 concluído.

### Decisões técnicas

- Extrair shell para AuthLayout em vez de layout paralelo.
- Titulo do card = `h2`; headline de marca = `h1`.
- CTA primario rosa nas telas auth migradas.
- PasswordReset incluido por ser continuidade do fluxo de recovery.

### Trade-offs

- SubscriptionGate tambem herdou o visual (usa AuthLayout) — consistente, fora do pedido explicito mas sem custo extra.

## Contexto utilizado

### Contexto mínimo

- AGENTS, GUIDE, context-map, index, esta task, slice 014

### Contexto sob demanda

| Fonte | Uso |
|---|---|
| Login + AuthLayout | extracao |
| Register*/Password* | aplicacao |

### Evitado

- mobile/, backend/, openapi

## Handoff

- Caminho: `.agents/state/handoffs/TASK-028.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/**`
- `front-end/src/pages/Auth/Login/**`
- `front-end/src/pages/Auth/PasswordRecovery/**`
- `front-end/src/pages/Auth/PasswordReset/**`
- `front-end/src/pages/Auth/RegisterProfessional/**`
- `front-end/src/pages/Auth/RegisterGuardian/**`
- governanca: slice 014, CR-028, index, handoff

## Validacoes executadas

- `npm run test -- --run src/pages/Auth` — ok
- `npm run lint` — ok
- `npm run build` — ok

## Pendencias pos-task

- Nenhuma

## Status final

done
