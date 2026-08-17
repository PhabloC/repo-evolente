# Task 179 - Linha pontilhada no traco escrito do modal de letras

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 030 - Escrita guiada de letras

### Arquivo do slice

- `tasks/slices/030-escrita-guiada-de-letras.md`

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| preview web | `GamePreviewModal.tsx` | traço pontilhado | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- a linha desenhada pelo usuário no modal de escrita fica pontilhada
- sem guia/template pontilhado de exemplo da letra

## Dependencias

- Task 169

## Resultado da execucao

- Removida a guia pontilhada de exemplo
- Traço do usuário no SVG do preview passou a usar `stroke-dasharray` pontilhado

## Arquivos alterados

- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.test.ts`
- `tasks/change-requests/179-linha-pontilhada-guia-modal-escrita-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-179.md`

## Validacoes executadas

- `npx vitest run src/pages/Main/Library/letterWritingGame.test.ts` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
