# Task 257 - Hardening de assets e bootstrap do caça-palavras no backend

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/031-jogo-caca-palavras.md`

## Dependencias

- Task 249
- Task 250
- Task 251

## Objetivo

Corrigir inconsistências do catálogo de palavras e do script de upload da capa do caça-palavras para que o jogo difícil use quantidade válida de palavras e o asset da capa seja publicado pelo caminho correto.

## Entrega verificavel

- Cada categoria do caça-palavras suporta a quantidade exigida pelo nível difícil ou o bootstrap valida/reduz `wordCount` com segurança
- O script `upload-caca-palavras-cover` lê o asset real a partir de `backend/assets/games/caca_palavras`
- `package.json` expõe comando de upload da capa do caça-palavras
- Testes cobrindo coerência entre categorias e dificuldades do caça-palavras

## Fora de escopo

- Ajustes na prévia web do caça-palavras
- Mudanças no runtime mobile
- Novas categorias além do necessário para corrigir o catálogo atual

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/031-jogo-caca-palavras.md`
- `.agents/state/handoffs/TASK-249.md`

## Contexto sob demanda

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `backend/src/modules/contents/word-search-game-assets.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/scripts/upload-caca-palavras-cover.mjs`
- `backend/package.json`

## Orcamento de contexto

baixo

## Estrategia de reducao

Restringir a mudança ao backend do caça-palavras e ao script de publicação da capa, sem reabrir front-end, mobile ou contrato.

## Referencia visual

- nao se aplica

## Resultado da execucao

- As categorias `cores`, `casa` e `escola` passaram a ter 12 palavras únicas, compatíveis com o nível difícil
- `contents.service` agora rejeita configs de caça-palavras cujo `wordCount` exceda a menor categoria disponível
- O script `upload-caca-palavras-cover.mjs` passou a ler a capa real em `backend/assets/games/caca_palavras`
- `backend/package.json` ganhou o comando `upload:caca-palavras-cover`
- Foram adicionados testes para garantir que o catálogo padrão suporta o nível difícil e que o bootstrap continua publicando o jogo corretamente

## Contexto utilizado

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `backend/src/modules/contents/word-search-game-assets.ts`
- `backend/src/modules/contents/word-search-game-assets.spec.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/scripts/upload-caca-palavras-cover.mjs`
- `backend/package.json`
- `.agents/state/handoffs/TASK-249.md`

## Handoff

- `.agents/state/handoffs/TASK-257.md`

## Arquivos alterados

- `backend/src/modules/contents/word-search-game-assets.ts`
- `backend/src/modules/contents/word-search-game-assets.spec.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/scripts/upload-caca-palavras-cover.mjs`
- `backend/package.json`

## Validacoes executadas

- `cd backend && npm run test -- contents-catalog-bootstrap.service.spec.ts word-search-game-assets.spec.ts` — ok
- `cd backend && npx eslint src/modules/contents/word-search-game-assets.ts src/modules/contents/word-search-game-assets.spec.ts src/modules/contents/contents.service.ts src/modules/contents/contents-catalog-bootstrap.service.spec.ts` — ok
- `cd backend && node --check scripts/upload-caca-palavras-cover.mjs` — ok
- `Test-Path backend/assets/games/caca_palavras/capa_caca_palavra.webp` — `True`

## Pendencias pos-task

- Rodar `npm run upload:caca-palavras-cover` em ambiente com credenciais reais quando quiser republicar a capa
- `typecheck` global do backend continua com falhas pré-existentes fora do escopo desta task

## Status final

done
