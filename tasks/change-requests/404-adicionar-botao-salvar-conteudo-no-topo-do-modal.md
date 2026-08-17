# Task 404 - Adicionar botão Salvar conteúdo no topo do modal

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
- conversa de quarta-feira, 5 de agosto de 2026, sobre o modal de edição da biblioteca

### Regra de aderencia visual

- manter o modal atual da biblioteca
- adicionar uma ação visível de salvar no topo do modal de edição
- preservar o rodapé existente, mas alinhar o rótulo da ação de edição para `Salvar conteúdo`

## Contexto de negocio

### Por que

Durante a edição de um conteúdo a ação de salvar não estava suficientemente evidente na área visível inicial do modal.

### O que

Expor um botão `Salvar conteúdo` no header do modal de edição e habilitá-lo quando houver alteração real no formulário.

### Comportamento esperado

- o modal de edição mostra `Salvar conteúdo` no topo
- o botão fica desabilitado até existir mudança real no formulário
- ao editar algum campo, o botão passa a ficar disponível
- o rodapé mantém a ação de submit com o mesmo rótulo em edição

### Fora de escopo

- redesign completo do modal
- mudanças no backend ou no fluxo de persistência

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
- `.agents/state/handoffs/TASK-403.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Header do modal | `front-end/src/pages/Main/Library/ContentFormModal.tsx` | adicionar a ação visível de salvar e atrelar ao `isDirty` | sim |
| Regressão do fluxo | `front-end/src/pages/Main/Library/index.test.tsx` | validar a presença e habilitação do botão em edição | sim |
| Ajuste visual local | `front-end/src/pages/Main/Library/styles.module.css` | confirmar que o bloco do header comporta a nova ação | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a execução ao modal da biblioteca e ao teste focado da página

## Criterios de conclusao

- [x] o modal de edição mostra `Salvar conteúdo` no topo
- [x] o botão de salvar em edição fica desabilitado sem alterações e habilita após edição
- [x] o teste da biblioteca cobre esse comportamento
- [x] a suíte focada da biblioteca passa

## Dependencias

- Task 403

## Resultado da execucao

- o header do modal da biblioteca passou a renderizar um submit visível em modo de edição
- o botão `Salvar conteúdo` agora respeita `isDirty` e também considera troca de arquivo como mudança pendente
- o rodapé de edição foi alinhado ao mesmo rótulo da ação principal

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-403.md`

### Sob demanda

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-404.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/404-adicionar-botao-salvar-conteudo-no-topo-do-modal.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-404.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
