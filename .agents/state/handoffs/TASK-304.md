# Handoff - Task 304

## Task

- identificador: 304
- titulo: Scroll no card de histórico recente web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: tornar o histórico recente mais usável sem crescer demais na página de trilha
- entrega verificavel: o card `Histórico recente` passa a ter rolagem interna

## Decisoes preservadas

- a mudança ficou restrita ao card lateral do histórico recente, preservando gráfico e resumo superior
- a lista de conclusões foi encapsulada em um contêiner scrollável com altura máxima estável
- foi adicionada uma referência acessível à lista rolável para reforçar a validação automatizada

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/304-scroll-no-card-de-historico-recente-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-303.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | manter o card scrollável com semântica mínima |
| `front-end/docs/ai/COMPONENT_REUSE.md` | escopo local | limitar a mudança ao card de histórico |
| `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | histórico recente | inserir o contêiner rolável |
| `front-end/src/pages/Main/Plans/styles.module.css` | scroll interno | aplicar altura máxima e overflow |
| `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | validação | cobrir a lista rolável |
| `front-end/src/pages/Main/Plans/index.test.tsx` | regressão leve | manter integridade da área de planejamentos |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de contrato |
| `backend/` | sem mudança funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: card de histórico recente com scroll interno
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/304-scroll-no-card-de-historico-recente-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx`: ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido para paginação ou agrupamento por dia no histórico recente

## Proximo contexto recomendado

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
