# Task 505 - Mobile: refinar UI da aba Biblioteca da trilha

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

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Dependencias

- Task 504

## Objetivo

Melhorar o design da aba Biblioteca: CTA anamnese, categorias, cards de conteúdo e seleção de dias.

## Contexto minimo

- Task 505
- `TrailLibraryPane.tsx`, `styles.ts` trail

## Contexto sob demanda

- tokens e componentes compartilhados (IconPill, Button)

## Orcamento de contexto

baixo

## Criterios de aceite

- [x] Hierarquia visual clara (CTA, categorias, cards)
- [x] Cards e chips de dia mais legíveis e consistentes com a trilha

## Resultado da execucao

Biblioteca com card de suggest, categorias com contador, cards com IconPill/mídia, composer de dias em chips.

## Contexto utilizado

- TrailLibraryPane, styles, IconPill

## Handoff

- `.agents/state/handoffs/TASK-505.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`
- `mobile/src/features/trail/screens/styles.ts`

## Validacoes executadas

- lints

## Pendencias pos-task

- nenhuma

## Status final

done
