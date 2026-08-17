# Task 296 - Ícones no dropdown de ações da tabela de pacientes

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

- nao se aplica; ajuste visual local sem alterar integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 018 - Fidelidade visual dashboard e pacientes web
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre o dropdown de ações

### Cobertura

- menu de ações da tabela de pacientes em `/pacientes`

### Lacunas

- sem novo print completo; o pedido cobre apenas adicionar ícones na frente de `Perfil` e `Inativar`

## Objetivo

Adicionar ícones às ações do dropdown da tabela de pacientes, preservando o mesmo comportamento funcional do menu.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-069.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | manter nome acessível e contraste do menu | sim |
| Front-end | `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}` | adicionar ícones e validar menu | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao dropdown local da página de pacientes

## Criterios de conclusao

- [x] item `Perfil` exibe ícone
- [x] item `Inativar/Reativar` exibe ícone
- [x] comportamento e acessibilidade do menu permanecem preservados

## Dependencias

- Task 069 - done

## Resultado da execucao

- o dropdown da tabela de pacientes passou a exibir ícone na frente de `Perfil`
- a ação de status passou a exibir `Power` para `Inativar` e `RotateCcw` para `Reativar`
- o item do menu ganhou espaçamento interno para acomodar os ícones sem quebrar alinhamento

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-069.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteracao de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao menu de ações do front-end web

## Handoff

- `.agents/state/handoffs/TASK-296.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `tasks/change-requests/296-icones-no-dropdown-de-acoes-da-tabela-de-pacientes.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-296.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
