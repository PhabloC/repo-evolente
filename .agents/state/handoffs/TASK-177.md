# Handoff - Task 177

## Task

- identificador: 177
- título: Remover scroll-behavior smooth global no front-end
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negócio: scroll nativo sem animação global
- entrega verificável: ausência de `scroll-behavior: smooth` no CSS global

## Decisões preservadas

- decisão: remover `scroll-behavior: smooth` do `html`
- motivo: sensação de scroll lento/travado na página
- impacto: rolagem volta ao comportamento nativo do browser

## Contexto utilizado

### Contexto mínimo lido

- `tasks/change-requests/177-remover-scroll-behavior-smooth-global.md`
- `front-end/src/styles/global.css`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/styles/global.css` | remoção | implementação |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `mobile/` | fora de escopo |
| `contracts/openapi.yaml` | sem API |

## Resultado por stack

- front-end: `scroll-behavior: smooth` removido
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/styles/global.css`
- `tasks/change-requests/177-remover-scroll-behavior-smooth-global.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-177.md`

## Validações executadas

- grep sem matches de `scroll-behavior` no front-end

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- se o modal continuar lento, remover `backdrop-filter: blur` do Modal

## Próximo contexto recomendado

- `front-end/src/ui/Modal/styles.module.css`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `mobile/`, `backend/`
- motivo: mudança só no CSS global web
