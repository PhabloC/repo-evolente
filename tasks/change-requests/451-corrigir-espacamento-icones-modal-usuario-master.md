# Task 451 - Corrigir espaçamento e ícones do modal de usuário master

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

- `tasks/slices/009-administracao-master.md`

## Objetivo

Corrigir inputs do modal de novo usuario master: mais espacamento e icones internos, sem quebrar layout.

## Criterios de conclusao

- [x] inputs com icone alinhado
- [x] espaçamento horizontal/vertical maior na grade
- [x] helper texts nao colapsam a grade

## Resultado da execucao

- `Input` ganhou `leadingIcon` com padding e alinhamento corretos
- grade do modal com gaps maiores
- spacer de mensagem para alinhar linhas da grade

## Arquivos alterados

- `front-end/src/ui/Input/index.tsx`
- `front-end/src/ui/Input/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/createMasterUserModal.module.css`

## Status final

done
