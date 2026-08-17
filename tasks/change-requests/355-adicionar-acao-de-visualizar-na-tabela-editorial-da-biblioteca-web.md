# Task 355 - Adicionar ação de visualizar na tabela editorial da biblioteca web

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

ajuste funcional orientado por referência enviada no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar a tabela editorial existente e expor a ação de visualização com ícone consistente ao usado nos cards de jogos

## Contexto de negocio

### Por que

Na tabela de áudio e vídeo da biblioteca o profissional não tinha acesso visual direto ao conteúdo, embora essa ação já existisse para jogos e para o master.

### O que

Exibir o ícone de visualizar conteúdo também na tabela editorial para perfis de leitura.

### Comportamento esperado

- a tabela de áudio e vídeo mostra a coluna `Ações`
- o botão com ícone de visualizar aparece também para o profissional
- ações de editar, inativar e excluir continuam restritas ao master

### Fora de escopo

- mudanças no modal de preview
- mudanças na paginação da tabela
- alteração das permissões de edição

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
- `.agents/state/handoffs/TASK-354.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Tabela editorial | `front-end/src/pages/Main/Library/index.tsx` | expor a coluna de ações no modo leitura | sim |
| Teste da biblioteca | `front-end/src/pages/Main/Library/index.test.tsx` | validar o botão `visualizar` para profissional | sim |
| Tabela compartilhada | `front-end/src/ui/Table/index.tsx` | confirmar que a coluna adicional renderiza corretamente | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a mudança à composição das colunas da tabela editorial da biblioteca

## Criterios de conclusao

- [x] tabela editorial sempre renderiza a coluna `Ações`
- [x] profissional visualiza o botão `Visualizar conteúdo`
- [x] ações de mutação continuam só para master
- [x] teste focado da biblioteca passa

## Dependencias

- Task 313

## Resultado da execucao

- a coluna `Ações` da tabela editorial passou a existir para qualquer perfil
- o botão com ícone `Eye` de visualizar conteúdo agora aparece também no modo leitura
- ações de editar, inativar/reativar e excluir continuam condicionadas a `canMutate`

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-354.md`

### Sob demanda

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `front-end/src/ui/Table/index.tsx`

### Contexto evitado

- `backend/` por não haver alteração de API
- outras páginas da biblioteca por não participarem da tabela editorial

## Handoff

- `.agents/state/handoffs/TASK-355.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/355-adicionar-acao-de-visualizar-na-tabela-editorial-da-biblioteca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-355.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
