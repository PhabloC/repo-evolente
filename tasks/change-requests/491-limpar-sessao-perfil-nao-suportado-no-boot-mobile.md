# Task 491 - Limpar sessão de perfil não suportado no boot mobile

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

pedido explícito (comportamento de boot)

### Fonte primaria visual

- pedido do produto: ao abrir o app, não persistir a tela "Perfil não suportado"; abrir login

## Contexto de negocio

### Por que

Sessão de `profissional` (ou papel sem shell mobile) fica salva e, no próximo boot, o app abre direto em `UnsupportedRole` em vez do login.

### O que

No restore (e no login), não manter sessão de papel não suportado no storage. Boot com sessão inválida para mobile deve cair no login. Master e responsável continuam restaurando sessão normalmente.

### Comportamento esperado

- abrir o app com sessão `profissional` (ou papel inválido) → login
- login com `profissional` → pode mostrar "Perfil não suportado" na sessão atual, mas sem persistir para o próximo boot
- master/responsável → restore e shells intactos

### Fora de escopo

- desabilitar restore de sessão para master/responsável
- alterar biometria
- alterar permissões de API

## Dependencias

- Slice 002 (auth mobile)

## Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 002
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/shared/utils/resolveMobileShell.ts`
- `mobile/src/routes/RootNavigator.tsx`

## Contexto sob demanda

- testes de auth/shell mobile se existirem

## Orcamento de contexto

baixo — um fluxo de restore/login

## Criterios de aceite

- [x] `restoreSession` com role unsupported limpa storage e retorna null
- [x] `signIn` com role unsupported não persiste sessão
- [x] master/responsável ainda persistem e restauram
- [x] teste cobrindo o restore unsupported
- [x] indice e handoff atualizados

## Resultado da execucao

`authService.restoreSession` limpa storage e retorna `null` para papéis sem shell mobile. `signIn` não persiste esses papéis. Master/responsável inalterados.

## Contexto utilizado

- task 491, slice 002, `authService.ts`, `resolveMobileShell.ts`, `RootNavigator.tsx`, testes de auth

## Handoff

`.agents/state/handoffs/TASK-491.md`

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `tasks/change-requests/491-limpar-sessao-perfil-nao-suportado-no-boot-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-491.md`

## Validacoes executadas

- `npm test -- --testPathPattern=authService.test --no-coverage` (pass)

## Pendencias pos-task

- Recarregar o app (cold start) para limpar a sessão `profissional` já salva no device

## Status final

done
