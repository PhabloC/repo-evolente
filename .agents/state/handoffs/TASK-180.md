# Handoff - Task 180

## Task

- identificador: 180
- título: Capa do jogo Escreva a letra no bucket
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 030 - Escrita guiada de letras
- objetivo de negócio: card do Escreva a letra com capa real
- entrega verificável: `coverUrl` apontando para `games/escreva_letra/capa_escreva_letra.webp`

## Decisões preservadas

- decisão: key estável `{prefix}/games/escreva_letra/capa_escreva_letra.webp`
- motivo: caminho pedido pelo solicitante a partir do asset local
- impacto: bootstrap anexa a URL pública no `gameConfig.coverUrl`; biblioteca já consome via `getLibraryGameCoverUrl`

## Contexto utilizado

### Contexto mínimo lido

- `tasks/change-requests/180-capa-jogo-escreva-a-letra-no-bucket.md`
- `games/escreva_letra/capa_escreva_letra.webp`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| bootstrap/assets | coverUrl | implementação |
| upload script | bucket | publish |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| letterImages da escrita | fora do pedido |

## Resultado por stack

- backend: upload + bootstrap cover
- front-end: já usa coverUrl no card (sem mudança de UI)
- mobile: demo trail atualizado com coverUrl

## Arquivos alterados

- `backend/src/modules/contents/alphabet-game-assets.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/scripts/upload-escreva-letra-cover.mjs`
- `backend/package.json`
- `contracts/openapi.yaml`
- `STORAGE_BUCKET_MAP.md`
- `mobile/src/features/trail/services/trailService.ts`
- tasks/index/slice/handoff

## Validações executadas

- upload ok → `https://storage.fasters.com.br/evolente/dev/games/escreva_letra/capa_escreva_letra.webp`
- bootstrap specs ok

## Pendências ou bloqueios

- se o card não atualizar, reiniciar o backend para o bootstrap anexar a capa no registro existente

## Próxima ação sugerida

- conferir o card Escreva a letra na biblioteca após reload do backend

## Próximo contexto recomendado

- `front-end/src/pages/Main/Library/libraryGames.ts`

## Contexto que não deve ser carregado na próxima etapa

- fonte: upload de letterImages da escrita
- motivo: não solicitado
