# Task 309 - Manter sugestao da anamnese como rascunho ate salvar trilha web

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

- nao se aplica; a solução reaproveita `getPatient` e o catálogo já expostos no contrato atual

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre a pagina da trilha

### Cobertura

- CTA `Sugerir pela anamnese`
- CTA `Salvar semana`
- comportamento de persistencia da trilha na pagina da crianca

### Lacunas

- sem mock novo; o foco está no comportamento e no estado dos botões

## Objetivo

Fazer a sugestão da anamnese preencher apenas o rascunho local da trilha até o profissional salvar explicitamente, e manter `Salvar semana` inativo quando não houver alterações pendentes.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-308.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | preservar semântica, foco e escopo local | sim |
| Trilha web | `front-end/src/pages/Main/Plans/PatientTrail/{index.tsx,index.test.tsx,utils.ts}` | trocar a sugestão persistente por rascunho local e controlar dirty state | sim |
| Serviços consumidos | `front-end/src/services/{patients/patientService.ts,contents/contentService.ts,trails/trailService.ts}` | reaproveitar anamnese e catálogo já disponíveis | sim |
| Tipos | `front-end/src/types/{guardian.ts,trail.ts,content.ts,patient.ts}` | manter coerência de dados do rascunho e da sugestão | sim |

## Orçamento de contexto

- baixo
- estrategia: resolver no front sem reabrir contrato/backend, usando `suggestedTrailCategories` da anamnese já carregada

## Criterios de conclusao

- [x] clicar em `Sugerir pela anamnese` não persiste a trilha imediatamente
- [x] a sugestão passa a existir apenas como rascunho local até `Salvar semana`
- [x] `Salvar semana` começa inativo e só habilita quando houver algo pendente para salvar
- [x] a sugestão sem edições ainda persiste corretamente ao salvar
- [x] validações focadas passam

## Dependencias

- Task 302 - done
- Task 304 - done

## Resultado da execucao

- a página passou a montar a sugestão localmente a partir de `patient.anamnese.suggestedTrailCategories` e do catálogo ativo já carregado
- o endpoint de sugestão deixou de ser chamado no clique do CTA e passou a ser usado apenas no `Salvar semana` quando o rascunho ainda corresponde exatamente à sugestão original
- foi adicionado controle de assinatura do rascunho para detectar dirty state real e desabilitar `Salvar semana` quando não há mudanças
- a trilha ganhou helpers locais para reindexação e comparação estável dos itens do rascunho

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-308.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/PatientTrail/{index.tsx,index.test.tsx,utils.ts}`
- `front-end/src/services/{patients/patientService.ts,contents/contentService.ts,trails/trailService.ts}`
- `front-end/src/types/{guardian.ts,trail.ts,content.ts,patient.ts}`

### Contexto evitado

- `contracts/openapi.yaml`, porque a solução reaproveitou dados já expostos
- `backend/`, porque não foi necessário criar endpoint novo nem mudar semântica do contrato
- `mobile/`, porque o ajuste ficou restrito ao fluxo web da trilha

## Handoff

- `.agents/state/handoffs/TASK-309.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/utils.ts`
- `tasks/change-requests/309-manter-sugestao-da-anamnese-como-rascunho-ate-salvar-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-309.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/PatientTrail/utils.ts` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
