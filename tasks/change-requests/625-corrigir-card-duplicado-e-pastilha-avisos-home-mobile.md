# Task 625 - Corrigir card duplicado e pastilha de avisos na Home mobile

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

- não aplicável; ajuste visual e de composição local.

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 — App do responsável: home, perfil e notificações
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Objetivo

Eliminar a duplicidade do card de avisos da Home e remover o segundo anel visual da pastilha de seu ícone.

## Comportamento esperado

- Apenas o primeiro card de avisos existente na Home é preservado.
- O card preservado usa pastilha plana, sem sombra/elevation que pareça uma segunda borda.
- Conteúdo, ação e estados do card preservado não são alterados.

## Referência visual

- Tipo: feedback visual do usuário.
- Mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`.

## Critérios de aceite

- [ ] A Home exibe apenas um card de avisos.
- [ ] A pastilha do ícone desse card exibe somente uma camada visual.
- [ ] O primeiro card de avisos continua com sua ação e seus estados atuais.
- [ ] Lint do escopo passa.

## Dependências

- Task 624 — done

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 010 e `.agents/state/handoffs/TASK-624.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Cards da Home | `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx` | identificar os dois cards e manter o primeiro |
| Pastilha clay | `mobile/src/features/shell/components/HomeActionCard/index.tsx` | aplicar a opção plana apenas ao card preservado |
| Referência visual | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | preservar linguagem visual |
| Convenções mobile | `mobile/docs/ai/AGENTS.md`, `CODE_STYLE.md`, `COMPONENT_REUSE.md`, `QA.md` | composição e validação |

## Orçamento de contexto

- baixo
- estratégia: alterar apenas a tela Home e usar a opção existente do card compartilhado; sem tocar API, notificações, backend ou outras telas.

## Resultado da execucao

- O card `Avisos da trilha`, primeiro na Home, recebeu `flatIconPill` e não mostra mais o anel externo da sombra clay.
- O segundo bloco de aviso visual, `Assinatura sem acesso`, foi removido da Home; o usuário mantém apenas o primeiro card de avisos solicitado.
- A ação e os estados de avisos (não lidos/em dia) foram preservados.

## Contexto utilizado

- Mínimo: AGENTS, GUIDE, context-map, índice, Task 625, Slice 010 e handoff Task 624.
- Sob demanda: tela Home, `HomeActionCard`, design system mobile e convenções locais de mobile.
- Não carregado: API, backend, rotas, web e demais features.

## Handoff

- `.agents/state/handoffs/TASK-625.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- backlog, Slice 010 e handoff desta task

## Validacoes executadas

- `npx eslint src/features/shell/screens/ResponsavelHomeScreen.tsx` — passou.
- `git diff --check` — passou.

## Pendencias pos-task

- Nenhuma.

## Status final

done
