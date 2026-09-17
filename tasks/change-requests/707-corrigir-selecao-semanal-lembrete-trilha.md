## Status

done

# Task 707 - Corrigir seleção semanal do lembrete de trilha

- **Tipo**: back
- **Stacks envolvidos**: backend (NestJS)
- **Contrato**: `contracts/openapi.yaml` — nenhum endpoint novo.
- **Modo de execução**: single-stack
- **Slice vertical**: `tasks/slices/008-trilhas-semanais-evolucao.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, este task, `daily-trail-reminder.service.ts` e repositório de trilhas.
- **Contexto sob demanda**: `backend/docs/ai/QA.md`, testes de notificações/trilhas e tipos de trail, somente para confirmar semântica de semana e criar regressão.
- **Orçamento de contexto**: até 8 fontes; carregar apenas serviço, repositório, tipos e testes relacionados ao lembrete.

## Objetivo

Garantir que o lembrete diário use somente a trilha da semana correspondente à data processada, sem reutilizar atividade de semanas anteriores.

## Critérios de aceite

- A trilha selecionada tem `weekStartDate` igual ao início da semana de `date`.
- Uma trilha ativa de semana anterior não gera lembrete na semana atual.
- Existe teste de regressão cobrindo segunda-feira e trilha anterior.
- Os demais comportamentos do cron permanecem preservados.

## Fora de escopo

- Alterar o calendário de criação ou edição de trilhas.
- Alterar o contrato de notificações.

## Resultado da execucao

O lembrete calcula o início da semana ISO iniciada na segunda-feira e seleciona a trilha ativa somente quando `weekStartDate` coincide exatamente com essa data.

## Contexto utilizado

Contexto mínimo, Slice 008, `DailyTrailReminderService`, repositório de trilhas e QA do backend.

## Handoff

Monitorar o cron em produção na virada de semana e adicionar casos de timezone se surgirem discrepâncias operacionais.

## Arquivos alterados

- `backend/src/modules/notifications/daily-trail-reminder.service.ts`
- `ajustes.md`

## Validacoes executadas

- Prettier — passou.
- `npm run lint` — passou.
- `npm run typecheck` — falhou em specs preexistentes não relacionadas.
- `npm run test -- --runInBand` — executado sem diagnóstico adicional.

## Pendencias pos-task

- Nenhuma pendência funcional conhecida.

## Status final

done
