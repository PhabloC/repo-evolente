# Task 034 - Recriar fundo ilustrado auth web

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

artefato documental + print de login + implementacao existente

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- `design-system/front/prints/login-desktop.png`
- `front-end/src/layout/AuthLayout/**`

## Origem da solicitacao

Pedido do usuario para remover o SVG da Task 033 e recriar o fundo das telas de login/cadastro com formas ou imagens relacionadas ao intuito da plataforma.

## Objetivo

Substituir integralmente a decoracao anterior por uma composicao vetorial elegante, leve e relacionada ao acompanhamento do desenvolvimento infantil.

## Escopo

- Remover a composicao SVG implementada na Task 033
- Criar uma nova ilustracao vetorial no `AuthLayout`
- Relacionar a linguagem visual a crescimento, marcos e desenvolvimento infantil
- Manter movimento sutil e suporte a `prefers-reduced-motion`
- Preservar formularios, conteudo e fluxo das telas auth

## Fora de escopo

- Alteracoes de fluxo ou autenticacao
- Backend e mobile
- Imagens raster externas

## Dependencias

- Task 033 - done

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
- `.agents/state/handoffs/TASK-033.md`

## Contexto sob demanda

| Gatilho | Fonte | Obrigatorio? |
|---|---|---|
| UI web auth | `design-system/front/Design_System_Evolente_Desktop.md` | sim |
| Fidelidade da tela | `design-system/front/prints/login-desktop.png` | sim |
| Recriar ilustracao | `front-end/src/layout/AuthLayout/index.tsx` e `styles.module.css` | sim |
| Regras locais e acessibilidade | `front-end/AGENTS.md`, `front-end/docs/ai/AGENTS.md`, `front-end/docs/ai/ACCESSIBILITY.md` | sim |

## Orçamento de contexto

- Risco: baixo
- Estrategia: limitar leitura ao template auth, referencia visual e regras locais diretamente aplicaveis

## Criterios de conclusao

- [x] Composicao da Task 033 removida integralmente
- [x] Novo fundo vetorial relacionado ao desenvolvimento infantil
- [x] Animacao sutil sem prejudicar legibilidade ou interacao
- [x] Responsividade e `prefers-reduced-motion` preservados
- [x] Lint e build executados com sucesso

## Resultado da execucao

- O fundo abstrato da Task 033 foi substituido integralmente por uma ilustracao SVG ligada ao produto.
- A nova composicao apresenta uma trilha de marcos de evolucao, personagem acolhedora, balao de comunicacao, ondas sonoras e blocos ludicos.
- Os elementos ocupam as bordas e mantem a regiao central livre para leitura e interacao com os formularios.
- As animacoes foram distribuidas por detalhe, com movimento curto e baixa intensidade.

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md` e `tasks/000-index.md`
- `tasks/slices/014-template-auth-unificado.md`
- `.agents/state/handoffs/TASK-033.md`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `design-system/front/prints/login-desktop.png`
- `front-end/AGENTS.md`, `front-end/docs/ai/AGENTS.md` e `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/layout/AuthLayout/index.tsx` e `styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-034.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `tasks/change-requests/034-recriar-fundo-ilustrado-auth-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-034.md`

## Validacoes executadas

- `npm run lint` em `front-end/` - ok
- `npm run build` em `front-end/` - ok
- Acessibilidade: SVG decorativo oculto da arvore acessivel e animacoes desativadas com `prefers-reduced-motion`

## Pendencias pos-task

- Nenhuma pendencia tecnica.

## Status final

done
