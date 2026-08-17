# Task 304 - Scroll no card de histórico recente web

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

- nao se aplica; ajuste visual e comportamental no card de histórico recente

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario

### Cobertura

- card `Histórico recente` da seção de evolução na trilha do paciente

### Lacunas

- sem novo print; a mudança deve apenas adicionar rolagem interna ao histórico, preservando o redesign recente

## Objetivo

Adicionar scroll interno ao card de histórico recente na seção de evolução da trilha do paciente.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-303.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | limitar a mudança ao card lateral | sim |
| Trilha | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | identificar o bloco do histórico recente | sim |
| Estilo | `front-end/src/pages/Main/Plans/styles.module.css` | aplicar altura e rolagem interna | sim |
| Teste | `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | cobrir a presença do container scrollável | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar só o card lateral do histórico recente, sem tocar no gráfico nem na grade semanal

## Criterios de conclusao

- [x] o card de histórico recente passa a ter scroll interno
- [x] o redesign da seção de evolução é preservado
- [x] validações focadas passam

## Dependencias

- Task 303 - done

## Resultado da execucao

- o card `Histórico recente` passou a usar uma área scrollável interna com altura máxima estável
- o redesign recente da seção de evolução foi preservado, sem mexer no gráfico nem no resumo superior
- a cobertura de teste foi atualizada para garantir a presença da lista rolável

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-303.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteração de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao card lateral do histórico recente na web
- gráfico e grade semanal, porque a mudança foi limitada ao scroll do histórico

## Handoff

- `.agents/state/handoffs/TASK-304.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/304-scroll-no-card-de-historico-recente-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-304.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

## Status

done
