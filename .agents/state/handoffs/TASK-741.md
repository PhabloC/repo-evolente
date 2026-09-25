# Handoff Task 741

- Slice: `tasks/slices/060-one-signal-push-mobile.md`
- Status final: `done`
- Decisão: substituir referências antigas de `logo-seal.png`/`logo-seal.webp` por `logo-seal-original.webp` na configuração Expo e nos componentes que carregam a logo; remover `NOTIFICATION_IMAGE_URL`, pois o push não envia mais mídia.
- Validações: configuração Expo carregada com sucesso e `git diff --check` passou.
- Pendência: confirmar a renderização no próximo build nativo.
