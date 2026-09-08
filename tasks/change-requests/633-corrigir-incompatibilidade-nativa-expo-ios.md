# Task 633 - Corrigir incompatibilidade nativa Expo no iOS

## Status

in_progress

## Tipo

mobile

## Stacks envolvidos

- mobile (Expo / React Native)

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim

## Contrato

Não aplicável; não há alteração de integração cliente-servidor.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/059-estabilidade-nativa-expo-ios.md`

## Objetivo

Alinhar as dependências nativas do Expo que causam crash no lançamento iOS e iniciar novas builds de loja corrigidas.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/059-estabilidade-nativa-expo-ios.md`

## Contexto sob demanda

- `errors_testflight/crashlog.crash`: causa do crash em `ExpoVideo`/`ExpoModulesCore`.
- `mobile/package.json` e lockfile: versões compatíveis pelo Expo CLI.
- `mobile/app.json`: avisos de configuração do Expo Doctor.
- `mobile/docs/ai/QA.md`: comandos de validação.

## Orçamento de contexto

Baixo (até 8 fontes). Estratégia: limitar a mudança ao alinhamento automático do SDK 57, peer dependency de áudio e configurações apontadas pelo diagnóstico.

## Critérios de aceite

- [ ] O Expo Doctor não aponta dependências Expo incompatíveis nem peer dependency nativa faltante.
- [ ] `expo-video` e `expo-modules-core` ficam alinhados ao SDK 57.
- [ ] Novas builds Android e iOS de loja são iniciadas após a correção.

## Dependências

- Slice 057 — concluído; a URL pública da API permanece no ambiente EAS de produção.
