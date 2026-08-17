# Task 072 - Efeito de fundo nas telas de login e cadastro

## Status

cancelled

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica; ajuste visual sem alteracao de integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 014 - Template auth unificado
- `tasks/slices/014-template-auth-unificado.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

feedback direto do usuario + tokens da marca Evolente

### Fonte primaria visual

- `front-end/src/layout/AuthLayout/{index.tsx,styles.module.css}`
- `front-end/src/styles/global.css` (tokens pink/blue/green/beige)
- padrao de movimento suave ja usado no sidebar (Task 070), adaptado a pagina auth clara

### Lacunas

- sem print novo do efeito; decisao: orbes/gradient blobs suaves e animados em baixa opacidade, sem competir com card e branding
- evitar ilustracao pesada das Tasks 033/034 que foi removida na 035

## Objetivo

Adicionar um efeito de fundo animado e discreto no background das telas de login/cadastro (via AuthLayout compartilhado).

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, `tasks/slices/014-template-auth-unificado.md`
- `.agents/state/handoffs/TASK-035.md`, `.agents/state/handoffs/TASK-070.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/layout/AuthLayout/**` | aplicar o efeito no shell auth | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | contraste e `prefers-reduced-motion` | sim |
| Tokens | `front-end/src/styles/global.css` | cores da marca | sim |

## Orçamento de contexto

- baixo; isolado ao AuthLayout

## Criterios de conclusao

- [ ] AuthLayout ganha efeito de fundo animado e discreto
- [ ] login, cadastro e recovery herdam o efeito sem mudanças por página
- [ ] `prefers-reduced-motion` desliga a animação
- [ ] legibilidade do card e do branding permanece
- [ ] lint/test/build do front-end aprovados

## Dependencias

- Task 028 - done
- Task 035 - done
- Task 070 - done

## Resultado da execucao

- solicitação revertida a pedido do usuario
- `AuthLayout` voltou ao fundo plano `var(--color-bg)`, sem orbes/malha/animação

## Contexto utilizado

### Mínimo

- pedido de desfazer do usuario + arquivos alterados pela Task 072

### Sob demanda

- `AuthLayout`

## Handoff

- `.agents/state/handoffs/TASK-072.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx` (revertido)
- `front-end/src/layout/AuthLayout/styles.module.css` (revertido)
- `tasks/change-requests/072-efeito-fundo-auth-login-cadastro.md`
- `tasks/slices/014-template-auth-unificado.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-072.md`

## Validacoes executadas

- reversao manual do markup e CSS do AuthLayout

## Pendencias pos-task

- nenhuma

## Status final

cancelled
