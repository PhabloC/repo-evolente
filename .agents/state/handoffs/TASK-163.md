# Handoff - Task 163

## Task

- identificador: 163
- título: Refatorar runtime de jogos mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 028 - Runtime de jogos mobile extensivel
- objetivo de negócio: preparar a base mobile para novos jogos sem inflar a trilha
- entrega verificável: runtime do alfabeto extraído para `features/games`
- status do slice: done

## Decisões preservadas

- decisão: manter jogo como `content` no contrato e na trilha
- motivo: o fluxo de catálogo e distribuição já está correto
- impacto: a extração foi apenas da camada de execução mobile

- decisão: criar `features/games` como runtime dedicado
- motivo: novos jogos não devem crescer dentro de `trail`
- impacto: renderers, serviços e utilitários de jogo agora têm fronteira própria

- decisão: introduzir `GameActivityRenderer`
- motivo: centralizar o switch por `gameType` em um único ponto
- impacto: adicionar novo jogo passa a ser extensão local da feature `games`

- decisão: preservar `TrailActivityItem` como contrato de entrada
- motivo: a trilha continua sendo o ponto de leitura e conclusão
- impacto: não foi criado modelo duplicado de atividade

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/163-refatorar-runtime-de-jogos-mobile.md`
- `tasks/slices/028-runtime-jogos-mobile-extensivel.md`
- `.agents/state/handoffs/TASK-158.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS mobile | UI | preservar a experiência entregue |
| openapi | API | garantir refactor sem mudança de contrato |
| `mobile/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | implementação | organizar nova feature |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| docs web/backend | stack não envolvida |
| `mobile/docs/ai/ACCESSIBILITY.md` | arquivo ausente na stack |

## Resultado por stack

- mobile: done

## Arquivos alterados

- `mobile/src/features/games/components/AlphabetGameRenderer/**`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/utils/alphabetGame.ts`
- `mobile/src/features/games/utils/alphabetGame.test.ts`
- `mobile/src/features/games/utils/gameMetadata.ts`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- remoção dos arquivos de jogo antes localizados em `mobile/src/features/trail/**`
- task/slice/index/handoff

## Validações executadas

- mobile lint: ok
- mobile typecheck: ok
- mobile test: ok (`14 suites`, `36 tests`)

## Pendências ou bloqueios

- sem bloqueio
- próximo `gameType` deve reutilizar `features/games`
- `mobile/docs/ai/ACCESSIBILITY.md` continua faltando

## Próxima ação sugerida

- usar `features/games` como base do próximo jogo terapêutico mobile

## Próximo contexto recomendado

- `tasks/change-requests/163-refatorar-runtime-de-jogos-mobile.md`
- `.agents/state/handoffs/TASK-163.md`
- `mobile/src/features/games/`

## Contexto que não deve ser carregado na próxima etapa

- fonte: fluxos web/backend do catálogo e trilha
- motivo: a próxima evolução de jogos pode se apoiar na base mobile já isolada
