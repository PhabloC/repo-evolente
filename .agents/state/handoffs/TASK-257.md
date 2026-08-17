# Handoff - Task 257

## Task

- identificador: 257
- título: Hardening de assets e bootstrap do caça-palavras no backend
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 031
- objetivo de negócio: manter o caça-palavras bootstrapado com palavras suficientes no nível difícil e com a capa publicável pelo caminho correto

## Decisões preservadas

- O nível difícil do caça-palavras permanece com `wordCount=12`
- O catálogo padrão foi expandido para garantir ao menos 12 palavras únicas por categoria
- A validação do backend agora bloqueia qualquer config cujo `wordCount` exceda a menor categoria
- O script de upload da capa usa `backend/assets/games/caca_palavras/capa_caca_palavra.webp`

## Contexto efetivamente usado

- task 257, índice, slice 031
- handoff `TASK-249`
- `word-search-game-assets`, `contents.service`, spec do bootstrap e script de upload da capa

## Arquivos alterados

- `backend/src/modules/contents/word-search-game-assets.ts`
- `backend/src/modules/contents/word-search-game-assets.spec.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/scripts/upload-caca-palavras-cover.mjs`
- `backend/package.json`

## Validacoes executadas

- specs focados de `contents` — ok
- lint focado nos arquivos TS alterados — ok
- `node --check` no script — ok
- asset da capa existe no caminho esperado — ok

## Pendencias ou bloqueios

- Falta apenas executar o upload real da capa quando houver necessidade operacional
- `typecheck` global do backend continua com falhas antigas fora do escopo

## Próximo contexto recomendado

- `backend/scripts/upload-caca-palavras-cover.mjs`
- `backend/src/modules/contents/word-search-game-assets.ts`
- `tasks/slices/031-jogo-caca-palavras.md`
