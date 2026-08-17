# Handoff - Task 157

## Task

- identificador: 157
- título: Biblioteca e planejamentos web para jogos terapeuticos
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 026 - Jogos terapeuticos
- objetivo de negócio: gestão e envio web do primeiro jogo terapêutico
- entrega verificável: biblioteca e planejamentos web suportam o jogo do alfabeto
- status do slice: in_progress

## Decisões preservadas

- decisão: manter o jogo dentro da biblioteca existente
- motivo: evitar fluxo administrativo paralelo
- impacto: master gerencia `game` no mesmo modal de conteúdo

- decisão: formulário do jogo usa campos textuais simples
- motivo: cabe no modal atual sem builder visual novo
- impacto: `letters`, `locale` e `voiceMode` são preenchidos no web e consumidos pelo app

- decisão: profissional continua read-only na biblioteca
- motivo: RBAC do catálogo não mudou
- impacto: envio ao paciente acontece apenas via `/planejamentos`

- decisão: planejamentos mostram labels de tipo e nome do jogo
- motivo: evitar ambiguidade entre áudio, vídeo e jogo
- impacto: o profissional já consegue montar trilha mista com o jogo do alfabeto

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/157-biblioteca-e-planejamentos-web-para-jogos-terapeuticos.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-156.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS desktop | UI | biblioteca/planejamentos/modais |
| openapi | API | `gameType` e `gameConfig` |
| front-end docs/ai | web | organização, typing e acessibilidade |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system mobile + docs mobile | Task web |

## Resultado por stack

- front-end: done

## Arquivos alterados

- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/types/trail.ts`
- `front-end/src/pages/Main/Library/**`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.test.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/test/setup.ts`
- task/slice/index/handoff

## Validações executadas

- front-end lint: ok
- front-end build: ok
- testes diretamente afetados (`Library` + `AddCatalogContentModal`): ok
- `npm run test` completo: falha pré-existente por timeout em `AdminUsers`

## Pendências ou bloqueios

- sem bloqueio para a Task 158
- suite completo do front-end ainda tem timeout em `AdminUsers`, fora deste escopo

## Próxima ação sugerida

- Executar `tasks/change-requests/158-execucao-mobile-do-jogo-alfabeto-falado.md`

## Próximo contexto recomendado

- Task 158
- `contracts/openapi.yaml` em `contents/trails`
- `mobile/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: áreas administrativas web
- motivo: próxima task é mobile e focada no renderer do jogo
