# Handoff - Task 309

## Task

- identificador: 309
- titulo: Manter sugestao da anamnese como rascunho ate salvar trilha web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: impedir persistência prematura da trilha sugerida
- entrega verificavel: a sugestão só vira trilha persistida após `Salvar semana`, e o botão de salvar só habilita com mudanças pendentes

## Decisoes preservadas

- a solução ficou só no front, reaproveitando `patient.anamnese.suggestedTrailCategories` e o catálogo ativo já carregado
- o clique em `Sugerir pela anamnese` passou a montar um rascunho local em vez de chamar o endpoint persistente
- quando o rascunho ainda é idêntico à sugestão original, o `Salvar semana` usa o endpoint de sugestão para preservar `seededFromAnamnese`
- quando o profissional altera a sugestão antes de salvar, a persistência segue pelo fluxo manual normal

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/309-manter-sugestao-da-anamnese-como-rascunho-ate-salvar-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-308.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | UI web | preservar semântica e limitar a mudança à trilha |
| `front-end/src/pages/Main/Plans/PatientTrail/{index.tsx,index.test.tsx,utils.ts}` | fluxo da trilha | introduzir rascunho local, dirty state e testes |
| `front-end/src/services/{patients/patientService.ts,contents/contentService.ts,trails/trailService.ts}` | dados já disponíveis | reutilizar anamnese, catálogo e persistência existente |
| `front-end/src/types/{guardian.ts,trail.ts,content.ts,patient.ts}` | coerência de tipos | modelar assinatura e sugestão local |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem mudança de contrato |
| `backend/` | sem endpoint novo nem alteração server-side |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: sugestão virou rascunho local até salvar; botão de salvar agora reflete dirty state real
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/utils.ts`
- `tasks/change-requests/309-manter-sugestao-da-anamnese-como-rascunho-ate-salvar-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx`: ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/PatientTrail/utils.ts`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se quiser explicitar visualmente um selo de “rascunho não salvo” na semana atual

## Proximo contexto recomendado

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/utils.ts`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`

## Contexto que nao deve ser carregado

- `backend/`
- `mobile/`
