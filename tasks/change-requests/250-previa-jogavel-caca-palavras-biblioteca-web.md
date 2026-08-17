# Task 250 - Prévia jogável do caça-palavras na biblioteca web

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

- nao se aplica (reusa `gameConfig` já existente)

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

comportamento do runtime mobile do slice 031 (setup + grade)

### Fonte primaria visual

- `mobile/src/features/games/components/WordSearchGameRenderer/` (paridade de fluxo)
- `design-system/front/Design_System_Evolente_Desktop.md` (tokens/UI web)

### Regra de aderencia visual

- Fluxo igual ao mobile: categoria → dificuldade → grade com seleção ponta a ponta
- Fechamento do modal só pelo X / backdrop / Escape (sem Fechar no rodapé)

## Contexto de negocio

### Por que

O master precisa testar o caça-palavras na biblioteca web, não só ver metadados.

### O que

Tornar o modal de visualizar jogo do `word-search` jogável na web.

### Comportamento esperado

- escolher categoria e dificuldade
- gerar grade com palavras H/V/diagonal
- marcar palavra tocando primeira e última letra
- listar palavras encontradas e opção de novo jogo
- sem botão Fechar no rodapé

### Fora de escopo

- editor de palavras no master
- mudanças no backend ou mobile
- conclusão de atividade / trilha

## Slice vertical

### Identificador do slice

Slice 031 - Jogo caça-palavras

### Arquivo do slice

- `tasks/slices/031-jogo-caca-palavras.md`

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/031-jogo-caca-palavras.md`

## Contexto sob demanda

- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `mobile/src/features/games/utils/wordSearchGame.ts` (lógica a portar)
- `front-end/src/pages/Main/Library/styles.module.css`

## Orçamento de contexto

baixo — uma tela de prévia e util compartilhado de lógica

## Dependencias

- Task 249 (done)

## Criterios de aceite

- [x] Prévia web permite jogar o caça-palavras
- [x] Paridade de regras com o mobile (categorias, dificuldades, seleção)
- [x] Sem botão Fechar no rodapé

## Resultado da execucao

- Portada a lógica de geração/seleção do mobile para `wordSearchGame.ts` no front-end
- Modal de visualizar caça-palavras agora é jogável: setup → grade → banco de palavras → novo jogo

## Contexto utilizado

- Task 250, slice 031, `GamePreviewModal`, utils mobile de word-search

## Handoff

- `.agents/state/handoffs/TASK-250.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/wordSearchGame.ts` (novo)
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/250-previa-jogavel-caca-palavras-biblioteca-web.md`
- `tasks/slices/031-jogo-caca-palavras.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run lint` no front-end (ok)

## Pendencias pos-task

- Nenhuma

## Status final

done
