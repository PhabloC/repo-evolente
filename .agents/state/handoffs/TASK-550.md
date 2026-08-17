# Handoff - Task 550

## Task

- identificador: TASK-550
- título: Mobile: parar fala ao sair do jogo e não cortar o elogio na escrita
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 048 (escrita relacionada no Slice 030)
- objetivo de negócio: narração dos jogos sem vazamento ao sair
- entrega verificável: unmount silencia fala; elogio da escrita termina antes do próximo enunciado

## Decisões preservadas

- decisão: cleanup de `stopGameSpeech()` mesmo sem `introAudioUrl`
- motivo: early-return do intro não registrava cleanup; Diálogo/Semáforo continuavam falando na tela seguinte
- impacto: todos os jogos no `GameSessionAudioProvider`

- decisão: `announcePraise` retorna Promise; escrita dá await antes de `setCurrentLetter`
- motivo: ambos chamavam `stopGameSpeech` no mesmo tick
- impacto: só a escrita encadeia; demais jogos continuam fire-and-forget

- decisão: `isIntroReady` derivado (`!url || completedIntroUrl === url`)
- motivo: evitar `setState` síncrono no efeito (react-hooks/set-state-in-effect)

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 550, slice 048

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `GameSessionAudio` | cleanup | stop incondicional |
| `AlphabetWritingGameRenderer` | corrida elogio/enunciado | await praise |
| slice 030 | item 4 | fluxo da escrita |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `front-end/` | Task 547 já cobriu a prévia web |

## Arquivos alterados

- `mobile/src/features/games/components/GameSessionAudio/index.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`

## Validações executadas

- validação: eslint provider + escrita — 0 erros

## Pendências ou bloqueios

- smoke sair do jogo e acertar letra não final

## Próxima ação sugerida

- validar no app; não reabrir web nesta CR

## Próximo contexto recomendado

- `GameSessionAudio/index.tsx`
- `AlphabetWritingGameRenderer/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `contracts/openapi.yaml`
- motivo: só ciclo de vida de áudio no runtime mobile
