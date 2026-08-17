# Handoff - Task 547

## Task

- identificador: TASK-547
- título: Prévia web: parar áudio ao fechar e não cortar o parabéns
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 048 - Narração intro/conclusão dos jogos
- objetivo de negócio: reproduzir áudios gravados ao entrar e ao concluir os jogos
- entrega verificável: fechar a prévia silencia MP3/TTS; o parabéns não é cortado pelo cleanup da narração

## Decisões preservadas

- decisão: `useGameIntroAudio` registra cleanup sempre que `isOpen` é true, mesmo com `enabled=false`
- motivo: fechar durante o jogo (Quebra-cabeça, Qual está faltando, Intruso, Sombras) não chamava `stopBrowserGameSpeech()`
- impacto: o hook cobre o close sem reescrever todos os `onClose`

- decisão: `useGameFinishAudio` toca `finishAudioUrl` só após o estado concluído
- motivo: o handler disparava o parabéns no mesmo tick do `setState`, e o cleanup da narração o interrompia
- impacto: Semáforo, Diálogo, Emoções, Jogo dos erros e Escreva a letra

- decisão: payload de `gameConfig`/`locale` fica em ref atualizada por efeito, fora das deps do play
- motivo: evitar re-disparar o parabéns em re-render e cumprir `react-hooks/refs`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/547-previa-web-parar-audio-ao-fechar-e-concluir.md`
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `ajustes_frontend.md` | review aberto | confirmar os dois bugs |
| `useGameIntroAudio.ts` e prévias Library | implementação | ciclo de vida do áudio |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI/mídia | silenciar ao fechar o modal |
| `front-end/docs/ai/CODE_STYLE.md` | hook novo | arquivo próprio |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` | não se aplica a esta task |
| `design-system/front/` | sem alteração visual |
| `contracts/openapi.yaml` | sem API |
| `mobile/` | fora de escopo |

## Resultado por stack

- front-end: cleanup de intro + hook de finish nas prévias afetadas
- backend: não se aplica
- mobile: não se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Library/useGameIntroAudio.ts`
- `front-end/src/pages/Main/Library/useGameFinishAudio.ts`
- `front-end/src/pages/Main/Library/TrafficLightPreviewModal.tsx`
- `front-end/src/pages/Main/Library/DialoguePreviewModal.tsx`
- `front-end/src/pages/Main/Library/EmotionsPreviewModal.tsx`
- `front-end/src/pages/Main/Library/SpotDifferencePreviewModal.tsx`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `tasks/change-requests/547-previa-web-parar-audio-ao-fechar-e-concluir.md`
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`
- `tasks/000-index.md`

## Validações executadas

- validação: eslint dos hooks e prévias Semáforo/Diálogo/Emoções/Erros — 0 erros
- validação: eslint `GamePreviewModal.tsx` — warning preexistente `exhaustive-deps` em `content`

## Pendências ou bloqueios

- item: smoke manual nas prévias citadas (fechar durante feedback; ouvir parabéns até o fim)

## Próxima ação sugerida

- validar na Biblioteca web os jogos do review; não reabrir mobile nesta CR

## Próximo contexto recomendado

- `front-end/src/pages/Main/Library/useGameIntroAudio.ts`
- `front-end/src/pages/Main/Library/useGameFinishAudio.ts`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `contracts/openapi.yaml`
- motivo: correção só de ciclo de vida de áudio na prévia web
