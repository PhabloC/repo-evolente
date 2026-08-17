# Handoff - Task 170

## Task

- identificador: 170
- título: Tolerancia da validacao de escrita de letras
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 030 - Escrita guiada de letras
- objetivo de negócio: escrita guiada com validação tolerante a traços infantis
- entrega verificável: `U` torto aceito no preview web e no mobile; formas distintas rejeitadas
- status do slice: done

## Decisões preservadas

- decisão: corrigir bounding box do front-end com epsilon `0.0001` em vez de mínimo `1`
- motivo: o mínimo `1` distorcia templates 0–1 e rejeitava até um `U` perfeito no preview
- impacto: normalização web fica alinhada ao mobile

- decisão: amostrar cada stroke separadamente
- motivo: flatten + samplePolyline criava segmento fantasma entre traços
- impacto: `U` em dois traços passa sem penalidade artificial

- decisão: limiares `0.28` / `0.30` para escrita infantil
- motivo: criança escreve torto; manter rejeição só para formas claramente distintas
- impacto: maior taxa de acerto sem aceitar linha vertical como `O`/`U`

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/170-tolerancia-validacao-escrita-de-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`

### Sob demanda

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`

## Arquivos alterados

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.test.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `tasks/change-requests/170-tolerancia-validacao-escrita-de-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-170.md`

## Validações executadas

- testes web `letterWritingGame.test.ts` — ok
- testes mobile `alphabetWritingGame` — ok
- typecheck mobile do utilitario — ok

## Pendências

- smoke manual no preview da biblioteca (escrever `U` torto e confirmar)

## Próxima ação sugerida

- testar no browser o card “Escreva a letra” e confirmar aceite do `U` imperfeito

## Próximo contexto recomendado

- apenas o utilitario/testes de escrita se houver novo ajuste fino de limiar

## Contexto que não deve ser carregado

- contrato OpenAPI
- bootstrap de catálogo
- design-system completo
- runtime UI além do preview já existente
