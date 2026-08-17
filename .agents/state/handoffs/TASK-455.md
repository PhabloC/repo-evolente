# Handoff TASK-455

## Task

Exportações CSV laranja e PDF nos relatórios admin

## Status final

done

## Decisões preservadas

- CSV usa `Button` primary (laranja do design system)
- PDF tabular com logo centrada no mesmo chrome do PDF de evolução
- API: `GET /admin/reports/:kind/export?format=csv|pdf` (default csv)
- Render PDF compartilhado via `renderHtmlToPdf` / `resolveReportLogoDataUri`

## Arquivos alterados

- `front-end/src/pages/Main/AdminReports/*`
- `front-end/src/services/admin/adminService.ts`
- `front-end/src/types/admin.ts`
- `backend/src/modules/admin/admin.controller.ts`
- `backend/src/modules/admin/admin.service.ts`
- `backend/src/modules/admin/utils/admin-report-pdf.util.ts`
- `backend/src/modules/reports/utils/report-export.util.ts`
- `contracts/openapi.yaml`

## Validações

- front AdminReports: 3 passed
- backend admin.service + admin-report-pdf: 8 passed

## Próxima ação

- reiniciar/recarregar backend se necessário e testar download PDF em `/admin/relatorios`
