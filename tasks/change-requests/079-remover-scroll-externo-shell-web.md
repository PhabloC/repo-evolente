# Task 079 - Remover scroll externo do shell web

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
- decisao: preservar o comportamento atual do scroll interno do painel autenticado e eliminar apenas o scroll externo do documento no desktop

## Objetivo

Remover o scroll externo lateral do shell autenticado web, mantendo apenas o scroll do conteúdo da página.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-078.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Shell autenticado | `front-end/src/layout/MainLayout/{index.tsx,styles.module.css}` | corrigir o overflow do documento e preservar o scroll interno | sim |
| Layout global | `front-end/src/styles/global.css` | validar o impacto do documento raiz | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao shell compartilhado autenticado, sem tocar as páginas internas individualmente

## Criterios de conclusao

- [x] scroll externo do documento deixa de aparecer no shell autenticado desktop
- [x] scroll interno do painel de conteúdo continua funcional
- [x] lint e build do front-end aprovados

## Dependencias

- Task 078 - done

## Resultado da execucao

- o `MainLayout` passou a sincronizar o overflow de `html/body` no desktop, bloqueando o scroll externo enquanto o shell autenticado estiver montado
- o comportamento continua responsivo: abaixo do breakpoint mobile o documento volta a rolar normalmente
- o scroll interno do painel `.content` foi preservado

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-078.md`

### Sob demanda

- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/layout/MainLayout/styles.module.css`
- `front-end/src/styles/global.css`

### Contexto evitado

- páginas internas do shell, backend e mobile por nao participarem da origem do overflow externo

## Handoff

- `.agents/state/handoffs/TASK-079.md`

## Arquivos alterados

- `front-end/src/layout/MainLayout/index.tsx`
- `tasks/change-requests/079-remover-scroll-externo-shell-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-079.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
