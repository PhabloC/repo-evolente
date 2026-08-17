# Task 305 - Evitar deslocamento do subtítulo ao abrir busca web

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

- nao se aplica; ajuste de layout no header compartilhado

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario com print do header

### Cobertura

- header compartilhado das páginas internas web

### Lacunas

- sem novo mock dedicado; a task deve impedir que o subtítulo seja empurrado quando a busca expansível abre

## Objetivo

Estabilizar o layout do header para a abertura da busca não deslocar o subtítulo nem o bloco de título da página.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-304.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | manter semântica e limitar o escopo ao header | sim |
| Header | `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | corrigir a estabilidade do layout na abertura da busca | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas a composição do header compartilhado, sem tocar nas páginas consumidoras

## Criterios de conclusao

- [x] abrir a busca não empurra o subtítulo da página
- [x] o comportamento recente da busca continua preservado
- [x] validações focadas passam

## Dependencias

- Task 298 - done

## Resultado da execucao

- o header passou a reservar a largura máxima da área de busca no desktop, evitando que o subtítulo seja empurrado quando o campo abre
- o comportamento recente da busca foi preservado, incluindo foco automático e fechamento por botão dedicado
- o ajuste ficou limitado ao CSS do header compartilhado, sem alterar as páginas consumidoras

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-304.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}`
- `front-end/src/pages/Main/Patients/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteração de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao header web compartilhado
- páginas específicas além da regressão leve em pacientes, porque a mudança foi centralizada no layout

## Handoff

- `.agents/state/handoffs/TASK-305.md`

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- `tasks/change-requests/305-evitar-deslocamento-do-subtitulo-ao-abrir-busca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-305.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx src/pages/Main/Patients/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

## Status

done
