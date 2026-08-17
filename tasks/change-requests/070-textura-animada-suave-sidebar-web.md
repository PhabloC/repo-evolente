# Task 070 - Adicionar textura animada suave no sidebar web

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

- nao se aplica; ajuste visual sem alteracao de integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre o sidebar

### Cobertura

- fundo do sidebar autenticado
- efeito de bolhas subindo com movimento bem suave

### Lacunas

- sem nova imagem de referencia para o padrão exato da textura
- decisao: usar bolhas abstratas em CSS, inspiradas em lava lamp, com baixa opacidade e animacao lenta para preservar legibilidade

## Objetivo

Adicionar um background com textura diferente e animacao sutil no sidebar da area autenticada web, sem competir com a navegacao.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-069.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar o objetivo visual da textura | sim |
| UI web | `lamp.md` | adaptar a estrutura HTML/CSS do efeito de lava lamp ao sidebar | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | garantir que a textura nao prejudique contraste e movimento | sim |
| Front-end | `front-end/src/layout/Sidebar/{index.tsx,styles.module.css}` | aplicar textura no shell compartilhado | sim |
| Front-end | `front-end/src/styles/global.css` | reutilizar tokens visuais existentes do shell | sim |

## Orçamento de contexto

- baixo
- estrategia: isolar a mudanca no `Sidebar` compartilhado e nos arquivos de rastreabilidade da task

## Criterios de conclusao

- [x] sidebar ganha textura visual distinta sem prejudicar leitura
- [x] animacao permanece suave e discreta
- [x] usuarios com `prefers-reduced-motion` nao recebem movimento desnecessario
- [x] build do front-end permanece aprovado

## Dependencias

- Task 041 - done

## Resultado da execucao

- o sidebar passou a usar uma adaptação do `lamp.md` com blobs reais, caps e filtro `goo`
- o conteudo interativo foi mantido acima da textura para preservar contraste e foco
- a animacao foi desligada em `prefers-reduced-motion`

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-069.md`

### Sob demanda

- feedback do usuario no chat
- `lamp.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/layout/Sidebar/{index.tsx,styles.module.css}`
- `front-end/src/styles/global.css`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao
- `backend/` e `mobile/` por estarem fora do escopo
- paginas de negocio por nao haver alteracao fora do shell compartilhado

## Handoff

- `.agents/state/handoffs/TASK-070.md`

## Arquivos alterados

- `front-end/src/layout/Sidebar/styles.module.css`
- `tasks/change-requests/070-textura-animada-suave-sidebar-web.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-070.md`

## Validacoes executadas

- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
