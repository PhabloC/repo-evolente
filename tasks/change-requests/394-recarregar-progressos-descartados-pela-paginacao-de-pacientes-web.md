# Task 394 - Recarregar progressos descartados pela paginação de pacientes web

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

- não se aplica (sem mudança de contrato)

## Modo de execução

single-stack

## Slice vertical

- Slice 007 - Gestao de pacientes do profissional
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Referência visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

correção funcional, sem mudança de layout

### Fonte primaria visual

- `front-end/src/pages/Main/Patients/index.tsx`

## Objetivo

Evitar que a coluna de progresso fique presa em "Carregando..." quando o usuário troca de página enquanto as requisições de progresso ainda estão em voo.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Carregamento de progresso | `front-end/src/pages/Main/Patients/index.tsx` | corrigir o descarte de resultados válidos | sim |
| Execução concorrente | `front-end/src/utils/mapWithConcurrency.ts` | entender o comportamento em lote e falha | sim |
| Cobertura | `front-end/src/pages/Main/Patients/index.test.tsx` | regressão de paginação com requisição em voo | sim |

## Orçamento de contexto

- baixo
- estratégia: ajuste no efeito de progresso da página de pacientes

## Critérios de conclusão

- [x] trocar de página não descarta mais o progresso já solicitado
- [x] voltar para a página anterior mostra o progresso resolvido
- [x] falha de lote marca erro apenas nos pacientes daquele lote
- [x] recarregar a lista continua invalidando resultados antigos
- [x] regressão coberta por teste que falha sem a correção
- [x] suíte da página executada

## Origem

- comentário de code review (`P2 MÉDIO`) apontando que a nova requisição incrementava `progressRequestRef` e descartava o resultado anterior, deixando pacientes presos em `status: 'loading'`

## Diagnostico

- o guard por `requestId` era incrementado a cada troca de página, então o resultado do lote anterior era descartado
- como os pacientes já tinham entrada `loading` no mapa, `patientsToFetch` não os selecionava de novo ao voltar; a célula ficava em "Carregando..." para sempre
- o `catch` também marcava erro em todos os pacientes da página atual, e não apenas nos do lote que falhou

## Resultado da execucao

- o guard deixou de ser por requisição e passou a ser por geração de dados (`progressGenerationRef`), incrementada apenas em `loadPatients`
- resultados são aplicados mesmo se o usuário mudou de página, porque o summary é por paciente e continua válido
- recarregar a lista (filtro, vínculo, mudança de status) segue invalidando lotes em voo, e como o mapa é limpo os pacientes são buscados de novo
- o `catch` passou a marcar erro somente nos ids do lote (`fetchedPatientIds`)

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 007
- contexto sob demanda: página de pacientes, `mapWithConcurrency`, teste da página
- contexto evitado: backend e contrato, porque a correção é de estado no cliente

## Handoff

- `.agents/state/handoffs/TASK-394.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Patients/index.test.tsx` (6 testes)
- verificação de que o teste novo falha ao simular o comportamento antigo
- `cd front-end && npx eslint src/pages/Main/Patients/index.tsx src/pages/Main/Patients/index.test.tsx`
- `cd front-end && npx tsc --noEmit` — erros preexistentes em `Library/GamePreviewModal.tsx`, `Library/index.test.tsx` e `PatientProfile/index.test.tsx`; nenhum nos arquivos desta task

## Pendencias pos-task

- erros preexistentes de typecheck no front-end seguem fora do escopo desta task

## Status final

done
