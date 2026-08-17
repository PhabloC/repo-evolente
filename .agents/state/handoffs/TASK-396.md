# Handoff - Task 396

## Task

- identificador: 396
- tipo: back
- status final: done

## Slice vertical

- Slice 011 - Relatorios de evolucao

## Decisões preservadas

- O denominador de adesão considera cada atividade pela data planejada.
- Data planejada = `weekStartDate + weekday - 1`.
- Datas civis são comparadas como `YYYY-MM-DD`, evitando efeitos de fuso.
- Trocar o filtro semanal por item não altera contrato nem persistência.

## Contexto utilizado

- serviço e spec de relatórios
- utilitário de semana das trilhas
- guias locais de backend

## Arquivos alterados

- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- task, slice, índice e handoff

## Validações

- 87 testes unitários passaram
- 1 teste e2e passou
- build passou
- lint dos arquivos alterados passou
- lint global segue bloqueado por passivo preexistente

## Pendências

- passivo global de lint fora do escopo

## Próximo contexto recomendado

- nenhum; correção localizada concluída
