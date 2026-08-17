# Task 321 - Migrar geração de PDF para Puppeteer com layout personalizado

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

- nao se aplica; o endpoint de download permanece o mesmo

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- feedback direto do usuario + asset local da marca

### Fonte primaria visual

- `backend/src/modules/reports/**`
- `front-end/src/assets/logo-completa.webp`

### Lacunas

- sem print do PDF final; o layout deve priorizar leitura estruturada, tabela separada para os dados e logo centralizada no topo quando o asset estiver acessível

## Objetivo

Substituir o gerador textual atual de PDF por uma geração com `puppeteer`, produzindo um PDF personalizado com layout estruturado em tabela e logo da Evolente no topo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-320.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Arquitetura backend | `backend/docs/ai/{ARCHITECTURE.md,SECURITY.md}` | manter a troca isolada no módulo `reports` | sim |
| Dependências backend | `backend/package.json` | adicionar `puppeteer` ao projeto | sim |
| Export util | `backend/src/modules/reports/utils/report-export.util.ts` | migrar a geração do PDF para HTML + Puppeteer | sim |
| Serviço de reports | `backend/src/modules/reports/reports.service.ts` | adaptar o fluxo assíncrono da geração do PDF | sim |
| Testes de reports | `backend/src/modules/reports/{utils/report-export.util.spec.ts,reports.service.spec.ts}` | ajustar cobertura do novo gerador | sim |
| Asset da marca | `front-end/src/assets/logo-completa.webp` | incluir a logo no topo do PDF, se o arquivo puder ser lido | sim |

## Orçamento de contexto

- medio
- estrategia: limitar a mudança ao módulo `reports`, à nova dependência e ao asset de logo já existente no repositório

## Criterios de conclusao

- [x] o PDF passa a ser gerado com `puppeteer`
- [x] o documento contém layout estruturado com tabela de informações separadas
- [x] a logo da Evolente aparece centralizada no topo quando o asset local estiver disponível
- [x] o fluxo de criação e download de relatórios continua funcional

## Dependencias

- Task 320 - done

## Resultado da execucao

- o backend passou a gerar PDFs com `puppeteer`, usando um template HTML estruturado em seções e tabelas
- a logo da Evolente foi integrada de forma opcional no topo do documento a partir de `front-end/src/assets/logo-completa.webp`
- o fluxo de criação/download de relatórios permaneceu no mesmo endpoint e foi validado por testes, build e smoke test real do PDF

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-320.md`

### Sob demanda

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/SECURITY.md`
- `backend/package.json`
- `backend/package-lock.json`
- `backend/src/modules/reports/utils/report-export.util.ts`
- `backend/src/modules/reports/utils/report-export.util.spec.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `front-end/src/assets/logo-completa.webp`

### Contexto evitado

- `front-end/src/pages`, porque a mudança não altera a interface web nem o contrato

## Handoff

- `.agents/state/handoffs/TASK-321.md`

## Arquivos alterados

- `backend/package.json`
- `backend/package-lock.json`
- `backend/src/modules/reports/utils/report-export.util.ts`
- `backend/src/modules/reports/utils/report-export.util.spec.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `tasks/change-requests/321-migrar-geracao-de-pdf-para-puppeteer-com-layout-personalizado.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-321.md`

## Validacoes executadas

- `cd backend && npm run test -- --runInBand src/modules/reports/utils/report-export.util.spec.ts src/modules/reports/reports.service.spec.ts`
- `cd backend && npm run build`
- `cd backend && node -e "const { buildEvolutionPdf } = require('./dist/modules/reports/utils/report-export.util'); ..."` - smoke test real do `puppeteer` com retorno `{"startsWithPdf":true,"size":294377}`

## Pendencias pos-task

- nenhuma

## Status final

done
