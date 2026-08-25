# Task 615 - Ajustes da busca global no ambiente master

## Status

in_progress

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /users?search={termo}&pageSize={limite}` — ampliar o filtro administrativo para nome e e-mail, preservando autorização exclusiva de master.

## Modo de execução

cross-stack

## Slice vertical

- Slice 017 — `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Corrigir a sobreposição e fluidez do balão da busca global e permitir ao master encontrar usuários reais do sistema após o debounce, exibindo o local do resultado.

## Dependências

- Task 614 — done (busca de destinos com debounce)

## Contexto mínimo

- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-614.md`
- `front-end/src/layout/{Header,MainLayout}/`
- `front-end/src/services/users/userService.ts`
- rota `GET /users` do contrato OpenAPI

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Busca por usuário real | `backend/src/modules/users/` | incluir filtro seguro por nome/e-mail para master. |
| UI do popup | print enviado nesta conversa | popup acima do CTA e abertura fluida do campo. |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | anunciar carregamento e resultados sem perder interação por teclado. |

## Orçamento de contexto

- médio
- estratégia: reutilizar a listagem administrativa existente, limitar a busca remota a master e dispará-la somente depois de 350 ms sem digitação.

## Critérios de aceite

- [x] O popup dos resultados fica acima do botão `Novo usuário` e dos demais CTAs do conteúdo.
- [x] A pesquisa do master encontra usuários reais pelo nome ou e-mail após o debounce.
- [x] O resultado de usuário identifica que foi encontrado em `Usuários` e abre a visualização sem permissão de edição.
- [x] A animação de abertura do campo não usa transição de largura que provoque travamento perceptível.
- [x] Autorização master, contrato, testes e verificações das stacks envolvidas são atualizados.

## Resultado da execução

- O popup passou a integrar uma camada superior do header; a busca do master consulta usuários reais após o debounce e abre o modal de consulta do perfil. A abertura removeu a animação de largura e preservou apenas opacidade/deslocamento curto do campo.

## Contexto utilizado

- Task 615, Slice 017, handoff da Task 614, Header/MainLayout/AdminUsers, listagem administrativa de usuários e rota `GET /users` do contrato.

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/types/admin.ts`
- `front-end/src/types/headerSearch.ts`
- `backend/src/modules/users/dto/list-users-query.dto.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.repository.ts`
- `backend/src/modules/users/users.typeorm.repository.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/migrations/1900000000000-EnableUnaccentForUserSearch.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `backend/test/app.e2e-spec.ts`
- `contracts/openapi.yaml`
- `tasks/000-index.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-615.md`

## Validações executadas

- Front: `npm run test -- --run src/layout/Header/index.test.tsx` — 6 testes aprovados, incluindo resultado remoto após o debounce.
- Front: `npm run build` bloqueado por fixtures preexistentes de Pacientes/Planejamentos sem `guardian.subscriptionAccessGranted`; não há erro apontado nos arquivos desta task.
- Back: lint, typecheck, build, testes unitários/e2e focados e `git -C backend diff --check` executados pelo agente; não houve erro reportado e o diff check indicou apenas avisos de LF/CRLF.

## Pendências pós-task

- Smoke visual recomendado para confirmar a sobreposição sobre o CTA em desktop e a abertura do campo em dispositivos menos potentes.
- Corrigir separadamente as fixtures de Pacientes/Planejamentos sem `guardian.subscriptionAccessGranted` para restabelecer o build global.

## Handoff

- Criado em `.agents/state/handoffs/TASK-615.md`.

## Status final

done
