# Task 574 - Aplicar claymorphism aos cards do perfil do responsável mobile

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

- não aplicável; alteração apenas visual.

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 — `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referência visual

- tipo: solicitação visual do usuário.
- escopo: aplicar linguagem claymorphism aos três cards do perfil do responsável: responsável, criança/trocar filho e relatórios.

## Contexto mínimo

- Governança raiz, índice, esta task, Slice 010 e handoff Task 573.

## Contexto sob demanda

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx` e estilos adjacentes para identificar os três cards;
- `mobile/src/features/shell/components/HomeActionCard/**` para preservar o componente compartilhado;
- `mobile/docs/ai/` de acessibilidade e componentes reutilizáveis, se disponível.

## Orçamento de contexto

- baixo; limitar ao perfil mobile e ao componente de card reutilizado.

## Estratégia de redução

- não alterar dados, navegação, ações, contratos ou os cards de outras telas.

## Dependências

- Task 357 (done)
- Task 369 (done)
- Task 570 (done)

## Resultado da execucao

- Os cards de responsável, criança, trocar filho e relatórios no perfil mobile agora usam uma variação claymorphism: cantos mais arredondados, superfícies claras, bordas suaves, sombras macias e pastilhas elevadas.
- A variação é opt-in no `HomeActionCard`, portanto os cards de outras telas não foram alterados.

## Contexto utilizado

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/docs/ai/COMPONENT_REUSE.md`

## Handoff

- `.agents/state/handoffs/TASK-574.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- Rastreabilidade da task, Slice 010, índice e handoff.

## Validacoes executadas

- `npx eslint` focado nos três arquivos alterados — ok.
- `git diff --check` — ok.
- `npm run lint` — bloqueado por 30 erros preexistentes de refs acessadas durante o render em `features/auth/**` e `shared/components/AppBackgroundBubbles/**`.
- `npm run typecheck` — bloqueado por erros preexistentes em telas admin, auth, jogos e trilha; nenhum erro nos arquivos desta task.

## Pendencias pos-task

- Validar o acabamento visual no dispositivo/Expo para calibrar sombras nativas se necessário.

## Status final

done
