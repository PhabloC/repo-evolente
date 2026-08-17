# Handoff - Task 276

## Status

done

## Decisões

- a sombra foi separada do card clipado para evitar artefatos quadrados nas quinas inferiores
- o `trilha.webp` ficou maior e com opacidade mais alta para aparecer com mais clareza
- o ajuste continuou restrito ao card "Avisos da trilha"

## Contexto utilizado

- `tasks/change-requests/276-corrigir-bg-e-sombra-do-card-de-avisos-home-mobile.md`
- `.agents/state/handoffs/TASK-275.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`

## Arquivos alterados

- `tasks/change-requests/276-corrigir-bg-e-sombra-do-card-de-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-276.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- validação visual dependente de execução do app

## Pendencias

- revisar no device se o recorte da ilustração ficou no ponto visual esperado

## Proximo contexto recomendado

- continuar desta task se houver novos ajustes finos de crop, opacidade ou sombra nesse card
