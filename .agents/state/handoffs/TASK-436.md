# Handoff — Task 436

## Identificador

- Task: 436 — Fluência em Ação: catálogo, prévia e runtime
- Slice: `tasks/slices/045-fluencia-em-acao.md`
- Status final: done

## Decisões preservadas

- `gameType: fluency`, categoria `fala` (Fluência)
- Sem menu / níveis / conquistas / microfone
- Só botão ouvir (TTS) + avançar
- Pool de 10 stages (`passage` | `rhythm`); `roundsPerRun: 10`
- Print: `design-system/front/prints/fluencia-em-acao.png`

## Contexto usado

- print fluência em ação
- padrão emotions (shuffle + vitória) + TTS word-spell
- openapi + bootstrap catalog

## Arquivos principais

- `contracts/openapi.yaml`
- `backend/.../fluency-game-assets.ts` + bootstrap + validate
- `front-end/.../FluencyPreviewModal.tsx` + `fluencyGame.ts`
- `mobile/.../FluencyGameRenderer/`

## Validações

- `contents-catalog-bootstrap.service.spec.ts` — PASS (15 jogos)
- backend `start:dev` — Nest started; fluency bootstrap

## Pendências

- Capas e ilustrações de cena no S3 (`fluencia_em_acao/`)
- Opcional: áudio gravado por etapa se `voiceMode: recorded`

## Próximo contexto

- Se for arte: `STORAGE_BUCKET_MAP.md` §17 + pasta `fluencia_em_acao/`
- Não recarregar slices de outros jogos
