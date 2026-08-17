# Handoff - Task 329

## Task

- identificador: 329
- título: Vincular audios gravados no alfabeto falado
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catalogo
- objetivo de negócio: usar áudio gravado por letra no jogo `Alfabeto falado`, com fallback para as letras ainda sem arquivo
- entrega verificável: bucket atualizado, conteúdo `alphabet` vinculado e playback funcionando em web/mobile
- status do slice: done

## Decisões preservadas

- decisão: usar `letterAudioUrls` dentro do `gameConfig`
- motivo: manter a vinculação no próprio conteúdo jogável sem abrir tabela ou entidade nova
- impacto: o mapeamento por letra fica versionado junto do conteúdo

- decisão: manter fallback por letra para TTS
- motivo: apenas cinco letras tinham arquivo gravado nesta fase
- impacto: `B`, `C`, `D` e demais letras continuam funcionando sem regressão

- decisão: tratar `audio_letro_o.mp4` como letra `O`
- motivo: o arquivo local veio com typo no nome
- impacto: a letra `O` também entrou no vínculo sem exigir rename manual

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/329-vincular-audios-gravados-no-alfabeto-falado.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-327.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `backend/.env.local`, `backend/.env` | execução real | credenciais de bucket e banco |
| `backend/src/modules/contents/` | domínio do jogo | tipos, validação e bootstrap |
| `backend/scripts/` | upload real | script dedicado |
| `front-end/src/pages/Main/Library/` | preview web | playback gravado com fallback |
| `mobile/src/features/games/` | jogo real | playback gravado com fallback |

## Resultado por stack

- backend: done
- front-end: done
- mobile: done

## Arquivos alterados

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `backend/scripts/upload-alphabet-letter-audios.mjs`
- `backend/package.json`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `mobile/package.json`
- `mobile/package-lock.json`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/alphabetGame.ts`
- `mobile/src/features/games/utils/alphabetGame.test.ts`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.test.tsx`
- `tasks/change-requests/329-vincular-audios-gravados-no-alfabeto-falado.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-329.md`

## Validações executadas

- `cd backend && npm run test -- contents.service.spec.ts` — ok
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok
- `cd mobile && npm test -- --runInBand src/features/games/services/gameSpeechService.test.ts src/features/games/components/AlphabetGameRenderer/index.test.tsx src/features/games/utils/alphabetGame.test.ts` — ok
- `cd backend && npm run upload:alphabet-letter-audios` — ok

## Pendências ou bloqueios

- sem bloqueios
- novas letras gravadas exigem rerun do mesmo fluxo com os novos arquivos

## Próxima ação sugerida

- abrir nova task apenas se o produto quiser gerenciar os áudios por letra direto pela interface da biblioteca
