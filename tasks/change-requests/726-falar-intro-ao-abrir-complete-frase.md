## Status

done

# Task 726 - Falar introdução ao abrir o Complete a frase

- **Tipo**: front
- **Stacks envolvidos**: front-end (React/Vite)
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; ajuste de sequência da prévia web.
- **Modo de execução**: single-stack
- **Slice vertical**: `tasks/slices/042-complete-a-frase.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task.
- **Contexto sob demanda**: `front-end/src/pages/Main/Library/SentenceFillPreviewModal.tsx`, `tasks/change-requests/725-intro-complete-a-frase.md`.
- **Orçamento de contexto**: até 8 fontes; limitar à fala da tela inicial e ao áudio da primeira rodada.

## Objetivo

Fazer a prévia web falar “Vamos jogar o Complete a frase.” assim que a tela inicial da atividade abrir.

## Resultado da execucao

- A fala inicial agora acontece na fase `setup`, antes do botão “Começar jogo”.
- Ao iniciar o jogo, a primeira rodada toca somente o `promptAudioUrl` da cena.
- O áudio `audioUrl` após acerto não foi alterado.

## Status final

done
