# Handoff — Task 434

## Identificador

- Task: 434 — Jogo das Emoções: catálogo, prévia e runtime
- Slice: `tasks/slices/044-jogo-das-emocoes.md`
- Status final: done

## Decisões preservadas

- `gameType: emotions`, categoria `emocoes` (Socioemocionais)
- Sem mapa e sem conquistas
- Pool de `stages` (identify / situation / coping); `roundsPerRun: 8` sorteados a cada entrada
- MVP visual com emoji (`sceneEmoji` / opções); capas S3 opcionais

## Contexto usado

- print `design-system/front/prints/jogo-das-emocoes-socioemocionais.png`
- padrão sentence-fill / word-spell (shuffle + vitória)
- openapi + bootstrap catalog

## Arquivos principais

- `contracts/openapi.yaml`
- `backend/.../emotions-game-assets.ts` + bootstrap + validate
- `front-end/.../EmotionsPreviewModal.tsx` + `emotionsGame.ts`
- `mobile/.../EmotionsGameRenderer/`

## Validações

- `contents-catalog-bootstrap.service.spec.ts` — PASS (14 jogos)

## Pendências

- Upload de capas ilustradas no S3 quando houver arte
- Trocar emojis por ilustrações do print quando disponíveis

## Próximo contexto

- Se for arte: `STORAGE_BUCKET_MAP.md` §16 + pasta `jogo_das_emocoes/`
- Não recarregar slices de outros jogos
