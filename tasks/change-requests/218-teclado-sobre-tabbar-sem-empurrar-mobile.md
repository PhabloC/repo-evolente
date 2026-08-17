# Task 218 - Teclado sobre a tab bar sem empurrá-la

## Status

done

## Tipo

mobile

## Objetivo

Ao focar o campo de busca, o teclado deve sobrepor a tab bar, sem empurrá-la para cima.

## Resultado da execucao

- `android.softwareKeyboardLayoutMode: "pan"` no `app.json`
- Removido `KeyboardAvoidingView` da home (campo já no topo)
- Tab bar ocultada enquanto o teclado está aberto, para não ser empurrada

## Status final

done

## Nota

Em build nativo Android, `softwareKeyboardLayoutMode: "pan"` exige rebuild para aplicar no manifesto.
