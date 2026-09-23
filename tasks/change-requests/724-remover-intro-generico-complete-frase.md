## Status

done

# Task 724 - Remover introdução genérica do Complete a frase

- **Tipo**: shared
- **Stacks envolvidos**: front-end, mobile
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; ajuste de sequência de áudio no cliente.
- **Modo de execução**: cross-stack
- **Slice vertical**: `tasks/slices/042-complete-a-frase.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task.
- **Contexto sob demanda**: `front-end/src/pages/Main/Library/SentenceFillPreviewModal.tsx`, `mobile/src/features/games/renderers/GameActivityRenderer.tsx`, `front-end/src/pages/Main/Library/useGameIntroAudio.ts`, `mobile/src/features/games/components/GameSessionAudio/`.
- **Orçamento de contexto**: até 8 fontes; limitar à remoção do intro genérico e preservação da sequência da cena.

## Objetivo

Evitar que o Complete a frase fale “Vamos jogar” ao entrar e iniciar a atividade diretamente com o áudio da primeira cena.

## Resultado da execucao

- Prévia web deixou de executar o `introAudioUrl` genérico no Complete a frase.
- Runtime mobile deixou de passar `introAudioUrl` genérico para essa atividade.
- O áudio `promptAudioUrl` da primeira cena passa a ser a primeira fala da rodada, seguido do áudio de acerto antigo após a resposta correta.

## Status final

done
