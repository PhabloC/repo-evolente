# Task 299 - Scroll horizontal na grade semanal do planejamento web

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

- nao se aplica; ajuste visual e responsivo na grade semanal de planejamentos

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

print de tela enviado no chat

### Cobertura

- card `Grade semanal` na tela de trilha do paciente

### Lacunas

- o print cobre apenas o estado com sete dias visiveis; a task deve preservar esse layout sem comprimir os cards em larguras menores

## Objetivo

Permitir rolagem horizontal na grade semanal da tela de planejamento para manter largura confortável dos cards diários e evitar colunas espremidas.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-298.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | validar semântica do contêiner de rolagem e limitar o escopo | sim |
| Planejamento | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | inserir o contêiner da grade semanal | sim |
| Estilo | `front-end/src/pages/Main/Plans/styles.module.css` | definir scroll horizontal e largura mínima das colunas | sim |
| Teste | `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | cobrir a presença da região de rolagem horizontal | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao card da grade semanal e a um teste focado de renderização

## Criterios de conclusao

- [x] a grade semanal passa a ter scroll horizontal quando não houver largura suficiente
- [x] os cards diários mantêm largura mínima e deixam de ser comprimidos
- [x] validações focadas passam

## Dependencias

- Task 048 - done
- Task 298 - done

## Resultado da execucao

- a grade semanal passou a ficar dentro de uma região dedicada de rolagem horizontal
- as sete colunas agora mantêm largura mínima estável, evitando cards espremidos em larguras intermediárias
- a responsividade deixou de reduzir o número de colunas visíveis por quebra de media query, priorizando a leitura confortável com scroll lateral

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-298.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteração de contrato
- `backend/` e `mobile/`, porque o ajuste foi exclusivo da composição web da grade semanal
- demais páginas internas, porque a mudança ficou isolada na tela de trilha do paciente

## Handoff

- `.agents/state/handoffs/TASK-299.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/299-scroll-horizontal-na-grade-semanal-do-planejamento-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-299.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

## Status

done
