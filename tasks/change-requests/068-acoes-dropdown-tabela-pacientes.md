# Task 068 - Consolidar ações da tabela de pacientes em dropdown

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

- nao se aplica; ajuste visual e estrutural sem alterar integração

## Modo de execucao

single-stack

## Slice vertical

- Slice 018 - Fidelidade visual dashboard e pacientes web
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre simplificação da tabela

### Cobertura

- remoção da coluna `Último vínculo`
- mover ações `Perfil` e `Inativar/Reativar` para dropdown nos três pontinhos

### Lacunas

- sem novo print de referência para o menu
- decisao: usar um menu simples e acessível acoplado ao botão de três pontinhos, mantendo as mesmas ações existentes

## Objetivo

Simplificar a tabela de pacientes removendo a coluna `Último vínculo` e consolidando as ações no menu de três pontinhos.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-067.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar a simplificação da tabela | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | garantir semântica e acionamento do menu por teclado | sim |
| Front-end | `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}` | implementar dropdown local e validar renderização | sim |

## Orçamento de contexto

- baixo
- estrategia: manter a mudança isolada ao módulo `Patients`

## Criterios de conclusao

- [x] a coluna `Último vínculo` é removida
- [x] `Perfil` e `Inativar/Reativar` passam a abrir via menu dos três pontinhos
- [x] o menu continua acessível e o teste focado da página permanece aprovado

## Dependencias

- Task 067 - done

## Resultado da execucao

- a tabela deixou de exibir a coluna `Último vínculo`
- as ações foram movidas para um dropdown local aberto pelo botão de três pontinhos
- o menu mantém as ações existentes sem alterar comportamento funcional

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-067.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver alteracao de contrato
- backend e mobile por estarem fora do escopo

## Handoff

- `.agents/state/handoffs/TASK-068.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `tasks/change-requests/068-acoes-dropdown-tabela-pacientes.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-068.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
