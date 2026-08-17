# Task 463 - Compactar espaçamento da aba Arquivo no modal

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/006-catalogo-conteudos-master.md`

## Objetivo

Reduzir o espaço visual excessivo na aba Arquivo do modal Nova atividade.

## Criterios de conclusao

- [x] conteúdo da aba Arquivo mais compacto
- [x] fieldset com conteúdo alinhado ao topo (sem vão artificial)
- [x] upload preservado

## Resultado da execucao

- `align-content: start` no fieldset
- card de mídia compacto; label "Arquivo" redundante removido
- shell de upload com altura/padding menores

## Arquivos alterados

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/000-index.md`

## Status final

done
