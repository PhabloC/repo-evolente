# Task 025 - Relatorios de evolucao PDF/CSV e compartilhamento

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` reports

## Modo de execucao

cross-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- Historico/relatorios DS desktop.

## Contexto de negocio

### Por que

Reportar evolucao com controle de acesso.

### O que

PDF/CSV; disponibilizar ao responsavel; UI profissional.

### Comportamento esperado

- Export PDF/CSV
- Flag disponibilizado
- 403 se nao liberado

### Fora de escopo

- Editor de laudo
- Viewer mobile obrigatorio

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: profissional gera; responsavel le liberados
- Casos de erro: sem dados; falha geracao
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: periodo vazio

## Especificacao tecnica

### Deve

- LGPD por vinculo
- Auditoria disponibilizacao

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Relatorio global

## Entradas

- `requirements/002-regras-de-negocio.md`
- `requirements/003-requisitos-nao-funcionais.md`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `contracts/openapi.yaml`
- `front-end/docs/ai/`
- `backend/docs/ai/`

## Dependencias

- Task 018

## Slice vertical

### Identificador do slice

Slice 011 - Relatorios

### Arquivo do slice

- `tasks/slices/011-relatorios-evolucao.md`

### Objetivo de negócio

Relatorios.

### Entrega verificável do slice

PDF/CSV + share.

### Fora do slice

- Viewer mobile dedicado

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |
| API | `contracts/openapi.yaml` | API | sim |
| NFR | `requirements/003-requisitos-nao-funcionais.md` | LGPD/storage | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- PDF e CSV
- Disponibilizacao
- Teste 403

## Instrucoes de implementacao

- API pronta para app consumir depois

## Validacao esperada

- npm run test
- npm run lint
- npm run build

## Entregaveis esperados

- API reports + UI profissional

## Riscos ou ambiguidades

- Viewer mobile nao especificado

## Resultado da execucao

Cross-stack concluído: API `/reports` (criar PDF/CSV, listar, download, share) com 403 para responsável antes da disponibilização; auditoria `report.created` / `report.shared`; UI profissional em `/relatorios`. PDF gerado sem libs externas (sem autorização de dependência). API pronta para consumo mobile futuro.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/011-relatorios-evolucao.md`
- handoff `TASK-024`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `requirements/002` §8 + `003` exportação | regras | PDF/CSV + share |
| `design-system/front/...Desktop.md` | UI | tabela/filtros/histórico |
| `contracts/openapi.yaml` | API | paths Reports criados |
| `front-end/docs/ai/ARCHITECTURE.md` + ACCESSIBILITY | front | Page→service + a11y |
| `backend/docs/ai/ARCHITECTURE.md` | back | módulo reports |
| Trails/Patients/Admin audit existentes | integração | evolução + vínculo + audit |

### Contexto não carregado

- mobile docs/UI (viewer fora de escopo)
- design-system/mobile

## Handoff

- `.agents/state/handoffs/TASK-025.md`

## Arquivos alterados

### Backend

- `backend/src/modules/reports/**`
- `backend/src/database/migrations/1800000000000-CreateEvolutionReportsTable.ts`
- `backend/src/app.module.ts`
- `backend/src/modules/admin/admin.module.ts` (export `AdminAuditRepository`)
- `contracts/openapi.yaml` (tag/paths/schemas Reports)

### Front-end

- `front-end/src/pages/Main/Reports/**`
- `front-end/src/services/reports/reportService.ts`
- `front-end/src/types/report.ts`
- `front-end/src/utils/downloadBlob.ts`
- `front-end/src/constants/routes.ts`, `navigation.ts`
- `front-end/src/routes/index.tsx`

### Governança

- esta task, `tasks/000-index.md`, slice 011, handoff TASK-025

## Validacoes executadas

- backend: lint + tests reports + build OK
- front-end: lint + build + test OK

## Aderencia ao design system

- Lista/tabela com filtros no topo, pills de status, ações no fim
- Tom profissional (sem gamificação)
- Acessibilidade: labels em filtros, `aria-live` em erro/sucesso, `aria-busy` no loading, botões nativos

## Pendencias pos-task

- Viewer mobile dedicado (fora de escopo; API já consumível)
- PDF é texto mínimo Helvetica — enriquecer layout se houver lib autorizada no futuro

## Status final

done
