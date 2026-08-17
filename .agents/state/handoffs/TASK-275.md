# Handoff - Task 275

## Status

done

## Decisões

- a imagem de fundo saiu de uma `Image` solta para uma camada absoluta dedicada
- o asset ficou maior e com `resizeMode="contain"` para aumentar a chance de leitura visual
- o conteúdo do card foi trazido explicitamente para frente com `zIndex`

## Contexto utilizado

- `tasks/change-requests/275-corrigir-renderizacao-do-bg-trilha-no-card-de-avisos-home-mobile.md`
- `.agents/state/handoffs/TASK-274.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/assets/trilha.webp`

## Arquivos alterados

- `tasks/change-requests/275-corrigir-renderizacao-do-bg-trilha-no-card-de-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-275.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`

## Validacoes executadas

- validação visual dependente de execução do app

## Pendencias

- ajustar opacidade/posição se a leitura no device ainda ficar discreta demais

## Proximo contexto recomendado

- partir desta task se houver novos ajustes finos de composição do card "Avisos da trilha"
