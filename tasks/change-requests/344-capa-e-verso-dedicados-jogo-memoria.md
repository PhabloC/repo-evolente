# Task 344 - Capa e verso dedicados no jogo da memória

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

- `contracts/openapi.yaml#/components/schemas/MemoryGameConfig`
- `contracts/openapi.yaml#/paths/~1contents`
- `contracts/openapi.yaml#/paths/~1trails~1my`

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

## Contexto de negocio

### Por que

O slice 032 já publicou as cartas do jogo da memória, mas a capa do jogo e o verso das cartinhas agora precisam usar arquivos dedicados enviados pelo usuário.

### O que

Subir `jogo_memoria/capa_jogo_memoria.webp` e `jogo_memoria/capinha_jogo.webp` para o bucket, ligar a capa ao `coverUrl` do jogo e usar o verso real nas cartas escondidas da prévia web e do mobile.

### Comportamento esperado

- capa do jogo publicada sob key estável em `games/memoria/`
- verso das cartinhas publicado sob key estável em `games/memoria/`
- `gameConfig.coverUrl` do conteúdo `memory` usa a capa dedicada
- `gameConfig.cardBackUrl` expõe o verso dedicado
- cartas escondidas mostram a capinha real na web e no mobile

### Fora de escopo

- troca do layout do jogo
- editor manual de capa/verso pela biblioteca
- novas categorias ou novas cartas

## Dependencias

- Task 343

## Slice vertical

### Identificador do slice

Slice 032 - Jogo da memória educativo

### Arquivo do slice

- `tasks/slices/032-jogo-memoria.md`

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/032-jogo-memoria.md`
- `.agents/state/handoffs/TASK-343.md`

## Contexto sob demanda

| Gatilho | Fonte | Por que |
| --- | --- | --- |
| assets raiz do jogo | `jogo_memoria/` | confirmar capa e verso dedicados |
| bootstrap e upload | `backend/src/modules/contents/`, `backend/scripts/upload-memory-game-assets.mjs` | publicar URLs públicas e atualizar `gameConfig` |
| contrato do jogo | `contracts/openapi.yaml` | expor `cardBackUrl` entre stacks |
| prévia web | `front-end/src/pages/Main/Library/` | mostrar a capa e o verso reais |
| renderer mobile | `mobile/src/features/games/` | mostrar o verso real no app |
| bucket map | `STORAGE_BUCKET_MAP.md` | documentar as novas keys estáveis |

## Orçamento de contexto

- risco: baixo
- estrategia de reducao: limitar a mudança ao `gameType` `memory`, sem reabrir o restante do catálogo de jogos

## Criterios de aceite

- [x] `capa_jogo_memoria.webp` e `capinha_jogo.webp` publicados no bucket sob prefixo estável
- [x] `gameConfig.coverUrl` do jogo da memória aponta para a capa dedicada
- [x] `gameConfig.cardBackUrl` existe no contrato, backend, web e mobile
- [x] cartas escondidas usam a capinha real na prévia web e no mobile
- [x] testes essenciais atualizados nas stacks tocadas

## Resultado da execucao

- **backend**: bootstrap do `memory` passou a resolver capa e verso dedicados em `games/memoria/`, com validação do novo campo `cardBackUrl`.
- **storage**: o script de upload do jogo da memória passou a incluir também os arquivos raiz `capa_jogo_memoria.webp` e `capinha_jogo.webp`.
- **front-end/mobile**: as cartas escondidas deixaram de usar `?` quando `cardBackUrl` estiver presente e a prévia web passou a exibir a capa dedicada do jogo.

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/slices/032-jogo-memoria.md`
- `.agents/state/handoffs/TASK-343.md`
- `jogo_memoria/`
- `backend/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `backend/src/modules/contents/`
- `backend/scripts/upload-memory-game-assets.mjs`
- `front-end/src/pages/Main/Library/`
- `mobile/src/features/games/`
- `contracts/openapi.yaml`
- `STORAGE_BUCKET_MAP.md`

## Handoff

- `.agents/state/handoffs/TASK-344.md`

## Arquivos alterados

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/memory-game-assets.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `backend/scripts/upload-memory-game-assets.mjs`
- `contracts/openapi.yaml`
- `STORAGE_BUCKET_MAP.md`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/memoryGame.ts`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/memoryGame.ts`
- `mobile/src/features/games/utils/memoryGame.test.ts`
- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/index.test.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/styles.ts`
- `tasks/slices/032-jogo-memoria.md`
- `tasks/change-requests/344-capa-e-verso-dedicados-jogo-memoria.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-344.md`

## Validacoes executadas

- `cd backend && npm run test -- contents-catalog-bootstrap.service.spec.ts contents.service.spec.ts`
- `cd backend && node --check scripts/upload-memory-game-assets.mjs`
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx`
- `cd mobile && npm test -- --runInBand src/features/games/utils/memoryGame.test.ts src/features/games/components/MemoryGameRenderer/index.test.tsx`
- `cd backend && npm run upload:memory-assets`

## Pendencias pos-task

- reiniciar o backend da instância em execução se o bootstrap ainda não tiver sido reprocessado após esta mudança

## Status final

done
