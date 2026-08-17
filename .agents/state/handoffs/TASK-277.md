# Handoff - Task 277

## Status

done

## Decisões

- o `trilha.webp` passou a preencher todo o card sem fade
- o fundo foi forçado com `width` e `height` em `100%`
- o `resizeMode` foi trocado para `stretch` para privilegiar presença visual total

## Contexto utilizado

- `tasks/change-requests/277-forcar-trilha-webp-100-porcento-no-bg-do-card-de-avisos-home-mobile.md`
- `.agents/state/handoffs/TASK-276.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`

## Arquivos alterados

- `tasks/change-requests/277-forcar-trilha-webp-100-porcento-no-bg-do-card-de-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-277.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- validação visual dependente de execução do app

## Pendencias

- revisar no app se vale voltar de `stretch` para outro modo após confirmar a presença do asset

## Proximo contexto recomendado

- continuar desta task se houver ajuste fino final de crop ou distorção da ilustração
