# Task 373 - Remover criação de relatório CSV e manter apenas PDF

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1reports`
- `contracts/openapi.yaml#/components/schemas/CreateEvolutionReportRequest`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Web

- tipo: refino incremental da página existente
- fonte primaria: `front-end/src/pages/Main/Reports/index.tsx`

### Mobile

- tipo: validação de compatibilidade do fluxo existente
- fonte primaria: `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- fonte secundaria: `mobile/src/features/reports/services/reportsService.ts`

## Objetivo

Remover o formato CSV da criação de relatórios, deixando o fluxo novo restrito a PDF na web e na API, sem quebrar o acesso a arquivos CSV antigos já existentes.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-372.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web de geração | `front-end/src/pages/Main/Reports/index.tsx` | remover seletor de formato e ajustar copy do bloco de criação | sim |
| Tipos web | `front-end/src/types/report.ts`, `front-end/src/constants/navigation.ts` | alinhar payload e textos do módulo | sim |
| API de relatórios | `backend/src/modules/reports/{dto/reports.dto.ts,reports.service.ts,reports.service.spec.ts,entities/evolution-report.entity.ts}` | fixar geração nova em PDF e validar comportamento | sim |
| Contrato | `contracts/openapi.yaml` | remover `format` do request de criação e atualizar descrições | sim |
| Compatibilidade mobile | `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`, `mobile/src/features/reports/services/reportsService.ts` | verificar se a remoção do CSV na criação exige ajuste no app do responsável | sim |

## Orçamento de contexto

- baixo
- estratégia: tocar apenas o fluxo de criação, o contrato correspondente e a copy de apoio, preservando o suporte de leitura/download para relatórios CSV legados

## Criterios de conclusao

- [x] a criação de relatórios não expõe mais o formato CSV na web
- [x] a API de criação deixa de aceitar `format` e passa a gerar PDF por padrão
- [x] o contrato OpenAPI reflete o novo payload de criação
- [x] o app mobile foi verificado para compatibilidade com relatórios legados
- [x] validações das stacks alteradas foram executadas

## Dependencias

- Task 025 - done
- Task 314 - done
- Task 364 - done
- Task 372 - done

## Resultado da execucao

- a página web de relatórios passou a gerar apenas PDF, sem seletor de formato nem copy comparando PDF com CSV
- o backend fixou a criação nova em PDF, removendo `format` do DTO e do contrato de request
- o download e a listagem continuam compatíveis com relatórios CSV antigos porque o tipo público do relatório e a rotina de leitura foram preservados
- o mobile não precisou de alteração funcional, pois já consome o formato retornado pelo histórico e segue apto a abrir arquivos legados

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-372.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/types/report.ts`
- `front-end/src/constants/navigation.ts`
- `backend/src/modules/reports/dto/reports.dto.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `backend/src/modules/reports/entities/evolution-report.entity.ts`
- `contracts/openapi.yaml`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/reports/services/reportsService.ts`

## Handoff

- `.agents/state/handoffs/TASK-373.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/types/report.ts`
- `front-end/src/constants/navigation.ts`
- `backend/src/modules/reports/dto/reports.dto.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `contracts/openapi.yaml`
- `tasks/change-requests/373-remover-criacao-de-relatorio-csv-e-manter-apenas-pdf.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-373.md`

## Validacoes executadas

- `cd backend && npm run test -- reports.service.spec.ts` — passou
- `cd front-end && npm run build` — falhou por erros preexistentes fora do escopo em `src/pages/Main/Library/GamePreviewModal.tsx`, `src/pages/Main/Library/index.test.tsx`, `src/pages/Main/Library/index.tsx` e `src/pages/Main/Patients/PatientProfile/index.test.tsx`

## Pendencias pos-task

- corrigir os erros preexistentes do build web para voltar a ter validação completa por `npm run build`

## Status final

done
