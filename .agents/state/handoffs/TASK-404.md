# Handoff - Task 404

## Task

- identificador: 404
- título: Adicionar botão Salvar conteúdo no topo do modal
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web

## Decisões preservadas

- o modal de edição da biblioteca passou a mostrar `Salvar conteúdo` no header
- o botão principal de edição só habilita quando há mudança real no formulário ou troca de arquivo
- o rodapé de edição foi mantido, mas com o mesmo rótulo da ação principal

## Contexto utilizado

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`

## Arquivos alterados

- modal da biblioteca, teste, task, slice, índice e handoff

## Validações executadas

- suíte `Library/index.test.tsx`

## Próximo contexto recomendado

- nenhum; ajuste localizado na visibilidade da ação de salvar no modal da biblioteca
