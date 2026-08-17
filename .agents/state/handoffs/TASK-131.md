# Handoff - Task 131

## Identificador

- Task 131 - Remover folga do SVG no hero da home mobile
- `tasks/change-requests/131-remover-folga-do-svg-no-hero-home-mobile.md`

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Status final

done

## Decisoes preservadas

- A folga visual foi tratada no proprio asset SVG e no modo de encaixe do `SvgUri`
- Copy, CTA e comportamento do hero nao foram alterados

## Contexto efetivamente usado

- Task 131, slice 022, handoff `TASK-129`, `mobile/assets/svg/fundo_estrelinha.svg` e `HomeHeroBanner`

## Arquivos alterados

- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok (11 suites, 22 testes)

## Pendencias

- Validar o enquadramento final em dispositivo fisico/Expo Go

## Proximo contexto recomendado

- `mobile/src/features/shell/components/HomeHeroBanner/`
