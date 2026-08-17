# Handoff - Task 306

## Task

- identificador: 306
- titulo: Corrigir header da trilha da crianca ao abrir busca web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: eliminar a regressao restante do header na pagina da trilha da crianca
- entrega verificavel: a abertura da busca deixa titulo e subtitulo estaveis mesmo com as acoes do topo presentes

## Decisoes preservadas

- a correção ficou no `Header` compartilhado, sem reestruturar a pagina da trilha
- paginas com acoes no topo passaram a usar heading e acoes em linhas separadas no desktop, evitando competicao horizontal
- o comportamento funcional da busca permaneceu igual ao da Task 298/305

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/306-corrigir-header-da-trilha-da-crianca-ao-abrir-busca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-305.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | UI web | preservar semantica e isolar a mudanca ao layout |
| `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | header compartilhado | separar heading e acoes quando houver acoes proprias |
| `front-end/src/pages/Main/Plans/{PatientTrail/index.tsx,styles.module.css}` | regressao da trilha | confirmar o consumidor afetado |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteracao de contrato |
| `backend/` | sem mudanca funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: header da trilha estabilizado ao abrir a busca com acoes no topo
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `tasks/change-requests/306-corrigir-header-da-trilha-da-crianca-ao-abrir-busca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx`: ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se aparecer outra regressao visual em paginas que usam acoes no topo do header

## Proximo contexto recomendado

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`

## Contexto que nao deve ser carregado

- `backend/`
- `mobile/`
