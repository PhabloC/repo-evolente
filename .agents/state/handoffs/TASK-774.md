# Handoff - Task 774

## Task

- identificador: 774
- título: Ocultar card Assinatura no perfil mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010 - App do responsavel: home, perfil e notificacoes
- objetivo de negócio: ocultar gestão de assinatura no perfil sem apagar o código
- entrega verificável: card Assinatura não renderiza; componente permanece

## Decisões preservadas

- decisão: `SHOW_SUBSCRIPTION_CARD = false` no `ResponsavelProfileScreen`
- motivo: pedido de ocultar sem excluir
- impacto: reativar = trocar flag para `true`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/774-ocultar-card-assinatura-perfil-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `ResponsavelProfileScreen.tsx` | ocultar | flag + render condicional |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `SubscriptionManagementCard` interno | não deletar; só não renderizar |

## Resultado por stack

- front-end ou next-js: n/a
- backend: n/a
- mobile: card Assinatura oculto no perfil

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/774-ocultar-card-assinatura-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-774.md`

## Validações executadas

- validação: eslint no perfil — passou

## Pendências ou bloqueios

- item: pill “Assinatura …” no card do responsável ainda visível

## Próxima ação sugerida

- Conferir perfil no app; se a loja ainda flagrar a pill, ocultá-la também

## Próximo contexto recomendado

- `ResponsavelProfileScreen.tsx` (flag e pill)

## Contexto que não deve ser carregado na próxima etapa

- fonte: Asaas / checkout web
- motivo: não alterados
