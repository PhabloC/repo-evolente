# Task 507 - Mobile: cards da Biblioteca no estilo do acervo master

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

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Dependencias

- Task 505, 506

## Objetivo

Na aba Biblioteca do responsável, exibir os conteúdos em cards/poster com capa como no acervo do perfil master.

## Criterios de aceite

- [x] Grid de cards com capa (coverUrl) como no master
- [x] Título, tipo e categoria no card
- [x] Seleção para adicionar à trilha preservada

## Resultado da execucao

Biblioteca usa `ContentCoverThumb` + grid poster 2 colunas no estilo `AdminContentsScreen`.

## Contexto utilizado

- AdminContentsScreen, ContentCoverThumb, TrailLibraryPane

## Handoff

- `.agents/state/handoffs/TASK-507.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/admin/contents/components/ContentCoverThumb/index.tsx`
- `mobile/src/features/admin/contents/adapters/adaptContent.ts`

## Validacoes executadas

- lints ok

## Pendencias pos-task

- nenhuma

## Status final

done
