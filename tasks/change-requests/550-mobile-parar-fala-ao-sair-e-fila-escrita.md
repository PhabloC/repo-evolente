# Task 550 - Mobile: parar fala ao sair do jogo e não cortar o elogio na escrita

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- ciclo de vida de áudio; sem alteração visual

## Origem da solicitacao

Code review em `ajustes_mobile.md` itens 3 e 4:

3. `GameSessionAudio` sem `introAudioUrl` não registra cleanup; falas continuam na tela seguinte.
4. Escreva a letra: `announcePraise` e o enunciado da próxima letra competem via `stopGameSpeech`.

## Objetivo

Silenciar o áudio ao desmontar a sessão do jogo, mesmo sem intro, e encadear elogio → enunciado da próxima letra na escrita guiada.

## Escopo

- Cleanup incondicional com `stopGameSpeech()` no provider
- Aguardar o elogio antes de `setCurrentLetter` na escrita
- `announcePraise` (e cues) devem poder ser awaited

## Fora de escopo

- Prévia web (Task 547)
- Novos áudios ou catálogo
- Fila genérica em todos os jogos além da escrita

## Slice vertical

### Identificador do slice

Slice 048 - Narração intro/conclusão dos jogos

### Arquivo do slice

- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

### Objetivo de negocio

Reproduzir áudios ao entrar e ao concluir os jogos, sem vazamento ao sair.

### Entrega verificavel do slice

Sair de Diálogo/Semáforo (e demais) silencia a fala; na escrita, o elogio termina antes do próximo enunciado.

### Fora do slice

- Web
- Trilha demo / login

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Provider | `GameSessionAudio/index.tsx` | cleanup | sim |
| Escrita | `AlphabetWritingGameRenderer` | fila elogio/enunciado | sim |
| Fala | `gameSpeechService.ts` | promises de speak/stop | sim |
| Slice escrita | `tasks/slices/030-escrita-guiada-de-letras.md` | item 4 reabre o fluxo da escrita | sim |
| UI | `design-system/mobile/` | sem mudança visual | nao |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 4
- Risco de contexto excessivo: baixo
- Estratégia: só provider + escrita + speech service

## Dependencias

- Task 526, 527, 254 (done)

## Criterios de conclusao

- Sem `introAudioUrl`, unmount chama `stopGameSpeech()`
- Acerto de letra não final: elogio completa, depois o enunciado da próxima
- Sem mudança visual

## Instrucoes de implementacao

- Registrar cleanup mesmo no early-return sem URL de intro
- `playCue` retorna a promise de `speakGameText`
- Na escrita, `await announcePraise()` antes de trocar `currentLetter`

## Validacao esperada

- Leitura do cleanup incondicional
- Leitura do handleConfirm com await
- Lint dos arquivos

## Entregaveis esperados

- Provider com stop no unmount
- Escrita com fila elogio → enunciado
- Task, índice, slices 048/030 e handoff

## Resultado da execucao

- `GameSessionAudioProvider` registra `stopGameSpeech()` no cleanup mesmo sem `introAudioUrl`
- Cues (`announcePraise` etc.) retornam `Promise` para poder encadear
- Escrita guiada: `await announcePraise()` antes de trocar a letra
- Slices 048 e 030 permanecem done

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 048

### Contexto sob demanda carregado

- `GameSessionAudio/index.tsx`, `AlphabetWritingGameRenderer`, `gameSpeechService.ts`, slice 030

### Contexto não carregado

- `design-system/mobile/`, `contracts/openapi.yaml`, `front-end/`

## Handoff

- `.agents/state/handoffs/TASK-550.md`
- Próximo contexto: smoke saindo de Diálogo/Semáforo e acertando letra não final

## Arquivos alterados

- `mobile/src/features/games/components/GameSessionAudio/index.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
- `tasks/change-requests/550-mobile-parar-fala-ao-sair-e-fila-escrita.md`
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`

## Validacoes executadas

- eslint provider + escrita: 0 erros
- leitura: cleanup incondicional; handleConfirm aguarda o elogio

## Pendencias pos-task

- Smoke: sair do jogo sem intro e confirmar que o áudio para
- Smoke: acertar letra não final e ouvir elogio completo antes do próximo enunciado

## Status final

done
