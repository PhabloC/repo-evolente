# Task 076 - Criar READMEs operacionais das stacks

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica; documentacao operacional sem alteracao de integracao

## Modo de execucao

cross-stack

## Slice vertical

- Slice 001 - Fundacao e contrato base
- `tasks/slices/001-fundacao-contrato-base.md`

## Objetivo

Criar ou atualizar READMEs operacionais para backend, front-end e mobile, deixando cada stack com instrucoes objetivas de setup, comandos e estrutura principal.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-075.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Backend | `backend/AGENTS.md`, `backend/GUIDE.md`, `backend/package.json`, `backend/README.md` | consolidar README operacional do backend | sim |
| Front-end | `front-end/AGENTS.md`, `front-end/GUIDE.md`, `front-end/package.json` | criar README operacional do front-end | sim |
| Mobile | `mobile/AGENTS.md`, `mobile/GUIDE.md`, `mobile/package.json` | criar README operacional do mobile | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a leitura a manifests e guias locais de cada stack, sem abrir requisitos, contrato ou design system

## Criterios de conclusao

- [ ] backend passa a ter README operacional mais completo e atual
- [ ] front-end passa a ter README proprio
- [ ] mobile passa a ter README proprio
- [ ] cada README descreve setup, comandos principais e estrutura basica da stack
- [ ] rastreabilidade da task e handoff atualizados

## Dependencias

- Task 049 - done

## Resultado da execucao

- o backend ganhou um README mais completo, cobrindo stack, setup, comandos, estrutura e fluxo local
- o front-end passou a ter README proprio com comandos, estrutura e referencias locais
- o mobile passou a ter README proprio com setup Expo, comandos e referencias locais

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-075.md`

### Sob demanda

- `backend/AGENTS.md`, `backend/GUIDE.md`, `backend/package.json`, `backend/README.md`
- `front-end/AGENTS.md`, `front-end/GUIDE.md`, `front-end/package.json`
- `mobile/AGENTS.md`, `mobile/GUIDE.md`, `mobile/package.json`

## Handoff

- `.agents/state/handoffs/TASK-076.md`

## Arquivos alterados

- `backend/README.md`
- `front-end/README.md`
- `mobile/README.md`
- `tasks/change-requests/076-criar-readmes-operacionais-das-stacks.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-076.md`

## Validacoes executadas

- nenhuma; alteracao restrita a documentacao

## Pendencias pos-task

- nenhuma

## Status final

done
