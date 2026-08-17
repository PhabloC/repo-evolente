# Handoff - Task 427

## Task

- identificador: 427
- título: Efeito de vidro sobre a capa do login web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 012
- objetivo de negócio: login visual web
- entrega verificável: vidro fosco sobre a capa do login

## Decisões preservadas

- decisão: blur na camada da imagem (`::before`) + verniz translúcido (`::after`)
- motivo: `backdrop-filter` sozinho não desfoca bem o background do mesmo elemento
- impacto: só com `coverBackground`

## Contexto utilizado

### Contexto mínimo lido

- Task 427, índice, handoff 426

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `AuthLayout/styles.module.css` | vidro | `.pageCover` |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| OpenAPI / mobile | n/a |

## Resultado por stack

- front-end: efeito vidro no login
- backend: n/a
- mobile: n/a

## Arquivos alterados

- `front-end/src/layout/AuthLayout/styles.module.css`
- `tasks/change-requests/427-efeito-vidro-capa-login-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-427.md`

## Validações executadas

- CSS aplicado; conteúdo com z-index acima do overlay

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- ajustar intensidade do blur/opacidade se o usuário pedir

## Próximo contexto recomendado

- `.pageCover` em `AuthLayout/styles.module.css`

## Contexto que não deve ser carregado na próxima etapa

- requirements / OpenAPI
