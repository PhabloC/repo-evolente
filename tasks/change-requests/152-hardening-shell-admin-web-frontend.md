# Task 152 - Hardening do shell e do admin web no frontend

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

- `contracts/openapi.yaml#/paths/~1admin~1audit-logs`
- `contracts/openapi.yaml#/paths/~1admin~1reports~1audit-logs~1export`
- `contracts/openapi.yaml#/paths/~1users`

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual por stack

### Front-end

- tipo: continuidade de interface existente
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md`
- apoio local: `front-end/src/layout/MainLayout/*`, `front-end/src/pages/Main/Admin/*`, `front-end/src/pages/Main/AdminReports/*`, `front-end/src/pages/Main/AdminUsers/*`

## Objetivo

Aplicar os ajustes do code review em `ajustes_frontend.md` para endurecer o comportamento do shell autenticado e do módulo admin web sem reabrir redesign visual amplo.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/152-hardening-shell-admin-web-frontend.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-079.md`
- `.agents/state/handoffs/TASK-088.md`
- `.agents/state/handoffs/TASK-089.md`
- `.agents/state/handoffs/TASK-151.md`

## Contexto sob demanda

- `ajustes_frontend.md`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/AGENTS.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/QA.md`
- `front-end/src/layout/MainLayout/*`
- `front-end/src/pages/Main/Admin/*`
- `front-end/src/pages/Main/AdminReports/*`
- `front-end/src/pages/Main/AdminUsers/*`
- `front-end/src/services/admin/adminService.ts`
- `front-end/src/services/users/userService.ts`
- testes existentes do admin/shell e novos testes que a correção exigir

## Orçamento de contexto

- medio: shell autenticado + admin web + serviços consumidos por essas telas
- bloquear se a correção exigir mudança de contrato, redesign visual amplo ou refatoração transversal fora do módulo

## Dependencias

- Task 079
- Task 080
- Task 085
- Task 088
- Task 089
- Task 151

## Validacao esperada

- `npm run lint`
- `npm run test`
- `npm run build`

## Observacao

- Origem: code review consolidado em `ajustes_frontend.md`
- Escopo validado: shell global + logs/admin users + exportação de relatórios

## Resultado da execucao

- shell autenticado voltou a depender apenas do container interno para controle de overflow, removendo mutação global de `html/body`
- o workspace admin passou a tolerar falha parcial nos diretórios auxiliares de logs, descartar respostas obsoletas e preservar fallback explícito para ator desconhecido
- o modal de inativação de usuário passou a bloquear reenvio durante request pendente
- a exportação de relatórios passou a tolerar `content-disposition` UTF-8 malformado sem quebrar o download
- foram adicionados testes de regressão para usuários, logs e exportação admin

## Contexto utilizado

- `ajustes_frontend.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-079.md`
- `.agents/state/handoffs/TASK-088.md`
- `.agents/state/handoffs/TASK-089.md`
- `.agents/state/handoffs/TASK-151.md`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/AGENTS.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/QA.md`
- `front-end/src/layout/MainLayout/*`
- `front-end/src/pages/Main/Admin/*`
- `front-end/src/pages/Main/AdminReports/*`
- `front-end/src/pages/Main/AdminUsers/*`
- `front-end/src/services/admin/adminService.ts`
- `front-end/src/services/users/userService.ts`

## Arquivos alterados

- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminReports/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `front-end/src/pages/Main/AdminLogs/index.test.tsx`
- `front-end/src/pages/Main/AdminReports/index.test.tsx`
- `tasks/change-requests/152-hardening-shell-admin-web-frontend.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-152.md`

## Validacoes executadas

- `cd front-end && npm run test` ok
- `cd front-end && npm run lint` ok
- `cd front-end && npm run build` ok

## Pendencias pos-task

- nenhuma mudança funcional pendente dentro do escopo desta task
- a suíte completa ainda emite warnings antigos de `act(...)` em testes de cadastro auth fora do escopo desta entrega

## Handoff

- `.agents/state/handoffs/TASK-152.md`
- próximo contexto recomendado: `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`, `front-end/src/pages/Main/AdminUsers/index.tsx`, `front-end/src/pages/Main/AdminReports/index.tsx`

## Status final

done
