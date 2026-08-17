# Task 210 - Ícone log-out no topo do perfil mobile

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

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 010 - App do responsavel: home, perfil e notificacoes

### Arquivo do slice

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system + pedido explícito

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- pedido: ícone log-out no topo superior direito; remover botão Sair do rodapé

## Contexto de negocio

### Por que

O logout está no final da página de perfil; o produto pediu atalho no topo direito.

### O que

Colocar ícone de log-out no topo superior direito da tela de perfil e remover o botão/card de sair do final.

### Comportamento esperado

- ícone log-out no topo direito chama o mesmo `onSignOut` atual
- botão/card "Sair" / "Encerrar sessão" removidos do final da página

### Fora de escopo

- alterar logout em telas master/admin
- mudança de contrato

## Dependencias

- Task 023 / Slice 010

## Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 010

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Perfil | `ResponsavelProfileScreen.tsx` | mover logout | sim |
| Header | `ScreenHeader` | slot de ação à direita (se útil) | sim |

## Orcamento de contexto

- Risco baixo

## Criterios de conclusao

- ícone log-out no topo direito do perfil
- sem botão Sair no final
- typecheck ok

## Resultado da execucao

- `ScreenHeader` aceita `rightAction` opcional.
- Perfil exibe ícone `LogOut` no topo direito com o mesmo `onSignOut`.
- Card "Encerrar sessão" e botão "Sair" removidos do final da página.

## Contexto utilizado

- task 210, slice 010, `ResponsavelProfileScreen`, `ScreenHeader`

## Handoff

- `.agents/state/handoffs/TASK-210.md`

## Arquivos alterados

- `mobile/src/shared/components/ScreenHeader/index.tsx`
- `mobile/src/shared/components/ScreenHeader/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `tasks/change-requests/210-icone-logout-topo-perfil-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-210.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
