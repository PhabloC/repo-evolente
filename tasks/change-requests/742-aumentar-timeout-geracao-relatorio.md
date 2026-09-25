# Task 742 - Aumentar timeout da geração de relatório PDF

## Status

done

## Objetivo

Corrigir o erro `timeout of 10000ms exceeded` ao gerar relatório PDF na tela de Relatórios, permitindo que o `POST /reports` aguarde a inicialização e renderização do Chromium sem alterar o timeout padrão das demais requisições.

## Tipo

front

## Stacks envolvidos

front-end (React/Vite)

## Contrato

`contracts/openapi.yaml#/paths/~1reports~1post`

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/011-relatorios-evolucao.md` (correção incremental do fluxo existente; não cria novo slice).

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `front-end/src/services/http/apiClient.ts`
- `front-end/src/services/reports/reportService.ts`
- `front-end/src/pages/Main/Reports/index.tsx`
- testes do serviço de relatórios e do cliente HTTP

## Contexto sob demanda

- `contracts/openapi.yaml`: validar o `POST /reports` e o formato da resposta.
- `front-end/docs/ai/QA.md`: executar os checks da stack front-end.
- `backend/src/modules/reports/utils/report-export.util.ts`: somente para registrar que a demora ocorre na renderização PDF e não alterar o backend nesta task.

## Orçamento de contexto

Até 8 fontes; priorizar cliente HTTP, serviço de reports, testes e contrato, sem carregar mobile ou UI fora do fluxo afetado.

## Critérios de aceite

- A criação de relatório PDF não falha automaticamente aos 10 segundos por timeout do cliente.
- O timeout aumentado é específico da criação do relatório e não altera o timeout padrão das outras chamadas.
- Existe teste garantindo a configuração específica do `POST /reports`.
- Contrato, índice e handoff ficam rastreáveis.

## Dependências

- Task 711, correção do runtime de PDF no backend, concluída.

## Status final

done

## Resultado da execucao

O serviço de geração de relatório passou a enviar `timeout: 60000` somente no `POST /reports`, permitindo que a primeira renderização do Chromium conclua sem herdar o limite global de 10 segundos. Listagem, download, compartilhamento e exclusão continuam usando o timeout padrão do cliente.

## Contexto utilizado

- `front-end/src/services/http/apiClient.ts` — confirmou o timeout global de 10 segundos.
- `front-end/src/services/reports/reportService.ts` — ponto de configuração do request de criação.
- `front-end/src/services/reports/reportService.test.ts` — cobertura da configuração específica.
- `contracts/openapi.yaml` — `POST /reports` é síncrono e responde após gerar o PDF.
- `front-end/docs/ai/QA.md` — checks locais da stack.

## Handoff

O timeout dedicado da geração PDF está definido em `REPORT_GENERATION_TIMEOUT_MS = 60000` no serviço de reports. Se a geração continuar excedendo 60 segundos em produção, o próximo contexto deve ser o tempo real do backend/Chromium e os logs do deploy, não aumentar novamente o timeout sem medir a causa.

## Arquivos alterados

- `front-end/src/services/reports/reportService.ts`
- `front-end/src/services/reports/reportService.test.ts`
- `tasks/change-requests/742-aumentar-timeout-geracao-relatorio.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-742.md`

## Validacoes executadas

- `npm run test -- --run src/services/reports/reportService.test.ts --pool=forks --maxWorkers=1` — passou (1 teste; processo levou cerca de 20s no ambiente).
- `npx eslint src/services/reports/reportService.ts src/services/reports/reportService.test.ts` — não concluiu no ambiente e foi interrompido após ausência prolongada de saída.
- `npm run build` — bloqueado por erros TypeScript preexistentes fora do escopo, em `SentenceFillPreviewModal.tsx`, `Patients`, `Plans` e `Plans/PatientTrail`.
- `git diff --check` — executar na reconciliação final.

## Pendencias pos-task

- Publicar o front-end e validar a geração em ambiente real.
- Se persistir timeout após 60 segundos, medir a duração do `POST /reports` no backend antes de qualquer novo ajuste.
