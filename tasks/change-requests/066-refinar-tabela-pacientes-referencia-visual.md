# Task 066 - Refinar tabela de pacientes por referência visual

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

- nao se aplica; preservar apenas os dados já retornados pela listagem atual de pacientes

## Modo de execucao

single-stack

## Slice vertical

- Slice 018 - Fidelidade visual dashboard e pacientes web
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`

## Referencia visual

### Tipo

imagem enviada pelo usuario no chat

### Cobertura

- tabela principal da página `/pacientes`
- cabeçalho, densidade das linhas, pills de status e paginação

### Lacunas

- a referência mostra colunas de sessão, planejamento e progresso que o payload atual não fornece
- o usuario pediu explicitamente para nao usar foto do paciente
- decisao: reproduzir a hierarquia visual da tabela usando somente dados reais atuais, com avatar textual por iniciais e sem inventar colunas clínicas

## Objetivo

Deixar a tabela da página de pacientes mais próxima da referência visual enviada, sem usar foto do paciente.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-046.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | imagem enviada pelo usuario no chat | orientar a tabela alvo | sim |
| Front-end | `front-end/AGENTS.md` | validar governanca local da stack | sim |
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | preservar semantica da tabela e nomes acessiveis das acoes | sim |
| Front-end | `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}` | implementar e validar o refino local | sim |
| UI compartilhada | `front-end/src/ui/Table/**` | confirmar as restricoes do componente e isolar o refino por classe local | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca à página de pacientes e ao uso do `Table` já existente

## Criterios de conclusao

- [x] a tabela de pacientes ganha composição mais próxima da referência
- [x] a primeira coluna usa avatar textual por iniciais, sem foto
- [x] a tabela continua usando apenas dados reais disponíveis no payload
- [x] paginação e status ficam visualmente mais próximos do design
- [x] teste focado da página de pacientes permanece aprovado

## Dependencias

- Task 040 - done
- Task 046 - done

## Resultado da execucao

- a tabela passou a exibir a primeira coluna com iniciais, nome e código como subtítulo
- a composição das colunas foi reorganizada para reforçar idade, responsável, vínculo, status e ações
- status, cabeçalho, ações e paginação foram refinados localmente para aproximar a linguagem visual da referência

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-046.md`

### Sob demanda

- imagem enviada pelo usuario no chat
- `front-end/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css,index.test.tsx}`
- `front-end/src/ui/Table/{index.tsx,styles.module.css}`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver alteracao de contrato
- backend e mobile por estarem fora do escopo
- páginas sem impacto direto

## Handoff

- `.agents/state/handoffs/TASK-066.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `tasks/change-requests/066-refinar-tabela-pacientes-referencia-visual.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-066.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx` - ok

## Pendencias pos-task

- a referência mostra colunas clínicas adicionais que seguem fora de escopo até existirem dados reais equivalentes

## Status final

done
