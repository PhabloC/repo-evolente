## Status

done

# Task 744 - Corrigir prebuild iOS para assets da logo

## Objetivo

Evitar a falha dos prebuilds iOS e Android ao converter assets `.webp`, preservando `logo-seal-original.webp` como fonte visual e usando uma conversão PNG equivalente nos campos nativos do Expo e OneSignal que exigem processamento.

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

- Task 743 — Corrigir ícone pequeno da notificação OneSignal — done

## Contexto mínimo

- `mobile/app.json`
- `mobile/app.config.js`
- `mobile/assets/logo-seal-original.webp`
- erro do prebuild iOS no EAS

## Contexto sob demanda

- implementação local do `expo-splash-screen` e `@expo/image-utils`: confirmar o caminho de conversão iOS.

## Orçamento de contexto

Até 5 fontes; limitar à configuração de assets nativos e validação do prebuild.

## Resultado da execução

Criado `logo-seal-original.png` por conversão direta do asset original. `icon`, adaptive icon, splash e `smallIcons` usam PNG; a propriedade raiz obsoleta `notification` foi removida conforme o Expo 57. `logo-seal-original.webp` permanece preservado como fonte original e continua sendo usado no favicon web.

## Arquivos alterados

- `mobile/app.json`
- `mobile/assets/logo-seal-original.png`
- `tasks/change-requests/744-corrigir-prebuild-ios-assets-webp.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-744.md`

## Validações executadas

- Conversão PNG preservando dimensões, pixels e transparência do WebP original.
- `npx expo prebuild --no-install --platform ios` no Windows: não gera projeto iOS por limitação da plataforma.
- Prebuilds EAS iOS e Android anteriores confirmaram que o `.webp` ainda era usado no caminho nativo de notificação.
- Novo prebuild Android local executado após a troca para PNG.

## Pendências pós-task

- Confirmar conclusão do build iOS no EAS.

## Status final

done
