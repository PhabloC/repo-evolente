# Task 308 - Limitar largura maxima das acoes do header web

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

feedback direto do usuario sobre o header da trilha

### Cobertura

- bloco da direita do header com busca, notificacoes e acoes de pagina

### Lacunas

- sem novo mock dedicado; a tarefa deve limitar a largura maxima do conteudo da direita para ele nao empurrar o heading

## Objetivo

Conter a largura do bloco de acoes do header compartilhado para reduzir a disputa horizontal com o titulo e subtitulo da pagina.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-307.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | preservar semantica e manter o escopo no header | sim |
| Header compartilhado | `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | limitar a largura maxima do bloco de acoes/busca | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas o CSS do `Header` compartilhado e validar com testes/lint focados

## Criterios de conclusao

- [x] o bloco da direita do header tem largura maxima controlada
- [x] a busca continua abrindo e fechando normalmente
- [x] a mudança nao exige alterar as paginas consumidoras
- [x] validacoes focadas passam

## Dependencias

- Task 298 - done
- Task 305 - done
- Task 307 - done

## Resultado da execucao

- o contêiner de ações do header passou a ter largura maxima no desktop
- a área de busca continua com a largura reservada, mas agora o conjunto da direita fica contido e deixa mais respiro para o heading
- nenhuma página consumidora precisou ser alterada

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-307.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteracao de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao header web compartilhado
- páginas consumidoras, porque a correção continuou centralizada no layout

## Handoff

- `.agents/state/handoffs/TASK-308.md`

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- `tasks/change-requests/308-limitar-largura-maxima-das-acoes-do-header-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-308.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
