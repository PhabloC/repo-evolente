# Handoff - Task 182

## Task

- identificador: 182
- título: Avatar no sidebar e na página de usuários web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 027 - Fotos de perfil em bucket
- objetivo de negócio: refletir foto persistida no shell e na listagem de usuários
- entrega verificável: sidebar e página de usuários exibem `avatarUrl` com fallback por inicial
- status do slice: done

## Decisões preservadas

- sem alteração de backend/contrato; `avatarUrl` já vinha da API
- sidebar lê `user.avatarUrl` do `authStore` via `MainLayout`
- listagem tipa `AdminUser.avatarUrl` e renderiza imagem na coluna Usuário
- sem foto continua mostrando a inicial

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/182-avatar-sidebar-e-pagina-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-162.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/layout/Sidebar/**`, `MainLayout` | sidebar | avatar do usuário logado |
| `front-end/src/pages/Main/Admin/**`, `AdminUsers/**` | listagem | avatar na tabela |
| `front-end/src/types/admin.ts` | tipagem | `avatarUrl` |

## Resultado por stack

- front-end: done

## Arquivos alterados

- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/styles.module.css`
- `front-end/src/layout/Sidebar/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/types/admin.ts`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validações executadas

- front-end lint: ok
- front-end test Sidebar + AdminUsers: ok
- front-end build: ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- abrir CR só se quiser avatar também no mobile/responsável ou em outras listagens (ex.: pacientes)

## Próximo contexto recomendado

- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`

## Contexto que não deve ser carregado na próxima etapa

- backend/storage de avatar
- motivo: esta entrega foi só de exibição no front
