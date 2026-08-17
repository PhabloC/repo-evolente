# Task 155 - Criar usuário master na página de usuários web

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1users/post`

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste incremental solicitado no chat

### Fonte primaria visual

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`

### Lacunas

- sem print dedicado
- decisao: seguir a linguagem operacional já consolidada na rota dedicada de usuários, adicionando CTA e fluxo de criação sem reabrir o layout global

## Objetivo

Permitir que o usuário master crie outro login de usuário master diretamente na página de usuários do admin web.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-077.md`
- `.agents/state/handoffs/TASK-154.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Contrato de criação | `contracts/openapi.yaml#/paths/~1users/post` | confirmar payload e resposta do cadastro administrativo | sim |
| UI web | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | manter coerência estrutural, acessibilidade e padrões da stack | sim |
| Fluxo atual da rota | `front-end/src/pages/Main/AdminUsers/index.tsx`, `front-end/src/pages/Main/Admin/sections.tsx`, `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`, `front-end/src/pages/Main/Admin/styles.module.css` | inserir CTA, modal e atualização da lista | sim |
| Tipos e serviços | `front-end/src/services/users/userService.ts`, `front-end/src/types/admin.ts`, `front-end/src/types/role.ts` | conectar criação ao endpoint existente e tipar o fluxo | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à rota `/admin/usuarios` e ao serviço de usuários, sem tocar backend nem outras áreas do módulo admin

## Criterios de conclusao

- [x] página de usuários expõe ação clara para criar outro usuário master
- [x] formulário cria o novo login via `POST /users` com feedback de sucesso/erro
- [x] listagem atualiza sem exigir refresh manual
- [x] lint, testes relevantes e build do front-end aprovados

## Dependencias

- Task 022 - done
- Task 077 - done
- Task 154 - done

## Resultado da execucao

- o contrato OpenAPI passou a documentar `POST /users` com payload e respostas alinhados ao backend já existente
- a rota `AdminUsers` ganhou CTA dedicado para criar outro login master sem sair da operação atual
- o modal de criação valida nome, e-mail, telefone opcional e senha forte antes de enviar o cadastro
- após sucesso, a página mostra feedback global e recarrega a listagem atual sem refresh manual

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-077.md`
- `.agents/state/handoffs/TASK-154.md`

### Sob demanda

- `contracts/openapi.yaml#/paths/~1users/post`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/services/users/userService.ts`
- `front-end/src/types/admin.ts`
- `front-end/src/types/role.ts`

### Contexto evitado

- backend, mobile, logs, relatórios e overview do admin por não participarem da criação do usuário master nesta entrega

## Handoff

- `.agents/state/handoffs/TASK-155.md`

## Arquivos alterados

- `tasks/change-requests/155-criar-usuario-master-na-pagina-de-usuarios-web.md`
- `contracts/openapi.yaml`
- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/createMasterUserModal.module.css`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/services/users/userService.ts`
- `front-end/src/types/admin.ts`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-155.md`

## Validacoes executadas

- `cd front-end && npm run test -- src/pages/Main/AdminUsers/index.test.tsx` - ok
- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
