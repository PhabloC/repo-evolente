# Handoff - Task 152

## Identificador

- Task 152 - Hardening do shell e do admin web no frontend
- `tasks/change-requests/152-hardening-shell-admin-web-frontend.md`

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Status final

done

## Decisoes preservadas

- o shell autenticado deixou de mutar `html` e `body`; o bloqueio de overflow fica restrito ao container visual do layout
- o carregamento dos logs continua priorizando `/admin/audit-logs`, mas agora usa `Promise.allSettled` para diretórios auxiliares e não derruba a tela quando usuários ou assinaturas falham
- nomes de atores desconhecidos nos logs passaram a usar fallback explícito com `actorUserId`; `Sistema` ficou reservado apenas para ações sem ator
- o diretório auxiliar de usuários para logs passou a buscar todas as páginas disponíveis em lotes de 100
- respostas obsoletas do workspace admin passaram a ser descartadas via `requestId`, evitando overwrite ao trocar filtro/página rapidamente
- a confirmação de inativação fecha o modal imediatamente e bloqueia reenvio enquanto a linha está pendente
- a extração de nome de arquivo em exportações tolera `filename*=` malformado e cai para o nome de fallback
- os testes do admin users receberam timeout explícito de 15s porque a suíte completa do front leva mais de 5s nesses cenários, sem indicar falha funcional

## Contexto efetivamente usado

- `ajustes_frontend.md`
- `tasks/change-requests/152-hardening-shell-admin-web-frontend.md`
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
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminLogs/index.tsx`
- `front-end/src/pages/Main/AdminReports/index.tsx`

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
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-152.md`

## Validacoes executadas

- `cd front-end && npm run test` ok
- `cd front-end && npm run lint` ok
- `cd front-end && npm run build` ok

## Pendencias

- warnings antigos de `act(...)` continuam aparecendo em testes de `RegisterProfessional` e `RegisterGuardian`, mas não foram introduzidos por esta task

## Proximo contexto recomendado

- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminReports/index.tsx`

## Contexto que nao deve ser carregado

- backend, mobile e redesign visual amplo, salvo se uma próxima task alterar contrato HTTP ou expandir o módulo admin para além do hardening já aplicado
