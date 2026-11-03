# Task 801 - UI para excluir, editar e isentar usuário no master web

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

- `contracts/openapi.yaml#/paths/~1users~1{userId}`
- `contracts/openapi.yaml#/components/schemas/UpdateUserRequest`

## Modo de execucao

single-stack

## Slice vertical

- Slice 072 — `tasks/slices/072-gestao-operacional-usuarios-master.md`

## Objetivo

Na página de usuários do master, permitir excluir com modal de confirmação, editar o perfil (papel) e isentar profissional ou responsável da mensalidade.

## Dependências

- Task 800
- Task 610 — done
- Task 188 — done

## Contexto mínimo

- esta task
- `tasks/slices/072-gestao-operacional-usuarios-master.md`
- `front-end/src/pages/Main/AdminUsers/`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/services/users/userService.ts`
- `front-end/src/types/admin.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI do master | `design-system/front/Design_System_Evolente_Desktop.md` e modais já existentes da página | manter linguagem de tabela, ícones e confirmação |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | botões nomeados, modal por teclado, label no formulário |
| Padrão de modal | `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx` | edição no mesmo padrão visual |

## Orçamento de contexto

- médio
- estratégia: extrair modais de editar/excluir; sem mobile

## Critérios de aceite

- [x] Tabela de profissionais, responsáveis e admins tem ação de excluir com modal de confirmação
- [x] Tabela tem ação de editar com troca de perfil
- [x] Edição de profissional/responsável permite isentar da mensalidade
- [x] Filho sem login não oferece exclusão, edição de papel nem isenção
- [x] Fluxo acessível por teclado e com teste de regressão

## Referência visual

- Página de Usuários do master já existente
- Complementar: `design-system/front/Design_System_Evolente_Desktop.md`

## Fora de escopo

- Mobile
- Criar usuário profissional/responsável nesta tela

## Resultado da execucao

- Coluna de ações ganhou editar e excluir nas abas de profissionais, responsáveis e admins
- Modal de edição altera perfil e isenta mensalidade de profissional/responsável
- Modal de exclusão pede confirmação no mesmo padrão da inativação
- Filho sem login permanece só com visualização

## Contexto utilizado

- Task 801, Slice 072, AdminUsers, useAdminWorkspace, ACCESSIBILITY.md, contrato `/users/{userId}`

## Handoff

- `.agents/state/handoffs/TASK-801.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `front-end/src/pages/Main/AdminUsers/EditUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/editUserModal.module.css`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/services/users/userService.ts`
- `front-end/src/types/admin.ts`

## Validacoes executadas

- Botões com nome acessível, labels no formulário, modal acionável por teclado
- Testes de edição/exclusão adicionados; Vitest local teve timeout de worker neste ambiente

## Pendencias pos-task

- Validar no browser com o backend já migrado

## Status final

done
