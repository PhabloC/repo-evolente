# Handoff - Task 426

## Task

- identificador: 426
- título: Fundo capa na tela de login web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 012
- objetivo de negócio: login visual web
- entrega verificável: fundo `capa-tela-login.webp` só em `/login`

## Decisões preservadas

- decisão: prop opcional `coverBackground` no AuthLayout
- motivo: cadastro/recovery/gate não devem herdar a capa automaticamente
- impacto: Login passa `coverBackground`; demais telas inalteradas

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/426-fundo-capa-login-web.md`
- `tasks/slices/012-login-visual-acesso-livre.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/layout/AuthLayout/` | fundo auth | prop + CSS |
| `front-end/src/pages/Auth/Login/` | login | ativar capa |
| `front-end/src/assets/capa-tela-login.webp` | asset | imagem |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem API |
| `mobile/` | fora de escopo |

## Resultado por stack

- front-end: capa cover no login via AuthLayout
- backend: n/a
- mobile: n/a

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `front-end/src/pages/Auth/Login/index.tsx`
- `tasks/change-requests/426-fundo-capa-login-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-426.md`

## Validações executadas

- vitest Login: 1 passed

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- revisar contraste do texto de branding sobre a capa, se necessário

## Próximo contexto recomendado

- `front-end/src/layout/AuthLayout/styles.module.css` (`.pageCover`)

## Contexto que não deve ser carregado na próxima etapa

- requirements / OpenAPI / mobile — sem mudança
