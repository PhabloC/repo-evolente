# Task 306 - Corrigir header da trilha da crianca ao abrir busca web

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

feedback direto do usuario com print da pagina da trilha

### Cobertura

- header da pagina da trilha da crianca
- interacao de abertura da busca compartilhada

### Lacunas

- sem novo mock dedicado; a tarefa deve impedir que o subtitulo seja empurrado quando a busca abre na pagina que possui acoes no topo

## Objetivo

Eliminar a regressao restante na pagina da trilha da crianca, mantendo titulo e subtitulo estaveis quando a busca do header abre em conjunto com as acoes da pagina.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-305.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | preservar semantica e limitar o escopo ao layout compartilhado | sim |
| Header compartilhado | `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | separar heading e acoes quando a pagina tiver acoes proprias | sim |
| Regressao da trilha | `front-end/src/pages/Main/Plans/{PatientTrail/index.tsx,styles.module.css}` | confirmar o consumidor afetado e preservar o layout local | sim |

## Orçamento de contexto

- baixo
- estrategia: centralizar a correção no `Header` e validar apenas o consumidor da trilha

## Criterios de conclusao

- [x] a abertura da busca nao empurra mais o subtitulo na pagina da trilha
- [x] o comportamento recente da busca continua preservado
- [x] as acoes do topo da trilha continuam acessiveis e estaveis
- [x] validacoes focadas passam

## Dependencias

- Task 298 - done
- Task 305 - done

## Resultado da execucao

- o `Header` passou a usar um layout em duas linhas quando a pagina injeta acoes proprias no topo, evitando competicao horizontal entre heading, busca e CTAs
- a pagina da trilha da crianca herdou a correção sem precisar de ajuste estrutural proprio
- a busca continuou com foco automatico, input estavel e fechamento apenas pelo botao dedicado

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-305.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}`
- `front-end/src/pages/Main/Plans/{PatientTrail/index.tsx,styles.module.css}`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteracao de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao header web compartilhado
- outras paginas internas, porque a regressao foi isolada ao caso com acoes no topo da trilha

## Handoff

- `.agents/state/handoffs/TASK-306.md`

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `tasks/change-requests/306-corrigir-header-da-trilha-da-crianca-ao-abrir-busca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-306.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
