# Task 356 - Refinar hover e badge dos cards de jogos no modo profissional web

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

nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste visual orientado por referência enviada no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar os cards do master e aplicar a animação de hover apenas na variação de leitura do profissional

## Contexto de negocio

### Por que

Os cards de jogos vistos pelo profissional ainda mantinham a badge e o botão de preview em uma disposição diferente da solicitada.

### O que

Mover a badge `Disponível na trilha` para baixo do título, remover o botão fixo de visualizar e mostrar o ícone apenas no hover/focus do card com overlay escurecido.

### Comportamento esperado

- badge abaixo do título no card de leitura do profissional
- botão fixo de visualizar removido dessa variação
- hover/focus no card escurece a capa e revela o ícone de preview
- cards do master permanecem sem essa animação

### Fora de escopo

- mudanças no modal de preview
- mudanças nos cards do master
- alterações na tabela editorial da biblioteca

## Slice vertical

### Identificador do slice

Slice 017 - Redesign interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-355.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Card de leitura | `front-end/src/pages/Main/Library/index.tsx` | ajustar a estrutura do card do profissional | sim |
| Estilos locais | `front-end/src/pages/Main/Library/styles.module.css` | criar overlay e comportamento de hover/focus | sim |
| Teste focado | `front-end/src/pages/Main/Library/index.test.tsx` | validar que o preview continua acessível no modo profissional | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a mudança aos cards de jogos em modo leitura no perfil profissional

## Criterios de conclusao

- [x] badge ficou abaixo do título
- [x] botão fixo de visualizar saiu do rodapé
- [x] hover/focus do card mostra overlay com ícone de preview apenas no modo profissional
- [x] teste focado da biblioteca passa

## Dependencias

- Task 355

## Resultado da execucao

- o card de leitura do profissional passou a usar um bloco de título com a badge logo abaixo
- o preview agora é acionado por um botão-overlay posicionado sobre o card
- o overlay escurecido e o ícone aparecem apenas na variação `gameCardReadOnly`

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-355.md`

### Sob demanda

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`

### Contexto evitado

- `backend/` por não haver alteração de API
- outras páginas fora da biblioteca

## Handoff

- `.agents/state/handoffs/TASK-356.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/356-refinar-hover-e-badge-dos-cards-de-jogos-no-modo-profissional-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-356.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
