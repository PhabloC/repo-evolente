# Task 307 - Limitar largura do heading no header da trilha web

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

- nao se aplica; ajuste de layout no header compartilhado da web

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre a pagina da trilha

### Cobertura

- header compartilhado da trilha da crianca
- bloco de titulo e subtitulo a esquerda

### Lacunas

- sem novo mock dedicado; a tarefa deve restaurar o layout original e impedir o deslocamento do texto apenas com limite de largura no heading

## Objetivo

Voltar o header ao comportamento estrutural anterior e corrigir a instabilidade restante limitando a largura maxima do conteudo textual à esquerda.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-306.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | preservar semantica e manter o escopo no header | sim |
| Header compartilhado | `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | reverter o layout em duas linhas e limitar a largura do heading | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas o `Header` compartilhado e suas validacoes focadas

## Criterios de conclusao

- [x] o header volta à estrutura anterior
- [x] o bloco de texto à esquerda ganha largura maxima para evitar o deslocamento
- [x] o comportamento da busca continua preservado
- [x] validacoes focadas passam

## Dependencias

- Task 298 - done
- Task 305 - done
- Task 306 - done

## Resultado da execucao

- a estrutura especial em duas linhas para páginas com ações foi removida do `Header`
- o bloco de heading voltou ao layout anterior e recebeu largura maxima controlada para reduzir a disputa horizontal com busca e ações
- a busca seguiu com foco automatico, input estavel e fechamento apenas pelo botao dedicado

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-306.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteracao de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao header web compartilhado
- páginas consumidoras, porque a correção continuou centralizada no layout

## Handoff

- `.agents/state/handoffs/TASK-307.md`

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `tasks/change-requests/307-limitar-largura-do-heading-no-header-da-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-307.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
