# Task 213 - Home: ícone usuário no topo e campo de busca em largura total

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

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia de design system

mobile + pedido explícito

## Objetivo

- Substituir o ícone de lupa no header por ícone de usuário que abre o perfil
- Colocar campo de busca em largura total abaixo do header (abre a busca já existente)

## Fora de escopo

- nova API de search
- redesign da tab bar

## Contexto minimo

- `HomeHeader`, `ResponsavelHomeScreen`, Task 209

## Criterios de conclusao

- ícone User abre perfil
- campo de busca full-width abaixo do header
- typecheck ok

## Resultado da execucao

- Header: avatar + Olá/nome + User + Bell
- Abaixo: campo de busca em largura total que abre o modal de busca

## Handoff

- `.agents/state/handoffs/TASK-213.md`

## Arquivos alterados

- `mobile/src/features/shell/components/HomeHeader/index.tsx`
- `mobile/src/features/shell/components/HomeHeader/styles.ts`
- `tasks/change-requests/213-home-icone-usuario-e-campo-busca-largura-total.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-213.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
