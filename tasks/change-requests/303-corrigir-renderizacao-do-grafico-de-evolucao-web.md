# Task 303 - Corrigir renderização do gráfico de evolução web

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

- nao se aplica; correção de renderização visual do gráfico de evolução

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre regressao visual

### Cobertura

- gráfico da seção `Progresso / evolução` na tela de trilha do paciente

### Lacunas

- sem novo print do estado esperado; a task deve restaurar a renderização do gráfico mantendo o redesign recente

## Objetivo

Corrigir a renderização do gráfico de evolução da criança na tela de trilha do paciente.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-302.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | corrigir a renderização sem ampliar o escopo | sim |
| Trilha | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | validar uso do Recharts e o container do gráfico | sim |
| Estilo | `front-end/src/pages/Main/Plans/styles.module.css` | garantir dimensões reais para o gráfico | sim |
| Teste | `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | cobrir a presença do gráfico renderizado | sim |

## Orçamento de contexto

- baixo
- estrategia: ajustar apenas a renderização do gráfico na seção de evolução sem reabrir o restante da tela

## Criterios de conclusao

- [x] o gráfico volta a aparecer no runtime
- [x] o redesign recente da seção é preservado
- [x] validações focadas passam

## Dependencias

- Task 302 - done

## Resultado da execucao

- o contêiner do gráfico passou a ter altura real, corrigindo a renderização do `ResponsiveContainer` do Recharts
- o redesign recente da seção de evolução foi preservado
- foi adicionada uma asserção focada no bloco do gráfico para evitar regressão silenciosa dessa renderização

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-302.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteração de contrato
- `backend/` e `mobile/`, porque a correção ficou restrita ao gráfico web da trilha
- demais áreas da tela de planejamentos, porque o ajuste foi localizado no contêiner de renderização

## Handoff

- `.agents/state/handoffs/TASK-303.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/303-corrigir-renderizacao-do-grafico-de-evolucao-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-303.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

## Status

done
