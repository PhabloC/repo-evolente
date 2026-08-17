# Task 245 - Overlay liquid glass sobre as bolhas do fundo mobile

## Status

done

## Tipo

mobile

## Objetivo

Camada liquid glass (blur + tint) por cima das bolhas.

## Resultado da execucao

- `expo-blur` instalado
- `AppBackgroundLiquidGlass` no `AppGate`, acima das bolhas e abaixo do conteúdo
- Opacidade das bolhas ajustada para permanecerem visíveis sob o vidro

## Arquivos alterados

- `mobile/src/shared/components/AppBackgroundLiquidGlass/index.tsx`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/shared/components/AppBackgroundBubbles/index.tsx`
- `mobile/package.json`

## Validacoes executadas

- `npm run typecheck` — pass

## Status final

done
