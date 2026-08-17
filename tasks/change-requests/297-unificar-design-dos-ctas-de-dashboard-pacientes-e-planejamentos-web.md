# Task 297 - Unificar design dos CTAs de dashboard, pacientes e planejamentos web

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

- nao se aplica; ajuste visual de CTAs sem alterar integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre consistencia visual

### Cobertura

- CTA `Criar planejamento` no dashboard
- CTA `Vincular por código` na página de pacientes
- CTA `Ver pacientes` na página de planejamentos

### Lacunas

- sem novo print; a tarefa é harmonizar o design existente entre os três botões

## Objetivo

Padronizar o visual dos principais CTAs operacionais entre dashboard, pacientes e planejamentos usando a mesma linguagem de botão.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-296.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | definir componente compartilhado e semântica | sim |
| Dashboard | `front-end/src/pages/Main/ShellHome/{index.tsx,index.test.tsx,styles.module.css}` | unificar CTA de criar planejamento | sim |
| Pacientes | `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}` | reaproveitar padrão do CTA já refinado | sim |
| Planejamentos | `front-end/src/pages/Main/Plans/{index.tsx,index.test.tsx,styles.module.css}` | aplicar o mesmo padrão ao CTA de ver pacientes | sim |
| Reuso | `front-end/src/ui/Button/**` | compor solução sem quebrar o componente base | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança aos CTAs citados e a um componente compartilhado pequeno, sem reabrir outras rotas

## Criterios de conclusao

- [x] os três CTAs usam o mesmo design visual
- [x] dashboard, pacientes e planejamentos continuam funcionais
- [x] testes focados das páginas afetadas passam

## Dependencias

- Task 037 - done
- Task 296 - done

## Resultado da execucao

- foi criado um componente compartilhado `PageActionButton` para concentrar o estilo comum dos CTAs operacionais
- `Criar planejamento`, `Vincular por código` e `Ver pacientes` passaram a usar o mesmo visual em dashboard, pacientes e planejamentos
- os CTAs duplicados dos estados vazios em pacientes e planejamentos tambem passaram a seguir o mesmo padrao

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-296.md`

### Sob demanda

- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/ui/Button/**`
- `front-end/src/components/PageActionButton/**`
- `front-end/src/pages/Main/ShellHome/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/pages/Main/Plans/{index.tsx,index.test.tsx,styles.module.css}`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteracao de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito a padronizacao visual de CTAs web
- outras rotas da area autenticada, porque o pedido cobria apenas dashboard, pacientes e planejamentos

## Handoff

- `.agents/state/handoffs/TASK-297.md`

## Arquivos alterados

- `front-end/src/components/PageActionButton/index.tsx`
- `front-end/src/components/PageActionButton/styles.module.css`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Plans/index.tsx`
- `tasks/change-requests/297-unificar-design-dos-ctas-de-dashboard-pacientes-e-planejamentos-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-297.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/ShellHome/index.test.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/components/PageActionButton/index.tsx src/pages/Main/ShellHome/index.tsx src/pages/Main/ShellHome/index.test.tsx src/pages/Main/Patients/index.tsx src/pages/Main/Plans/index.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
