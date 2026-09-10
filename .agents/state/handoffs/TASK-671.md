# TASK-671

- Slice: `048-narracao-intro-conclusao-jogos`
- Status final: done
- Script ampliado para publicar os 30 áudios de figuras e vincular `audioUrl` por item no catálogo.
- Arquivos: `backend/scripts/upload-game-session-audios.mjs`.
- Validação: `node --check` passou.
- Pendência: executar `npm run upload:game-session-audios` em ambiente com credenciais S3 e banco configurados.
