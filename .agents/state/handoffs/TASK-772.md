# Handoff - Task 772

## Task

- identificador: 772
- título: Copy do login mobile sem menção a pagamento
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 039 - Gateway Asaas e ciclo de assinatura
- objetivo de negócio: gate mobile sem copy interpretável como pagamento no app
- entrega verificável: modal de login com mensagem neutra

## Decisões preservadas

- decisão: nova mensagem `Esta conta ainda não tem acesso ao aplicativo. Se precisar de ajuda, fale com o suporte Evolente.`
- motivo: Apple/Google Play barraram copy que citava assinatura e regularização no site
- impacto: modal `Não foi possível entrar` deixa de mencionar pagamento/assinatura/site

- decisão: perfil e `SubscriptionManagementCard` ficaram fora de escopo
- motivo: pedido focou no corpo do modal de login
- impacto: pode ser necessário nova task se a loja flagrar essas telas

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/772-copy-login-mobile-sem-mencao-pagamento.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `mobile/src/features/auth/services/authService.ts` | alterar copy | string do throw |
| `mobile/src/features/auth/screens/SignInScreen.tsx` | confirmar modal | título/corpo |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| Asaas / SubscriptionGate web | fora de escopo |
| design-system | só texto |

## Resultado por stack

- front-end ou next-js: n/a
- backend: n/a
- mobile: mensagem do gate de login atualizada

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `tasks/change-requests/772-copy-login-mobile-sem-mencao-pagamento.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `.agents/state/handoffs/TASK-772.md`

## Validações executadas

- validação: eslint/jest `authService` na sessão de execução

## Pendências ou bloqueios

- item: copy de pagamento ainda existe em perfil e `SubscriptionManagementCard` se a loja exigir limpeza mais ampla

## Próxima ação sugerida

- gerar novo build e reenviar para revisão; se rejeitarem de novo, limpar copy de perfil/assinatura no app

## Próximo contexto recomendado

- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx` (se ampliar)

## Contexto que não deve ser carregado na próxima etapa

- fonte: checkout Asaas / gate web
- motivo: não afetados por esta change
