# Handoff - Task 258

## Task

- identificador: 258
- status final: done

## Decisoes preservadas

- o modal de criação de usuário master passou a seguir o mesmo padrão de telefone já usado no produto
- a validação continua opcional, mas só aceita números brasileiros com 10 ou 11 dígitos
- o payload enviado ao `createUser` agora sai sem máscara

## Contexto efetivamente usado

- `tasks/change-requests/258-normalizar-telefone-no-criar-usuario-master-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-155.md`
- `front-end/src/utils/phone.ts`
- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `tasks/change-requests/258-normalizar-telefone-no-criar-usuario-master-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-258.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/AdminUsers/index.test.tsx`
- `cd front-end && npm run lint`

## Pendencias ou bloqueios

- nenhuma

## Proximo contexto recomendado

- carregar a task 258 e os arquivos de `AdminUsers` se houver novo hardening no fluxo de criação/edição de usuários
