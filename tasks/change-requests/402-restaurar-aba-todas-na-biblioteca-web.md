# Task 402 - Restaurar aba Todas na biblioteca web

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

ajuste funcional orientado por feedback no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- conversa de 5 de agosto de 2026 sobre a seção `Conteúdos`

### Regra de aderencia visual

- manter a lista de abas criada na Task 401
- recolocar `Todas` como primeira aba da sequência
- fazer `Todas` exibir o acervo inteiro e as demais exibirem apenas atividades com categorias vinculadas

## Contexto de negocio

### Por que

O usuário precisava manter uma visão geral inicial de todo o conteúdo antes de navegar pelos recortes temáticos.

### O que

Adicionar novamente a aba `Todas` como primeiro item da barra e ajustar o filtro local para que apenas as demais abas recortem o conteúdo por categorias relacionadas.

### Comportamento esperado

- a primeira aba é `Todas`
- `Todas` começa ativa e mostra todo o conteúdo disponível
- as demais abas continuam mostrando apenas atividades com categorias vinculadas ao tema

### Fora de escopo

- mudanças no backend ou na persistência de categorias
- alterações nos modais da biblioteca

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
- `.agents/state/handoffs/TASK-401.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste de ordem/filtro | `front-end/src/pages/Main/Library/index.tsx` | restaurar `Todas` e revisar o recorte local | sim |
| Regressão da página | `front-end/src/pages/Main/Library/index.test.tsx` | validar aba inicial e recortes por tema | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a execução à mesma página e aos testes já existentes

## Criterios de conclusao

- [x] `Todas` é a primeira aba da seção `Conteúdos`
- [x] `Todas` começa ativa e mostra o conjunto completo do acervo
- [x] as demais abas continuam filtrando por categorias vinculadas
- [x] o teste focado da biblioteca passa

## Dependencias

- Task 401

## Resultado da execucao

- a aba `Todas` voltou para a primeira posição da barra de navegação da biblioteca
- o estado inicial da página passou a mostrar o conteúdo completo da biblioteca
- as abas temáticas preservaram o comportamento de recorte por categorias vinculadas

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-401.md`

### Sob demanda

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`

## Handoff

- `.agents/state/handoffs/TASK-402.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/402-restaurar-aba-todas-na-biblioteca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-402.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
