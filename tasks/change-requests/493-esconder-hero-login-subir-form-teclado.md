# Task 493 - Esconder hero do login e subir form ao focar inputs

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

pedido explícito (comportamento com teclado)

### Fonte primaria visual

- pedido: ao focar e-mail/senha, esconder logo + bem-vindo + subtítulo; inputs sobem e ocupam o topo

## Contexto de negocio

### Por que

Task 492 só compactava o hero; o produto quer o hero inteiro oculto e o formulário no lugar de cima.

### O que

No login, com teclado/foco nos inputs: ocultar logo, título e subtítulo (além da menina/nuvem) e elevar o bloco dos campos para o topo.

### Comportamento esperado

- foco e-mail/senha → hero e menina ocultos; form no topo
- fechar teclado → layout original

### Fora de escopo

- recovery/reset
- mudança de copy/assets

## Dependencias

- Task 492

## Contexto minimo

- task 492/493, SignInScreen, useAuthKeyboardLift, styles

## Contexto sob demanda

- nenhum além do mínimo

## Orcamento de contexto

baixo

## Criterios de aceite

- [x] logo, bem-vindo e subtítulo somem com o teclado
- [x] inputs sobem e ocupam a área superior
- [x] teclado fechado restaura layout
- [x] indice e handoff atualizados

## Resultado da execucao

Hero (logo + bem-vindo + subtítulo) recolhe a altura/opacidade 0; spacer flex some; bottomCluster perde `marginTop: auto` e sobe ao topo com LayoutAnimation. Menina/nuvem continua oculta.

## Contexto utilizado

- SignInScreen, styles, useAuthKeyboardLift, task 492/493

## Handoff

`.agents/state/handoffs/TASK-493.md`

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/493-esconder-hero-login-subir-form-teclado.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-493.md`

## Validacoes executadas

- lint nos arquivos alterados

## Pendencias pos-task

- smoke visual no device

## Status final

done
