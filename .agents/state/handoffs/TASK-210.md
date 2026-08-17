# Handoff - Task 210

## Task

- identificador: 210
- título: Ícone log-out no topo do perfil mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010
- objetivo de negócio: home, perfil e notificações do responsável
- entrega verificável: logout no topo direito do perfil

## Decisões preservadas

- decisão: `ScreenHeader` ganhou slot opcional `rightAction`
- motivo: reutilizar header sem duplicar layout só no perfil
- impacto: outras telas continuam iguais sem a prop

- decisão: remover card "Encerrar sessão" + botão Sair do final
- motivo: pedido do produto
- impacto: logout só pelo ícone no topo

## Contexto utilizado

### Contexto mínimo lido

- task 210, slice 010, índice

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `ResponsavelProfileScreen.tsx` | mover logout | UI |
| `ScreenHeader` | slot direito | ação no topo |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| master/admin logout | fora de escopo |

## Resultado por stack

- mobile: perfil com LogOut no topo direito

## Arquivos alterados

- `mobile/src/shared/components/ScreenHeader/index.tsx`
- `mobile/src/shared/components/ScreenHeader/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `tasks/change-requests/210-icone-logout-topo-perfil-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-210.md`

## Validações executadas

- `npm run typecheck` — ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- perfil mobile se houver mais ajustes de header

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend/auth contract
- motivo: signOut já existente
