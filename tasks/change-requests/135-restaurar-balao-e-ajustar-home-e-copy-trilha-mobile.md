# Task 135 - Restaurar balão e ajustar home e copy da trilha mobile

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

- `mobile/assets/svg/fundo_balao_fala.svg`
- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/assets/svg/fundo_trilha_livro.svg`

## Restricao explicita do usuario

- O balão não deveria ficar preto
- A imagem da home ainda está com padding nas laterais
- O texto da trilha precisa mudar e quebrar para não ficar em cima do livro

## Objetivo

Restaurar a cor do balão de avisos, expandir o fundo da home para largura total real e ajustar a copy da trilha com quebra controlada para evitar colisão com a ilustração.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/135-restaurar-balao-e-ajustar-home-e-copy-trilha-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-134.md`

## Contexto sob demanda

- `mobile/assets/svg/fundo_balao_fala.svg`
- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`

## Orcamento de contexto

- ~8 fontes
- estrategia de reducao: ajustar apenas os assets e a copy/estilo local da trilha

## Criterios de aceite

- O balão de avisos volta à cor original prevista no SVG
- O fundo da home ocupa a largura total do hero sem inset lateral
- O texto da trilha não sobrepõe o livro e tem quebra controlada

## Fora de escopo

- Mudar navegação, CTA ou comportamento
- Reestruturar outras telas do responsável

## Dependencias

- Task 129
- Task 133
- Task 134

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- O gradiente `speech-fill` do balão foi restaurado no SVG de avisos, removendo o preenchimento preto
- O fundo da home com estrelinha foi expandido para o canvas completo, eliminando o inset lateral residual
- A copy do hero da trilha foi encurtada e quebrada em duas linhas, com largura máxima controlada para não invadir o livro

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 022 e handoff `TASK-134`
- Contexto sob demanda carregado: SVGs de home/avisos e arquivos da tela de trilha

## Handoff

- `.agents/state/handoffs/TASK-135.md`

## Arquivos alterados

- `mobile/assets/svg/fundo_balao_fala.svg`
- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `tasks/change-requests/135-restaurar-balao-e-ajustar-home-e-copy-trilha-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-135.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar visual final em dispositivo fisico/Expo Go

## Status final

done
