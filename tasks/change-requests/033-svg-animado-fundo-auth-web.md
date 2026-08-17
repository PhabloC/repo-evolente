# Task 033 - SVG animado elegante no fundo auth web

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

implementacao existente + print de login

### Fonte primaria visual

- `design-system/front/prints/login-desktop.png`
- apoio: `front-end/src/layout/AuthLayout/**`

## Origem da solicitacao

Pedido do usuario: adicionar desenhos de fundo com SVG animado mais elegante na pagina de login/cadastro.

## Objetivo

Reintroduzir um fundo decorativo sofisticado nas telas auth web usando SVG animado leve e sutil.

## Escopo

- Adicionar SVG decorativo ao `AuthLayout`
- Aplicar animacoes suaves em camadas do SVG
- Respeitar `prefers-reduced-motion`
- Manter formularios e layout existentes
- Atualizar backlog e handoff

## Fora de escopo

- Mobile
- Mudancas de fluxo
- Canvas/WebGL

## Dependencias

- Task 028 — done
- Task 029 — done
- Task 032 — done

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
- `.agents/state/handoffs/TASK-032.md`

## Contexto sob demanda

| Gatilho | Fonte | Obrigatorio? |
|---|---|---|
| Inserir fundo animado | `front-end/src/layout/AuthLayout/index.tsx` | sim |
| Estilizar e animar SVG | `front-end/src/layout/AuthLayout/styles.module.css` | sim |
| Regras locais da stack | `front-end/AGENTS.md`, `front-end/docs/ai/AGENTS.md` | sim |

## Orçamento de contexto

- Risco: baixo

## Criterios de conclusao

- [x] Fundo SVG elegante presente nas telas auth web
- [x] Animacao sutil sem interferir na usabilidade
- [x] `prefers-reduced-motion` suportado
- [x] Lint da stack web executado com sucesso

## Resultado da execucao

### Resumo por stack

- **front-end**: `AuthLayout` passou a renderizar um fundo SVG com orbs difusos, linhas orgânicas e pontos de destaque animados de forma suave, substituindo o fundo neutro por uma camada visual mais refinada.

### Relação com o slice

- Slice 014 mantido; refinamento visual incremental no template auth compartilhado.

### Decisões técnicas

- SVG inline no layout para facilitar ajuste fino de composição e responsividade.
- Animações separadas por camadas (`orbs`, `lines`, `sparks`) para movimento discreto.
- Fallback acessível com `prefers-reduced-motion: reduce`.

### Trade-offs

- Há mais CSS e markup do que no fundo neutro, mas com custo baixo e controle visual melhor do que imagens raster.

## Contexto utilizado

### Contexto mínimo

- AGENTS, GUIDE, context-map, index, esta task, slice 014, handoff 032

### Contexto sob demanda

| Fonte | Uso |
|---|---|
| `front-end/src/layout/AuthLayout/index.tsx` | inserir SVG |
| `front-end/src/layout/AuthLayout/styles.module.css` | animacoes e responsividade |
| `front-end/AGENTS.md` e `front-end/docs/ai/AGENTS.md` | validacao de regras locais |

### Evitado

- backend
- mobile
- requirements
- openapi

## Handoff

- Caminho: `.agents/state/handoffs/TASK-033.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `tasks/change-requests/033-svg-animado-fundo-auth-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-033.md`

## Validacoes executadas

- `npm run lint` — ok

## Pendencias pos-task

- Nenhuma

## Status final

done

