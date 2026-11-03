# Task 783 - Traço contínuo no Escreva a letra

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

cross-stack

## Origem da solicitacao

Pedido do usuário: trocar o traço pontilhado do jogo Escreva a letra por uma linha contínua (sem pontilhado).

## Objetivo

O traço desenhado pelo usuário no jogo Escreva a letra deve aparecer como linha sólida, sem `stroke-dasharray` pontilhado, no preview web e no runtime mobile.

## Escopo

- remover pontilhado do traço no preview web (`.writingPreviewStroke`)
- remover `strokeDasharray` pontilhado no `AlphabetWritingGameRenderer` mobile
- manter validação, espessura, cor e restante do fluxo inalterados

## Fora de escopo

- reintroduzir guia/template pontilhado da letra
- alterar heurística de validação da escrita

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
- `.agents/state/handoffs/TASK-179.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| estilo web | `front-end/src/pages/Main/Library/styles.module.css` | remover `stroke-dasharray` do traço | sim |
| runtime mobile | `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx` | remover `strokeDasharray` | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: alterar só o estilo visual do traço; não reabrir validação nem design-system

## Criterios de conclusao

- [x] traço do usuário no preview web é linha contínua
- [x] traço do usuário no mobile é linha contínua
- [x] sem guia pontilhada de exemplo da letra

## Dependencias

- Task 179

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md`
- nota: mudança visual mínima (sólido vs pontilhado); sem print novo

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- nota: mudança visual mínima (sólido vs pontilhado); sem print novo

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-179.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `styles.module.css` / `GamePreviewModal.tsx` | traço web | remoção do pontilhado |
| `AlphabetWritingGameRenderer/index.tsx` | traço mobile | remoção do `strokeDasharray` |

## Resultado da execucao

- Preview web: removida a classe `.writingPreviewStroke` com `stroke-dasharray`; o `polyline` permanece com linha sólida (`strokeLinecap`/`strokeLinejoin` round).
- Mobile: removido `strokeDasharray="0.032 0.038"` do `Polyline` do jogo Escreva a letra.

## Handoff

- `.agents/state/handoffs/TASK-783.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
- `tasks/change-requests/783-traco-continuo-escreva-letra.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-783.md`

## Validacoes executadas

- revisão estática: sem `stroke-dasharray` / `strokeDasharray` no traço do Escreva a letra (web e mobile)

## Pendencias pos-task

- nenhuma

## Status final

done
