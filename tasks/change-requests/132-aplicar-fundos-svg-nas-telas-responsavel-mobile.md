# Task 132 - Aplicar fundos SVG nas telas de atividades, perfil e avisos do responsavel mobile

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

- `design-system/mobile/prints/home-responsavel-referencia.png`
- `mobile/assets/svg/fundo_trilha_livro.svg`
- `mobile/assets/svg/fundo_perfil.svg`
- `mobile/assets/svg/fundo_balao_fala.svg`

## Restricao explicita do usuario

- Usar `fundo_trilha_livro.svg` como background da pagina de atividades
- Usar `fundo_perfil.svg` como background da pagina de perfil
- Usar `fundo_balao_fala.svg` como background da pagina de avisos

## Objetivo

Trocar os fundos decorativos manuais dos heroes de atividades, perfil e avisos pelos SVGs especificados, preservando copy, CTA e comportamento atual.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/132-aplicar-fundos-svg-nas-telas-responsavel-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-131.md`

## Contexto sob demanda

- `mobile/assets/svg/fundo_trilha_livro.svg`
- `mobile/assets/svg/fundo_perfil.svg`
- `mobile/assets/svg/fundo_balao_fala.svg`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`

## Orcamento de contexto

- ~10 fontes
- estrategia de reducao: limitar a mudanca aos heroes das telas alvo e aos assets de fundo

## Criterios de aceite

- Perfil usa `fundo_perfil.svg` no hero
- Avisos usa `fundo_balao_fala.svg` no hero
- Atividades usa `fundo_trilha_livro.svg` no hero da lista e do detalhe
- Copy, CTA, navegacao e regras de negocio permanecem inalterados

## Fora de escopo

- Refino de copy
- Alteracoes na home, tab bar, queries, services ou contrato
- Reescrita global dos imports ou dos estilos das telas

## Dependencias

- Task 128
- Task 129
- Task 131

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Os heroes de perfil, avisos e atividades passaram a renderizar os SVGs especificados via `SvgUri`
- O conteudo de cada hero foi encapsulado em uma camada dedicada acima do background para preservar legibilidade e interacao
- As formas circulares decorativas antigas foram removidas dos estilos compartilhados dessas telas

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 022 e handoff `TASK-131`
- Contexto sob demanda carregado: assets SVG especificados, telas alvo e estilos locais de shell/trail

## Handoff

- `.agents/state/handoffs/TASK-132.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/styles.ts`
- `tasks/change-requests/132-aplicar-fundos-svg-nas-telas-responsavel-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-132.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar visual em dispositivo fisico/Expo Go para calibrar enquadramento final de cada asset

## Status final

done
