# Handoff - Task 171

## Task

- identificador: 171
- título: Recalibrar tolerancia da escrita sem aceitar rabisco
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 030 - Escrita guiada de letras
- status do slice: done

## Decisões preservadas

- decisão: opção A — só recalibrar, sem biblioteca nova
- motivo: pedido explícito do usuário após a validação ficar permissiva demais
- impacto: média ≤ 0.15, p90 ≤ 0.25 e topo aberto para `U`

- decisão: manter bbox epsilon e amostragem por stroke da Task 170
- motivo: o bug original do preview web continua corrigido
- impacto: `U` perfeito/torto continua válido; scribble e círculo como `U` falham

## Contexto utilizado

- task 171, slice 030, handoff 170
- utilitarios/testes web e mobile de escrita

## Arquivos alterados

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.test.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `tasks/change-requests/171-recalibrar-tolerancia-escrita-sem-aceitar-rabisco.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-171.md`

## Validações executadas

- testes web letterWritingGame — ok
- testes mobile alphabetWritingGame — ok

## Pendências

- smoke manual no preview
- se ainda não bastar, evoluir para opção B (`$P`/`ndollar-js`)

## Próxima ação sugerida

- testar no browser: `U` torto deve passar; rabisco/qualquer coisa deve falhar

## Próximo contexto recomendado

- só utilitarios de escrita, se houver novo ajuste fino

## Contexto que não deve ser carregado

- contrato, design-system completo, bootstrap de catálogo
