# Task 483 - Fluência: áudio gravado por etapa no runtime mobile

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

- sem mudança de schema; compatibilização do parser/runtime mobile com `audioUrl` já publicado no `gameConfig`

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/045-fluencia-em-acao.md`

## Objetivo

Fazer o renderer mobile de Fluência em Ação reproduzir áudio gravado por etapa quando o conteúdo vier com `voiceMode: recorded` e `audioUrl`, sem reabrir escopo de microfone ou gravação local.

## Criterios de aceite

- [x] parser mobile preserva `audioUrl` por etapa
- [x] renderer envia `audioUrl` para `speakGameText`
- [x] teste de regressão cobre stage gravado
- [x] handoff gerado

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/045-fluencia-em-acao.md`
- `tasks/change-requests/483-fluencia-audio-gravado-runtime-mobile.md`
- `.agents/state/handoffs/TASK-436.md`

## Contexto sob demanda

- `mobile/AGENTS.md` e `mobile/docs/ai/AGENTS.md` — governança local da stack
- `mobile/docs/ai/REPO_MAP.md` e `mobile/docs/ai/QA.md` — localização e validação mínima
- `design-system/mobile/Design_System_Evolente_App_Mobile.md` — manter tom e feedback existentes do jogo

## Orçamento de contexto

- 8 fontes
- estratégia: limitar à stack mobile e ao slice 045

## Resultado da execucao

O runtime mobile de Fluência em Ação agora preserva `audioUrl` por etapa e tenta reproduzir o áudio gravado configurado antes do fallback existente para TTS.

## Contexto utilizado

- slice 045
- handoff da task 436
- renderer/parser mobile de fluência

## Handoff

- `.agents/state/handoffs/TASK-483.md`

## Arquivos alterados

- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/fluencyGame.ts`
- `mobile/src/features/games/components/FluencyGameRenderer/index.tsx`
- `mobile/src/features/games/components/FluencyGameRenderer/index.test.tsx`
- `tasks/slices/045-fluencia-em-acao.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- --runInBand src/features/games/components/FluencyGameRenderer/index.test.tsx` — PASS

## Pendencias pos-task

- nenhuma para o runtime mobile; gravação/captação continua fora de escopo

## Status final

done
