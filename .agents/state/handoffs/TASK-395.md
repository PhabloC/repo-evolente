# Handoff - Task 395

## Task

- identificador: 395
- título: Preservar filtro ao atualizar relatórios web
- tipo: front
- status final: done

## Slice vertical

- Slice 011 - Relatorios de evolucao

## Decisões preservadas

- `selectedPatientId` é a única fonte do filtro do histórico.
- `createPatientId` pertence somente ao formulário de geração.
- gerar, disponibilizar e excluir recarregam o histórico com `selectedPatientId || undefined`.

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- task, slice, índice e handoff

## Validações

- lint do arquivo passou
- suíte geral: 109/111 testes; dois timeouts preexistentes em AdminUsers
- build bloqueado por erros TypeScript preexistentes em outros arquivos

## Pendências

- nenhuma relativa à correção
