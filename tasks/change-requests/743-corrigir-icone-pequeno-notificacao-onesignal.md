## Status

done

# Task 743 - Corrigir ícone pequeno da notificação OneSignal

## Objetivo

Usar exatamente `mobile/assets/logo-seal-original.webp`, que já possui transparência, no `notification.icon` e no `smallIcons` do OneSignal, sem modificar ou gerar uma nova logo.

## Tipo

mobile

## Stacks envolvidos

mobile (Expo/EAS)

## Perfil do projeto

stack web `front-end` (React/Vite); mobile `sim` (Expo)

## Contrato

Não aplicável.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/060-one-signal-push-mobile.md`

## Dependências

- Task 741 — Trocar logo usada na configuração do app — done

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/060-one-signal-push-mobile.md`
- `mobile/app.json`
- `mobile/app.config.js`
- `mobile/assets/logo-seal-original.webp`
- `mobile/node_modules/onesignal-expo-plugin` versão instalada

## Contexto sob demanda

- `mobile/docs/ai/QA.md`: validar a configuração Expo final.
- Documentação oficial do `onesignal-expo-plugin`: confirmar requisitos do `smallIcons`.

## Orçamento de contexto

Até 6 fontes; limitar às regras locais de QA, configuração Expo/OneSignal e assets do ícone.

## Entrega verificável

- Existe um asset dedicado ao ícone pequeno Android, com nome compatível e formato adequado.
- `smallIcons` aponta para o asset dedicado.
- A logo visual continua sendo usada nos demais pontos do aplicativo.
- A configuração Expo é carregada sem erro.

## Resultado da execução

Foi mantido o asset original `mobile/assets/logo-seal-original.webp`, sem alteração ou conversão. Tanto `notification.icon` quanto `smallIcons` do OneSignal apontam para esse arquivo.

## Contexto utilizado

Contexto mínimo da raiz, slice 060, handoff da Task 741, `mobile/app.json`, `mobile/app.config.js`, QA mobile, implementação instalada do `onesignal-expo-plugin` 2.7.1 e documentação oficial do plugin.

## Handoff

O próximo build nativo deve confirmar a renderização de `logo-seal-original.webp` nas notificações Android.

## Arquivos alterados

- `mobile/app.json`
- `tasks/change-requests/743-corrigir-icone-pequeno-notificacao-onesignal.md`
- `tasks/000-index.md`
- `tasks/slices/060-one-signal-push-mobile.md`
- `.agents/state/handoffs/TASK-743.md`

## Validações executadas

- Configuração Expo carregada com sucesso; `notification.icon` e `smallIcons` apontam para `./assets/logo-seal-original.webp`.
- `npm run lint` passou com 1 warning preexistente em `src/shared/notifications/oneSignal.ts`.
- `npm run typecheck` falhou por 15 erros preexistentes em arquivos fora do escopo da task.
- `npm run test -- --runInBand` falhou em 1 suíte preexistente (`MemoryGameRenderer`) por erro de módulo nativo `expo-audio`; 41 suítes passaram.

## Pendências pós-task

- Validar visualmente em novo build nativo Android.

## Fora de escopo

- Alterar o payload ou o comportamento de envio das notificações.
- Alterar logos de splash, autenticação ou ícone geral do aplicativo.
- Alterar configuração iOS.

## Status final

done
