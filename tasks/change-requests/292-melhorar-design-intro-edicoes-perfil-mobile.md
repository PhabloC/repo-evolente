# Task 292 - Melhorar design da secao intro das edicoes de perfil mobile

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

refino incremental — print da seção "Seus dados" + linguagem dos cards

## Objetivo

Melhorar o design da seção introdutória das páginas de edição (responsável e criança).

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-291.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Intro | `editProfileStyles.ts`, telas de edição | card com ícone | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] seção "Seus dados" com visual de card (ícone, tipografia, sombra)
- [x] intro da edição da criança no mesmo padrão

## Dependencias

- Task 291 - done

## Resultado da execucao

- intro virou card com pastilha de ícone, título bold, descrição 14/20 e sombra alinhada aos demais cards
- aplicado em edição do responsável (`User`) e da criança (`Baby`)

## Handoff

- `.agents/state/handoffs/TASK-292.md`

## Arquivos alterados

- `tasks/change-requests/292-melhorar-design-intro-edicoes-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-292.md`
- `mobile/src/features/profile/screens/editProfileStyles.ts`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/screens/EditChildProfileScreen.tsx`

## Validacoes executadas

- validação visual dependente de reload

## Pendencias pos-task

- nenhuma

## Status final

done
