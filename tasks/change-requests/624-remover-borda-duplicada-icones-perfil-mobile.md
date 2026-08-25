# Task 624 - Remover borda duplicada dos ícones no perfil mobile

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

- não aplicável; correção visual local.

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 — App do responsável: home, perfil e notificações
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Objetivo

Remover o efeito de duas bordas em tons distintos nas pastilhas dos ícones dos cards do perfil do responsável.

## Comportamento esperado

- Cada ícone de card do perfil mantém apenas um contorno visual coerente com a variação clay.
- A correção preserva tamanho, cor do ícone, sombra, conteúdo e ações dos cards.

## Referência visual

- Tipo: feedback visual do usuário.
- Evidência: imagem anexada nesta solicitação, que evidencia a borda interna e externa em cores diferentes.
- Mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`.

## Critérios de aceite

- [ ] Pastilhas dos cards de perfil não exibem borda interna e externa simultaneamente.
- [ ] Ícones permanecem legíveis e centralizados.
- [ ] Componentes fora do perfil não recebem alteração visual.
- [ ] Lint do escopo passa.

## Dependências

- Task 575 — done

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 010 e `.agents/state/handoffs/TASK-575.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Pastilhas do perfil | `mobile/src/features/shell/components/HomeActionCard/index.tsx`, `styles.ts` | localizar e remover o segundo contorno apenas na variação clay |
| Uso no perfil | `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx` e cards associados | confirmar que a alteração é opt-in do perfil |
| Referência visual | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | preservar linguagem visual |
| Convenções mobile | `mobile/docs/ai/AGENTS.md`, `CODE_STYLE.md`, `COMPONENT_REUSE.md`, `QA.md` | reutilização e validação |

## Orçamento de contexto

- baixo
- estratégia: limitar a inspeção ao componente compartilhado e a seus consumidores no perfil, sem alterar API, rotas, backend ou demais telas.

## Resultado da execucao

- A pastilha dos ícones passa a usar a opção `flatIconPill` nos cards do perfil, removendo apenas a sombra/elevation que formava o segundo anel.
- A opção foi aplicada ao card do responsável, Assinatura, crianças, cadastro/troca de filho e Relatórios.
- Os cards clay fora do Perfil não foram alterados.

## Contexto utilizado

- Mínimo: AGENTS, GUIDE, context-map, índice, Task 624, Slice 010 e handoff Task 575.
- Sob demanda: `HomeActionCard`, `SubscriptionManagementCard`, `ResponsavelProfileScreen`, design system mobile e convenções locais de mobile.
- Não carregado: API, backend, rotas, web e demais features.

## Handoff

- `.agents/state/handoffs/TASK-624.md`

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/children/utils/childFormInput.ts` (checagem defensiva de tipos corrigida durante a validação)
- backlog, Slice 010 e handoff desta task

## Validacoes executadas

- `npm test -- --runInBand src/features/children/utils/childFormInput.test.ts` — passou (1 suíte, 2 testes).
- `npx eslint` nos componentes/tela alterados e utilitário de data — passou.
- `git diff --check` — passou.
- `npm run typecheck` — continua bloqueado por erros preexistentes e fora deste escopo em Admin, Auth, jogos e trilha; não há mais erro na alteração desta task.

## Pendencias pos-task

- Nenhuma para o escopo desta task. Os erros de typecheck globais permanecem fora do escopo.

## Status final

done
