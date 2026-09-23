## Status

done

# Task 721 - Subir áudios das cenas do Complete a frase

- **Tipo**: shared
- **Stacks envolvidos**: backend, front-end, mobile
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; upload de assets e atualização da configuração persistida do conteúdo.
- **Modo de execução**: cross-stack
- **Slice vertical**: `tasks/slices/042-complete-a-frase.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task.
- **Contexto sob demanda**: `backend/scripts/upload-sentence-fill-phrase-audios.mjs`, `backend/src/modules/contents/sentence-fill-game-assets.ts`, `front-end/src/pages/Main/Library/SentenceFillPreviewModal.tsx`, `mobile/src/features/games/components/SentenceFillGameRenderer/`, e os arquivos de `audios-atividades/Jogo_complete_frase/audio_atividades2/`.
- **Orçamento de contexto**: até 8 fontes; limitar a execução ao upload, vínculo das URLs por rodada e validação dos consumidores existentes.

## Objetivo

Publicar no S3 os 10 áudios gravados da pasta `audio_atividades2` e vinculá-los às respectivas cenas/rodadas do jogo **Complete a frase**.

## Critérios de aceite

- [x] Os 10 arquivos MP3 são publicados em `games/complete_a_frase/audio/frase-01.mp3` até `frase-10.mp3`.
- [x] Cada rodada do conteúdo `sentence-fill` possui `audioUrl` apontando para seu áudio correspondente.
- [x] O conteúdo usa `voiceMode: recorded`.
- [x] O script reconhece os títulos dos novos arquivos e mantém compatibilidade com os nomes antigos conhecidos.
- [x] Validações diretas do upload e dos consumidores web/mobile foram executadas; há falhas preexistentes registradas abaixo nos checks amplos do backend.

## Dependências

- Task 432 — done
- Task 541 — done
- Task 688 — done

## Resultado da execucao

- Os 10 arquivos de `audio_atividades2` foram publicados em `dev/games/complete_a_frase/audio/frase-01.mp3` até `frase-10.mp3`.
- O conteúdo `Complete a frase` (`906ebcf0-5b13-46e8-85cf-70b84349281c`) foi atualizado com `voiceMode: recorded` e `audioUrl` nas 10 rodadas.
- O web e o mobile já utilizavam `round.audioUrl` ao concluir corretamente cada cena; nenhuma alteração nesses consumidores foi necessária.
- O matcher do script passou a normalizar maiúsculas e acentos para reconhecer títulos como `O-que-está-no-barco` e `Quem-láte-no-quintal`.

## Contexto utilizado

- `backend/scripts/upload-sentence-fill-phrase-audios.mjs` para upload e persistência dos vínculos.
- `backend/src/modules/contents/sentence-fill-game-assets.ts` e Slice 042 para confirmar a ordem das 10 rodadas.
- `front-end/src/pages/Main/Library/SentenceFillPreviewModal.tsx` para confirmar reprodução do áudio gravado na prévia.
- `mobile/src/features/games/components/SentenceFillGameRenderer/index.tsx` e `mobile/src/features/games/utils/sentenceFillGame.ts` para confirmar reprodução por rodada.
- Os 10 arquivos MP3 em `audios-atividades/Jogo_complete_frase/audio_atividades2/`.

## Handoff

- Task concluída. Os áudios estão publicados no ambiente `dev` e vinculados ao conteúdo persistido.
- Para uma validação manual futura, abrir a atividade no web e no mobile, acertar uma rodada e confirmar a reprodução do MP3 correspondente.

## Arquivos alterados

- `backend/scripts/upload-sentence-fill-phrase-audios.mjs`
- `tasks/change-requests/721-upload-audios-complete-frase-cenas.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-721.md`

## Validacoes executadas

- `npm run upload:sentence-fill-phrase-audios` — concluído; 10 uploads S3 e atualização das 10 rodadas no banco.
- Consulta direta ao banco — confirmou `round_1` a `round_10` com URLs `frase-01.mp3` a `frase-10.mp3`.
- Busca nos consumidores web/mobile — confirmou uso de `round.audioUrl` no acerto.
- `node --check backend/scripts/upload-sentence-fill-phrase-audios.mjs` — concluído sem erros.
- `npm test -- --runInBand src/modules/contents/contents-catalog-bootstrap.service.spec.ts` — falhou em 2 expectativas preexistentes não relacionadas à alteração: `voiceMode` da Fluência e preservação de rodadas do Jogo dos Erros.
- `npm run typecheck` — falhou em erros preexistentes de tipagem em specs de vários módulos, incluindo o spec de bootstrap do catálogo.

## Pendencias pos-task

- Corrigir as falhas preexistentes dos testes de bootstrap e do `typecheck` do backend em task separada.
- Executar validação manual de reprodução em web e mobile, se necessário.

## Status final

done
