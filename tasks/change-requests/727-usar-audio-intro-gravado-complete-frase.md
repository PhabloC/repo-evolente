## Status

done

# Task 727 - Usar áudio de introdução gravado do Complete a frase

- **Tipo**: shared
- **Stacks envolvidos**: front-end, mobile
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; uso do `introAudioUrl` já persistido.
- **Modo de execução**: cross-stack
- **Slice vertical**: `tasks/slices/042-complete-a-frase.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task.
- **Contexto sob demanda**: `audio_jogo_complete_frase.mp3`, `useGameIntroAudio.ts`, `GameSessionAudioProvider`, `GameActivityRenderer` e Task 726.
- **Orçamento de contexto**: até 8 fontes; limitar à troca de TTS pelo áudio gravado já publicado.

## Objetivo

Usar o arquivo gravado `audio_jogo_complete_frase.mp3` como introdução ao abrir a atividade, em vez de gerar a frase por TTS.

## Resultado da execucao

- Web voltou a reproduzir `introAudioUrl` na tela inicial da prévia.
- Mobile voltou a receber `introAudioUrl` no provider de áudio.
- O áudio `promptAudioUrl` da cena e o `audioUrl` de acerto permanecem separados.

## Status final

done
