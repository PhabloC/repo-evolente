# Handoff - Task 460

## Task

- identificador: 460
- título: Melhorar prévia sem capa no modal Nova atividade
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: `tasks/slices/006-catalogo-conteudos-master.md`
- objetivo de negócio: catálogo master com prévia coerente no modal
- entrega verificável: empty state tipado no lugar de "Sem capa ainda"

## Decisões preservadas

- decisão: áudio/vídeo não têm capa própria; copy reflete prévia por tipo de mídia
- motivo: "Sem capa ainda" sugeria upload pendente inexistente neste fluxo
- impacto: apenas UI da sidebar do `ContentFormModal`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/460-melhorar-previa-capa-modal-nova-atividade.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-459.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `ContentFormModal.tsx` | empty state da capa | copy + markup |
| `styles.module.css` | hierarquia visual | badge/título/hint |
| `ACCESSIBILITY.md` | UI web | aria-label / aria-hidden |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem mudança de API |
| `backend/` / `mobile/` | fora do escopo |
| DS documental completo | ajuste local suficiente |

## Resultado por stack

- front-end: prévia tipada com ícone em badge, título e hint
- backend: n/a
- mobile: n/a

## Arquivos alterados

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`

## Validações executadas

- validação: markup/CSS do fallback — ok
- validação: a11y mínima do bloco — ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma; validar visualmente no modal Nova atividade (áudio/vídeo)

## Próximo contexto recomendado

- `ContentFormModal.tsx` (bloco cover fallback) se houver ajuste fino de copy

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend/mobile/openapi
- motivo: mudança só de prévia visual no front
