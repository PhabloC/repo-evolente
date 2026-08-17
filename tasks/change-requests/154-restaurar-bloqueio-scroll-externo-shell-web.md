# Task 154 - Restaurar bloqueio do scroll externo no shell web

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

- nao se aplica; ajuste de layout sem alterar integracoes

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste incremental solicitado no chat

### Fonte primaria visual

- `front-end/src/layout/MainLayout/{index.tsx,styles.module.css}`

### Lacunas

- sem print dedicado
- decisao: restaurar o bloqueio do scroll do documento no shell autenticado e preservar apenas o scroll interno da area de conteudo

## Objetivo

Eliminar o scroll da página inteira no shell autenticado web, mantendo apenas o scroll interno do conteúdo da tela.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-079.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Shell autenticado | `front-end/src/layout/MainLayout/{index.tsx,styles.module.css}` | restaurar o bloqueio do overflow externo no desktop | sim |
| Layout global | `front-end/src/styles/global.css` | validar o impacto do documento raiz | sim |
| Acessibilidade web | `front-end/docs/ai/ACCESSIBILITY.md` | validar que o ajuste nao quebra foco e navegação | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao shell autenticado compartilhado e ao documento raiz, sem tocar páginas internas

## Criterios de conclusao

- [x] scroll externo do documento nao aparece no shell autenticado desktop
- [x] scroll interno do painel de conteúdo continua funcional
- [x] lint e build do front-end aprovados

## Dependencias

- Task 079 - done
- Task 152 - done

## Resultado da execucao

- o `MainLayout` voltou a sincronizar `html`, `body` e `#root` com `overflow: hidden` no desktop autenticado, eliminando o scroll externo do documento
- a sincronização respeita o breakpoint mobile; abaixo de `960px` o documento volta ao comportamento natural para não quebrar a navegação responsiva
- o scroll vertical continua restrito à área `.content`, preservando o comportamento esperado das páginas internas

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-079.md`

### Sob demanda

- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/layout/MainLayout/styles.module.css`
- `front-end/src/styles/global.css`
- `front-end/docs/ai/ACCESSIBILITY.md`

### Contexto evitado

- páginas internas do shell, backend e mobile por nao participarem da origem do overflow externo

## Handoff

- `.agents/state/handoffs/TASK-154.md`

## Arquivos alterados

- `tasks/change-requests/154-restaurar-bloqueio-scroll-externo-shell-web.md`
- `front-end/src/layout/MainLayout/index.tsx`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-154.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
