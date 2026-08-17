# Task 099 - Corrigir camada da menina atras da nuvem no login mobile

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

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Fonte primaria visual

- screenshot atual do usuario
- `design-system/mobile/prints/login-mobile.png`

## Objetivo

Colocar o corpo da menina atras da nuvem de forma estavel, criando SVG de onda adequado se necessario, sem cortar o formulario.

## Escopo

- Separar stacking: shapes < menina < nuvem+form < texto/logo
- Criar/ajustar SVG da nuvem (onda com fill opaco)
- Manter input de e-mail visivel
- lint/typecheck

## Dependencias

- Task 098 — done

## Criterios de conclusao

- [x] menina atras da onda da nuvem
- [x] form sem corte
- [x] lint/typecheck ok

## Resultado da execucao

### Resumo por stack

- **mobile**: criado `nuvem_login_onda.svg` com fill opaco; menina em camada absoluta separada do texto; `cloudPanel` (nuvem+form) acima da menina; hero/texto acima sem elevá-la.

### Decisões técnicas

- Causa: `heroSection` com zIndex alto envolvia a menina e a empurrava acima da nuvem.
- Solucao: menina fora do hero; painel nuvem+form `zIndex: 2`; hero `zIndex: 3`.
- Novo SVG de onda autorizada pelo usuario nesta task.

## Handoff

- `.agents/state/handoffs/TASK-099.md`

## Arquivos alterados

- `mobile/assets/nuvem_login_onda.svg`
- `mobile/src/features/auth/components/SignInCloud.tsx`
- `mobile/src/features/auth/components/SignInCloud.styles.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/099-corrigir-camada-menina-atras-nuvem-login-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-099.md`

## Validacoes executadas

- lint ok
- typecheck ok

## Pendencias pos-task

- Nenhuma

## Status final

done
