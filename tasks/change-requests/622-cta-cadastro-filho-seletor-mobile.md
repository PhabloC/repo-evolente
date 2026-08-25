# Task 622 - CTA de cadastro de filho no seletor mobile

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

- não altera contrato; navega para o cadastro de filho da Task 621

## Modo de execucao

single-stack

## Slice vertical

- Slice 055 - Cadastro de filho no perfil mobile
- `tasks/slices/055-cadastro-filho-perfil-mobile.md`

## Objetivo

Disponibilizar o cadastro de filho também na tela “Qual filho você vai gerenciar?”.

## Critérios de aceite

- [x] Empty state apresenta `Cadastrar filho` e abre o formulário.
- [x] Lista de filhos também permite cadastrar outro filho.
- [x] CTA é acessível e não altera seleção ou logout.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 055 e handoff Task 621

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Tela de seleção | `mobile/src/features/children/screens/SelectChildScreen.tsx` | encaixar CTA |
| Rota de criação | `CreateChildScreen`, `RootNavigator`, params | navegação existente |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | linguagem de botão e feedback |

## Orçamento de contexto

- baixo
- estratégia: alterar apenas o seletor e usar a rota já entregue; sem API ou backend.

## Status final

done

## Resultado da execucao

- O estado sem filhos agora explica que o cadastro é feito no app e oferece `Cadastrar filho`.
- Com filhos na lista, o seletor exibe `Cadastrar outro filho` antes do botão de sair.
- Ambos os CTAs navegam para a rota `CreateChild` já entregue na Task 621.

## Contexto utilizado

- Task 622, Slice 055, handoff Task 621, seletor de filho, rota existente e design system mobile.

## Handoff

- `.agents/state/handoffs/TASK-622.md`

## Arquivos alterados

- `mobile/src/features/children/screens/SelectChildScreen.tsx`
- task, slice, índice e handoff desta execução

## Validacoes executadas

- `npx eslint src/features/children/screens/SelectChildScreen.tsx` — passou.
- `npm run typecheck` — passou.
- Jest do seletor: 2 suítes, 6 testes passaram.

## Pendencias pos-task

- Nenhuma.
