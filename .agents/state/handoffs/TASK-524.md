# Handoff — Task 524

## Identificador

TASK-524

## Título

Jogo dos erros mobile: aspect ratio 4/3

## Slice vertical

`tasks/slices/035-jogo-dos-erros.md`

## Status final

done

## Decisões preservadas

- Runtime mobile do Spot Difference usa `aspectRatio: 4 / 3` (igual ao modal web da Task 516), não quadrado 1:1
- `resizeMode="cover"` no `Image` para preencher o painel sem letterboxing

## Contexto mínimo lido

- backlog + slice 035 + esta task

## Contexto sob demanda carregado

- `SpotDifferenceGameRenderer` (index + styles)
- critério visual da Task 516 (front)

## Arquivos alterados

- `mobile/src/features/games/components/SpotDifferenceGameRenderer/styles.ts`
- `mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx`

## Validações executadas

- revisão estática do aspect ratio e resizeMode

## Pendências

- smoke visual no Expo com o jogo aberto

## Próxima ação sugerida

- Abrir uma rodada no app e confirmar que as duas imagens mostram a cena completa sem corte

## Próximo contexto recomendado

- apenas o renderer mobile se houver ajuste fino de layout

## Contexto que não deve ser carregado

- assets S3, bootstrap, hotspots, front-end Library CSS (já alinhado)
