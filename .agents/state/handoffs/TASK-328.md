# Handoff - Task 328

## Task

- identificador: 328
- título: Ajustar acentuacao e badge de status na biblioteca
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catalogo
- objetivo de negócio: melhorar a legibilidade da tabela e a clareza visual do status no catálogo
- entrega verificável: labels acentuados e bolinha à esquerda na badge de status
- status do slice: done

## Decisões preservadas

- decisão: centralizar os labels de dificuldade em helper compartilhado
- motivo: evitar repetição de textos sem acento em tabela e preview
- impacto: futuras telas do catálogo podem reutilizar o mesmo padrão

- decisão: seguir o padrão visual de badges já usado em outras telas internas
- motivo: manter consistência visual do produto
- impacto: a badge da biblioteca ficou alinhada ao resto do sistema

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/328-ajustar-acentuacao-e-badge-de-status-na-biblioteca.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-327.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/constants/contentOptions.ts` | labels compartilhados | helper de dificuldade |
| `front-end/src/pages/Main/Library/` | UI web | tabela, preview, CSS e testes |

## Resultado por stack

- front-end: done

## Arquivos alterados

- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/MediaPreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/328-ajustar-acentuacao-e-badge-de-status-na-biblioteca.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-328.md`

## Validações executadas

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok

## Pendências ou bloqueios

- sem bloqueios

## Próxima ação sugerida

- abrir nova task apenas se o produto quiser padronizar a mesma badge e os mesmos labels em outros módulos
