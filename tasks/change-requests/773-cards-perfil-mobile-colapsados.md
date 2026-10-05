# Task 773 - Cards do perfil mobile colapsados (ícone + nome)

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

- `design-system/mobile/` (padrão visual dos cards existentes; sem print novo)

### Regra de aderencia visual

- preservar clay/tints do `HomeActionCard`; no estado colapsado mostrar só ícone/leading + título

## Origem da solicitacao

Pedido do usuário: nos cards do perfil, mostrar só ícone e nome; o conteúdo interno só após o clique (também reduz exposição inicial de copy sensível de pagamento/assinatura).

## Objetivo

No perfil do responsável, os cards de informação ficam colapsados (ícone + nome) e expandem o conteúdo ao toque; a ação de CTA (editar, ver relatórios etc.) permanece no rodapé quando expandido.

## Escopo

- Prop `collapsible` no `HomeActionCard`
- Aplicar nos cards do `ResponsavelProfileScreen` (responsável, assinatura, filhos, relatórios e atalhos)
- `SubscriptionManagementCard` passa a ser colapsável

## Fora de escopo

- Cards da home / notificações
- Alterar copy de pagamento (já tratado em 772 no login)
- Novas telas de detalhe

## Entradas

- pedido explícito do usuário
- `mobile/src/features/shell/components/HomeActionCard/`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/components/SubscriptionManagementCard/`

## Slice vertical

### Identificador do slice

Slice 010 - App do responsavel: home, perfil e notificacoes

### Arquivo do slice

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

### Objetivo de negocio

Perfil mais limpo e com conteúdo detalhado sob demanda.

### Entrega verificavel do slice

Cards do perfil iniciam com ícone + nome; toque revela conteúdo interno.

### Fora do slice

- redesign visual completo do perfil

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Card base | `HomeActionCard` | implementar colapso | sim |
| Tela perfil | `ResponsavelProfileScreen` | aplicar collapsible | sim |
| Card assinatura | `SubscriptionManagementCard` | passar prop | sim |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 3
- Risco de contexto excessivo: baixo
- Estratégia: só shell do perfil; sem home/design system completo

## Dependencias

- Task 772 (contexto de copy sensível no login; não bloqueante)

## Criterios de conclusao

- [x] Cards do perfil começam colapsados (ícone + nome)
- [x] Toque no card expande/recolhe o conteúdo
- [x] CTA do rodapé (quando houver `onPress`) continua executando a ação ao expandir
- [x] Home e outras telas com `HomeActionCard` sem `collapsible` permanecem iguais

## Instrucoes de implementacao

- Adicionar `collapsible?: boolean` (default false) em `HomeActionCard`
- Colapsado: esconder status, description, children e footer; mostrar chevron de expansão
- Expandido: conteúdo completo; toque no footer dispara `onPress`; toque no corpo alterna colapso
- Marcar cards do perfil com `collapsible`

## Validacao esperada

- eslint nos arquivos alterados
- checagem manual do perfil no app

## Entregaveis esperados

- `HomeActionCard` colapsável
- perfil e card de assinatura atualizados
- task, índice, slice e handoff

## Resultado da execucao

- `HomeActionCard` ganhou `collapsible`: colapsado = ícone/leading + título + chevron; expandido = status, description, children e CTA.
- Perfil do responsável e `SubscriptionManagementCard` usam `collapsible`.
- CTA do rodapé (Editar, Ver relatórios etc.) só aparece expandido e dispara `onPress` sem recolher.

## Contexto utilizado

- Task 773, Slice 010, HomeActionCard, ResponsavelProfileScreen, SubscriptionManagementCard.

## Handoff

- `.agents/state/handoffs/TASK-773.md`

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/773-cards-perfil-mobile-colapsados.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-773.md`

## Validacoes executadas

- `npx eslint` nos arquivos alterados — passou.

## Pendencias pos-task

- Validar visualmente no device/simulador no perfil.
- Se a loja ainda exigir, limpar copy de pagamento nos textos que aparecem após expandir o card Assinatura.

## Status final

done
