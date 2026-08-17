# Task 197 - Ícone SavePlus no botão criar usuário master

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto de negocio

### O que

Trocar o ícone do botão de criar usuário master para `SavePlus`.

## Criterios de conclusao

- [x] botão de criar usuário master usa SavePlus
- [x] lint ok

## Resultado da execucao

### Decisoes tomadas

- Header do modal mantém `ShieldPlus` (contexto admin/master).
- CTA "Criar usuário master" usa `SavePlus`, alinhado ao "Novo usuário".

### Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `tasks/change-requests/197-icone-save-plus-criar-usuario-master.md`
- `tasks/000-index.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/197-icone-save-plus-criar-usuario-master.md`

### Validacao executada

- `cd front-end && npm run lint` — ok
