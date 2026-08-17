# Task 301 - Corrigir overflow e arraste da grade semanal web

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

- nao se aplica; correção visual e comportamental na grade semanal do planejamento

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

print de tela e feedback direto do usuario

### Cobertura

- card `Grade semanal` na tela de trilha do paciente

### Lacunas

- o problema reportado combina layout e interação; a task deve manter o scroll lateral, mas sem vazamento visual para fora do card e com arraste funcionando de fato

## Objetivo

Conter a grade semanal dentro do card à direita e corrigir o gesto de arraste horizontal para os cards do planejamento.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-300.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | corrigir interação sem reabrir escopo amplo | sim |
| Planejamento | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | ajustar o gesto de arraste | sim |
| Estilo | `front-end/src/pages/Main/Plans/styles.module.css` | conter overflow e revisar o contêiner da grade | sim |
| Teste | `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | validar o arraste após a correção | sim |

## Orçamento de contexto

- baixo
- estrategia: evoluir apenas a implementação recém-criada da grade semanal, sem tocar em fluxos de salvar ou catálogo

## Criterios de conclusao

- [x] a grade semanal não vaza visualmente para fora do card à direita
- [x] o arraste horizontal dos cards funciona no uso real
- [x] validações focadas passam

## Dependencias

- Task 299 - done
- Task 300 - done

## Resultado da execucao

- o card da grade semanal passou a conter o conteúdo horizontalmente, sem deixar os cards vazarem visualmente para fora à direita
- o gesto de arraste foi refeito com `pointer events`, deixando o drag horizontal mais robusto no contêiner real da grade
- a implementação continua ignorando controles interativos internos, preservando cliques normais em botões e ações dos cards

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-300.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/ui/Card/{index.tsx,styles.module.css}`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteração de contrato
- `backend/` e `mobile/`, porque a correção ficou restrita à composição web da grade semanal
- demais fluxos de planejamentos, porque o ajuste ficou localizado na tela de trilha

## Handoff

- `.agents/state/handoffs/TASK-301.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/301-corrigir-overflow-e-arraste-da-grade-semanal-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-301.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

## Status

done
