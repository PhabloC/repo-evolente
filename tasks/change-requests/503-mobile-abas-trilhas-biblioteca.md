# Task 503 - Mobile: abas Trilhas e Biblioteca na área Trilha

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

- Task 500 (sem mudança de API)

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Dependencias

- Task 502

## Objetivo

Na aba Trilha do shell, exibir sub-abas **Trilhas** e **Biblioteca**: Trilhas mostra a semana; Biblioteca lista atividades por categoria e inclui CTA para gerar trilha pela anamnese (modo dono).

## Contexto minimo

- Task 503
- slice 047
- handoff TASK-502
- `TrailTodayScreen`, `TrailLibraryScreen`

## Contexto sob demanda

- `mobile/src/features/trail/**` — UI e hooks

## Orcamento de contexto

medio

## Criterios de aceite

- [x] Sub-abas Trilhas | Biblioteca dentro da área Trilha (sem nova tab no tab bar do shell)
- [x] Aba Trilhas: visão semanal (accordion) + empty/dono
- [x] Aba Biblioteca: conteúdos agrupados por categoria
- [x] Botão gerar trilha pela anamnese na Biblioteca (quando `canManage`)
- [x] Adicionar à semana a partir da biblioteca (modo dono)

## Resultado da execucao

Sub-abas implementadas em `TrailTodayScreen`; painel `TrailLibraryPane` com categorias e CTA anamnese.

## Contexto utilizado

- Task 503, slice 047, TrailTodayScreen, hooks trail

## Handoff

- `.agents/state/handoffs/TASK-503.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`
- `mobile/src/features/trail/screens/TrailLibraryScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`

## Validacoes executadas

- lints nos arquivos alterados: ok

## Pendencias pos-task

- validar visualmente no app (reload)

## Status final

done
