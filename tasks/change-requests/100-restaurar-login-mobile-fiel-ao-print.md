# Task 100 - Restaurar login mobile fiel ao print original

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas

### Fonte primaria visual

- `design-system/mobile/prints/login-mobile.png`
- `mobile/assets/girl.png`
- `mobile/assets/nuvem_evolente_mobile_svg.svg`
- `mobile/assets/logo-completa.webp`

### Regra de aderencia

- Fidelidade ao print original
- Sem cadastro
- Sem emoji na saudacao
- Menina com corpo atras da nuvem
- Lucide nos icones de campo

## Objetivo

Corrigir o regresso visual do login e restaurar a composicao do print, com stacking estavel da menina atras da nuvem.

## Escopo

- Reestruturar camadas (decoracoes < menina < nuvem+form < header)
- Restaurar paths do SVG oficial da nuvem
- Realinhar logo, copy, girl, form e shapes top/bottom
- Validar lint/typecheck

## Dependencias

- Task 099 — done

## Criterios de conclusao

- [x] layout coerente com o print (sem cadastro)
- [x] menina atras da nuvem
- [x] form completo sem corte
- [x] lint/typecheck ok

## Resultado da execucao

### Resumo por stack

- **mobile**: login reconstruido com camadas estaveis (`layerGirl` < `layerBody`/`cloudPanel` < `layerHeader`); SVG oficial da nuvem restaurado; cobertura opaca sob a onda para web; sem cadastro e sem emoji.

### Decisões técnicas

- Header absoluto separado para nao elevar a menina junto com o texto.
- Paths de `nuvem_evolente_mobile_svg.svg` restaurados no `SignInCloud`.
- `cloudOpaqueCover` evita a menina “vazar” por cima do painel no Expo web.

## Handoff

- `.agents/state/handoffs/TASK-100.md`

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInCloud.tsx`
- `mobile/src/features/auth/components/SignInCloud.styles.ts`
- `tasks/change-requests/100-restaurar-login-mobile-fiel-ao-print.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-100.md`

## Validacoes executadas

- lint ok
- typecheck ok

## Pendencias pos-task

- Validacao visual humana no Expo web

## Status final

done
