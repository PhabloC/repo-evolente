## Status

done

## Título

Fixar altura dos cards da Biblioteca mobile

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

Impedir que títulos maiores alterem a altura visual dos cards da Biblioteca mobile.

## Entrega verificável

Todos os cards da grade têm a mesma altura, inclusive com títulos de duas linhas.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`
- `mobile/src/features/trail/screens/styles.ts`

## Contexto sob demanda

- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`: confirmar limite de linhas do título.

## Orçamento de contexto

Baixo; estilos e markup do card.

## Resultado da execucao

Altura total e altura do corpo do card foram fixadas para acomodar capas, badge, título de até duas linhas e categoria sem expansão variável.

## Contexto utilizado

- Estilos e markup do card da Biblioteca mobile.

## Handoff

Cards equalizados com altura total fixa e corpo com altura fixa.

## Arquivos alterados

- `mobile/src/features/trail/screens/styles.ts`
- `tasks/change-requests/682-fixar-altura-cards-biblioteca-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-682.md`

## Validacoes executadas

- Revisão estática dos estilos.

## Pendencias pos-task

- Nenhuma.

## Status final

done
