# Handoff - Task 012

## Task

- identificador: 012
- título: API de assinatura e gate de acesso
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 005 - Assinatura
- objetivo de negócio: Gate pagamento
- entrega verificável: API gate
- status do slice: in_progress (UI 013 pendente)

## Decisões preservadas

- decisão: `PaymentProvider` + `FakePaymentProvider`; `PAYMENT_PROVIDER=fake` por padrão
- motivo: gateway/valores TBD; sem hardcode de gateway real
- impacto: Task 013 consome fake; troca futura via DI/env

- decisão: sucesso → `subscription.active` + `accessGranted=true` no perfil; master isento
- motivo: requisitos §5 + premissa do index
- impacto: `AccessGrantedGuard` bloqueia profissional/responsável sem pagamento

- decisão: `amountCents=null`; env vars futuras documentadas
- motivo: não inventar preços
- impacto: copy TBD na UI 013

- decisão: checkout/confirm exigem JWT; webhook fake público
- motivo: segurança + caso de borda webhook simulado
- impacto: pós-cadastro 009/011 precisa login antes de pagar (013)

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/012-api-assinatura-gate.md`
- `tasks/slices/005-assinatura-liberacao-acesso.md`
- `.agents/state/handoffs/TASK-011.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002/003 | regras/NFR | pagamento/gate |
| openapi | API | paths |
| ARCHITECTURE/SECURITY | back | módulo/adapter |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system / front / mobile | sem UI |

## Resultado por stack

- backend + contrato: done

## Arquivos alterados

- `backend/src/modules/subscriptions/**`
- grant access em professionals/guardians
- migration subscriptions
- `contracts/openapi.yaml`
- task/index/slice/handoff

## Validações executadas

- lint/test/typecheck: ok (27 tests)

## Pendências ou bloqueios

- Task 013 UI; gateway real; aplicar guard em rotas de produto

## Próxima ação sugerida

- Executar Task 013 (`tasks/013-tela-pagamento-web.md`)

## Próximo contexto recomendado

- task 013 + DS Desktop assinatura + openapi subscriptions + front-end docs

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend docs completos / mobile
- motivo: Task 013 é front; carregar só paths OpenAPI de subscription
