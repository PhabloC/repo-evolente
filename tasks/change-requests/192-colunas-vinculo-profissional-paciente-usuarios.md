# Task 192 - Colunas de vínculo profissional-paciente na página de usuários

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

- `contracts/openapi.yaml#/paths/~1admin~1professionals-tree` (fonte dos vínculos)

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto de negocio

### O que

Na aba Profissionais, exibir quantidade de pacientes vinculados. Na aba Pacientes, exibir se há profissional vinculado (um ou nenhum).

### Premissas

- Contagens e vínculos vêm de `/admin/professionals-tree` (já carregada).
- Pacientes sem vínculo ainda não entram na listagem atual (árvore só retorna vinculados); a coluna já trata o caso "Sem vínculo".

## Contexto mínimo

- esta task
- `front-end/src/pages/Main/AdminUsers/**`

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- coluna Pacientes na aba profissionais
- coluna Profissional na aba pacientes
- testes atualizados

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

- Aba Profissionais: coluna **Pacientes** com contagem por profissional.
- Aba Pacientes: coluna **Profissional** com badge Vinculado + nome, ou Sem vínculo.

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validacoes executadas

- lint ok
- AdminUsers tests ok (8)

## Handoff

- `.agents/state/handoffs/TASK-192.md`

## Status final

done
