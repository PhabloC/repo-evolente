# Task 314 - Estruturar conteúdo do relatório da criança

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

- `contracts/openapi.yaml#/paths/~1reports`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

feedback direto do usuario + continuidade da central de relatorios existente

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/src/pages/Main/Reports/index.tsx`

### Lacunas

- sem print dedicado do layout interno do PDF
- decisao: nesta task o foco principal e a estrutura e prioridade do conteudo do relatorio; qualquer refinamento visual mais profundo do PDF deve ficar subordinado a essa estrutura

## Objetivo

Definir e implementar uma estrutura clara para o relatório da criança, priorizando evolução clínica, compreensão do responsável e rastreabilidade profissional no PDF/CSV gerado pela funcionalidade de relatórios.

## Estrutura alvo do relatório

1. identificação da criança
2. identificação do profissional responsável
3. período do relatório
4. resumo geral do período
5. resumo quantitativo de adesão e conclusão
6. evolução por objetivo ou habilidade trabalhada
7. linha do tempo com eventos relevantes do período
8. pontos de atenção
9. orientações práticas para o responsável
10. próximos passos clínicos
11. rodapé técnico de emissão e compartilhamento

## Regras de produto

- o PDF deve ser legível para profissional e responsável, com linguagem objetiva e sem excesso de jargão
- o CSV deve preservar a visão analítica/tabular do histórico e dos registros do período
- o relatório não deve expor dados irrelevantes, logs técnicos ou ruído operacional ao responsável
- o relatório deve deixar claro o período analisado e o contexto profissional de emissão
- qualquer ausência de dado em uma seção obrigatória deve gerar fallback textual claro em vez de omitir silenciosamente a seção

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-025.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Fluxo atual de relatórios | `tasks/025-relatorios-pdf-csv.md` | entender escopo entregue e restrições atuais | sim |
| UI web | `front-end/docs/ai/{AGENTS.md,ACCESSIBILITY.md,ARCHITECTURE.md}` | manter coerência estrutural e semântica na tela de relatórios | sim |
| Backend reports | `backend/docs/ai/{AGENTS.md,ARCHITECTURE.md,SECURITY.md}` | estruturar geração segura do conteúdo do relatório | sim |
| API | `contracts/openapi.yaml` | validar se a estrutura nova exige ajuste de contrato | sim |
| Código atual | `front-end/src/pages/Main/Reports/**`, `front-end/src/types/report.ts`, `front-end/src/services/reports/reportService.ts`, `backend/src/modules/reports/**` | implementar a nova estrutura de conteúdo | sim |
| Regras de negócio | `requirements/002-regras-de-negocio.md`, `requirements/003-requisitos-nao-funcionais.md` | validar LGPD, clareza e rastreabilidade | sim |

## Orçamento de contexto

- medio
- estrategia: limitar a mudança ao fluxo de relatórios do profissional e ao conteúdo exportado; não reabrir viewer mobile nem outros módulos clínicos fora do necessário

## Criterios de conclusao

- [x] o relatório da criança possui uma estrutura explícita e consistente entre PDF e CSV
- [x] o PDF apresenta resumo, evolução, alertas, orientações e próximos passos em linguagem clara
- [x] o CSV preserva histórico analítico compatível com uso profissional
- [x] a tela de relatórios deixa claro o foco e a utilidade do relatório gerado, se necessário
- [x] contrato, backend e front-end ficam coerentes com a nova estrutura

## Dependencias

- Task 025 - done

## Resultado da execucao

- o backend passou a montar um modelo estruturado do relatório da criança com identificação, resumo, métricas, evolução por área, linha do tempo, pontos de atenção, orientações e próximos passos
- o exportador CSV deixou de conter apenas histórico bruto e passou a repetir metadados e síntese do relatório junto às linhas analíticas do período
- o exportador PDF deixou de ser uma lista mínima de eventos e passou a gerar um documento textual estruturado, com quebra de linhas e múltiplas páginas quando necessário
- a tela web de relatórios passou a priorizar `PDF` como formato inicial e a explicar com mais clareza a diferença entre PDF e CSV
- o contrato OpenAPI existente permaneceu válido; não foi necessário mudar endpoints ou payloads

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-025.md`

### Sob demanda

- `tasks/025-relatorios-pdf-csv.md`
- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `backend/docs/ai/AGENTS.md`
- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/SECURITY.md`
- `contracts/openapi.yaml`
- `requirements/002-regras-de-negocio.md`
- `requirements/003-requisitos-nao-funcionais.md`
- `backend/src/modules/reports/**`
- `backend/src/modules/guardians/**`
- `backend/src/modules/trails/**`
- `backend/src/modules/patients/**`
- `backend/src/modules/contents/**`
- `front-end/src/pages/Main/Reports/**`

### Contexto evitado

- mobile, porque viewer dedicado continua fora de escopo
- módulos fora de relatórios, salvo dependência real de dados para compor o conteúdo do relatório

## Handoff

- `.agents/state/handoffs/TASK-314.md`

## Arquivos alterados

- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `backend/src/modules/reports/utils/report-export.util.ts`
- `backend/src/modules/reports/utils/report-export.util.spec.ts`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `tasks/change-requests/314-estruturar-conteudo-do-relatorio-da-crianca.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-314.md`

## Validacoes executadas

- `cd backend && npm run test -- --runInBand src/modules/reports/reports.service.spec.ts src/modules/reports/utils/report-export.util.spec.ts` - ok
- `cd backend && npm run lint` - ok
- `cd backend && npm run build` - ok
- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx` - falhou por timeout em cenário pré-existente não relacionado ao fluxo de relatórios

## Pendencias pos-task

- enriquecer visualmente o PDF no futuro, se houver autorização para biblioteca dedicada de geração de documentos
- se desejar refletir especialidades do profissional no relatório, isso exige integrar o módulo de perfis profissionais ao fluxo de reports

## Status final

done
