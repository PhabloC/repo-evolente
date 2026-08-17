# Task 475 - Quebra-cabeça: 10 níveis com dificuldade progressiva

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `JigsawRound` (campo `difficulty` opcional)

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/038-quebra-cabeca.md`

## Referencia visual

- print: `design-system/front/prints/quebra-cabeca-cognicao.png`
- governa: tabuleiro, banco de peças, fluxo de encaixe
- lacunas: badge de dificuldade e grades > 3×3 (inferir layout existente)

## Objetivo

Expandir o quebra-cabeça de 5 para 10 níveis com dificuldades fácil / médio / difícil e grade crescente (3×3 → 4×4 → 5×5).

## Comportamento esperado

- 4 níveis fáceis (3×3), 3 médios (4×4), 3 difíceis (5×5)
- Reusar as 5 cenas de arte existentes (`full.webp`) com grades diferentes
- Exibir dificuldade e progresso na prévia web e no runtime mobile
- Bootstrap refresca o catálogo para a nova estrutura

## Contexto mínimo

- AGENTS, GUIDE, context-map, 000-index, esta task, slice 038
- handoff TASK-417
- `jigsaw-game-assets.ts`

## Contexto sob demanda

- `contracts/openapi.yaml` (JigsawRound) — ao alterar schema
- front/mobile parsers e renderers jigsaw — ao expor difficulty e grade
- specs de bootstrap — ao validar 10 rounds

## Orçamento de contexto

- risco: medio — reuso de cenas + merge de bootstrap precisa forçar template
- estrategia: não gerar arte nova; peças usam `full.webp` com clip por grade

## Criterios de aceite

- [x] 10 rodadas no bootstrap (4 fácil 3×3, 3 médio 4×4, 3 difícil 5×5)
- [x] Campo `difficulty` nas rodadas (contrato + tipos)
- [x] UI web e mobile mostram dificuldade
- [x] Specs de bootstrap atualizados
- [x] Handoff gerado

## Resultado da execucao

Catálogo jigsaw expandido para 10 níveis progressivos; UI mostra nível + dificuldade + grade; bootstrap atualiza estrutura mesmo com conteúdo existente.

## Contexto utilizado

Task 475, slice 038, handoff 417, assets/openapi/parsers/renderers jigsaw.

## Handoff

- `.agents/state/handoffs/TASK-475.md`

## Arquivos alterados

- `backend/src/modules/contents/jigsaw-game-assets.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `contracts/openapi.yaml`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/jigsawGame.ts`
- `front-end/src/pages/Main/Library/JigsawPreviewModal.tsx`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/jigsawGame.ts`
- `mobile/src/features/games/components/JigsawGameRenderer/index.tsx`
- `tasks/slices/038-quebra-cabeca.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx jest --runInBand --testPathPatterns=contents-catalog-bootstrap.service.spec` — PASS

## Pendencias pos-task

- Reiniciar backend para aplicar refresh no banco local
- Smoke na prévia web (níveis médio/difícil)

## Status final

done
