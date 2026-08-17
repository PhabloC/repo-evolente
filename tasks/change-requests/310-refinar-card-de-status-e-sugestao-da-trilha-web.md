# Task 310 - Refinar card de status e sugestao da trilha web

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

- nao se aplica; ajuste visual local na página da trilha

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario com print da seção da trilha

### Cobertura

- bloco de status da semana
- mensagem de sugestão/local draft da trilha

### Lacunas

- sem novo mock detalhado; a tarefa deve elevar a hierarquia visual e a legibilidade do bloco existente

## Objetivo

Melhorar o design do bloco de status e mensagem da trilha para a sugestão da anamnese ficar mais clara, acolhida e consistente com o restante da página.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-309.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | preservar semântica, contraste e escopo local | sim |
| Trilha web | `front-end/src/pages/Main/Plans/{PatientTrail/index.tsx,styles.module.css}` | refinar o bloco de status/sugestão da semana | sim |

## Orçamento de contexto

- baixo
- estrategia: ajustar apenas a marcação e o CSS do bloco de status da trilha

## Criterios de conclusao

- [x] a mensagem de sugestão fica visualmente destacada e melhor hierarquizada
- [x] o status da trilha continua claro e legível
- [x] a mudança fica restrita à página da trilha
- [x] validações focadas passam

## Dependencias

- Task 302 - done
- Task 309 - done

## Resultado da execucao

- o bloco de status da semana ganhou uma composição em card de destaque, com ícone, rótulo auxiliar e mensagem principal melhor hierarquizada
- o status salvo/ativo da trilha passou a conviver melhor com o feedback de sugestão sem parecer texto solto
- a mudança ficou isolada na página da trilha, sem alterar contrato ou outros módulos

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-309.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/{PatientTrail/index.tsx,styles.module.css}`

### Contexto evitado

- `contracts/openapi.yaml`, porque não houve alteração de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao visual da trilha web

## Handoff

- `.agents/state/handoffs/TASK-310.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/310-refinar-card-de-status-e-sugestao-da-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-310.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
