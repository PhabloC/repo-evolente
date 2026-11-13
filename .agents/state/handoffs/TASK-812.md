# Handoff - Task 812

## Task

- identificador: 812
- título: Botão falar com o suporte no login mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 002
- objetivo de negócio: autenticação e recuperação de senha
- entrega verificável: CTA mailto no login mobile

## Decisões preservadas

- decisão: CTA no login (não no paywall), espelhando Task 788 com `Button` ghost + `Linking` mailto
- motivo: pedido explícito para Apple/mobile na página de login; web já tem suporte na assinatura (811)
- impacto: mesmo e-mail `evolenteapp@gmail.com`; telefone e tablet compartilham `loginForm`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/812-botao-falar-com-suporte-login-mobile.md`
- `tasks/slices/002-autenticacao.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `SignInScreen.tsx` / `styles.ts` | UI login | inserir CTA |
| `openResponsibleSignup.ts` | padrão Linking | espelhar mailto |
| `front-end/.../support.ts` | e-mail | mesmo endereço |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| paywall/IAP | fora de escopo |
| OpenAPI / backend | sem API |
| front-end SubscriptionGate | já feito na 811 |

## Resultado por stack

- front-end: n/a
- backend: n/a
- mobile: CTA suporte no login

## Arquivos alterados

- `mobile/src/features/auth/constants.ts`
- `mobile/src/features/auth/utils/openSupportEmail.ts`
- `mobile/src/features/auth/utils/openSupportEmail.test.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`

## Validações executadas

- validação: Jest `openSupportEmail.test.ts`

## Pendências ou bloqueios

- item: conferir no device iOS que o Mail abre; publicar build/OTA se necessário

## Próxima ação sugerida

- Nenhuma obrigatória; validar no app se desejado.

## Próximo contexto recomendado

- `SignInScreen.tsx` e `openSupportEmail.ts` se ajustar copy/e-mail.

## Contexto que não deve ser carregado na próxima etapa

- fonte: assinatura web, Asaas, IAP
- motivo: fora deste CTA de login
