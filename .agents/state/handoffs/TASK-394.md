# Handoff - Task 394

## Task

- identificador: 394
- título: Recarregar progressos descartados pela paginação de pacientes web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 007 - Gestao de pacientes do profissional

## Decisões preservadas

- o guard de concorrência deixou de ser por requisição e virou por geração de dados (`progressGenerationRef`), incrementada só em `loadPatients`
- resultados de progresso são por paciente, então trocar de página não os invalida e eles são aplicados mesmo fora da página atual
- recarregar a lista continua invalidando lotes em voo; como o mapa é limpo junto, os pacientes são buscados novamente
- falha de lote marca erro apenas nos ids daquele lote, não em toda a página visível

## Contexto utilizado

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/utils/mapWithConcurrency.ts`
- `front-end/src/pages/Main/Patients/index.test.tsx`

## Arquivos alterados

- página de pacientes, teste, task, slice, índice e handoff

## Validações executadas

- suíte `Patients/index.test.tsx` (6 testes)
- teste novo confirmado como regressão real: falha ao simular o guard antigo
- eslint nos arquivos alterados
- `npx tsc --noEmit` com erros apenas preexistentes em outros arquivos

## Pendências ou bloqueios

- erros preexistentes de typecheck no front-end (`GamePreviewModal`, `Library/index.test.tsx`, `PatientProfile/index.test.tsx`)

## Próximo contexto recomendado

- `front-end/src/pages/Main/Patients/index.tsx`, se o carregamento de progresso for migrado para cache de query
