## Status

done

# Task 740 - Corrigir apresentação do push OneSignal

## Objetivo

Fazer a notificação push do Evolente usar a logo como ícone pequeno do Android e remover a imagem grande exibida abaixo do conteúdo.

## Tipo

shared

## Stacks envolvidos

mobile (Expo/EAS), backend (NestJS)

## Perfil do projeto

stack web `front-end` (React/Vite); mobile `sim` (Expo)

## Contrato

Não aplicável; a mudança ajusta configuração nativa do OneSignal e o payload enviado ao provedor, sem endpoint público novo.

## Modo de execução

cross-stack

## Slice vertical

`tasks/slices/060-one-signal-push-mobile.md`

## Referência visual

Print enviado pelo solicitante, cobrindo o estado Android expandido da notificação de relatório. Governa o ícone à esquerda do título e a ausência de imagem grande abaixo do texto. Não cobre iOS nem estados recolhidos.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/060-one-signal-push-mobile.md`
- `mobile/app.json`, `mobile/app.config.js`
- `backend/src/patterns/adapters/onesignal-push-notification.adapter.ts`

## Contexto sob demanda

- `mobile/node_modules/onesignal-expo-plugin/README.md`: confirmar as propriedades de ícone Android suportadas pelo plugin.
- `mobile/docs/ai/QA.md` e `backend/docs/ai/QA.md`: executar as validações das duas stacks.
- teste/fixture do adapter OneSignal, se necessário, para garantir que o payload não contenha mídia.

## Orçamento de contexto

Até 8 fontes; limitar à configuração do ícone Android, payload REST do OneSignal e testes/validações diretamente relacionados.

## Critérios de aceite

- O build mobile configura um ícone de notificação do Evolente no OneSignal/Android.
- O payload backend não envia `big_picture` nem `ios_attachments` para notificações comuns.
- Dados, título, corpo e identificação do usuário permanecem inalterados.
- `npm run lint`, `npm run typecheck` e testes relevantes são executados nas stacks alteradas.

## Dependências

- Tasks 703, 705 e 714, concluídas.

## Resultado da execucao

O plugin OneSignal/Expo passou a registrar `logo-seal.png` como ícone pequeno da notificação Android, com a cor de destaque Evolente. O adapter backend deixou de enviar `big_picture` e `ios_attachments`, removendo a imagem grande do push sem alterar título, corpo, dados ou external ID.

## Contexto utilizado

Contexto mínimo da raiz, slice 060, configuração Expo, documentação do plugin OneSignal, adapter backend e QA local de mobile/backend.

## Handoff

Próximo build nativo Android deve ser instalado para confirmar a renderização do ícone no dispositivo; alterações de ícone não chegam via OTA.

## Arquivos alterados

- `mobile/app.json`
- `backend/src/patterns/adapters/onesignal-push-notification.adapter.ts`
- `backend/src/patterns/adapters/onesignal-push-notification.adapter.spec.ts`
- `tasks/000-index.md`
- `tasks/slices/060-one-signal-push-mobile.md`
- `.agents/state/handoffs/TASK-740.md`

## Validacoes executadas

- Configuração Expo development/production — passou; `notification.icon`, `smallIcons` e modo OneSignal conferidos.
- Lint focado do adapter — passou.
- Teste unitário do adapter — passou; confirma ausência de `big_picture`/`ios_attachments`.
- `git diff --check` — passou.
- `mobile npm run lint` — passou com warning preexistente em `oneSignal.ts` (`require`).
- `mobile npm run typecheck` — falhou por erros preexistentes em telas/jogos/trilha/admin.
- `mobile npm run test -- --runInBand` — 40 suites/141 testes passaram; 2 suites falharam por timeout/Expo nativo preexistente.
- `backend npm run lint` — falhou por erro preexistente em `daily-trail-reminder.service.ts`; o adapter ficou limpo no lint focado.
- `backend npm run build` — passou.

## Pendencias pos-task

- Gerar e instalar novo build nativo Android para validação visual real.
- Corrigir futuramente os erros preexistentes de typecheck/lint/teste registrados acima.

## Status final

done
