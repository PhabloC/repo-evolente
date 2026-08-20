# Task 589 - Isolar cache de filhos por responsavel no mobile

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

- Sem alteracao de contrato; consumo existente de `GET /guardians/me/children`.

## Modo de execucao

single-stack

## Slice vertical

- Slice 051 - `tasks/slices/051-seletor-filho-mobile.md`

## Contexto mínimo

- Indice, Slice 051, hook de filhos e sessao mobile.

## Contexto sob demanda

- TanStack Query e consumidores do hook, para propagar a chave por usuario.

## Orçamento de contexto

- baixo; limitar a sessao e selecao de filhos.

## Estratégia de redução

- Sem alterar API, storage ou telas fora do bootstrap/seletor.

## Resultado da execucao

- A query de filhos agora inclui o `userId` autenticado na chave e permanece desabilitada sem sessao.

## Contexto utilizado

- `mobile/src/features/children/hooks/useGuardianChildrenQuery.ts`
- `mobile/src/features/children/hooks/useSelectChildScreen.ts`
- `mobile/src/features/children/hooks/useChildSelectionBootstrap.ts`

## Handoff

- `.agents/state/handoffs/TASK-589.md`

## Arquivos alterados

- Hooks de selecao e consulta de filhos do mobile.

## Validacoes executadas

- `npx jest src/features/children/hooks/useGuardianChildrenQuery.test.ts --runInBand` - ok.
- `npm run typecheck` no mobile - bloqueado por erros preexistentes fora do escopo (admin, jogos e trilhas).

## Pendencias pos-task

- Nenhuma.

## Status final

done
