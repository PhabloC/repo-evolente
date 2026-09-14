## Status

done

## Título

Equalizar altura dos cards do acervo master mobile

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

`tasks/slices/009-administracao-master.md`

## Objetivo

Manter os cards do acervo da conta master com dimensões uniformes.

## Entrega verificável

Cards com títulos curtos ou longos têm a mesma altura e largura na grade.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `mobile/src/features/admin/contents/screens/AdminContentsScreen.tsx`
- `mobile/src/features/admin/contents/screens/listStyles.ts`

## Contexto sob demanda

- `mobile/src/features/admin/contents/components/ContentCoverThumb/index.tsx`: comportamento da capa.

## Orçamento de contexto

Baixo; somente o acervo master mobile.

## Resultado da execucao

Cards do acervo master receberam altura fixa, corpo fixo e título limitado a duas linhas.

## Contexto utilizado

- Markup do `GridPoster` e estilos do acervo master.

## Handoff

Equalização aplicada no acervo master mobile.

## Arquivos alterados

- `mobile/src/features/admin/contents/screens/listStyles.ts`
- `tasks/change-requests/683-equalizar-altura-cards-acervo-master-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-683.md`

## Validacoes executadas

- Revisão estática dos estilos.

## Pendencias pos-task

- Nenhuma.

## Status final

done
