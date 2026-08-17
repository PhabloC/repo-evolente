# Task 465 - Remover margem branca do modal de prévia de vídeo

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

Eliminar o espaço branco excessivo abaixo do conteúdo no modal de prévia de atividade (áudio/vídeo).

## Criterios de conclusao

- [x] modal não herda altura fixa dos setup de jogos
- [x] shell sem min-height forçado que cria vão
- [x] altura acompanha o conteúdo (com max-height)

## Resultado da execucao

- `mediaPlayModalBody` próprio com `max-height` (sem height fixa)
- `mediaPlayShell` sem `min-height: 36rem`

## Arquivos alterados

- `front-end/src/pages/Main/Library/MediaPreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/000-index.md`

## Status final

done
