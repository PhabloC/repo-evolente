# Task 461 - Scroll na seção Dados do modal Nova atividade

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- handoff `TASK-460` / layout do modal (Task 459)

## Contexto sob demanda

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css` (shell/panel/fieldset + memorySetupModalBody)

## Orçamento de contexto

- baixo; bug de overflow/altura no modal
- não carregar backend, mobile, openapi

## Objetivo

Garantir que a aba Dados (e o painel do formulário) role dentro do modal sem cortar campos no rodapé.

## Criterios de conclusao

- [x] campos finais da seção Dados acessíveis via scroll
- [x] header e footer do modal permanecem visíveis
- [x] abas Dados/Arquivo preferencialmente fixas no topo do painel
- [x] create/edit/view preservados

## Dependencias

- Task 459 / 460 (modal biblioteca)

## Resultado da execucao

- Body próprio `contentEditModalBody` (altura limitada + overflow hidden)
- Shell preenche 100% da altura; body em grid com `minmax(0,1fr)`
- Fieldset com `overflow: auto`; abas fixas no topo do painel

## Contexto utilizado

- CSS do modal de conteúdo + bodyClassName herdado de memory setup

## Handoff

- `.agents/state/handoffs/TASK-461.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/461-scroll-secao-dados-modal-nova-atividade.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-461.md`

## Validacoes executadas

- cadeia de altura: modal body → shell → panel → fieldset com scroll

## Pendencias pos-task

- nenhuma; validar visualmente no browser com a aba Dados

## Status final

done
