# Handoff - Task 790

## Task

- identificador: 790
- título: Manter CTAs visíveis quando o login mostra erro de campo
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002
- objetivo de negócio: validação visível sem esconder Criar conta / Esqueci senha
- entrega verificável: CTAs abaixo dos inputs permanecem na tela

## Decisões preservadas

- decisão: `mainColumn` com `justifyContent: 'flex-end'` e cluster `flexShrink: 0`
- motivo: o overflow anterior cortava o fundo do formulário
- impacto: falta de altura corta hero/nuvem, não os CTAs

- decisão: comprimir hero/nuvem quando `hasFieldErrors`
- motivo: os HelperTexts aumentam a altura do form
- impacto: logo e menina diminuem só enquanto o erro de campo existir

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, Task 790, Slice 002

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `SignInScreen.tsx` / `styles.ts` | overflow | empilhar pelo fundo |
| `useSignInForm.ts` | erros | `hasFieldErrors` |
| `TextField` | HelperText | causa da altura extra |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end / backend / OpenAPI | sem mudança |

## Resultado por stack

- mobile: CTAs do login permanecem visíveis com erro de campo

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/hooks/useSignInForm.ts`
- task 790, índice, slice 002, este handoff

## Validações executadas

- eslint — passou

## Pendências ou bloqueios

- conferir no Expo o submit com campos inválidos

## Próxima ação sugerida

- tocar Entrar sem preencher e ver se Criar conta e Esqueci minha senha continuam na tela

## Próximo contexto recomendado

- `mobile/src/features/auth/screens/SignInScreen.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: Asaas / contrato
- motivo: fora desta task
