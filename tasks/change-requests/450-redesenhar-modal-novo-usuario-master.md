# Task 450 - Redesenhar modal de novo usuário master

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica; preservar payload e validacao existentes

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/009-administracao-master.md`

## Referencia visual

- print do modal atual no chat; redesign solicitado como layout totalmente diferente

## Objetivo

Recriar o modal de cadastro de usuario master com composicao visual nova (painel lateral + formulario), mantendo campos e regras.

## Criterios de conclusao

- [x] layout diferente do stack vertical simples
- [x] mesmos campos/validacoes/API
- [x] responsivo e acessivel

## Resultado da execucao

- modal com `hideHeader` e shell custom
- painel esquerdo azul (contexto master + checklist de acessos)
- formulario em grade 2x2 a direita, footer com acoes
- CTA primario em `info` (azul)

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/createMasterUserModal.module.css`

## Status final

done
