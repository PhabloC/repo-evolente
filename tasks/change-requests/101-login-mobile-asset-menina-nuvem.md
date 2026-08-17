# Task 101 - Usar asset unico menina_nuvem no login mobile

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

### Fonte primaria visual

- `design-system/mobile/prints/login-mobile.png`
- `mobile/assets/menina_nuvem.png`

## Objetivo

Substituir menina e nuvem separados pelo asset unico `menina_nuvem.png` e ajustar tipografia/logo.

## Escopo

- Usar `menina_nuvem.png` no login
- Remover SignInCloud / girl separada
- Texto de bem-vindo acima da nuvem, sem quebra em "Bem-vindo(a)!"
- Logo um pouco menor
- lint/typecheck

## Dependencias

- Task 100 — done

## Criterios de conclusao

- [x] asset unico no login
- [x] texto fora da nuvem e sem quebra no titulo
- [x] logo menor
- [x] lint/typecheck ok

## Resultado da execucao

### Resumo por stack

- **mobile**: login usa `menina_nuvem.png`; texto em fluxo normal acima da imagem; titulo com hifen inquebravel + `numberOfLines={1}`; logo reduzida (~210x88); `SignInCloud` removido.

## Handoff

- `.agents/state/handoffs/TASK-101.md`

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/shared/components/AppText/index.tsx`
- removidos `SignInCloud.tsx` / `SignInCloud.styles.ts`
- `tasks/change-requests/101-login-mobile-asset-menina-nuvem.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-101.md`

## Validacoes executadas

- lint ok
- typecheck ok

## Status final

done
