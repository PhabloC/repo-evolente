# Task 174 - Imagens do alfabeto falado no bucket

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/components/schemas/AlphabetGameConfig`

## Modo de execucao

cross-stack

## Referencia de design system

### Web

- stack de referencia visual: front-end
- tipo de referencia visual: artefato de design system
- fonte primaria visual: `design-system/front/Design_System_Evolente_Desktop.md`

### Mobile

- stack de referencia visual: mobile
- tipo de referencia visual: artefato de design system
- fonte primaria visual: `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- A capa deve identificar o card do jogo na biblioteca; as imagens por letra devem substituir o placeholder textual no runtime e na prévia, sem mudar o fluxo de toque/escuta.

## Contexto de negocio

### Por que

As artes do alfabeto falado já existem em `alfabero_falado/` na raiz e precisam viver no bucket para o card e o jogo usarem as imagens reais.

### O que

Enviar capa + letras A–Z para o bucket e ligar as URLs públicas ao jogo “Alfabeto falado” (catálogo, biblioteca web e execução mobile).

### Comportamento esperado

- `capa_jogo_alfabeto.webp` e `letra_*.webp` estão no bucket sob prefixo de ambiente
- o bootstrap do jogo publica `coverUrl` e `letterImages` no `gameConfig`
- o card da biblioteca usa a capa quando disponível
- o renderer mobile e a prévia web mostram a imagem de cada letra ao tocar/escutar

### Fora de escopo

- upload genérico de mídia para conteúdos `game` via `POST /contents/{id}/media`
- imagens no jogo de escrita guiada
- autenticação/autorização nova no storage
- remoção da pasta local `alfabero_falado/` do repositório

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: nao se aplica (assets públicos de catálogo; bootstrap/código)
- Casos de erro: URL ausente cai para placeholder textual; bootstrap idempotente
- Decisoes humanas: usar bucket S3 já configurado; paths estáveis sob `games/alphabet`
- Casos de borda: jogo já existente no banco recebe update das URLs sem duplicar conteúdo

## Especificacao tecnica

### Deve

- fazer upload das 27 imagens para `{prefix}/games/alphabet/...`
- estender `AlphabetGameConfig` com `coverUrl` e `letterImages` opcionais
- atualizar bootstrap, contrato, web e mobile
- atualizar `STORAGE_BUCKET_MAP.md`

### Nao deve

- nao abrir upload de mídia para `game` no endpoint de contents
- nao alterar o jogo de escrita
- nao quebrar TTS existente

## Entradas

- `alfabero_falado/`
- `STORAGE_BUCKET_MAP.md`
- `contracts/openapi.yaml`
- `backend/.env.local` (credenciais de storage já existentes)
- docs locais das stacks envolvidas sob demanda

## Dependencias

- Task 160
- Task 161
- Task 165
- Task 158
- Task 168

## Slice vertical

### Identificador do slice

Slice 026 - Jogos terapeuticos e alfabeto falado

### Arquivo do slice

- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

### Objetivo de negócio

Completar o alfabeto falado com artes de capa e por letra servidas pelo bucket.

### Entrega verificável do slice

Capa e letras do alfabeto falado disponíveis via URL pública e renderizadas na biblioteca e no jogo.

### Fora do slice

- outros jogos, áudio gravado, autoria por UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Contexto sob demanda

| Gatilho | Fonte | Por que |
| --- | --- | --- |
| paths do bucket | `STORAGE_BUCKET_MAP.md` | padronizar keys |
| schema do jogo | `contracts/openapi.yaml` AlphabetGameConfig | estender contrato |
| bootstrap | `backend/src/modules/contents/` | publicar URLs |
| card/preview | `front-end/src/pages/Main/Library/` | capa e letras |
| runtime | `mobile/src/features/games/` | imagens por letra |
| assets locais | `alfabero_falado/` | origem do upload |

## Orçamento de contexto

- risco: médio (cross-stack + storage)
- estrategia de reducao: não carregar writing game além do necessário para não quebrar; não reabrir slices de auth/pagamento

## Criterios de aceite

- [x] 27 arquivos no bucket sob `games/alphabet`
- [x] `gameConfig` do Alfabeto falado contém `coverUrl` e 26 `letterImages`
- [x] card da biblioteca mostra a capa
- [x] mobile e preview web mostram imagem da letra
- [x] testes essenciais das stacks atualizados

## Resultado da execucao

- Upload de 27 webps para `dev/games/alphabet/...` via `npm run upload:alphabet-assets`
- Contrato e tipagens com `coverUrl` + `letterImages`
- Bootstrap idempotente anexou as URLs ao jogo existente
- Biblioteca web usa capa no card; preview e mobile usam artes por letra

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `STORAGE_BUCKET_MAP.md`
- `contracts/openapi.yaml` (AlphabetGameConfig)
- `alfabero_falado/`
- módulos contents/games/library das stacks envolvidas

## Handoff

- `.agents/state/handoffs/TASK-174.md`

## Arquivos alterados

- `backend/scripts/upload-alphabet-game-assets.mjs`
- `backend/package.json`
- `backend/src/modules/contents/alphabet-game-assets.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `contracts/openapi.yaml`
- `STORAGE_BUCKET_MAP.md`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/features/games/utils/alphabetGame.ts`
- `mobile/src/features/games/utils/alphabetGame.test.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetGameRenderer/styles.ts`
- `tasks/change-requests/174-imagens-do-alfabeto-falado-no-bucket.md`
- `tasks/000-index.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-174.md`

## Validacoes executadas

- `npm run upload:alphabet-assets` (27 uploads OK)
- backend: bootstrap + contents.service specs OK
- mobile: AlphabetGameRenderer + alphabetGame utils OK
- front-end: Library/index.test OK
- log runtime: `Default alphabet game assets (cover + letter images) attached.`

## Pendencias pos-task

- Pasta local `alfabero_falado/` permanece na raiz (fonte de reupload); remoção é opcional e fora desta task
- Jogo de escrita ainda sem artes por letra

## Status final

done
