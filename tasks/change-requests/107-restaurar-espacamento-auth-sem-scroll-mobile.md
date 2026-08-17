# Task 107 - Restaurar espacamento do auth mobile sem scroll

## Status

done

## Tipo

mobile

## Objetivo

Restaurar proporções/espacamentos anteriores do login e recuperacao (sem espremer no topo e sem margem lateral), mantendo a tela sem scroll.

## Resultado

- Logo, tipografia, nuvem e inputs restaurados ao tamanho anterior
- `canvas` com `justifyContent: 'space-between'` para distribuir sem scroll
- `screenContent` full-bleed (`paddingHorizontal: 0`, `width: '100%'`)
- Sem ScrollView

## Status final

done
