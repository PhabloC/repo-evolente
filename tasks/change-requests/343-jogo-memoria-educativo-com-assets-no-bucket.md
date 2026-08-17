# Task 343 - Jogo da memória educativo com assets no bucket

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

- `contracts/openapi.yaml#/components/schemas`
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

### Regra de aderencia visual

- O jogo deve priorizar leitura infantil, peças grandes e fluxo simples para uso individual, sem introduzir pressão competitiva.

## Contexto de negocio

### Por que

O produto já possui runtime extensível para jogos terapêuticos e agora precisa de um jogo da memória educativo infantil usando as imagens reais já organizadas por categoria em `jogo_memoria/`.

### O que

Subir as imagens de `jogo_memoria/` para o bucket e criar o jogo da memória com categorias ilustradas para uso no catálogo, na prévia web e na execução mobile.

### Comportamento esperado

- imagens das categorias `animais`, `cores`, `frutas` e `objetos` publicadas no bucket
- novo conteúdo `memory` criado/atualizado por bootstrap no catálogo
- `gameConfig` expõe capa, categorias e cartas com URLs públicas
- prévia web permite escolher categoria e jogar sozinho
- app mobile permite escolher categoria e jogar sozinho com feedback infantil de acerto

### Fora de escopo

- upload manual de cartas pela biblioteca
- criação de novas categorias via UI
- trilhas com parametrização de tamanho de tabuleiro por profissional

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: mesmas do catálogo atual de jogos; sem papéis novos
- Casos de erro: bucket sem URL pública; categoria sem cartas suficientes; assets faltantes
- Decisoes humanas: jogo individual; foco infantil educativo; uso das imagens já presentes em `jogo_memoria/`
- Casos de borda: rebootstrap idempotente; fallback quando parte dos assets ainda não existir no bucket

## Especificacao tecnica

### Deve

- adicionar `memory` como novo `gameType`
- definir schema/config do jogo com capa, categorias e cartas ilustradas
- criar script de upload dos assets locais para o bucket configurado
- publicar e consumir URLs públicas no bootstrap, web e mobile
- manter compatibilidade com os jogos existentes

### Nao deve

- nao quebrar `alphabet`, `alphabet-writing` ou `word-search`
- nao exigir upload manual via UI para o jogo funcionar
- nao depender de assets locais em tempo de execução

## Entradas

- `jogo_memoria/`
- `STORAGE_BUCKET_MAP.md`
- `contracts/openapi.yaml`
- `backend/.env.local`
- docs locais das stacks envolvidas sob demanda

## Dependencias

- Task 156
- Task 157
- Task 163
- Task 168
- Task 255
- Task 257

## Slice vertical

### Identificador do slice

Slice 032 - Jogo da memória educativo

### Arquivo do slice

- `tasks/slices/032-jogo-memoria.md`

### Objetivo de negócio

Entregar um novo jogo terapêutico infantil baseado em memória visual, com assets reais no bucket e execução individual no app.

### Entrega verificável do slice

Conteúdo `memory` disponível no catálogo com assets públicos, prévia jogável web e renderer mobile funcional.

### Fora do slice

