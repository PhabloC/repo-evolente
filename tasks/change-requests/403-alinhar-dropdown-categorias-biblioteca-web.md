# Task 403 - Alinhar dropdown de categorias da biblioteca web

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
- conversa de 5 de agosto de 2026 sobre o modal de conteúdo da biblioteca

### Regra de aderencia visual

- manter o modal atual da biblioteca
- trocar apenas os rótulos do dropdown `Categoria` para seguir as categorias definidas pelo usuário
- preservar compatibilidade com os valores internos já aceitos pela API

## Contexto de negocio

### Por que

O dropdown `Categoria` do modal da biblioteca ainda exibia a taxonomia antiga e divergente das categorias aprovadas para a seção `Conteúdos`.

### O que

Alinhar as opções visíveis do select de categoria às categorias pedidas pelo usuário: `Articulação`, `Cognição`, `Atenção`, `Vocabulário`, `Leitura e Escrita`, `Frases`, `Socioemocionais`, `Fluência` e `Diálogo`.

### Comportamento esperado

- o dropdown mostra apenas as categorias alinhadas ao novo agrupamento
- os labels antigos como `Articulatório` não aparecem mais no modal
- o fluxo de criação/edição continua salvando com os valores internos já suportados

### Fora de escopo

- mudanças no backend ou no enum persistido de categorias
- remodelagem completa da taxonomia de conteúdos

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
- `.agents/state/handoffs/TASK-402.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Dropdown do modal | `front-end/src/constants/contentOptions.ts` | redefinir labels visíveis das categorias de conteúdo | sim |
| Formulário da biblioteca | `front-end/src/pages/Main/Library/ContentFormModal.tsx` | apontar o select para a lista atualizada e manter defaults compatíveis | sim |
| Regressão do modal | `front-end/src/pages/Main/Library/index.test.tsx` | validar as opções visíveis do dropdown | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a execução ao modal da biblioteca, suas constantes e ao teste focado da página

## Criterios de conclusao

- [x] o dropdown `Categoria` da biblioteca segue as categorias definidas no chat
- [x] `Articulatório` deixa de aparecer como opção visível no modal
- [x] o teste focado da biblioteca valida as novas opções do select
- [x] a suíte focada da biblioteca passa

## Dependencias

- Task 402

## Resultado da execucao

- o dropdown `Categoria` do modal da biblioteca passou a exibir apenas as categorias alinhadas às abas novas da seção `Conteúdos`
- a fonte de opções do formulário foi separada da taxonomia antiga da anamnese
- os defaults do modal mantiveram compatibilidade com categorias legadas como `memoria` e `matematica`

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-402.md`

### Sob demanda

- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`

## Handoff

- `.agents/state/handoffs/TASK-403.md`

## Arquivos alterados

- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/403-alinhar-dropdown-categorias-biblioteca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-403.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
