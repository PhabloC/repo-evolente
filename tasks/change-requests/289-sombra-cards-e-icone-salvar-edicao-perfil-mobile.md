# Task 289 - Sombra nos cards e icone no salvar das edicoes de perfil mobile

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

refino incremental — sombra alinhada ao HomeActionCard

## Objetivo

Colocar box-shadow nos cards das páginas de edição e ícone no botão "Salvar alterações".

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-288.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Cards | `ProfileSectionCard`, `ProfileAvatarEditor` | sombra | sim |
| Botão | telas de edição | `leftIcon={Save}` | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] cards da edição com box-shadow
- [x] botão Salvar alterações com ícone

## Dependencias

- Task 288 - done

## Resultado da execucao

- sombra aplicada em `ProfileSectionCard` e `ProfileAvatarEditor`
- botão "Salvar alterações" com `leftIcon={Save}` nas duas telas

## Contexto utilizado

- estilos dos cards, `Button`, telas de edição

## Handoff

- `.agents/state/handoffs/TASK-289.md`

## Arquivos alterados

- `tasks/change-requests/289-sombra-cards-e-icone-salvar-edicao-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-289.md`
- `mobile/src/features/profile/components/ProfileSectionCard/styles.ts`
- `mobile/src/features/profile/components/ProfileAvatarEditor/styles.ts`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/screens/EditChildProfileScreen.tsx`

## Validacoes executadas

- validação visual dependente de reload

## Pendencias pos-task

- nenhuma

## Status final

done
