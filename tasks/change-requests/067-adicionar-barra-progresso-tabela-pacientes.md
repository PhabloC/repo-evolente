# Task 067 - Adicionar barra de progresso visual na tabela de pacientes

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

- nao se aplica; sem dados reais de progresso no payload atual da listagem

## Modo de execucao

single-stack

## Slice vertical

- Slice 018 - Fidelidade visual dashboard e pacientes web
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre a tabela de pacientes

### Cobertura

- coluna visual de progresso da tabela em `/pacientes`

### Lacunas

- a API atual nao expõe percentual de progresso por paciente nessa listagem
- decisao: incluir a barra visual com estado honesto `Sem dado` e preenchimento neutro até existir integração real

## Objetivo

Adicionar a barrinha de progresso à tabela de pacientes sem inventar percentuais clínicos inexistentes.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-066.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar a necessidade da barra visual | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | garantir que a coluna continue compreensível sem depender só de cor | sim |
| Front-end | `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}` | adicionar a coluna e validar o estado honesto | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao modulo `Patients`

## Criterios de conclusao

- [x] a tabela de pacientes passa a exibir a coluna visual de progresso
- [x] a coluna deixa claro que o dado ainda nao está disponível
- [x] teste focado da página de pacientes permanece aprovado

## Dependencias

- Task 066 - done

## Resultado da execucao

- a tabela ganhou uma coluna `Progresso` com barra neutra e texto `Sem dado`
- o ajuste preservou fidelidade visual sem inventar percentual de acompanhamento

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-066.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver mudanca de contrato
- backend e mobile por estarem fora do escopo

## Handoff

- `.agents/state/handoffs/TASK-067.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `tasks/change-requests/067-adicionar-barra-progresso-tabela-pacientes.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-067.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx` - ok

## Pendencias pos-task

- quando a API expuser percentual real de progresso, a barra deve trocar o estado neutro por dado integrado

## Status final

done
