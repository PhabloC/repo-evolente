# Task 290 - Revelar bolhas no stack das telas de edicao de perfil mobile

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

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

bolhas globais das demais telas

## Objetivo

Corrigir o fundo das telas de edição: o `contentStyle` bege do stack cobria as bolhas mesmo com `Screen` transparente.

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-288.md`
- `mobile/src/routes/RootNavigator.tsx`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Stack options | `RootNavigator.tsx` | remover contentStyle bege | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] EditGuardianProfile e EditChildProfile herdam `contentStyle` transparente do stack
- [x] bolhas visíveis nas telas de edição

## Dependencias

- Task 288 - done

## Resultado da execucao

- removido `contentStyle: { backgroundColor: colors.background }` das rotas de edição no `RootNavigator`
- rotas passam a herdar o padrão transparente do navigator

## Contexto utilizado

- `RootNavigator.tsx`, print do usuário, handoff 288

## Handoff

- `.agents/state/handoffs/TASK-290.md`

## Arquivos alterados

- `tasks/change-requests/290-revelar-bolhas-stack-edicao-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-290.md`
- `mobile/src/routes/RootNavigator.tsx`

## Validacoes executadas

- validação visual dependente de reload

## Pendencias pos-task

- nenhuma

## Status final

done
