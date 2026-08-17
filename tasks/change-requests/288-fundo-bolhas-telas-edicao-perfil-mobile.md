# Task 288 - Fundo de bolhas nas telas de edicao de perfil mobile

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

comportamento das demais telas do shell (bolhas globais)

### Fonte primaria visual

- `AppBackgroundBubbles` no `AppGate`
- `Screen` com `backgroundColor` transparente (padrão)

## Objetivo

Fazer as páginas de edição do responsável e da criança revelarem o mesmo fundo de bolhas das outras páginas.

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-287.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Fundo opaco nas edições | `EditGuardianProfileScreen.tsx`, `EditChildProfileScreen.tsx` | remover `backgroundColor={colors.background}` | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] edição do responsável mostra bolhas no fundo
- [x] edição da criança mostra bolhas no fundo

## Dependencias

- Task 287 - done

## Resultado da execucao

- removido `backgroundColor={colors.background}` das duas telas de edição
- `Screen` volta ao padrão transparente e revela `AppBackgroundBubbles`

## Contexto utilizado

- telas de edição, `Screen`, handoff 287

## Handoff

- `.agents/state/handoffs/TASK-288.md`

## Arquivos alterados

- `tasks/change-requests/288-fundo-bolhas-telas-edicao-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-288.md`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/screens/EditChildProfileScreen.tsx`

## Validacoes executadas

- validação visual dependente de reload

## Pendencias pos-task

- nenhuma

## Status final

done
