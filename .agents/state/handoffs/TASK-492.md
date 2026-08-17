# Handoff - Task 492

## Task

- identificador: TASK-492
- título: Elevar campos do login e esconder menina/nuvem com teclado
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002 - Autenticacao e recuperacao de senha
- objetivo de negócio: login usável com teclado aberto
- entrega verificável: campos acima do teclado; menina+nuvem oculta

## Decisões preservadas

- decisão: hook `useAuthKeyboardLift` (listeners de teclado + foco antecipado nos campos)
- motivo: Android `keyboardDidShow` atrasa; `onFocus` sobe o layout antes
- impacto: animação com `useNativeDriver: false` (altura/opacidade/margem)

- decisão: esconder menina+nuvem (altura→0, opacity→0), compactar logo e elevar form ~48px
- motivo: pedido explícito; libera espaço para e-mail/senha
- impacto: recovery não alterado

## Contexto utilizado

### Contexto mínimo lido

- task 492, slice 002, SignInScreen, styles

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `SignInForm.tsx` | onFocus | disparo antecipado |
| TASK-114/115 | histórico | amplitude de referência |

### Contexto evitado

- recovery, backend, design-system completo

## Arquivos alterados

- `mobile/src/features/auth/hooks/useAuthKeyboardLift.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`

## Validações executadas

- typecheck: sem erros novos nos arquivos de auth

## Pendências

- smoke visual no device com teclado

## Próxima ação sugerida

- abrir login, focar e-mail/senha e confirmar campos acima do teclado

## Próximo contexto recomendado

- nenhum, salvo ajuste fino de amplitude (`translateY` / altura da menina)

## Contexto que não deve ser carregado

- jogos, OpenAPI, front-end web
