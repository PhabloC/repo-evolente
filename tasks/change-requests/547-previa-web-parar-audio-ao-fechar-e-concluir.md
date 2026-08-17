# Task 547 - Prévia web: parar áudio ao fechar e não cortar o parabéns

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora de escopo desta task)

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- sem alteração visual; comportamento de áudio na prévia da biblioteca

### Regra de aderencia visual

- não reinterpretar layout, tokens ou copy; só ciclo de vida de MP3/TTS

## Origem da solicitacao

Code review em `ajustes_frontend.md`:

1. `useGameIntroAudio` não registra cleanup quando `enabled=false`; fechar a prévia durante feedback deixa MP3/TTS tocando.
2. Ao concluir, o cleanup do efeito de narração chama `stopBrowserGameSpeech()` depois do áudio final ter começado e o interrompe.

## Objetivo

Corrigir o ciclo de vida do áudio nas prévias web: silenciar ao fechar o modal fora do setup, e reproduzir o áudio de conclusão depois da limpeza da narração anterior.

## Escopo

- Registrar cleanup de `useGameIntroAudio` enquanto o modal estiver aberto, independente de `enabled`
- Iniciar o áudio de `finishAudioUrl` em efeito do estado concluído, depois do cleanup da narração, em Semáforo, Diálogo, Emoções, Jogo dos erros e Escreva a letra (mesmo padrão)
- Remover `speakLibraryFinishAudio` dos handlers que disparam a transição para concluído nesses jogos

## Fora de escopo

- Runtime mobile
- Novos áudios, contrato ou catálogo
- Alteração visual dos modais
- Reescrever todos os `onClose` se o hook de intro já silenciar no close/`isOpen=false`

## Entradas

- `ajustes_frontend.md`
- `front-end/src/pages/Main/Library/useGameIntroAudio.ts`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `front-end/src/pages/Main/Library/librarySharedFeedback.ts`
- prévias: TrafficLight, Dialogue, Emotions, SpotDifference, GamePreviewModal (escrita)
- Task 538, Task 542
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Slice vertical

### Identificador do slice

Slice 048 - Narração intro/conclusão dos jogos

### Arquivo do slice

- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

### Objetivo de negocio

Reproduzir áudios gravados ao entrar e ao concluir os jogos terapêuticos.

### Entrega verificavel do slice

Áudio de conclusão toca até o fim na prévia web; fechar o modal durante o jogo silencia MP3/TTS.

### Fora do slice

- Mobile
- Prioridade 2/3 restante

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Processo/contexto | `.agents/references/context-engineering.md` | somente se houver duvida sobre slice, handoff ou orçamento | nao |
| UI web | `design-system/front/` | somente se esta task alterar UI web | nao |
| API | `contracts/openapi.yaml` | somente se esta task consumir/criar endpoint | nao |
| Stack local | `front-end/docs/ai/ACCESSIBILITY.md` | estados dinâmicos de áudio em modal | sim |
| Stack local | `front-end/docs/ai/CODE_STYLE.md` | ao criar hook compartilhado | sim |
| Implementação | `useGameIntroAudio.ts`, `libraryGameSpeech.ts`, `librarySharedFeedback.ts`, prévias citadas | ao corrigir o ciclo de vida | sim |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 5
- Risco de contexto excessivo: baixo
- Estratégia para reduzir contexto: não carregar requirements, contrato, mobile nem design-system; limitar às prévias com o padrão do review

## Dependencias

- Task 538 (done) — intro na prévia web
- Task 542 (done) — feedbacks curtos + finish na prévia web

## Criterios de conclusao

- Fechar Quebra-cabeça, Qual está faltando, Intruso ou Sombras durante um feedback silencia o áudio
- Concluir Semáforo, Diálogo, Emoções, Jogo dos erros e Escreva a letra toca o parabéns sem corte imediato
- Sem mudança visual nos modais

## Instrucoes de implementacao

