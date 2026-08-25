# Handoff - Task 615

## Task

- TASK-615 - Ajustes da busca global no ambiente master
- Slice 017 — Redesign da interface interna web
- status final: done

## Decisões preservadas

- O popup da busca pertence à camada elevada do Header (`z-index` 30 dentro de header em camada 10), para ficar acima dos CTAs do conteúdo.
- A abertura do campo não anima mais `width`; apenas o conteúdo interno recebe transição curta de opacidade e deslocamento.
- Só o master consulta usuários reais, pelo endpoint administrativo existente, após 350 ms sem digitação. A consulta aceita nome/e-mail parcialmente, sem diferença de caixa ou acentos.
- Um resultado de usuário leva a `/admin/usuarios?profileId=...`; a tela abre o modal de perfil já somente leitura e limpa o parâmetro da URL.

## Contexto efetivamente usado

- Task 615, Slice 017, handoff Task 614, Header/MainLayout/AdminUsers, serviço de usuários, contrato `GET /users` e acessibilidade web.

## Arquivos alterados

- Header, MainLayout e AdminUsers do `front-end`; tipo `headerSearch` e parâmetro `search` de listagem administrativa.
- Repositórios/serviço/DTO/testes/migration de usuários no backend e contrato OpenAPI.

## Validações

- `npm run test -- --run src/layout/Header/index.test.tsx` — 6 testes aprovados, incluindo resultado remoto após o debounce.
- `npm run build` do front-end está bloqueado por fixtures preexistentes de Pacientes/Planejamentos sem `guardian.subscriptionAccessGranted`, fora dos arquivos desta task.
- Backend: lint, typecheck, build, testes focados/e2e e diff check foram executados sem erro reportado pelo agente.

## Pendências ou bloqueios

- Smoke visual do popup sobre CTAs e da abertura do campo em dispositivo de menor desempenho.
- Corrigir separadamente as fixtures de Pacientes/Planejamentos sem `guardian.subscriptionAccessGranted` para restabelecer o build global.

## Próximo contexto recomendado

- `front-end/src/layout/Header/` e `backend/src/modules/users/`, se for necessário expandir a busca para outros domínios além de usuários master.
