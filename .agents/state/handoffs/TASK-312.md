# Handoff - Task 312

## Task

- identificador: 312
- titulo: Adicionar confirmacao antes de salvar semana na trilha web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: evitar persistência acidental da semana
- entrega verificavel: `Salvar semana` exige confirmação explícita antes de gravar

## Decisoes preservadas

- o modal de confirmação reaproveita o mesmo padrão da confirmação de inativação
- a lógica de persistência permaneceu centralizada em `handleSave`
- o botão continua desabilitado quando não há mudanças pendentes

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/312-adicionar-confirmacao-antes-de-salvar-semana-na-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-311.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | UI web | preservar semântica e escopo local |
| `front-end/src/pages/Main/Plans/PatientTrail/{index.tsx,index.test.tsx}` | fluxo da trilha | adicionar confirmação antes do salvamento |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de contrato |
| `backend/` | sem mudança funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: salvar semana agora exige confirmação em modal
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `tasks/change-requests/312-adicionar-confirmacao-antes-de-salvar-semana-na-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx`: ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se quiser adicionar resumo das alterações dentro do modal antes da confirmação

## Proximo contexto recomendado

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`

## Contexto que nao deve ser carregado

- `backend/`
- `mobile/`
