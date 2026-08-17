# Handoff - Task 403

## Task

- identificador: 403
- título: Alinhar dropdown de categorias da biblioteca web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web

## Decisões preservadas

- o select `Categoria` do modal da biblioteca passou a usar uma lista própria, separada da taxonomia da anamnese
- os rótulos visíveis seguem as categorias definidas no chat em 5 de agosto de 2026
- categorias legadas como `memoria` e `matematica` continuam abrindo no modal por fallback compatível

## Contexto utilizado

- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`

## Arquivos alterados

- constantes de conteúdo, modal da biblioteca, teste, task, slice, índice e handoff

## Validações executadas

- suíte `Library/index.test.tsx`

## Próximo contexto recomendado

- nenhum; ajuste localizado no dropdown do modal da biblioteca
