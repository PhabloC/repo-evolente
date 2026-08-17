# Task 069 - Desacoplar dropdown da tabela de pacientes

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

- nao se aplica; correção visual sem alteração de integração

## Modo de execucao

single-stack

## Slice vertical

- Slice 018 - Fidelidade visual dashboard e pacientes web
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre o comportamento do dropdown

### Cobertura

- dropdown de ações da tabela em `/pacientes`

### Lacunas

- sem nova referência visual para o posicionamento do menu
- decisao: renderizar o menu em portal no `body`, ancorado ao botão de três pontinhos

## Objetivo

Fazer o dropdown de ações abrir fora da área de overflow da tabela de pacientes.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-068.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar o clipping do dropdown | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | preservar semântica e fechamento do menu | sim |
| Front-end | `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}` | mover o menu para portal e validar | sim |

## Orçamento de contexto

- baixo
- estrategia: manter a correção isolada ao módulo `Patients`

## Criterios de conclusao

- [x] o dropdown deixa de ser cortado/quebrar a tabela
- [x] o menu continua abrindo a partir dos três pontinhos
- [x] teste focado da página permanece aprovado

## Dependencias

- Task 068 - done

## Resultado da execucao

- o dropdown passou a ser renderizado em portal no `body`
- o posicionamento agora usa coordenadas do botão com `position: fixed`
- a tabela deixou de expandir ou cortar o menu por overflow

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-068.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver alteracao de contrato
- backend e mobile por estarem fora do escopo

## Handoff

- `.agents/state/handoffs/TASK-069.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `tasks/change-requests/069-desacoplar-dropdown-tabela-pacientes.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-069.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
