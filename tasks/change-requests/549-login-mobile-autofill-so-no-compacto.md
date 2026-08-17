# Task 549 - Login mobile: autofill só desligado com teclado compacto

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- sem mudança de layout; só props de autofill dos campos

## Origem da solicitacao

Code review em `ajustes_mobile.md` item 2: `autoComplete="off"` permanente impede gerenciadores de credenciais mesmo com `compact=false`.

## Objetivo

Restaurar preenchimento de e-mail/senha quando o teclado não está recolhendo a tela, mantendo o bloqueio de Samsung Pass só no estado compacto (Task 495).

## Escopo

- Condicionar `autoComplete`, `importantForAutofill` e `textContentType` ao `compact` em `SignInForm.tsx`

## Fora de escopo

- Layout do login
- `app.json` / `softwareKeyboardLayoutMode`
- Tela de recuperação de senha

## Slice vertical

### Identificador do slice

Slice 002 - Autenticação e recuperação de senha

### Arquivo do slice

- `tasks/slices/002-autenticacao.md`

### Objetivo de negocio

Permitir login por e-mail/senha no mobile.

### Entrega verificavel do slice

Com teclado fechado, o gerenciador de credenciais pode oferecer e-mail/senha; com teclado aberto (`compact`), o autofill permanece desligado.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Implementação | `SignInForm.tsx` | ao condicionar as props | sim |
| Histórico | Task 495 | confirmar intenção do Samsung Pass | sim |
| UI | `design-system/mobile/` | sem mudança visual | nao |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 2
- Risco de contexto excessivo: baixo
- Estratégia: só o formulário de login

## Dependencias

- Task 495 (done)

## Criterios de conclusao

- `compact=false`: `email`/`password` (ou equivalentes iOS/Android)
- `compact=true`: `off` / `no` / `none`
- Comentário do form continua válido

## Instrucoes de implementacao

- E-mail: `autoComplete="email"`, `textContentType="emailAddress"`, `importantForAutofill="yes"` fora do compacto
- Senha: `autoComplete="password"`, `textContentType="password"` fora do compacto

## Validacao esperada

- Leitura das props nos dois estados
- Lint do arquivo

## Entregaveis esperados

- `SignInForm` condicional
- Task, índice, slice e handoff

## Resultado da execucao

- `SignInForm`: autofill `email`/`password` com teclado fechado; `off`/`no`/`none` só com `compact`
- Preserva a intenção da Task 495 (Samsung Pass no teclado aberto)
- Slice 002 permanece done

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 002

### Contexto sob demanda carregado

- `SignInForm.tsx`, Task 495, `TextField` (repassa `TextInputProps`)

### Contexto não carregado

- `design-system/mobile/` — sem mudança visual

## Handoff

- `.agents/state/handoffs/TASK-549.md`
- Próximo contexto: validar gerenciador de senhas no device com teclado fechado

## Arquivos alterados

- `mobile/src/features/auth/components/SignInForm.tsx`
- `tasks/change-requests/549-login-mobile-autofill-so-no-compacto.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`

## Validacoes executadas

- eslint `SignInForm.tsx`: 0 erros
- leitura das props nos dois estados de `compact`

## Pendencias pos-task

- Smoke no Android/iOS: teclado fechado oferece credenciais; teclado aberto não dispara Samsung Pass

## Status final

done
