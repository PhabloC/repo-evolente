# Task 634 - Login web mobile apenas com formulário

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end (React/Vite)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (não envolvido; o escopo é a responsividade da web)

## Contrato

Não se aplica.

## Modo de execução

single-stack

## Referência de design system

- Stack de referência visual: front-end
- Fonte primária: `design-system/front/prints/login-desktop.png`
- Lacuna registrada: o print não define a variante responsiva; o pedido do usuário governa que, no mobile, fique apenas o formulário.

## Objetivo

Em telas de até 560px, apresentar no `/login` somente o formulário funcional, sem a área institucional ou o cabeçalho decorativo do card.

## Escopo

- Adicionar uma variante reutilizável do `AuthLayout` para ocultar conteúdo não pertencente ao formulário no mobile.
- Aplicar a variante somente na `LoginPage`.
- Preservar o layout desktop e a semântica/acessibilidade dos controles do formulário.
- Adicionar teste de regressão do contrato da variante.

## Fora de escopo

- App React Native.
- Fluxos de autenticação, API ou outras telas auth.
- Redesign desktop.

## Dependências

- Task 026 — done
- Task 428 — done

## Slice vertical

- Slice 012 - Login visual e acesso livre web
- `tasks/slices/012-login-visual-acesso-livre.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/012-login-visual-acesso-livre.md`
- `.agents/state/handoffs/TASK-026.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI responsiva | `design-system/front/prints/login-desktop.png` | preservar o desktop e registrar a lacuna mobile |
| Implementação | `front-end/src/layout/AuthLayout/**` | variante responsiva reutilizável |
| Aplicação | `front-end/src/pages/Auth/Login/**` | limitar a variante ao login |
| UI web | `front-end/docs/ai/AGENTS.md`, `ACCESSIBILITY.md`, `CODE_STYLE.md`, `QA.md` | padrões e validação |

## Orçamento de contexto

- Risco: baixo.
- Estratégia: não carregar API, backend, app mobile, requirements nem outras telas auth.

## Critérios de conclusão

- [x] Em viewport de até 560px, branding, selo e título/subtítulo do card não são exibidos visualmente no login.
- [x] Campos, links e CTAs do formulário continuam disponíveis e acessíveis.
- [x] Desktop permanece inalterado.
- [x] Teste específico e lint dos arquivos alterados passam; validações completas registradas abaixo.

## Resultado da execucao

- `AuthLayout` recebeu a opção `formOnlyOnMobile`, que em telas de até 560px oculta branding, selo, título e subtítulo, remove o verniz do card e mantém o conteúdo de `children`.
- A opção foi ativada apenas na `LoginPage`; as outras telas que compartilham o layout não mudaram.
- O formulário mantém campos rotulados, links, CTAs e controles de teclado; o desktop não recebe nenhuma regra nova.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, índice, esta task, Slice 012 e handoff da Task 026.
- Contexto sob demanda: print desktop (para preservar o desktop), `AuthLayout`, LoginPage e os guias locais de arquitetura, estilo, acessibilidade e QA.
- Não carregados: API, backend, mobile nativo, OpenAPI, requirements e outras telas auth.

## Handoff

- `.agents/state/handoffs/TASK-634.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/Login/index.test.tsx`
- esta task, `tasks/slices/012-login-visual-acesso-livre.md`, `tasks/000-index.md` e o handoff.

## Validacoes executadas

- `npm run test -- --run src/pages/Auth/Login/index.test.tsx` — ok (2 testes).
- `npx eslint src/layout/AuthLayout/index.tsx src/pages/Auth/Login/index.tsx src/pages/Auth/Login/index.test.tsx` — ok.
- `npm run lint` — pendência preexistente em `src/layout/MainLayout/index.tsx` e `src/pages/Auth/SubscriptionGate/index.test.tsx`.
- `npm run build` — pendências preexistentes de tipos em pacientes e planos; nenhuma aponta para os arquivos desta task.

## Pendencias pos-task

- Corrigir os erros preexistentes de lint e build em task própria.

## Status final

done
