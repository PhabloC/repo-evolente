# Task 247 - Fix transição edição perfil + máscara telefone

## Status

done

## Tipo

mobile

## Objetivo

Corrigir flash/travada do perfil atrás da edição e máscara de telefone.

## Resultado da execucao

- Telas de edição com fundo opaco + `contentStyle` bege (sem transparência na transição)
- `freezeOnBlur` no stack
- Navegação via `requestAnimationFrame`
- Máscara BR no telefone; envio só com dígitos

## Arquivos alterados

- `RootNavigator.tsx`
- `EditGuardianProfileScreen.tsx`
- `EditChildProfileScreen.tsx`
- `ResponsavelProfileScreen.tsx`
- `formatProfile.ts`

## Validacoes executadas

- typecheck mobile — pass

## Status final

done
