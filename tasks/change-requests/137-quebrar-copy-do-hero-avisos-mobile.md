# Task 137 - Quebrar copy do hero de avisos no mobile

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

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas + composicao local existente

### Fonte primaria visual

- hero da tela de avisos ja consolidado no slice 022

## Restricao explicita do usuario

- Colocar quebra de linha na copy da página de avisos

## Objetivo

Adicionar quebra manual na copy do hero de avisos para melhorar a composição visual.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/137-quebrar-copy-do-hero-avisos-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-136.md`

## Contexto sob demanda

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Orcamento de contexto

- ~5 fontes
- estrategia de reducao: alterar somente a copy do hero de avisos

## Criterios de aceite

- A copy do hero de avisos recebe quebra de linha controlada
- Nao ha mudanca de layout estrutural, navegacao ou comportamento

## Fora de escopo

- Refino de outras telas
- Mudanca de assets ou estilos compartilhados

## Dependencias

- Task 132
- Task 135

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- O texto do hero de avisos passou a quebrar em três linhas de forma manual, preservando a mesma mensagem

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 022 e handoff `TASK-136`
- Contexto sob demanda carregado: `ResponsavelNotificationsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-137.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `tasks/change-requests/137-quebrar-copy-do-hero-avisos-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-137.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar visual final em dispositivo fisico/Expo Go

## Status final

done
