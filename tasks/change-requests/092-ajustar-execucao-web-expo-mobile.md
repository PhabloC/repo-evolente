# Task 092 - Ajustar execucao web do Expo mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica; ajuste de execucao local da stack mobile no alvo web

## Modo de execucao

single-stack

## Slice vertical

- Slice 001 - Fundacao e contrato base
- `tasks/slices/001-fundacao-contrato-base.md`

## Objetivo

Evitar conflito da versao web do Expo mobile com a porta padrao do Metro e tornar a execucao local previsivel no navegador.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-004.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Execucao local mobile web | `mobile/AGENTS.md` e `mobile/docs/ai/AGENTS.md` | confirmar regras locais da stack | sim |
| Falha em `npm run web` | `mobile/package.json` | ajustar script da stack | sim |
| Orientacao operacional | `mobile/README.md` | alinhar comando e porta documentada | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a execucao ao bootstrap operacional do Expo web sem reabrir UI, contrato ou features do app

## Criterios de conclusao

- [x] `npm run web` deixa de depender da porta padrao `8081`
- [x] a versao web do app responde em porta dedicada e documentada
- [x] a documentacao operacional do mobile fica alinhada ao novo comando

## Dependencias

- Task 004 - done

## Resultado da execucao

- o script `npm run web` do mobile passou a usar a porta dedicada `19006`, evitando colisao com a porta padrao do Metro usada por outros fluxos React Native/Expo
- o README operacional da stack passou a indicar explicitamente a URL local da versao web e o cuidado com a URL de API acessivel pelo navegador
- a validacao local confirmou resposta HTTP 200 da app Expo web em `http://localhost:19006`

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-004.md`

### Sob demanda

- `mobile/AGENTS.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/package.json`
- `mobile/README.md`

### Contexto evitado

- `design-system/mobile/`, `requirements/` e `contracts/openapi.yaml` por nao haver mudanca de UI, regra de negocio ou integracao cliente-servidor

## Handoff

- `.agents/state/handoffs/TASK-092.md`

## Arquivos alterados

- `mobile/package.json`
- `mobile/README.md`
- `tasks/change-requests/092-ajustar-execucao-web-expo-mobile.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-092.md`

## Validacoes executadas

- `cd mobile && npm run lint` - ok
- `cd mobile && npm run typecheck` - ok
- `cd mobile && npm run web` - ok; app respondeu `HTTP 200` em `http://localhost:19006`

## Pendencias pos-task

- revisar `EXPO_PUBLIC_API_URL` no `.env` quando o alvo web precisar apontar para um backend acessivel pelo navegador local

## Status final

done