- criação/edição editorial das cartas pela biblioteca
- ranking ou multiplayer

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/032-jogo-memoria.md`

## Contexto sob demanda

| Gatilho | Fonte | Por que |
| --- | --- | --- |
| mapa do bucket | `STORAGE_BUCKET_MAP.md` | padronizar as keys públicas |
| contrato do jogo | `contracts/openapi.yaml` | tipar `gameType` e `gameConfig` |
| bootstrap e validação | `backend/src/modules/contents/` | criar o conteúdo e validar schema |
| assets locais | `jogo_memoria/` | origem real das imagens por categoria |
| biblioteca e prévia | `front-end/src/pages/Main/Library/` | exibir card, capa e prévia jogável |
| runtime mobile | `mobile/src/features/games/` | executar o jogo individual no app |
| regras locais | `front-end/docs/ai/`, `mobile/docs/ai/`, `backend/docs/ai/` | alinhar arquitetura e qualidade por stack |

## Orçamento de contexto

- risco: medio
- estrategia de reducao: limitar a mudança ao novo `gameType` `memory`, reusar padrões de bootstrap e preview já existentes e evitar reabrir fluxos da biblioteca fora do jogo

## Criterios de aceite

- [x] assets de `jogo_memoria/` publicados no bucket sob prefixo estável
- [x] conteúdo `memory` existe no catálogo com `coverUrl` e categorias com cartas ilustradas
- [x] biblioteca web mostra o novo jogo e abre prévia jogável individual
- [x] mobile renderiza o jogo da memória com seleção de categoria e fluxo individual
- [x] testes essenciais atualizados nas stacks tocadas

## Resultado da execucao

- **backend**: novo `gameType` `memory`, schema validado em `contents.service`, bootstrap idempotente no catálogo e script `upload-memory-game-assets` criado para publicar as imagens reais por categoria.
- **front-end**: biblioteca web reconhece o jogo da memória, agrupa em `Memória e associação`, exibe capa a partir dos assets do bucket e abre prévia jogável individual com escolha de categoria e pares ilustrados.
- **mobile**: runtime extensível ganhou `MemoryGameRenderer`, utilitários dedicados e fluxo individual infantil com categoria, cartas embaralhadas e feedback textual.
- **storage**: upload real concluído em **quarta-feira, 29 de julho de 2026**, com 66 imagens publicadas sob `dev/games/memoria/{categoria}/{arquivo}.webp`.

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/slices/032-jogo-memoria.md`
- `STORAGE_BUCKET_MAP.md`
- `contracts/openapi.yaml`
- `jogo_memoria/`
- `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ARCHITECTURE.md`, `front-end/docs/ai/ACCESSIBILITY.md`
- `mobile/docs/ai/ARCHITECTURE.md`, `mobile/docs/ai/CODE_STYLE.md`
- `backend/src/modules/contents/`
- `front-end/src/pages/Main/Library/`
- `mobile/src/features/games/`

## Handoff

- `.agents/state/handoffs/TASK-343.md`

## Arquivos alterados

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/memory-game-assets.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `backend/scripts/upload-memory-game-assets.mjs`
- `backend/package.json`
- `contracts/openapi.yaml`
- `STORAGE_BUCKET_MAP.md`
- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/utils/contentGames.ts`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/memoryGame.ts`
- `front-end/src/pages/Main/Library/memoryGameDefaults.ts`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `mobile/src/features/games/utils/gameMetadata.ts`
- `mobile/src/features/games/utils/memoryGame.ts`
- `mobile/src/features/games/utils/memoryGame.test.ts`
- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/index.test.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/styles.ts`
- `tasks/slices/032-jogo-memoria.md`
- `tasks/change-requests/343-jogo-memoria-educativo-com-assets-no-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-343.md`

## Validacoes executadas

- `cd backend && npm run test -- contents-catalog-bootstrap.service.spec.ts contents.service.spec.ts` — ok em **quarta-feira, 29 de julho de 2026**
- `cd backend && npx eslint src/modules/contents/entities/content.entity.ts src/modules/contents/memory-game-assets.ts src/modules/contents/contents-catalog-bootstrap.service.ts src/modules/contents/contents.service.ts src/modules/contents/contents.in-memory.repository.ts src/modules/contents/contents-catalog-bootstrap.service.spec.ts src/modules/contents/contents.service.spec.ts` — ok em **quarta-feira, 29 de julho de 2026**
- `cd backend && node --check scripts/upload-memory-game-assets.mjs` — ok em **quarta-feira, 29 de julho de 2026**
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok em **quarta-feira, 29 de julho de 2026**
- `cd mobile && npm test -- --runInBand src/features/games/utils/memoryGame.test.ts src/features/games/components/MemoryGameRenderer/index.test.tsx` — ok em **quarta-feira, 29 de julho de 2026**
- `cd backend && npm run upload:memory-assets` — ok em **quarta-feira, 29 de julho de 2026** com 66 uploads concluídos

## Pendencias pos-task

- Reiniciar o backend no ambiente que consome o banco atual para que o bootstrap materialize o conteúdo `memory` no catálogo se essa instância ainda não tiver reiniciado após a mudança.

## Status final

done
