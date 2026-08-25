# Task 607 - Recovery mobile aplica elevação do login ao focar input

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

- Não se aplica; preserva o fluxo atual de recuperação de senha.

## Modo de execução

single-stack

## Slice vertical

- Slice 002 — `tasks/slices/002-autenticacao.md`

## Objetivo

Ao tocar no campo de e-mail da tela **Esqueci minha senha**, aplicar o mesmo comportamento visual e de teclado já consolidado no login: o formulário sobe e o layout volta ao estado normal somente depois que o teclado realmente fechar.

## Dependências

- Task 496 — done
- Task 549 — done

## Contexto mínimo

- esta task
- Slice 002
- `.agents/state/handoffs/TASK-496.md`
- hook de elevação de teclado, telas de login e recuperação do `mobile/src/features/auth/`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Reutilizar comportamento | `SignInScreen` e `useAuthKeyboardLift` | aplicar o mesmo ciclo de foco/teclado sem duplicar lógica |
| Layout mobile | `mobile/src/features/auth/screens/styles.ts` | manter a posição do formulário visível acima do teclado |
| UI | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | preservar linguagem visual existente |
| Acessibilidade | `mobile/docs/ai/ACCESSIBILITY.md` | foco, rótulo e retorno consistente após fechar teclado |
| Cobertura | testes de auth/recovery existentes | validar foco e restauração do layout |

## Orçamento de contexto

- baixo
- estratégia: somente recovery, login como referência e hook compartilhado; sem alterar API, reset de senha ou cadastro.

## Critérios de aceite

- [x] Tocar no input de e-mail da recuperação ativa o mesmo estado compacto/elevação usado no login.
- [x] O campo fica utilizável acima do teclado, sem corte de conteúdo relevante pelo mesmo layout animado do login.
- [x] Trocar foco e fechar o teclado preserva o debounce/restauração já adotados no login.
- [x] Não há mudança no envio da recuperação, validação, API ou tela de reset.
- [x] Cobertura focada e validação manual no emulador/device são registradas.

## Referência visual

- Fonte: `design-system/mobile/Design_System_Evolente_App_Mobile.md`.
- Sem print novo; o login mobile é a referência comportamental explícita para o estado com teclado aberto.

## Resultado da execução

- A tela de recuperação reutiliza `useAuthKeyboardLift`, recolhendo hero e ilustração e elevando o formulário quando o e-mail recebe foco ou o teclado abre.
- `PasswordRecoveryForm` encaminha o foco do campo ao hook; o envio, a validação e a API não foram alterados.
- O retorno ao layout normal usa o debounce de 200 ms já consolidado no hook do login.

## Contexto utilizado

- `mobile/src/features/auth/screens/SignInScreen.tsx` e `useAuthKeyboardLift.ts` como referência comportamental.
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx` e `components/PasswordRecoveryForm.tsx` como escopo de alteração.
- `mobile/docs/ai/{AGENTS,MOBILE_PATTERNS,CODE_STYLE,QA}.md` e o design system mobile. `ACCESSIBILITY.md`, citado na task, não existe no repositório.

## Arquivos alterados

- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/components/PasswordRecoveryForm.tsx`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-607.md`

## Validações executadas

- `git -C mobile diff --check` — aprovado.
- `npm run lint`, `npm run typecheck` e `npm run test -- --watch=false` — iniciados separadamente, mas o ambiente manteve processos Expo/ESLint/TypeScript/Jest bloqueados sem resultado; as execuções iniciadas foram encerradas.
- Validação manual em emulador/device — pendente: confirmar que o campo de e-mail permanece visível ao abrir o teclado e que o layout restaura após fechá-lo.

## Pendências pós-task

- Executar a validação visual manual no emulador ou dispositivo e, com o ambiente de tooling normalizado, rodar lint, typecheck e testes completos.

## Handoff

- `.agents/state/handoffs/TASK-607.md`

## Status final

done
