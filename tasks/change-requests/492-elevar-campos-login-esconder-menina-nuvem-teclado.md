# Task 492 - Elevar campos do login e esconder menina/nuvem com teclado

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

Slice 002 - Autenticacao e recuperacao de senha

### Arquivo do slice

- `tasks/slices/002-autenticacao.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

pedido explícito + print de login (comportamento com teclado)

### Fonte primaria visual

- `design-system/mobile/prints/login-mobile.png` (estado sem teclado)
- pedido: ao focar e-mail/senha, campos sobem; SVG menina+nuvem pode sumir

## Contexto de negocio

### Por que

Ao focar os inputs, o teclado cobre os campos. A elevação anterior (Tasks 114/115) não está mais ativa na tela atual.

### O que

Ao abrir o teclado no login, elevar os campos de e-mail/senha e esconder a ilustração menina+nuvem para liberar espaço.

### Comportamento esperado

- foco em e-mail ou senha / teclado aberto → campos visíveis acima do teclado
- menina+nuvem some enquanto o teclado estiver aberto
- fechar teclado → layout original restaura
- recovery/reset fora de escopo

### Fora de escopo

- PasswordRecovery / PasswordReset
- alterar copy ou assets
- biometria

## Dependencias

- Tasks 114/115 (comportamento histórico de elevação)
- Task 101 (asset menina_nuvem)

## Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 002
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`

## Contexto sob demanda

- `mobile/src/features/auth/components/SignInForm.tsx`
- handoffs TASK-114 / TASK-115 se úteis
- `mobile/docs/ai/CODE_STYLE.md`

## Orcamento de contexto

baixo — tela de login e estilos locais

## Criterios de aceite

- [x] teclado aberto: campos de e-mail/senha sobem e ficam usáveis
- [x] teclado aberto: menina+nuvem escondida
- [x] teclado fechado: layout original
- [x] indice e handoff atualizados

## Resultado da execucao

Hook `useAuthKeyboardLift` anima progresso 0→1 no show/hide do teclado (e no foco dos campos). No login: menina+nuvem recolhe (altura/opacidade), logo/hero compactam e o form sobe (~48px). Recovery intacto.

## Contexto utilizado

- task 492, slice 002, SignInScreen, styles, SignInForm

## Handoff

`.agents/state/handoffs/TASK-492.md`

## Arquivos alterados

- `mobile/src/features/auth/hooks/useAuthKeyboardLift.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `tasks/change-requests/492-elevar-campos-login-esconder-menina-nuvem-teclado.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-492.md`

## Validacoes executadas

- typecheck nos arquivos de auth sem erros novos (erros pré-existentes em games/trail/admin)

## Pendencias pos-task

- validar visualmente no device/emulador com teclado aberto

## Status final

done
