# Task 462 - Remover margem branca da prévia de capa

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

## Contexto mínimo

- task 460/461, CSS `contentEditCover*`

## Contexto sob demanda

- `front-end/src/pages/Main/Library/styles.module.css`

## Orçamento de contexto

- baixo

## Objetivo

Eliminar faixa branca à direita da prévia sem capa no modal Nova atividade.

## Criterios de conclusao

- [x] fallback da capa preenche 100% da largura do card
- [x] proporção controlada no container pai

## Resultado da execucao

- `aspect-ratio`/`max-height` no `.contentEditCover`
- filhos (`image`/`fallback`) com `width/height: 100%`

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/462-remover-margem-branca-previa-capa.md`
- `tasks/000-index.md`

## Status final

done
