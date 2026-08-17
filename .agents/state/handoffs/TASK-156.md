# Handoff - Task 156

## Task

- identificador: 156
- título: API de jogos terapeuticos e conteudos jogaveis
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 026 - Jogos terapeuticos
- objetivo de negócio: modelagem backend e contrato para conteúdo jogável
- entrega verificável: API pronta para cadastrar e distribuir o jogo do alfabeto
- status do slice: in_progress

## Decisões preservadas

- decisão: estender `contents` em vez de criar módulo novo
- motivo: o jogo entra como item do catálogo existente
- impacto: `mediaType=game` convive com `audio` e `video`

- decisão: primeiro `gameType` suportado é `alphabet`
- motivo: recorte do slice é MVP do alfabeto falado
- impacto: app poderá escolher renderer específico sem engine genérica

- decisão: `gameConfig` mínimo contém `letters`, `locale` e `voiceMode`
- motivo: metadados suficientes para abrir o jogo no app sem inventar contrato novo
- impacto: Task 157 só precisa editar esse payload; Task 158 só precisa consumi-lo

- decisão: upload de mídia continua exclusivo para áudio/vídeo
- motivo: jogo interativo não usa `POST /contents/{id}/media` nesta fase
- impacto: backend rejeita upload para `mediaType=game`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/156-api-jogos-terapeuticos-e-conteudos-jogaveis.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-020.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002 | regras | validar atores e trilha |
| openapi | API | estender `contents` |
| backend docs/ai | implementação back | DTOs, service, migration |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system front/mobile | task sem UI |
| docs web/mobile | stack não envolvida |

## Resultado por stack

- backend: done

## Arquivos alterados

- `backend/src/modules/contents/**`
- `backend/src/modules/trails/trails.service.spec.ts`
- `backend/src/database/migrations/1780000000000-AddGameFieldsToContents.ts`
- `contracts/openapi.yaml`
- task/slice/index/handoff

## Validações executadas

- backend lint: ok
- backend test: ok (16 suites / 62 tests)

## Pendências ou bloqueios

- nenhuma bloqueante para a Task 157
- decisão de TTS/fallback gravado permanece para a execução mobile

## Próxima ação sugerida

- Executar `tasks/change-requests/157-biblioteca-e-planejamentos-web-para-jogos-terapeuticos.md`

## Próximo contexto recomendado

- Task 157
- `contracts/openapi.yaml` em `contents/trails`
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `mobile/docs/ai/` e `design-system/mobile/`
- motivo: a próxima task é web
