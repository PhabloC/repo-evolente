## Status

done

# Task 722 - Reproduzir áudio da cena ao entrar no Complete a frase

- **Tipo**: shared
- **Stacks envolvidos**: backend, front-end, mobile
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; extensão do game config persistido, sem novo endpoint.
- **Modo de execução**: cross-stack
- **Slice vertical**: `tasks/slices/042-complete-a-frase.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task.
- **Contexto sob demanda**: `tasks/change-requests/721-upload-audios-complete-frase-cenas.md`, `backend/scripts/upload-sentence-fill-phrase-audios.mjs`, `backend/src/modules/contents/sentence-fill-game-assets.ts`, `backend/src/modules/contents/contents.service.ts`, `front-end/src/pages/Main/Library/SentenceFillPreviewModal.tsx`, `mobile/src/features/games/components/SentenceFillGameRenderer/` e os áudios de `audio_atividades`/`audio_atividades2`.
- **Orçamento de contexto**: até 8 fontes; limitar a alteração à separação entre áudio de entrada da rodada e áudio da frase completa após acerto.

## Objetivo

Reproduzir o áudio-pergunta de cada cena assim que a rodada aparecer no jogo **Complete a frase**, mantendo o áudio da frase completa que já é reproduzido após o acerto.

## Critérios de aceite

- [x] Cada rodada suporta um áudio de entrada separado do áudio de acerto.
- [x] O áudio de `audio_atividades2` toca ao entrar na primeira rodada e ao avançar para cada nova rodada, no web e no mobile.
- [x] O áudio completo de `audio_atividades` continua sendo usado após o acerto.
- [x] Os 10 objetos S3 são separados entre `prompt-01.mp3`…`prompt-10.mp3` e `frase-01.mp3`…`frase-10.mp3`.
- [x] Configuração, consumidores e validações diretas permanecem compatíveis.

## Dependências

- Task 432 — done
- Task 541 — done
- Task 688 — done
- Task 721 — done

## Resultado da execucao

- Adicionado `promptAudioUrl` por rodada para o áudio-pergunta de entrada.
- Web e mobile reproduzem `promptAudioUrl` quando a rodada aparece ou muda.
- `audioUrl` continua sendo usado após o acerto para reproduzir a frase completa.
- Os áudios completos antigos foram restaurados em `dev/games/complete_a_frase/audio/frase-01.mp3` a `frase-10.mp3`.
- Os novos áudios de perguntas foram publicados em `dev/games/complete_a_frase/audio/prompt-01.mp3` a `prompt-10.mp3`.
- O banco foi atualizado com os dois URLs em todas as 10 rodadas.

## Contexto utilizado

- Task 721 e handoff anterior para preservar o mapeamento dos 10 áudios.
- Tipos e validador de `sentence-fill` no backend, web e mobile.
- `SentenceFillPreviewModal` e `SentenceFillGameRenderer` para separar entrada e acerto.
- Pastas `audio_atividades` (frases completas) e `audio_atividades2` (perguntas).

## Handoff

- Task concluída. A entrada de cada cena usa `promptAudioUrl`; o acerto usa `audioUrl`.
- Próximo passo opcional: validar manualmente uma rodada no web e outra no mobile, confirmando a sequência de dois áudios.

## Arquivos alterados

- `backend/scripts/upload-sentence-fill-phrase-audios.mjs`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/sentence-fill-game-assets.ts`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/SentenceFillPreviewModal.tsx`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/components/SentenceFillGameRenderer/index.tsx`
- `tasks/change-requests/722-reproduzir-audio-ao-entrar-na-frase.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-722.md`

## Validacoes executadas

- `npm run upload:sentence-fill-phrase-audios` — concluído; 20 objetos publicados/atualizados e banco atualizado.
- Consulta direta ao banco — confirmou `audioUrl` e `promptAudioUrl` nas rodadas 1 a 10.
- `node --check scripts/upload-sentence-fill-phrase-audios.mjs` — concluído sem erros.
- Busca de código — confirmou que web/mobile usam o novo `promptAudioUrl` na entrada e `audioUrl` no acerto.
- Builds/typecheck de front-end, mobile e backend iniciados em paralelo, mas interrompidos após mais de um minuto sem progresso nem saída de erro.

## Pendencias pos-task

- Validação manual opcional da sequência de reprodução em web e mobile.
- Reexecutar builds isoladamente se for necessário um resultado de compilação; a execução paralela ficou sem progresso.

## Status final

done
