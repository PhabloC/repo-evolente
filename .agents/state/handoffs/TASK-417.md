# Handoff — Task 417

## Identificador

- task: 417
- slice: 038
- status final: done

## Decisões

- `gameType: jigsaw`, categoria `memoria`
- 5 rodadas 3×3; `preFilledPieceIds` no tabuleiro; demais no banco
- Web: HTML5 drag-and-drop + toque peça→slot
- Mobile: toque peça→slot (mesmo fluxo terapêutico)
- Capas: `capa_quebra_cabeca.webp` (card) e `capa-modal-quebra-cabeca.webp` (modal)
- Assets: `games/quebra_cabeca/rounds/round_{n}/piece_{row}_{col}.webp`

## Validacoes

- Upload S3: 52 assets
- Bootstrap specs pass (catálogo length 9)

## Próxima ação

Reiniciar backend se o hot-reload não criou o conteúdo; abrir na aba Cognição e validar a prévia.
