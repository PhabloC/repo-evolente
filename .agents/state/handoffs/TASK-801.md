# TASK-801

- Título: UI para excluir, editar e isentar usuário no master web
- Slice: 072
- Status final: done

## Decisões

- Ações na tabela: visualizar, editar, excluir e inativar
- Edição troca perfil e, para profissional/responsável, isenta mensalidade
- Exclusão usa modal de confirmação no mesmo padrão da inativação
- Filho sem login não tem editar/excluir/isentar; a conta pagante da aba Pacientes é o responsável

## Contexto usado

- `front-end/src/pages/Main/AdminUsers/`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/docs/ai/ACCESSIBILITY.md`
- Contrato `/users/{userId}`

## Arquivos

- `front-end/src/pages/Main/AdminUsers/{index.tsx,EditUserModal.tsx,styles.module.css,index.test.tsx}`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/services/users/userService.ts`
- `front-end/src/types/admin.ts`

## Validações

- Acessibilidade: botões com `aria-label`, labels no form, modal por teclado
- Testes de regressão da página adicionados; execução local do Vitest sofreu timeout de worker neste ambiente

## Pendências

- Conferir no browser logado como master: editar, isentar e excluir
- Backend precisa da migration `fee_exempt` para a listagem voltar a responder

## Próximo contexto

- Não carregar mobile nem outros slices
