# Task 455 - Exportações CSV laranja e PDF nos relatórios admin

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Contrato

- `contracts/openapi.yaml` — query `format=csv|pdf` nos endpoints `/admin/reports/*/export`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/slices/025-hardening-exportacoes-admin-backend.md`

## Objetivo

Na pagina `/admin/relatorios`, deixar o botao CSV laranja e permitir exportar PDF com o mesmo cabecalho visual do relatorio do profissional (logo Evolente no topo).

## Criterios de conclusao

- [x] botao Exportar CSV usa visual laranja (primary)
- [x] botao Exportar PDF por tipo de relatorio
- [x] PDF admin reutiliza logo/topo no padrao do PDF de evolucao
- [x] API aceita format csv/pdf
- [x] openapi e testes atualizados

## Entrega

- Front: CSV `variant="primary"` (laranja) + PDF secundário
- Backend: `buildAdminTabularPdf` reusa `resolveReportLogoDataUri` + `renderHtmlToPdf`
- Query `?format=pdf|csv` (default csv)
