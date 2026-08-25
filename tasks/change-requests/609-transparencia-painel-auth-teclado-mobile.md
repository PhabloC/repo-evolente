# Task 609 - Transparência do painel auth ao abrir teclado no mobile

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

Não se aplica; não altera API, autenticação, nem navegação.

## Modo de execução

single-stack

## Slice vertical

- Slice 002 — `tasks/slices/002-autenticacao.md`

## Objetivo

Quando o usuário focar um campo e o teclado abrir, tornar transparente o painel claro que envolve o formulário das telas de login e recuperação de senha do app mobile.

## Dependências

- Task 493 — done (elevação do formulário com teclado)
- Task 607 — done (elevação na recuperação)
- Task 608 — done (fundo liquid glass no auth)

## Contexto mínimo

- esta task
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-608.md`
- `mobile/src/features/auth/screens/{SignInScreen,PasswordRecoveryScreen}.tsx`
- `mobile/src/features/auth/screens/styles.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Alteração de UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | preservar contraste, paleta e respiro. |
| Implementação e qualidade mobile | `mobile/docs/ai/{AGENTS,CODE_STYLE,QA}.md` | respeitar padrões locais e validar a alteração. |

## Orçamento de contexto

- baixo
- estratégia: reutilizar o estado `isKeyboardOpen` já existente, sem alterar hooks, formulários, navegação ou camadas de fundo.

## Critérios de aceite

- [x] Ao abrir o teclado no login, o `formSection` deixa de ter preenchimento claro.
- [x] Ao abrir o teclado na recuperação de senha, o mesmo painel fica transparente.
- [x] Ao fechar o teclado, o preenchimento original `rgba(255, 249, 241, 0.9)` é restaurado.
- [x] Nenhum fluxo de autenticação, acessibilidade ou interação é alterado.

## Referência visual

- Fonte mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`.
- Comportamento explícito solicitado: o painel de conteúdo que sobe com o teclado fica transparente durante o foco.

## Resultado da execução

- Adicionado o estilo `formSectionKeyboardOpen`, com fundo `transparent`.
- Login e recuperação aplicam esse estilo somente quando `isKeyboardOpen` for verdadeiro; ao fechar o teclado, o painel volta ao preenchimento `rgba(255, 249, 241, 0.9)` já existente.

## Contexto utilizado

- Task 609, Slice 002 e handoff da Task 608.
- Telas `SignInScreen` e `PasswordRecoveryScreen`, estilos compartilhados do auth e `useAuthKeyboardLift` já utilizado pelas duas telas.
- Design system mobile e guias locais de implementação/qualidade.

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/609-transparencia-painel-auth-teclado-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-609.md`

## Validações executadas

- `npm run lint` — aprovado.
- `npm run typecheck` — aprovado.
- `git diff --check` — aprovado.
- `npm run test` — iniciado, mas o ambiente não devolveu o resumo/encerramento do Jest; requer repetição local.

## Pendências pós-task

- Confirmar visualmente em Android/iOS que o painel fica transparente ao abrir o teclado e volta ao creme ao fechá-lo.
- Repetir `npm run test` em ambiente que devolva o resultado completo do Jest.

## Handoff

- `.agents/state/handoffs/TASK-609.md`

## Status final

done
