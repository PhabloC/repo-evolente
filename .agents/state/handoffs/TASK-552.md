# Handoff - Task 552

## Task

- identificador: TASK-552
- título: Bootstrap Descubra a palavra: mesclar palavras por ID
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 043
- objetivo de negócio: Descubra a palavra no catálogo sem wipe no bootstrap
- entrega verificável: palavras e URLs editados pelo admin sobrevivem à reinicialização

## Decisões preservadas

- decisão: `mergeWordSpellWords` por ID, no padrão fluency/jigsaw (Task 488)
- motivo: categoria existente substituía a lista inteira por `template.words`
- impacto: palavra custom permanece; template ausente é append; URLs vazios recebem fallback

- decisão: preservar categorias atuais e append das categorias do template ainda ausentes
- motivo: admin pode ter só Insetos editado; demais categorias do template não devem sumir nem apagar a editada
- impacto: `insetos` custom + novas categorias do template na mesma config

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 552, slice 043

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `word-spell-game-assets.ts` | merge | `mergeWordSpellWords` |
| `catalog-config-merge.ts` | padrão Task 488 | `preferNonEmpty` |
| `catalog-config-merge.spec.ts` | regressão | pulga custom + palavra-admin |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| UI biblioteca | fora de escopo |

## Resultado por stack

- backend: merge por ID no builder word-spell
- front-end / mobile: fora de escopo

## Arquivos alterados

- `backend/src/modules/contents/word-spell-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`

## Validações executadas

- validação: Jest filtro word-spell — PASS
- validação: eslint builder + spec — 0 erros

## Pendências ou bloqueios

- smoke: bootstrap com palavra admin extra não some

## Próxima ação sugerida

- Task 553 (precedência intro/conclusão) no mesmo review

## Próximo contexto recomendado

- `word-spell-game-assets.ts` `mergeWordSpellWords`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `contracts/openapi.yaml`
- motivo: builder interno do catálogo
