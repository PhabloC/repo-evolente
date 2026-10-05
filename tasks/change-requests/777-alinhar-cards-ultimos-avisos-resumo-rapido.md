# Task 777 - Alinhar cards de Últimos avisos ao Resumo rápido

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

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- cards `HomeActionCard` clay já usados em "Resumo rápido" na mesma tela

### Regra de aderencia visual

- Últimos avisos usam o mesmo padrão clay do Resumo rápido

## Origem da solicitacao

Pedido do usuário: na tela de Avisos, os cards de "Últimos avisos" devem ter o mesmo design dos cards de "Resumo rápido".

## Objetivo

Substituir os cards customizados da lista de avisos por `HomeActionCard` clay.

## Escopo

- Itens de Últimos avisos com `HomeActionCard`
- Remover imports órfãos (`Image`, `IconPill`)

## Fora de escopo

- Alterar Resumo rápido / empty state
- Backend
- Limpeza de estilos órfãos em `styles.ts`

## Slice vertical

- Slice 010 - `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Criterios de conclusao

- [x] Últimos avisos usam `HomeActionCard` clay
- [x] Marcar como lido permanece no CTA/toque
- [x] Título, corpo, status e data visíveis

## Resultado da execucao

- Lista de avisos migrada para `HomeActionCard` (clay, hideAccentBar, iconPillRounded, withShadow).
- Não lido: tint orange, status Novo, CTA Marcar como lido.
- Lido: tint blue, status Lido, sem CTA.
- Data na description junto com o corpo.

## Handoff

- `.agents/state/handoffs/TASK-777.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `tasks/change-requests/777-alinhar-cards-ultimos-avisos-resumo-rapido.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-777.md`

## Validacoes executadas

- eslint na tela de avisos — passou

## Pendencias pos-task

- Estilos `noticeItem*` em `styles.ts` ficaram órfãos; limpar se desejado.

## Status final

done
