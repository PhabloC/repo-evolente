# Task 085 - Exportações CSV de relatórios do master web e API

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1admin~1reports~1users~1export`
- `contracts/openapi.yaml#/paths/~1admin~1reports~1professionals~1export`
- `contracts/openapi.yaml#/paths/~1admin~1reports~1subscriptions~1export`
- `contracts/openapi.yaml#/paths/~1admin~1reports~1audit-logs~1export`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato documental + continuidade da central do master

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/src/pages/Main/AdminReports/index.tsx`

### Lacunas

- nao existe print dedicado dessa interação
- decisao: adicionar exportações reais dentro da central já estruturada, preservando a linguagem visual existente

## Objetivo

Permitir que o master baixe exportações CSV reais de relatórios administrativos próprios do seu papel, começando por usuários, vínculos profissionais, assinaturas e logs.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-084.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API admin | `contracts/openapi.yaml` | declarar os novos endpoints de exportação CSV do master | sim |
| Backend admin | `backend/src/modules/admin/{admin.controller.ts,admin.service.ts,admin.service.spec.ts}` | implementar geração e download dos CSVs | sim |
| Fontes administrativas existentes | `backend/src/modules/users/users.service.ts`, `backend/src/modules/subscriptions/entities/subscription.entity.ts` | reaproveitar dados já disponíveis para montar os relatórios | sim |
| UI do master | `front-end/src/pages/Main/AdminReports/{index.tsx,styles.module.css}` | adicionar botões reais de exportação e feedback de download | sim |
| Service web | `front-end/src/services/admin/adminService.ts`, `front-end/src/utils/downloadBlob.ts` | consumir os endpoints binários e baixar os arquivos | sim |
| Guias locais | `backend/docs/ai/AGENTS.md`, `front-end/docs/ai/{AGENTS.md,ACCESSIBILITY.md}` | garantir coerência estrutural e semântica | sim |

## Orçamento de contexto

- medio
- estrategia: limitar a primeira entrega a exportações CSV baseadas apenas em fontes administrativas já existentes; sem filtros avançados nem agregações clínicas novas

## Criterios de conclusao

- [x] backend expõe endpoints CSV do master para usuários, vínculos, assinaturas e logs
- [x] contrato OpenAPI documenta os novos endpoints
- [x] página `/admin/relatorios` possui ações reais de exportação
- [x] download dos arquivos funciona no front-end
- [x] lint/build do front-end e lint/test/build do backend aprovados

## Dependencias

- Task 043 - done
- Task 083 - done
- Task 084 - done

## Resultado da execucao

- o backend passou a expor quatro exportações CSV do master: usuários, profissionais e vínculos, assinaturas e logs de auditoria
- o contrato OpenAPI foi atualizado com os novos downloads administrativos
- a central `/admin/relatorios` ganhou botões reais de exportação, com feedback visual e download do arquivo no navegador

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-084.md`

### Sob demanda

- `contracts/openapi.yaml`
- `backend/AGENTS.md`
- `backend/docs/ai/AGENTS.md`
- `backend/src/modules/admin/{admin.controller.ts,admin.service.ts,admin.service.spec.ts}`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/subscriptions/entities/subscription.entity.ts`
- `front-end/AGENTS.md`
- `front-end/docs/ai/{AGENTS.md,ACCESSIBILITY.md}`
- `front-end/src/services/admin/adminService.ts`
- `front-end/src/pages/Main/AdminReports/{index.tsx,styles.module.css}`
- `front-end/src/types/admin.ts`
- `front-end/src/utils/downloadBlob.ts`

### Contexto evitado

- modulo clínico de relatórios do profissional, mobile e filtros avançados do admin para manter a primeira entrega concentrada em exportação CSV do que já existe

## Handoff

- `.agents/state/handoffs/TASK-085.md`

## Arquivos alterados

- `backend/src/modules/admin/admin.controller.ts`
- `backend/src/modules/admin/admin.service.ts`
- `backend/src/modules/admin/admin.service.spec.ts`
- `backend/src/modules/admin/utils/admin-report-csv.ts`
- `contracts/openapi.yaml`
- `front-end/src/pages/Main/AdminReports/index.tsx`
- `front-end/src/pages/Main/AdminReports/styles.module.css`
- `front-end/src/services/admin/adminService.ts`
- `front-end/src/types/admin.ts`
- `tasks/change-requests/085-exportacoes-csv-relatorios-master-web-e-api.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-085.md`

## Validacoes executadas

- `cd backend && npm run lint` - ok
- `cd backend && npm run test -- --runInBand` - ok
- `cd backend && npm run build` - ok
- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
