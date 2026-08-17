# Task 211 - Header do perfil: voltar, título central e sem textos extras

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

pedido explícito de UI

### Fonte primaria visual

- pedido: remover "Dados da conta..." e "Responsável"; seta voltar à esquerda; "Perfil" ao centro; manter logout à direita

## Contexto de negocio

### Por que

O header do perfil ainda usa eyebrow/description e o título não está centralizado com navegação de volta.

### O que

Simplificar o topo do perfil para barra com voltar | Perfil | logout.

### Comportamento esperado

- sem textos "Responsável" e "Dados da conta e das crianças vinculadas."
- seta à esquerda volta para a home (página anterior no shell)
- título "Perfil" centralizado
- logout permanece à direita

### Fora de escopo

- alterar ScreenHeader global das demais telas
- mudar tab bar

## Dependencias

- Task 210

## Contexto minimo

- task 210/211, slice 010, `ResponsavelProfileScreen`, `ResponsavelShellNavigator`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Header atividade | `TrailActivityScreen` topBar | reutilizar padrão visual da seta | sim |

## Orcamento de contexto

- Risco baixo

## Criterios de conclusao

- header simplificado com voltar, título central e logout
- typecheck ok

## Resultado da execucao

- Removidos "Responsável" e "Dados da conta e das crianças vinculadas."
- Topo do perfil: seta voltar (home) | "Perfil" central | logout.

## Contexto utilizado

- task 211, perfil, shell navigator

## Handoff

- `.agents/state/handoffs/TASK-211.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `tasks/change-requests/211-header-perfil-voltar-titulo-central-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-211.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
