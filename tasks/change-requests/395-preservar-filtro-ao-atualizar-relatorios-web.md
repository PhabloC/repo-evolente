# Task 395 - Preservar filtro ao atualizar relatórios web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- sem alteração

## Modo de execução

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Objetivo

Manter o histórico coerente com o filtro de paciente exibido após gerar, disponibilizar ou excluir um relatório.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `front-end/docs/ai/`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Filtro e atualização | `front-end/src/pages/Main/Reports/index.tsx` | separar filtro do histórico e paciente do formulário |

## Orçamento de contexto

- baixo
- alteração pontual na página de relatórios

## Critérios de conclusão

- [x] geração preserva o filtro visível
- [x] disponibilização preserva o filtro visível
- [x] exclusão preserva o filtro visível
- [x] lint do arquivo passa

## Resultado da execução

- os três recarregamentos passaram a usar apenas `selectedPatientId || undefined`
- `createPatientId` continua restrito ao formulário de criação e não influencia mais o histórico

## Validações executadas

- `npx eslint src/pages/Main/Reports/index.tsx` — passou
- `npm test -- --run` — 109 testes passaram; 2 timeouts preexistentes em `AdminUsers/index.test.tsx`
- `npm run build` — bloqueado por quatro erros preexistentes em `Library/GamePreviewModal.tsx`, `Library/index.test.tsx` e `Patients/PatientProfile/index.test.tsx`

## Handoff

- `.agents/state/handoffs/TASK-395.md`

## Status final

done
