## Status

done

## Título

Equalizar altura e largura dos cards da Biblioteca mobile

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Objetivo

Garantir que os cards de atividades da Biblioteca mobile mantenham dimensões uniformes na grade.

## Entrega verificável

Cards da mesma grade apresentam a mesma largura e altura, preservando capa, textos e ações.

## Fora de escopo

- Alterar dados ou navegação.
- Alterar cards de outras telas.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`
- `mobile/src/features/trail/screens/styles.ts`

## Contexto sob demanda

- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`: confirmar a estrutura da grade e do card.

## Orçamento de contexto

Baixo; somente estilos e markup da grade da Biblioteca.

## Resultado da execucao

A célula da grade passou a esticar o card em toda a coluna e a altura mínima do card foi explicitada, mantendo dimensões uniformes.

## Contexto utilizado

- Estilos e markup da grade da Biblioteca mobile.

## Handoff

Equalização aplicada em `libraryPosterCell` e `libraryPosterCard`.

## Arquivos alterados

- `mobile/src/features/trail/screens/styles.ts`
- `tasks/change-requests/681-equalizar-dimensoes-cards-biblioteca-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-681.md`

## Validacoes executadas

- Revisão estática dos estilos da grade; typecheck global permanece com falhas preexistentes.

## Pendencias pos-task

- Nenhuma específica desta alteração.

## Status final

done
