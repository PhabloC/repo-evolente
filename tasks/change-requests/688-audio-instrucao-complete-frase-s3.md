# Task 688 - Áudio da instrução Complete a frase no S3

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Contrato

- Não aplicável; alteração de asset e configuração persistida do jogo.

## Modo de execução

cross-stack

## Slice vertical

- `tasks/slices/042-complete-a-frase.md`

## Objetivo

Usar o áudio gravado `mulher-2026-09-11-10-54-[excited]Toque-na-palavra-que-complete-a-frase.mp3` como fala da instrução “Toque na palavra que completa a frase” na atividade Complete a frase.

## Entrega verificável

- áudio publicado em `games/complete_a_frase/audio/intro.mp3` no S3;
- configuração do conteúdo `sentence-fill` apontando para o áudio publicado;
- prévia web e runtime mobile reproduzindo a instrução gravada.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/042-complete-a-frase.md`
- `tasks/change-requests/432-complete-a-frase-catalogo-runtime.md`
- `tasks/change-requests/541-complete-frase-previa-web-audio-gravado.md`

## Contexto sob demanda

- `backend/scripts/upload-game-session-audios.mjs`: upload do intro e vínculo no banco;
- `front-end/src/pages/Main/Library/SentenceFillPreviewModal.tsx`: validação da prévia;
- `mobile/src/features/games/components/GameSessionAudio/`: validação do runtime.

## Orçamento de contexto

- 8 fontes; carregar somente os caminhos acima e os arquivos necessários para validação.

## Dependências

- Task 432 — done
- Task 541 — done

## Status final

done

## Resultado da execucao

- O áudio gravado foi publicado em `dev/games/complete_a_frase/audio/intro.mp3`.
- O conteúdo `Complete a frase` foi atualizado com `introAudioUrl` e os demais vínculos de áudio preservados pelo script.
- A prévia web e o runtime mobile já consomem `introAudioUrl` no fluxo existente.

## Contexto utilizado

- Task 432 e Task 541 para confirmar o contrato existente de áudio e a integração da prévia.
- `backend/scripts/upload-game-session-audios.mjs` para upload e persistência.
- Implementações web/mobile que consomem `introAudioUrl`.

## Handoff

- Task concluída; o próximo agente pode validar visualmente a reprodução da introdução em web e mobile, se necessário.

## Arquivos alterados

- `backend/scripts/upload-game-session-audios.mjs`
- `tasks/000-index.md`
- `tasks/change-requests/688-audio-instrucao-complete-frase-s3.md`
- `.agents/state/handoffs/TASK-688.md`

## Validacoes executadas

- `npm run upload:game-session-audios` — concluído; upload S3 e atualização do banco concluídos sem erros.
- Confirmação no log: `Complete a frase (...) with introAudioUrl`.

## Pendencias pos-task

- Nenhuma pendência técnica conhecida.
