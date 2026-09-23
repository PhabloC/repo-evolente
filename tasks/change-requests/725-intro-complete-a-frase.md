## Status

done

# Task 725 - Intro específico do Complete a frase

- **Tipo**: shared
- **Stacks envolvidos**: front-end, mobile
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; ajuste de sequência de áudio no cliente.
- **Modo de execução**: cross-stack
- **Slice vertical**: `tasks/slices/042-complete-a-frase.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task.
- **Contexto sob demanda**: `SentenceFillPreviewModal`, `GameSessionAudioProvider`, `GameActivityRenderer` e Task 724.
- **Orçamento de contexto**: até 8 fontes; limitar à fala inicial e à sequência da primeira cena.

## Objetivo

Fazer o Complete a frase falar “Vamos jogar o Complete a frase.” ao abrir, antes do áudio da primeira cena.

## Resultado da execucao

- Web e mobile usam a fala inicial específica da atividade via TTS.
- Depois da introdução, a rodada reproduz o `promptAudioUrl` do S3.
- O áudio antigo `audioUrl` continua reservado ao acerto.

## Status final

done
