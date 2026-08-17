# Task 485 - Compatibilizar quebra-cabeça legado sem `difficulty` no mobile

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

- sem mudança de schema; adaptação compatível no parser mobile

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/038-quebra-cabeca.md`

## Objetivo

Manter jogáveis no mobile as rodadas legadas de quebra-cabeça que ainda não trazem `difficulty`, inferindo a dificuldade pelo grid e preservando o seletor introduzido recentemente.

## Criterios de aceite

- [x] parser mobile infere `difficulty` por grid 3×3 / 4×4 / 5×5 quando o campo estiver ausente
- [x] filtro por dificuldade continua funcionando com configs novas e legadas
- [x] teste de regressão cobre rodadas sem `difficulty`
- [x] handoff gerado

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/038-quebra-cabeca.md`
- `tasks/change-requests/485-compatibilizar-quebra-cabeca-legado-sem-difficulty-mobile.md`
- `.agents/state/handoffs/TASK-479.md`

## Contexto sob demanda

- `mobile/AGENTS.md` e `mobile/docs/ai/AGENTS.md` — governança local
- `mobile/docs/ai/REPO_MAP.md` e `mobile/docs/ai/QA.md` — localização e validação
- `design-system/mobile/Design_System_Evolente_App_Mobile.md` — preservar fluxo guiado e setup atual

## Orçamento de contexto

- 8 fontes
- estratégia: limitar a `jigsawGame.ts`, renderer mobile e handoff do slice

## Resultado da execucao

Rodadas legadas sem `difficulty` voltaram a entrar no setup do quebra-cabeça mobile porque o parser agora deriva a dificuldade pelo tamanho do grid antes do filtro.

## Contexto utilizado

- slice 038
- handoff da task 479
- parser/filtro mobile do quebra-cabeça

## Handoff

- `.agents/state/handoffs/TASK-485.md`

## Arquivos alterados

- `mobile/src/features/games/utils/jigsawGame.ts`
- `mobile/src/features/games/utils/jigsawGame.test.ts`
- `tasks/slices/038-quebra-cabeca.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- --runInBand src/features/games/utils/jigsawGame.test.ts` — PASS

## Pendencias pos-task

- nenhuma

## Status final

done
