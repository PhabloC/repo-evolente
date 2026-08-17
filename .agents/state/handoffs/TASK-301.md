# Handoff - Task 301

## Task

- identificador: 301
- titulo: Corrigir overflow e arraste da grade semanal web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: manter a grade semanal contida visualmente e com arraste horizontal funcional
- entrega verificavel: os cards não vazam à direita e a grade pode ser arrastada horizontalmente com o mouse

## Decisoes preservadas

- o contêiner da grade semanal passou a limitar `overflow` dentro do próprio card para eliminar o vazamento visual à direita
- o arraste foi refeito com `pointer events`, substituindo a abordagem anterior baseada em listeners globais de mouse
- a lógica continua bloqueando o início do drag em elementos interativos internos, para não quebrar botões e controles da grade

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/301-corrigir-overflow-e-arraste-da-grade-semanal-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-300.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | validar a interação do contêiner arrastável |
| `front-end/docs/ai/COMPONENT_REUSE.md` | escopo local | manter a correção isolada na grade semanal |
| `front-end/src/ui/Card/{index.tsx,styles.module.css}` | overflow percebido | verificar o contêiner pai da grade |
| `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | gesto de arraste | reimplementar o drag com pointer events |
| `front-end/src/pages/Main/Plans/styles.module.css` | contenção visual | ajustar overflow e largura do scroller |
| `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | validação | cobrir o arraste após a correção |
| `front-end/src/pages/Main/Plans/index.test.tsx` | regressão leve | manter integridade da área de planejamentos |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de contrato |
| `backend/` | sem mudança funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: grade semanal contida visualmente e com arraste horizontal funcional
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/301-corrigir-overflow-e-arraste-da-grade-semanal-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx`: ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido para adicionar hint visual fixo de “arraste para o lado”

## Proximo contexto recomendado

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
