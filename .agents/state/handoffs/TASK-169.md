# Handoff - Task 169

## Task

- identificador: 169
- título: Segundo jogo escrita guiada de letras
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 030 - Escrita guiada de letras
- objetivo de negócio: entregar o segundo jogo terapêutico do alfabeto com escrita guiada e feedback imediato
- entrega verificável: novo jogo disponível no catálogo, visível na biblioteca, selecionável em trilhas e jogável no mobile
- status do slice: done

## Decisões preservadas

- decisão: reutilizar TTS nativo para instruções e feedback do novo jogo
- motivo: manter consistência com o primeiro jogo e evitar dependência de upload de áudio
- impacto: a voz continua funcional em web/mobile, com qualidade dependente do dispositivo

- decisão: validar a escrita com heurística local por checkpoints em vez de reconhecimento externo
- motivo: atender o fluxo pedido sem criar dependência de IA ou backend novo
- impacto: o conjunto inicial fica controlado e precisa de teste real antes de expandir

- decisão: manter a autoria do jogo em código e expor na UI apenas metadados gerenciáveis
- motivo: o catálogo do master deve ativar/inativar e categorizar jogos, não construir a mecânica
- impacto: o modal de edição preserva `gameConfig` existente sem reabrir campos técnicos

## Contexto utilizado

- `tasks/change-requests/169-segundo-jogo-escrita-guiada-de-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-168.md`
- `.agents/state/handoffs/TASK-167.md`
- `.agents/state/handoffs/TASK-163.md`
- `contracts/openapi.yaml`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/utils/gameMetadata.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.test.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.test.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/styles.ts`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `tasks/change-requests/169-segundo-jogo-escrita-guiada-de-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`

## Validações executadas

- `cd backend && npm run test -- contents` — ok
- `cd front-end && npm run lint` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npm run test -- src/pages/Main/Library/index.test.tsx` — ok
- `cd mobile && npm run lint` — ok
- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm run test -- games` — ok

## Pendências ou bloqueios

- sem bloqueio
- validar a tolerância da heurística de escrita em dispositivo real antes de ampliar além do conjunto inicial

## Próximo contexto recomendado

- se o próximo passo for ampliar o catálogo, carregar `TASK-169.md`, `TASK-168.md` e os módulos `Library`/`features/games`
