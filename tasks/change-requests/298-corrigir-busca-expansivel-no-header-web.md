# Task 298 - Corrigir busca expansível no header web

## Status

in_progress

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica; ajuste comportamental e visual no header web

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre comportamento da busca

### Cobertura

- busca expansivel do header das paginas internas web

### Lacunas

- sem novo print; a mudanca deve preservar o visual atual e corrigir a interacao

## Objetivo

Separar a acao de abrir/fechar da busca expansivel do header para que o clique no campo de texto nao recolha a busca, com um icone proprio para fechar.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-297.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | validar semântica e foco do campo expansível | sim |
| Header | `front-end/src/layout/Header/{index.tsx,styles.module.css}` | corrigir a busca expansível | sim |
| Testes | `front-end/src/layout/Header/**/*.test.tsx` | cobrir abrir, manter aberto ao focar e fechar | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao componente de header compartilhado e a testes focados do proprio componente

## Criterios de conclusao

- [x] clicar na lupa abre a busca sem fechar ao clicar no input
- [x] existe um icone proprio para fechar a busca
- [x] testes focados do header passam

## Dependencias

- Task 297 - done

## Resultado da execucao

- a busca expansivel do header deixou de usar um `input` aninhado dentro do botao da lupa
- a interacao foi separada em tres partes: abrir pela lupa, digitar no campo sem recolher e fechar por um icone dedicado
- o campo agora recebe foco automatico ao abrir, preservando a fluidez do uso por teclado e mouse

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-297.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}`
- `front-end/src/pages/Main/Patients/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve integracao
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao header web compartilhado
- outras paginas internas, porque a mudanca foi centralizada no componente de layout

## Handoff

- `.agents/state/handoffs/TASK-298.md`

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `tasks/change-requests/298-corrigir-busca-expansivel-no-header-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-298.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx src/pages/Main/Patients/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

## Status

done
