# Task 594 - Validar agregado antes do cadastro familiar

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Sem alteração; preserva `POST /patients`.

## Modo de execucao

single-stack

## Slice vertical

- Slice 049 - `tasks/slices/049-cadastro-responsavel-sem-filho.md`

## Contexto mínimo

- Índice, Slice 049, registro familiar e testes de guardians.

## Contexto sob demanda

- Repositórios de guardians e users, para manter a validação antes da primeira gravação.

## Orçamento de contexto

- baixo; limitar ao agregado família criado pelo profissional.

## Estratégia de redução

- Validar filho e anamnese antecipadamente sem alterar endpoint ou fluxo público.

## Resultado da execucao

- `registerFamily` valida CPF, nascimento, diferença entre CPFs, disponibilidade do CPF da criança e anamnese antes de criar usuário ou perfil.

## Contexto utilizado

- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/patients/patients.service.spec.ts`

## Handoff

- `.agents/state/handoffs/TASK-594.md`

## Arquivos alterados

- Serviço de guardians e testes direcionados de patients.

## Validacoes executadas

- `npx jest src/modules/patients/patients.service.spec.ts --runInBand` - 11 testes ok.
- `npm run lint` e `npm run build` no backend - ok.

## Pendencias pos-task

- Nenhuma.

## Status final

done
