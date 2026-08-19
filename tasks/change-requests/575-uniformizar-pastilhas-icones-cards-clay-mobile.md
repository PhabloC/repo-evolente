# Task 575 - Uniformizar pastilhas de ícone dos cards clay mobile

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

- não aplicável; ajuste visual local.

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 — `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referência visual

- tipo: feedback visual do usuário.
- escopo: remover a borda destoante das pastilhas de ícone nos cards clay do perfil mobile, mantendo apenas profundidade suave.

## Contexto mínimo

- Governança raiz, índice, esta task, Slice 010 e handoff Task 574.

## Contexto sob demanda

- `mobile/src/features/shell/components/HomeActionCard/styles.ts` para ajustar somente a variação clay;
- `mobile/src/features/shell/components/HomeActionCard/index.tsx` para confirmar o escopo opt-in.

## Orçamento de contexto

- baixo; limitar ao componente de card e seus estilos.

## Estratégia de redução

- não alterar ícones, cores, tamanho, conteúdo, ações ou os cards fora do perfil.

## Dependências

- Task 574 (done)

## Resultado da execucao

- Removida a borda branca das pastilhas de ícone na variação clay dos cards do perfil mobile.
- O relevo macio por sombra foi preservado, deixando os ícones coerentes entre si sem contorno destoante.

## Contexto utilizado

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`

## Handoff

- `.agents/state/handoffs/TASK-575.md`

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- Rastreabilidade da task, Slice 010, índice e handoff.

## Validacoes executadas

- `npx eslint` focado no componente e estilos — ok.
- `git diff --check` — ok.

## Pendencias pos-task

- Nenhuma.

## Status final

done
