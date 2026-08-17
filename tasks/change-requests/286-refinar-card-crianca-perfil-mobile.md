# Task 286 - Refinar card da crianca no perfil mobile

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

refino incremental + print do cabeçalho "Criança" a remover

### Fonte primaria visual

- print do cabeçalho "Criança / 1 vinculada / Toque na criança..." (remover)
- card da criança (manter e refinar)

## Objetivo

Remover o cabeçalho do card agregado "Criança" e manter só o card da criança vinculada, com ícone de calendário no nascimento e código em linha própria com ícone.

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-285.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Card criança | `ResponsavelProfileScreen.tsx` | reestruturar | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] cabeçalho "Criança / 1 vinculada / toque..." removido
- [x] card da criança mantido
- [x] nascimento com ícone de calendário
- [x] código em linha abaixo com ícone

## Dependencias

- Task 285 - done

## Resultado da execucao

- removido o card agregado com título "Criança", status e instrução
- cada criança virou um `HomeActionCard` próprio com nome, CTA e metadados
- nascimento com `Calendar`; código em linha separada com `Hash`

## Contexto utilizado

- `ResponsavelProfileScreen.tsx`, handoff 285

## Handoff

- `.agents/state/handoffs/TASK-286.md`

## Arquivos alterados

- `tasks/change-requests/286-refinar-card-crianca-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-286.md`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`

## Validacoes executadas

- validação visual dependente de reload

## Pendencias pos-task

- nenhuma

## Status final

done