- Em `useGameIntroAudio`, registrar cleanup com `stopBrowserGameSpeech()` sempre que `isOpen` for true, mesmo com `enabled=false`
- Extrair hook de conclusão (`useGameFinishAudio` ou equivalente) que toca `speakLibraryFinishAudio` só depois do estado concluído, com `await Promise.resolve()` para não perder a corrida do cleanup irmão
- Nos handlers de vitória afetados, apenas transicionar estado; não disparar o áudio final no mesmo tick do `setState`

## Validacao esperada

- Leitura do ciclo: close com `enabled=false` registra cleanup
- Leitura do ciclo: finish inicia em efeito do estado `done`/`finished`, não no handler
- Lint dos arquivos alterados

## Entregaveis esperados

- Hook de intro com cleanup independente de `enabled`
- Áudio de conclusão iniciado após cleanup da narração nas prévias afetadas
- Task, índice, slice e handoff atualizados

## Riscos ou ambiguidades

- `gameConfig` no array de deps do efeito de finish não deve re-disparar o parabéns em re-render
- Escreva a letra: `enabled` do finish só quando `progressIndex` já cobriu todas as letras e `currentLetter` é null, para não tocar no mount

## Resultado da execucao

- front-end: `useGameIntroAudio` registra `stopBrowserGameSpeech()` enquanto o modal está aberto, mesmo fora do setup
- front-end: `useGameFinishAudio` toca o parabéns só depois do estado concluído, após o cleanup da narração irmã
- Semáforo, Diálogo, Emoções, Jogo dos erros e Escreva a letra deixam de disparar finish no handler
- Slice 048 permanece done; esta CR corrige o ciclo de vida da prévia web
- Sem contrato e sem mudança visual
- Acessibilidade: fechar o modal silencia MP3/TTS (estado dinâmico de mídia); sem alteração de foco/rótulos
- Qualidade estrutural: hook de conclusão em arquivo próprio ao lado de `useGameIntroAudio`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

### Contexto sob demanda carregado

- `ajustes_frontend.md` — origem do review
- `front-end/src/pages/Main/Library/useGameIntroAudio.ts` e prévias citadas — ciclo de vida do áudio
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts` / `librarySharedFeedback.ts` — stop/finish
- `front-end/docs/ai/ACCESSIBILITY.md` — estados dinâmicos de mídia
- `front-end/docs/ai/CODE_STYLE.md` — hook compartilhado

### Contexto não carregado

- `requirements/` — sem ambiguidade de negócio
- `design-system/front/` — sem alteração visual
- `contracts/openapi.yaml` — sem API
- `mobile/` — fora de escopo

## Handoff

- `.agents/state/handoffs/TASK-547.md`
- Decisão: cleanup do intro independe de `enabled`; finish em efeito do estado concluído, com payload em ref para não re-disparar
- Próximo contexto: smoke manual nas prévias citadas
- Pendência: aviso preexistente `react-hooks/exhaustive-deps` em `GamePreviewModal.tsx` (efeito da escrita)

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

## Validacoes executadas

- eslint nos hooks e prévias Semáforo/Diálogo/Emoções/Erros: 0 erros
- eslint `GamePreviewModal.tsx`: 0 erros; 1 warning preexistente (`content` no efeito da escrita)
- leitura do ciclo: `isOpen && !enabled` agora registra cleanup; finish sai do handler

## Qualidade estrutural

- `useGameFinishAudio` em arquivo próprio na pasta Library, no mesmo padrão de `useGameIntroAudio`
- sem novos tipos de domínio; props do hook ficam no próprio arquivo

## Aderencia ao design system

- tipo: nao se aplica
- fonte primaria: comportamento de áudio, sem UI
- desvios: nenhum

## Pendencias pos-task

- Smoke manual: fechar Quebra-cabeça/Qual está faltando/Intruso/Sombras durante feedback
- Smoke manual: concluir Semáforo, Diálogo, Emoções, Jogo dos erros e Escreva a letra e ouvir o parabéns até o fim

## Status final

done
