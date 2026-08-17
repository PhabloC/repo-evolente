# Task 255 - Hardening do bootstrap do catálogo de jogos no backend

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

- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

## Dependencias

- Task 159
- Task 165
- Task 174
- Task 180

## Objetivo

Endurecer o bootstrap do catálogo de jogos para resolver URLs públicas de assets de forma consistente com o adapter de storage ativo e para impedir duplicação de jogos em inicializações concorrentes.

## Entrega verificavel

- Bootstrap resolve `coverUrl` e imagens do alfabeto mesmo quando `STORAGE_S3_PUBLIC_BASE_URL` estiver vazio
- Resolução de URL reaproveita o mesmo fallback público já adotado no storage S3-compativel
- O catálogo possui proteção contra duplicação de jogos por `gameType`
- A inicialização do bootstrap permanece idempotente em reinícios e cenários concorrentes
- Testes cobrindo fallback de URL e garantia de unicidade

## Fora de escopo

- Mudanças na UI da biblioteca
- Novos jogos além dos já existentes
- Mudanças no runtime mobile

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `.agents/state/handoffs/TASK-159.md`
- `.agents/state/handoffs/TASK-180.md`

## Contexto sob demanda

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/alphabet-game-assets.ts`
- `backend/src/modules/contents/contents.repository.ts`
- `backend/src/modules/contents/contents.typeorm.repository.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/database/migrations/**`

## Orcamento de contexto

medio

## Estrategia de reducao

Limitar a mudança ao módulo `contents`, ao bootstrap do catálogo e à persistência necessária para garantir unicidade por `gameType`, sem reabrir contrato, front-end ou mobile.

## Referencia visual

- nao se aplica

## Resultado da execucao

- O bootstrap de jogos passou a resolver a base pública dos assets com fallback consistente para S3 (`endpoint/bucket`) quando `STORAGE_S3_PUBLIC_BASE_URL` vier vazio
- O repositório de `contents` ganhou busca e upsert por `gameType`, reduzindo a janela de duplicação no bootstrap
- Foi adicionada migration com deduplicação prévia e índice único em `contents.game_type`
- Os specs do bootstrap cobrem o fallback de URL e a idempotência com os três jogos padrão

## Contexto utilizado

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/alphabet-game-assets.ts`
- `backend/src/modules/contents/contents.repository.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/src/modules/contents/contents.typeorm.repository.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/database/migrations/1820000000000-AddUniqueIndexToContentsGameType.ts`
- `.agents/state/handoffs/TASK-159.md`
- `.agents/state/handoffs/TASK-180.md`

## Handoff

- `.agents/state/handoffs/TASK-255.md`

## Arquivos alterados

- `backend/src/modules/contents/alphabet-game-assets.ts`
- `backend/src/modules/contents/contents.repository.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/src/modules/contents/contents.typeorm.repository.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/database/migrations/1820000000000-AddUniqueIndexToContentsGameType.ts`

## Validacoes executadas

- `cd backend && npm run test -- contents-catalog-bootstrap.service.spec.ts` — ok
- `cd backend && npx eslint src/modules/contents/alphabet-game-assets.ts src/modules/contents/contents.repository.ts src/modules/contents/contents.in-memory.repository.ts src/modules/contents/contents.typeorm.repository.ts src/modules/contents/entities/content.entity.ts src/modules/contents/contents-catalog-bootstrap.service.ts src/modules/contents/contents-catalog-bootstrap.service.spec.ts src/database/migrations/1820000000000-AddUniqueIndexToContentsGameType.ts` — ok
- `cd backend && npm run typecheck` — falhou por erros pré-existentes fora do escopo em `src/modules/admin/utils/admin-report-csv.spec.ts` e `test/app.e2e-spec.ts`

## Pendencias pos-task

- Rodar a nova migration em ambiente com banco real antes do próximo deploy
- Se houver dados duplicados de jogos em algum ambiente, validar o resultado da deduplicação preservando apenas um registro por `gameType`

## Status final

done
