# Handoff - Task 167

## Task

- identificador: 167
- título: TTS nativo no jogo do alfabeto sem upload de audio
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 028 - Runtime de jogos mobile extensivel
- objetivo de negócio: eliminar a dependência de áudio gravado para a fala básica do jogo
- entrega verificável: o alfabeto continua falando letras com voz nativa mesmo sem upload de áudio
- status do slice: done

## Decisões preservadas

- decisão: manter `expo-speech` como integração de voz
- motivo: a stack mobile já tinha essa base e ela atende o caso de letras isoladas
- impacto: não foi necessário introduzir SDK externo nem assets de áudio

- decisão: tratar `voiceMode=recorded` como fallback para TTS nativo
- motivo: o objetivo é não depender de upload manual de áudio
- impacto: o jogo segue operacional mesmo quando o catálogo não fornece mídia gravada

## Contexto utilizado

- `tasks/change-requests/167-tts-nativo-no-jogo-do-alfabeto-sem-upload-de-audio.md`
- `tasks/slices/028-runtime-jogos-mobile-extensivel.md`
- `.agents/state/handoffs/TASK-158.md`
- `.agents/state/handoffs/TASK-163.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `contracts/openapi.yaml`

## Arquivos alterados

- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.test.tsx`
- `tasks/change-requests/167-tts-nativo-no-jogo-do-alfabeto-sem-upload-de-audio.md`
- `tasks/slices/028-runtime-jogos-mobile-extensivel.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run typecheck` — ok
- `npm run test -- gameSpeechService AlphabetGameRenderer` — ok

## Pendencias ou bloqueios

- sem bloqueio
- a qualidade final da voz continua dependente da engine nativa disponível em cada aparelho

## Proxima acao sugerida

- se quiser padronizar mais a experiência, o próximo passo natural é só ajustar copy/feedback do jogo ou testar a voz em dispositivos reais iOS e Android
