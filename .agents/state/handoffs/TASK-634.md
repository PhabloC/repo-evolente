# Handoff - Task 634

## Task

- identificador: 634
- título: Login web mobile apenas com formulário
- slice: 012 - Login visual e acesso livre web
- status final: done

## Decisões preservadas

- A variante `formOnlyOnMobile` pertence ao `AuthLayout`, mas é ativada apenas pelo login.
- Até 560px, branding, selo, título e subtítulo não são exibidos; campos, links e CTAs permanecem funcionais.
- O pedido do usuário preenche a lacuna da referência visual, que só cobre desktop.

## Contexto efetivamente usado

- Slice 012, handoff da Task 026, print do login desktop, `AuthLayout`, LoginPage e guias web de acessibilidade/estilo/QA.

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/Login/index.test.tsx`
- task, slice e índice.

## Validações executadas

- Teste da LoginPage: ok (2 testes).
- Lint dos arquivos alterados: ok.
- Lint e build completos bloqueados por erros preexistentes fora deste escopo.

## Pendências

- Corrigir lint em `MainLayout`/`SubscriptionGate` e erros de tipos em pacientes/planos em task separada.

## Próximo contexto recomendado

- Para novo ajuste de login web: esta task, o handoff e `front-end/src/layout/AuthLayout/**`.
