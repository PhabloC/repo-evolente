# Task 495 - Login com resize: form no topo acima do teclado

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

- Slice 002 - `tasks/slices/002-autenticacao.md`

## Objetivo

Corrigir o estado com teclado em que há espaço vazio no topo e só o e-mail aparece: usar `resize` no Android, esconder hero/menina e ancorar e-mail+senha+ações no topo da área útil acima do teclado. Reduzir interferência do Samsung Pass nos campos de login.

## Criterios de aceite

- [x] com teclado: hero/menina ocultos
- [x] e-mail e senha no topo da área útil (resize + bottomClusterLifted)
- [x] autofill desligado no login para reduzir Samsung Pass
- [x] indice/handoff atualizados

## Resultado da execucao

- `app.json`: `softwareKeyboardLayoutMode` de `pan` → `resize`
- Login: hero/menina recolhem; form sobe ao topo da janela redimensionada
- Campos com `autoComplete=off` / `importantForAutofill=no` / `textContentType=none`
- Biometria oculta enquanto teclado aberto (`compact`)

## Arquivos alterados

- `mobile/app.json`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `tasks/change-requests/495-login-resize-form-topo-acima-teclado.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-495.md`

## Pendencias pos-task

- Reiniciar o Expo (mudança de `app.json` pode exigir restart nativo) e validar no device

## Status final

done
