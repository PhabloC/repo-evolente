# Handoff - Task 147

## Identificador

- Task 147 - Tentar ocultar barra de navegacao nativa no Android mobile
- `tasks/change-requests/147-tentar-ocultar-barra-de-navegacao-nativa-no-android-mobile.md`

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Status final

done

## Decisoes preservadas

- A tentativa de ocultacao foi centralizada no provider global do app e limitada ao Android
- O app reaplica `hidden` quando o sistema reporta a barra como visivel novamente
- A limitacao nativa permanece: alguns devices ou o Expo Go podem reexibir a barra

## Arquivos alterados

- `mobile/package.json`
- `mobile/src/app/providers/AppProviders.tsx`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
