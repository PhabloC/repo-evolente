# Task 287 - Foto de perfil nos cards de responsavel e crianca no perfil mobile

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

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

comportamento existente de avatar

### Fonte primaria visual

- `ChildAvatar` + `resolveChildAvatarSource` (foto ou default por sexo)
- `HomeHeader` (foto do responsável ou inicial provisória)

## Objetivo

Nos cards de responsável e criança do perfil, exibir a foto de perfil; se não houver, usar o fallback provisório já existente no app.

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-286.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Avatar criança | `ChildAvatar`, `resolveChildAvatarSource` | fallback por sexo | sim |
| Avatar responsável | `profile.avatarUrl` / session + inicial | fallback provisório | sim |
| Slot no card | `HomeActionCard` | prop `leading` | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] card da criança mostra foto ou avatar provisório por sexo
- [x] card do responsável mostra foto ou inicial provisória

## Dependencias

- Task 286 - done

## Resultado da execucao

- `HomeActionCard` ganhou prop `leading` para foto/avatar
- responsável: `avatarUrl` ou inicial amarela (mesmo esquema do header)
- criança: `ChildAvatar` com foto ou default por sexo

## Contexto utilizado

- `HomeActionCard`, `ChildAvatar`, `ResponsavelProfileScreen`, handoff 286

## Handoff

- `.agents/state/handoffs/TASK-287.md`

## Arquivos alterados

- `tasks/change-requests/287-foto-perfil-cards-responsavel-crianca-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-287.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`

## Validacoes executadas

- validação visual dependente de reload

## Pendencias pos-task

- nenhuma

## Status final

done
