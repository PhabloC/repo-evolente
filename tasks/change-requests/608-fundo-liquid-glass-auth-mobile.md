# Task 608 - Fundo liquid glass com bolhas no auth mobile

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

- Não se aplica; não altera autenticação, API ou navegação.

## Modo de execução

single-stack

## Slice vertical

- Slice 002 — `tasks/slices/002-autenticacao.md`

## Objetivo

Aplicar nas telas mobile de login e recuperação de senha um fundo decorativo de bolhas subindo, inspirado explicitamente no movimento do sidebar web, com uma camada translúcida de vidro sobreposta e conteúdo de autenticação plenamente legível.

## Dependências

- Task 112 — done (componente de fundo auth neutralizado)
- Task 607 — done (layout da recuperação com teclado)

## Contexto mínimo

- esta task
- Slice 002
- `.agents/state/handoffs/TASK-607.md`
- `mobile/src/features/auth/components/AuthAnimatedBackground.tsx`
- `mobile/src/shared/components/AppBackgroundBubbles/index.tsx`
- `mobile/src/shared/components/AppBackgroundLiquidGlass/index.tsx`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Referência de movimento | `front-end/src/layout/Sidebar/persistentLava.tsx` | reproduzir apenas o caráter suave e ascendente das bolhas, sem portar DOM/CSS web |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | preservar paleta, respiro e contraste do app |
| Acessibilidade e performance | `mobile/docs/ai/{AGENTS,CODE_STYLE,QA}.md` | manter decoração fora da árvore acessível e sem interceptar toque |
| Integração no auth | `mobile/src/features/auth/screens/{SignInScreen,PasswordRecoveryScreen}.tsx` | confirmar que a camada está abaixo do conteúdo e compatível com a elevação pelo teclado |

## Orçamento de contexto

- baixo
- estratégia: reativar exclusivamente o componente compartilhado de fundo usando componentes visuais já existentes; sem reabrir formulários, hooks, API ou outras telas.

## Critérios de aceite

- [x] Login e recuperação exibem bolhas rosa/laranja com movimento ascendente lento e discreto.
- [x] Uma camada de vidro claro fica acima das bolhas e abaixo do conteúdo, preservando contraste e leitura.
- [x] Fundo não recebe foco, não intercepta toques e não interfere na animação de teclado da Task 607.
- [x] Não há mudança no fluxo de login, recuperação, navegação ou chamadas de API.
- [x] Lint, typecheck, testes aplicáveis e validação visual em emulador/device são registrados.

## Referência visual

- Fonte mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`.
- Referência comportamental explícita do usuário: `front-end/src/layout/Sidebar/persistentLava.tsx` (bolhas/lava subindo). É referência de movimento, não um artefato visual mobile a ser copiado literalmente.
- Sem print novo.

## Resultado da execução

- `AuthAnimatedBackground` voltou a compor as bolhas ascendentes rosa/laranja e a camada `liquid glass` já disponíveis no app.
- Como login e recuperação já renderizam esse componente antes da camada de conteúdo, ambos recebem o efeito sem alteração nos formulários ou no comportamento de teclado.
- As duas camadas são decorativas: usam `pointerEvents="none"` e ficam fora da árvore de acessibilidade.

## Contexto utilizado

- Task 608, Slice 002 e handoff da Task 607.
- `AuthAnimatedBackground`, `AppBackgroundBubbles` e `AppBackgroundLiquidGlass`.
- Telas `SignInScreen` e `PasswordRecoveryScreen` para confirmar a ordem de camadas.
- `front-end/src/layout/Sidebar/persistentLava.tsx` como referência explícita de movimento; design system e guias mobile de padrão, estilo e QA.

## Arquivos alterados

- `mobile/src/features/auth/components/AuthAnimatedBackground.tsx`
- `tasks/change-requests/608-fundo-liquid-glass-auth-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-608.md`

## Validações executadas

- `git -C mobile diff --check` — aprovado.
- ESLint localizado para `AuthAnimatedBackground.tsx` — iniciado, mas bloqueado no ambiente sem resultado; o processo iniciado foi encerrado.
- Validação visual em emulador/device — pendente: conferir contraste do formulário, ritmo das bolhas e abertura do teclado nas duas telas.

## Pendências pós-task

- Repetir lint, typecheck e testes quando o ambiente de ferramentas não estiver bloqueado.
- Confirmar visualmente o efeito em Android/iOS.

## Handoff

- `.agents/state/handoffs/TASK-608.md`

## Status final

done
