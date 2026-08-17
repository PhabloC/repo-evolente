# Task 488 - Hardening do bootstrap e dos assets de jogos no backend

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem mudança de contrato; ajuste nos builders e scripts internos de catálogo

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/006-catalogo-conteudos-master.md`

## Objetivo

Preservar edições persistidas em configs de jogos durante o bootstrap e impedir uploads de assets com extensão/MIME divergentes do conteúdo real.

## Criterios de aceite

- [x] `fluency`, `dialogue`, `emotions` e `jigsaw` preservam conteúdo existente por ID e só adicionam entradas ausentes
- [x] scripts de upload de `fluency`, `dialogue` e `emotions` preservam extensão/MIME reais dos arquivos publicados
- [x] testes de regressão cobrem o merge dos builders
- [x] handoff gerado

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/change-requests/488-hardening-bootstrap-assets-jogos-backend.md`
- `.agents/state/handoffs/TASK-486.md`

## Contexto sob demanda

- `backend/AGENTS.md` e `backend/docs/ai/AGENTS.md`
- `backend/docs/ai/SECURITY.md` e `backend/docs/ai/QA.md`
- `backend/src/modules/contents/`
- `backend/scripts/upload-*.mjs`

## Orçamento de contexto

- 9 fontes
- estratégia: focar apenas nos builders de jogo e nos scripts citados pelo review

## Resultado da execucao

Os builders passaram a reutilizar as configurações persistidas como fonte principal, adicionando apenas estágios/rodadas ausentes, e os scripts de upload agora publicam as imagens com a extensão e o `Content-Type` corretos.

## Contexto utilizado

- slice 006
- handoff 486
- builders `fluency`, `dialogue`, `emotions`, `jigsaw`
- scripts de upload correspondentes

## Handoff

- `.agents/state/handoffs/TASK-488.md`

## Arquivos alterados

- `backend/src/modules/contents/fluency-game-assets.ts`
- `backend/src/modules/contents/dialogue-game-assets.ts`
- `backend/src/modules/contents/emotions-game-assets.ts`
- `backend/src/modules/contents/jigsaw-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `backend/scripts/upload-fluency-assets.mjs`
- `backend/scripts/upload-dialogue-assets.mjs`
- `backend/scripts/upload-emotions-assets.mjs`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- --runInBand src/modules/subscriptions/subscriptions.service.spec.ts src/modules/admin/admin.service.spec.ts src/modules/contents/catalog-config-merge.spec.ts src/modules/users/dto/update-own-profile.dto.spec.ts` — PASS
- `npx eslint src/modules/subscriptions/subscriptions.service.ts src/modules/subscriptions/subscriptions.service.spec.ts src/modules/users/dto/update-own-profile.dto.ts src/modules/users/dto/update-own-profile.dto.spec.ts src/modules/admin/admin.service.ts src/modules/admin/admin.service.spec.ts src/modules/contents/fluency-game-assets.ts src/modules/contents/dialogue-game-assets.ts src/modules/contents/emotions-game-assets.ts src/modules/contents/jigsaw-game-assets.ts src/modules/contents/catalog-config-merge.spec.ts` — PASS

## Pendencias pos-task

- os scripts seguem sem conversão para WebP; o hardening atual passa a respeitar o arquivo fonte escolhido

## Status final

done
