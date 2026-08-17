# Task 176 - Remover botao Fechar do rodape do modal de visualizar jogo

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

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- Fechamento do modal permanece pelo X do header, backdrop e Escape.

## Contexto de negocio

### Por que

O botão Fechar no final do modal é redundante com o X do cabeçalho.

### O que

Remover o botão Fechar do rodapé do modal de visualizar jogo, mantendo Limpar/Confirmar no preview de escrita.

### Comportamento esperado

- sem botão Fechar no final do modal
- fechamento continua via X, clique fora e Escape
- preview de escrita mantém Limpar e Confirmar

### Fora de escopo

- mudanças no componente Modal base
- backend e mobile

## Slice vertical

### Identificador do slice

Slice 029 - Catalogo inicial de jogos terapeuticos

### Arquivo do slice

- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `.agents/state/handoffs/TASK-175.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI preview | `front-end/src/pages/Main/Library/GamePreviewModal.tsx` | implementação | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: apenas GamePreviewModal

## Criterios de conclusao

- nenhum botão Fechar no rodapé do preview
- Limpar/Confirmar preservados no preview de escrita

## Dependencias

- Task 175

## Resultado da execucao

- Removidos os botões Fechar dos três estados do `GamePreviewModal`
- Preview de escrita ficou com Limpar e Confirmar

## Contexto utilizado

- task 176, slice 029, handoff 175, `GamePreviewModal.tsx`

## Handoff

- `.agents/state/handoffs/TASK-176.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/176-remover-botao-fechar-rodape-modal-visualizar-jogo.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-176.md`

## Validacoes executadas

- revisão estática do componente
- classes CSS órfãs removidas

## Pendencias pos-task

- nenhuma

## Status final

done
