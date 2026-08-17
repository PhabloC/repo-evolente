# Task 320 - Restaurar acentuação nos relatórios PDF

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

- nao se aplica; ajuste interno na geração do arquivo PDF

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- nao se aplica

### Tipo de referencia visual

- feedback direto do usuario

### Fonte primaria visual

- `backend/src/modules/reports/**`

### Lacunas

- sem artefato visual; a validação é textual no conteúdo do PDF gerado

## Objetivo

Garantir que os relatórios em PDF sejam gerados com acentuação correta em português.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-319.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Arquitetura backend | `backend/docs/ai/{ARCHITECTURE.md,SECURITY.md}` | manter ajuste interno consistente e seguro | sim |
| Export util | `backend/src/modules/reports/utils/report-export.util.ts` | corrigir serialização e rótulos do PDF | sim |
| Testes utilitários | `backend/src/modules/reports/utils/report-export.util.spec.ts` | validar acentuação e estrutura | sim |
| Serviço de reports | `backend/src/modules/reports/reports.service.ts` | corrigir textos do conteúdo emitido | sim |
| Teste do módulo | `backend/src/modules/reports/reports.service.spec.ts` | validar o PDF no fluxo real | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao módulo `reports` e aos testes associados

## Criterios de conclusao

- [x] o PDF contém títulos e textos com acentuação correta
- [x] o buffer do PDF continua válido no fluxo atual sem dependências externas
- [x] os testes do módulo `reports` continuam passando

## Dependencias

- Task 319 - done

## Resultado da execucao

- o gerador de PDF passou a serializar o conteúdo em `latin1`, preservando caracteres acentuados compatíveis com o PDF textual simples usado no projeto
- os rótulos e textos do relatório foram atualizados para português com acentuação correta
- os testes do utilitário de exportação e do fluxo completo de `reports` foram ajustados para validar os textos acentuados no PDF

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-319.md`

### Sob demanda

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/SECURITY.md`
- `backend/src/modules/reports/utils/report-export.util.ts`
- `backend/src/modules/reports/utils/report-export.util.spec.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`

### Contexto evitado

- `front-end/`, porque a correção é interna à geração do PDF no backend

## Handoff

- `.agents/state/handoffs/TASK-320.md`

## Arquivos alterados

- `backend/src/modules/reports/utils/report-export.util.ts`
- `backend/src/modules/reports/utils/report-export.util.spec.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `tasks/change-requests/320-restaurar-acentuacao-nos-relatorios-pdf.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-320.md`

## Validacoes executadas

- `cd backend && npm run test -- --runInBand src/modules/reports/utils/report-export.util.spec.ts src/modules/reports/reports.service.spec.ts`
- `cd backend && npm run build`

## Pendencias pos-task

- nenhuma

## Status final

done
