# Task 302 - Refinar seção de evolução da trilha web

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

- nao se aplica; refino visual e informacional da seção de evolução na trilha do paciente

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario com print da tela atual

### Cobertura

- seção `Progresso / evolução` da tela de trilha do paciente

### Lacunas

- sem novo mock completo; a task deve melhorar o design atual e tornar o gráfico de evolução da criança mais evidente sem alterar a regra de negócio

## Objetivo

Redesenhar a seção de evolução da trilha para destacar melhor a evolução da criança, com gráfico mais claro, resumos visuais e histórico recente mais útil.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-301.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | refinar a seção mantendo semântica e escopo restrito | sim |
| Trilha | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | reorganizar dados e blocos da seção de evolução | sim |
| Estilo | `front-end/src/pages/Main/Plans/styles.module.css` | redesenhar o card de evolução e o gráfico | sim |
| Teste | `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | cobrir renderização da seção refinada | sim |

## Orçamento de contexto

- baixo
- estrategia: atuar apenas na composição da seção de evolução da tela de trilha, sem reabrir grade semanal, catálogo ou persistência

## Criterios de conclusao

- [x] a seção de evolução tem hierarquia visual melhor que a versão atual
- [x] existe um gráfico de evolução da criança claramente legível
- [x] o histórico recente continua acessível de forma mais organizada
- [x] validações focadas passam

## Dependencias

- Task 301 - done

## Resultado da execucao

- a seção de evolução foi reorganizada em resumo superior, leitura rápida, gráfico de tendência e histórico recente
- o gráfico passou a destacar a evolução da criança com área + linha, tornando a progressão semanal mais legível
- o histórico recente foi separado em uma timeline lateral mais clara, preservando o acesso às últimas conclusões

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-301.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteração de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito à seção web de evolução da trilha
- grade semanal, catálogo e persistência, porque a task focou apenas o bloco de progresso/evolução

## Handoff

- `.agents/state/handoffs/TASK-302.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/302-refinar-secao-de-evolucao-da-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-302.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

## Status

done
