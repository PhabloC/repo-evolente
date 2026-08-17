# Task 285 - Refinar metadados do card de responsavel no perfil mobile

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

refino incremental + print do card do responsável

### Fonte primaria visual

- print do card "Phablo Carvalho" enviado pelo usuário
- `ResponsavelProfileScreen.tsx`
- `HomeActionCard`

## Objetivo

No card do responsável: ícone de carta ao lado do e-mail, ícone de user ao lado do parentesco, e "Assinatura ativa" na parte de baixo com background e bolinha verde.

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-284.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Card do responsável | `ResponsavelProfileScreen.tsx`, `styles.ts` | montar metadados | sim |
| Descrição opcional | `HomeActionCard` | não forçar description em texto único | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] e-mail com ícone de carta à esquerda
- [x] parentesco com ícone de user à esquerda
- [x] assinatura embaixo com background e bolinha verde (quando ativa)

## Dependencias

- Task 284 - done

## Resultado da execucao

- `description` do `HomeActionCard` ficou opcional
- card do responsável passou a renderizar metadados com `Mail` + e-mail, `User` + parentesco e pastilha de assinatura com bolinha verde

## Contexto utilizado

- `ResponsavelProfileScreen.tsx`, `screens/styles.ts`, `HomeActionCard`

## Handoff

- `.agents/state/handoffs/TASK-285.md`

## Arquivos alterados

- `tasks/change-requests/285-refinar-metadados-card-responsavel-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-285.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`

## Validacoes executadas

- validação visual dependente de reload

## Pendencias pos-task

- nenhuma

## Status final

done
