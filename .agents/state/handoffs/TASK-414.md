# Handoff — Task 414

## Identificador

- task: 414
- slice: 035
- status final: done

## Decisões

- `gameType: spot-difference` com 5 rodadas (`rounds[]`)
- Cada rodada: `imageAUrl` + `imageBUrl` + `differences[]` (hotspots normalizados 0–1) + `exercise`
- Erros clicáveis na prévia web e no mobile; após achar todos → exercício com repetições → próxima rodada
- Categoria catálogo: `articulatorio`
- Bootstrap sempre regenera `rounds` a partir dos assets padrão (hotspots atualizáveis)

## Arquivos

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/scripts/upload-spot-difference-assets.mjs`
- `front-end/.../SpotDifferencePreviewModal.tsx` + CSS
- `mobile/.../SpotDifferenceGameRenderer/`
- `jogo_dos_erros/` (capa + 5 pares A/B)

## Validacoes

- Upload S3: 12 assets
- Bootstrap specs atualizados (catálogo length 6)

## Próxima ação

Reiniciar backend para criar/atualizar “Jogo dos erros”. QA visual dos hotspots; recalibrar `x/y/radius` se necessário.
