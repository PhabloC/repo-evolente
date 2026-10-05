# Handoff - Task 773

## Task

- identificador: 773
- título: Cards do perfil mobile colapsados (ícone + nome)
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010 - App do responsavel: home, perfil e notificacoes
- objetivo de negócio: perfil limpo com detalhe sob demanda
- entrega verificável: cards colapsados no perfil; expandem no toque

## Decisões preservadas

- decisão: prop `collapsible` no `HomeActionCard` (default false)
- motivo: home/avisos não mudam; só o perfil ativa o modo
- impacto: colapsado = ícone + título; expandido = conteúdo + CTA

- decisão: toque no corpo alterna expand/collapse; toque no footer dispara `onPress`
- motivo: separar “ver detalhes” de “executar ação”
- impacto: Editar/Ver relatórios só no rodapé expandido

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/773-cards-perfil-mobile-colapsados.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `HomeActionCard` | colapso | implementação |
| `ResponsavelProfileScreen` | aplicar | collapsible nos cards |
| `SubscriptionManagementCard` | assinatura | prop collapsible |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| Home / avisos | sem `collapsible` |
| design-system completo | padrão visual já no card |

## Resultado por stack

- front-end ou next-js: n/a
- backend: n/a
- mobile: cards do perfil colapsáveis

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/773-cards-perfil-mobile-colapsados.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-773.md`

## Validações executadas

- validação: eslint nos arquivos alterados — passou

## Pendências ou bloqueios

- item: validação visual no dispositivo
- item: copy de pagamento ainda existe dentro do card Assinatura após expandir

## Próxima ação sugerida

- Recarregar o app e conferir o perfil; se a loja ainda reclamar, limpar textos de pagamento/site no conteúdo expandido.

## Próximo contexto recomendado

- `ResponsavelProfileScreen.tsx`
- `SubscriptionManagementCard/index.tsx` (se limpar copy)

## Contexto que não deve ser carregado na próxima etapa

- fonte: home/avisos HomeActionCard consumers
- motivo: não usam collapsible
