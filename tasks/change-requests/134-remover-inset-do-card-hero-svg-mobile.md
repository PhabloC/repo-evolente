# Task 134 - Remover inset do card hero com SVG nas telas mobile

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

prints de telas + assets locais

### Fonte primaria visual

- heroes mobile do responsavel com fundos SVG aplicados nas tasks 129, 132 e 133

## Restricao explicita do usuario

- As imagens ainda precisam preencher totalmente o card hero, sem inset nas bordas

## Objetivo

Remover o inset residual criado pelo `padding` do próprio card hero, movendo o espaçamento para a camada de conteúdo acima do SVG.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/134-remover-inset-do-card-hero-svg-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-133.md`

## Contexto sob demanda

- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`

## Orcamento de contexto

- ~6 fontes
- estrategia de reducao: ajustar apenas o layout do hero compartilhado por shell e trilha

## Criterios de aceite

- O fundo SVG encosta nas bordas do card hero
- O conteúdo interno mantém o mesmo respiro visual
- Nenhuma regra de negócio ou navegação é alterada

## Fora de escopo

- Alterar SVGs novamente
- Reposicionar conteúdos fora do hero

## Dependencias

- Task 133

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- O `padding` foi removido do container `heroCard` nas telas de shell e trilha
- O espaçamento interno e a altura mínima passaram para `heroContent`, preservando a leitura e liberando o fundo absoluto para preencher o card todo

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 022 e handoff `TASK-133`
- Contexto sob demanda carregado: estilos locais de shell e trail

## Handoff

- `.agents/state/handoffs/TASK-134.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`
- `tasks/change-requests/134-remover-inset-do-card-hero-svg-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-134.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar visual em dispositivo fisico/Expo Go

## Status final

done
