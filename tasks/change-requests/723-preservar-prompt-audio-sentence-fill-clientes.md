## Status

done

# Task 723 - Preservar promptAudioUrl nos clientes do Complete a frase

- **Tipo**: shared
- **Stacks envolvidos**: front-end, mobile
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; correção de parsing do game config existente.
- **Modo de execução**: cross-stack
- **Slice vertical**: `tasks/slices/042-complete-a-frase.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task.
- **Contexto sob demanda**: `front-end/src/pages/Main/Library/sentenceFillGame.ts`, `mobile/src/features/games/utils/sentenceFillGame.ts`, `tasks/change-requests/722-reproduzir-audio-ao-entrar-na-frase.md`.
- **Orçamento de contexto**: até 8 fontes; limitar ao parsing e à reprodução do `promptAudioUrl` já persistido.

## Objetivo

Preservar `promptAudioUrl` ao converter a configuração recebida pela API, permitindo que o áudio do S3 seja reproduzido ao entrar em cada rodada.

## Resultado da execucao

- Web e mobile passaram a incluir `promptAudioUrl` em cada `SentenceFillRound` parseado.
- O efeito de entrada de rodada da Task 722 agora recebe o URL do S3; `audioUrl` de acerto permanece separado.

## Validacoes executadas

- Consulta do banco confirmou `promptAudioUrl` e `audioUrl` nas 10 rodadas.
- Busca de código confirmou a preservação nos parsers web e mobile.

## Status final

done
