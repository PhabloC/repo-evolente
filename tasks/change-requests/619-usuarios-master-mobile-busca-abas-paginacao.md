# Task 619 - Usuários master mobile: busca, abas e paginação

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /users` com `role`, `search`, `page` e `pageSize`.

## Modo de execução

single-stack

## Slice vertical

- Slice 009 — `tasks/slices/009-administracao-master.md`

## Objetivo

Dar ao master no app mobile pesquisa de usuários, abas Master/Profissionais/Pacientes e paginação da lista.

## Dependências

- Task 615 — done (`search` administrativo já existe no contrato)

## Contexto mínimo

- esta task
- `tasks/slices/009-administracao-master.md`
- `mobile/src/features/admin/{screens/AdminUsersScreen.tsx,hooks/useAdmin.ts,services/adminService.ts,types/admin.ts}`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI mobile | `mobile/src/features/admin/screens/usersStyles.ts` | seguir a composição e tokens existentes. |
| Acessibilidade | `mobile/docs/ai/MOBILE_PATTERNS.md` | controles de busca, aba e paginação acessíveis. |

## Orçamento de contexto

- baixo
- estratégia: reutilizar a paginação e filtros do endpoint de usuários, com busca local no modo demo.

## Critérios de aceite

- [x] Campo pesquisa nome/e-mail e reinicia na primeira página.
- [x] Abas filtram Master, Profissionais e Pacientes (responsáveis).
- [x] Paginação respeita total e não permite ultrapassar limites.
- [x] Estados de carregamento, vazio e controles possuem rótulos acessíveis.

## Resultado da execução

- Implementada lista filtrável e paginada por endpoint, incluindo dados demo.

## Contexto utilizado

- Task 619, Slice 009, AdminUsersScreen, service/types de admin e padrões mobile.

## Arquivos alterados

- `mobile/src/features/admin/{screens/AdminUsersScreen.tsx,screens/usersStyles.ts,services/adminService.ts,types/admin.ts}`.

## Validações executadas

- Typecheck mobile executado; os erros restantes são preexistentes em MasterProfile, Auth, jogos e Trail. As referências de cor desta task foram corrigidas.

## Pendências pós-task

- Smoke em dispositivo para layout das abas estreitas.

## Handoff

- Criado em `.agents/state/handoffs/TASK-619.md`.

## Status final

done
