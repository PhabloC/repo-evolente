# Handoff — Task 415

## Identificador

- task: 415
- slice: 036
- status final: done

## Decisões

- `gameType: whats-missing`, categoria `memoria` (Cognição)
- 5 rodadas com `items`, `missingItemId` e `options` clicáveis
- Setup com capa + Começar jogo (mesmo padrão dos outros jogos)
- Assets em `games/qual_esta_faltando/`

## Arquivos

- `whats-missing-game-assets.ts`, upload script
- `WhatsMissingPreviewModal.tsx` + CSS
- `WhatsMissingGameRenderer` (mobile)
- `jogo_qual_esta_faltando/`

## Validacoes

- Upload S3: 17 assets
- Bootstrap specs pass (catálogo length 7)
- Backend criou conteúdo no bootstrap

## Próxima ação

Abrir na biblioteca (aba Cognição) e validar prévia. Ajustar opções/rodadas se necessário.
