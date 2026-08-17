# Task 032 - Remover formas de fundo da tela auth web

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

prints de telas + implementacao existente

### Fonte primaria visual

- `design-system/front/prints/login-desktop.png`
- apoio: `front-end/src/layout/AuthLayout/**`

## Origem da solicitacao

Pedido do usuario: remover as bolinhas/formas geometricas do fundo da pagina de login/cadastro.

## Objetivo

Remover os elementos decorativos de fundo do template compartilhado das telas auth web.

## Escopo

- Remover markup decorativo do `AuthLayout`
- Remover estilos nao utilizados das formas de fundo
- Preservar layout, branding, card e formularios existentes
- Atualizar backlog e handoff

## Fora de escopo

- Mobile
- Alteracoes de fluxo
- Redesign do restante da tela auth

## Dependencias

- Task 028 — done
- Task 029 — done

## Slice vertical

### Identificador do slice

Slice 014 - Template auth unificado

### Arquivo do slice

- `tasks/slices/014-template-auth-unificado.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/014-template-auth-unificado.md`
- `.agents/state/handoffs/TASK-031.md`

## Contexto sob demanda

| Gatilho | Fonte | Obrigatorio? |
|---|---|---|
| Remover fundo decorativo | `front-end/src/layout/AuthLayout/index.tsx` | sim |
| Limpar estilos das formas | `front-end/src/layout/AuthLayout/styles.module.css` | sim |
| Regras locais da stack | `front-end/AGENTS.md`, `front-end/docs/ai/AGENTS.md` | sim |

## Orçamento de contexto

- Risco: baixo

## Criterios de conclusao

- [x] Formas geometricas removidas das telas auth web
- [x] `AuthLayout` sem markup/estilos mortos do fundo
- [x] Lint da stack web executado com sucesso

## Resultado da execucao

### Resumo por stack

- **front-end**: removido o bloco decorativo absoluto do `AuthLayout`, eliminando as bolinhas/formas do fundo em login, cadastro, recovery, reset e gate que reutilizam o template.

### Relação com o slice

- Slice 014 mantido; ajuste visual incremental no template compartilhado.

### Decisões técnicas

- Remoção no layout compartilhado em vez de override por página.
- Limpeza dos seletores `.decor`/`.shape*` para evitar CSS órfão.

### Trade-offs

- O fundo fica mais limpo e neutro; perde apenas a camada decorativa, sem impacto funcional.

## Contexto utilizado

### Contexto mínimo

- AGENTS, GUIDE, context-map, index, esta task, slice 014, handoff 031

### Contexto sob demanda

| Fonte | Uso |
|---|---|
| `front-end/src/layout/AuthLayout/index.tsx` | remover markup |
| `front-end/src/layout/AuthLayout/styles.module.css` | remover estilos |
| `front-end/AGENTS.md` e `front-end/docs/ai/AGENTS.md` | validacao de regras locais |

### Evitado

- backend
- mobile
- requirements
- openapi

## Handoff

- Caminho: `.agents/state/handoffs/TASK-032.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `tasks/change-requests/032-remover-formas-fundo-auth-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-032.md`

## Validacoes executadas

- `npm run lint` — ok

## Pendencias pos-task

- Nenhuma

## Status final

done

