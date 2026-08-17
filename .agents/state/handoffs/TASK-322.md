# Handoff - Task 322

## Task

- identificador: 322
- titulo: Formatar datas do PDF em dd/mm/aaaa
- tipo: back
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao
- objetivo de negocio: padronizar a leitura de datas no PDF para o formato brasileiro
- entrega verificavel: datas exibidas no documento passam a aparecer como `dd/mm/aaaa`

## Decisoes preservadas

- a mudança ficou restrita ao render do PDF, sem alterar CSV nem contrato
- a normalização de datas foi aplicada no template HTML do PDF, cobrindo campos isolados e datas dentro de textos
- o padrão trata tanto `YYYY-MM-DD` quanto timestamps ISO, sempre convertendo para `dd/mm/aaaa`

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/322-formatar-datas-do-pdf-em-dd-mm-aaaa.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-321.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `backend/src/modules/reports/utils/report-export.util.ts` | render do PDF | aplicar normalização de datas |
| `backend/src/modules/reports/utils/report-export.util.spec.ts` | cobertura | validar o novo formato no HTML do PDF |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `front-end/` | ajuste exclusivo da apresentação no PDF do backend |

## Resultado por stack

- backend: datas do PDF formatadas em `dd/mm/aaaa`
- front-end: sem alterações
- mobile: sem alterações

## Arquivos alterados

- `backend/src/modules/reports/utils/report-export.util.ts`
- `backend/src/modules/reports/utils/report-export.util.spec.ts`
- `tasks/change-requests/322-formatar-datas-do-pdf-em-dd-mm-aaaa.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd backend && npm run test -- --runInBand src/modules/reports/utils/report-export.util.spec.ts src/modules/reports/reports.service.spec.ts`: ok
- `cd backend && npm run build`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- só revisitar se surgir regra para horário local junto da data, por exemplo `dd/mm/aaaa HH:mm`

## Proximo contexto recomendado

- `backend/src/modules/reports/utils/report-export.util.ts`
