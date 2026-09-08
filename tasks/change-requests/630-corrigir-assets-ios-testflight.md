# Task 630 - Corrigir assets iOS para TestFlight

## Status

blocked

## Tipo

mobile

## Stacks envolvidos

- mobile (Expo / React Native)

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim

## Contrato

Não aplicável; não há integração cliente-servidor.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/056-build-ios-testflight.md`

## Objetivo

Substituir os assets WebP usados como ícone e splash por PNG compatível com o prebuild iOS do Expo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/056-build-ios-testflight.md`

## Contexto sob demanda

- `mobile/app.json` e `mobile/assets/logo-seal.webp`: localizar as referências incompatíveis e gerar o PNG equivalente.
- `mobile/docs/ai/AGENTS.md`: validar a configuração local Expo.

## Orçamento de contexto

Baixo (até 8 fontes). Estratégia: limitar a alteração aos assets e à configuração de build, sem carregar requisitos, design system ou contrato.

## Critérios de aceite

- [ ] O ícone e a splash configurados no Expo usam PNG.
- [ ] `npx expo prebuild --no-install --platform ios` conclui sem erro de MIME WebP.
- [ ] Uma nova build iOS de produção é iniciada no EAS.

## Dependências

- Slice 055 — concluído.

## Resultado da execucao

- Convertido `mobile/assets/logo-seal.webp` para `mobile/assets/logo-seal.png` (1024×1024).
- Atualizadas as referências de ícone, splash e adaptive icon no `mobile/app.json`.
- A build iOS de produção 1.0.0 (3) concluiu com sucesso no EAS.
- Após a configuração da API pública no EAS, foi iniciada a build iOS 1.0.0 (4), que confirmou o carregamento de `EXPO_PUBLIC_API_URL`.
- O envio ao TestFlight requer login Apple interativo no terminal local; a automação não pode receber senha ou código 2FA.

## Contexto utilizado

- `mobile/app.json`, `mobile/assets/logo-seal.webp`, `mobile/docs/ai/AGENTS.md` e logs da build EAS.

## Handoff

- `.agents/state/handoffs/TASK-630.md`

## Arquivos alterados

- `mobile/assets/logo-seal.png`
- `mobile/app.json`
- `mobile/eas.json`
- `tasks/slices/056-build-ios-testflight.md`
- `tasks/change-requests/630-corrigir-assets-ios-testflight.md`
- `tasks/000-index.md`

## Validacoes executadas

- Build EAS iOS 1.0.0 (3): concluída com sucesso.
- Build EAS iOS 1.0.0 (4): iniciada em `13d785bf-4269-489d-80bf-62dd68597e61` com ambiente `production`.
- Prebuild local iOS: indisponível no Windows; a validação ocorreu no macOS do EAS.

## Pendencias pos-task

- No terminal local, enviar a build EAS `81281959-e5d2-4746-9efd-2bf7c48b839c` ao App Store Connect, autenticando com Apple ID e 2FA.

## Status final

blocked
