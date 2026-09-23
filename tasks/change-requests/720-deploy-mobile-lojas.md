## Status

in_progress

# Task 720 - Fazer deploy Android e iOS do mobile

- **Tipo**: mobile
- **Stacks envolvidos**: mobile (Expo/EAS)
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; operação de build/submissão.
- **Modo de execução**: single-stack
- **Slice vertical**: `tasks/slices/061-deploy-lojas-mobile.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task.
- **Contexto sob demanda**: `mobile/app.json`, `mobile/app.config.js`, `mobile/eas.json`, `mobile/docs/ai/QA.md` e estado de builds/credenciais EAS, somente para validar e executar a distribuição.
- **Orçamento de contexto**: até 8 fontes; limitar a configuração EAS, validações mobile e submissão às lojas.

## Objetivo

Gerar e distribuir a versão de produção do app Evolente para Android e iOS.

## Critérios de aceite

- [ ] Validações locais mínimas do mobile executadas.
- [ ] Build Android de produção concluída no EAS.
- [ ] Build iOS de produção concluída no EAS.
- [ ] Android submetido ao teste interno da Google Play, se a conta/credencial estiver disponível.
- [ ] iOS submetido ao App Store Connect/TestFlight, se a conta/credencial estiver disponível.
- [ ] Bloqueios externos registrados com identificador/link da build e próximo passo.

## Dependências

- Tasks 630, 632, 705 e 714 concluídas ou com pendências de distribuição registradas.

## Status final

blocked

## Resultado da execucao

As builds de produção já existentes foram identificadas no EAS e estão concluídas para a versão 1.0.1: Android build 13 (`3adcf8fe-8905-476b-bcd0-0da86dbecd67`) e iOS build 12 (`6aa1a823-f671-4c2d-823f-e3baa88aae89`). A tentativa de submissão foi bloqueada por configuração externa de lojas.

## Contexto utilizado

- Contexto mínimo da raiz, Slice 061 e esta task.
- `mobile/app.json`, `mobile/app.config.js` e `mobile/eas.json`.
- Sessão EAS autenticada e lista de builds do projeto `0abcf4a5-f7d4-4ae3-8749-96de08c374e6`.
- `mobile/docs/ai/QA.md` não foi necessário para ampliar o escopo; as validações locais do pacote foram executadas.

## Handoff

As builds de loja estão prontas no EAS. Para concluir: configurar a Google Service Account no EAS e submeter o Android build 13; definir `ascAppId` no perfil `submit.production` ou executar a submissão iOS interativa com Apple ID/2FA e enviar o iOS build 12 ao TestFlight.

## Arquivos alterados

- `tasks/slices/061-deploy-lojas-mobile.md`
- `tasks/change-requests/720-deploy-mobile-lojas.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/720-deploy-mobile-lojas.md`

## Validacoes executadas

- `npm run lint` — passou com 1 warning preexistente em `oneSignal.ts`.
- `npm run typecheck` — falhou em erros preexistentes de admin, auth, jogos e trilhas.
- `npm run test -- --runInBand` — 40 suítes passaram e 1 falhou por incompatibilidade de mock/runtime de `expo-audio` em `MemoryGameRenderer`.
- `eas whoami` — autenticado como `phabloc`.
- `eas build:list` — confirmou builds de produção concluídas: Android 1.0.1 (13) e iOS 1.0.1 (12).
- `eas submit --platform android --id 3adcf8fe-8905-476b-bcd0-0da86dbecd67 --non-interactive --wait` — bloqueado: Google Service Account não configurada.
- `eas submit --platform ios --id 6aa1a823-f671-4c2d-823f-e3baa88aae89 --non-interactive --wait` — bloqueado: `ascAppId` ausente no perfil de submissão.
- `eas submit --platform ios --id 6aa1a823-f671-4c2d-823f-e3baa88aae89` — iniciou fluxo interativo e aguardou Apple ID; cancelado antes da autenticação para não usar a conta sugerida sem confirmação.

## Pendencias pos-task

- Configurar a credencial da Google Play no EAS e reenviar a build Android 13.
- Informar o App Store Connect App ID (`ascAppId`) no `submit.production` ou fazer submissão iOS interativa com Apple ID/2FA.


