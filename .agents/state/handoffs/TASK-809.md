# Handoff - Task 809

## Task

- identificador: 809
- título: Aviso de assinatura expirada no login mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 039
- objetivo de negócio: ciclo Asaas com gate de acesso
- entrega verificável: login avisa expiração e renovação na web

## Decisões preservadas

- decisão: o aviso vale para assinatura que não é Apple e já teve pagamento (`firstPaidAt`) ou está overdue/suspended, sem acesso
- motivo: checkout cancelado sem pagamento não é assinatura expirada; compra Apple renova na App Store
- impacto: quem nunca assinou continua com a mensagem neutra da task 772; a biometria passa pelo mesmo gate

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- slice 039 e task 772

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `mobile/src/features/auth/services/authService.ts` | gate do login | mensagem |
| `mobile/src/features/auth/screens/SignInScreen.tsx` | modal | título |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `design-system/mobile/` | só texto do modal existente |

## Resultado por stack

- mobile: login bloqueado explica expiração e renovação na web

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/utils/resolveBlockedLoginMessage.ts`

## Validações executadas

- Jest authService e resolveBlockedLoginMessage: passou

## Pendências ou bloqueios

- item: nenhuma

## Próxima ação sugerida

- próxima task ou próximo passo: publicar o app (OTA ou build) para o aviso chegar no celular

## Próximo contexto recomendado

- arquivos/trechos que devem ser carregados: `mobile/src/features/auth/services/authService.ts`

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend e design-system
- motivo: a API já devolve o status da assinatura
