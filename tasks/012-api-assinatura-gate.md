# Task 012 - API de assinatura e gate de acesso

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` subscription

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- `nao se aplica`

### Regra de aderencia visual

- Sem UI.

## Contexto de negocio

### Por que

Acesso completo depende de pagamento.

### O que

Assinatura, status, gate e abstracao de gateway (TBD).

### Comportamento esperado

- Bloqueia sem assinatura
- Confirmacao libera
- Master isento (premissa)

### Fora de escopo

- Gateway definitivo

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: profissional/responsavel
- Casos de erro: pendente/recusado
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: webhook simulado

## Especificacao tecnica

### Deve

- Interface provider
- Fake provider testavel

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Hardcode gateway sem decisao

## Entradas

- `requirements/001-escopo-produto.md`
- `requirements/003-requisitos-nao-funcionais.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/`

## Dependencias

- Tasks 008 e 010

## Slice vertical

### Identificador do slice

Slice 005 - Assinatura

### Arquivo do slice

- `tasks/slices/005-assinatura-liberacao-acesso.md`

### Objetivo de negócio

Gate pagamento.

### Entrega verificável do slice

API gate.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/005-assinatura-liberacao-acesso.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |
| NFR | `requirements/003-requisitos-nao-funcionais.md` | LGPD/storage | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- Guard bloqueia
- Fake sucesso libera

## Instrucoes de implementacao

- Documentar env vars futuras

## Validacao esperada

- npm run test
- npm run lint

## Entregaveis esperados

- API assinatura

## Riscos ou ambiguidades

- Gateway/precos TBD

## Resultado da execucao

### Resumo por stack

- **backend**: módulo `SubscriptionsModule` com `PaymentProvider` + `FakePaymentProvider`; checkout/confirm/webhook fake; `AccessGrantedGuard` bloqueia sem assinatura; sucesso define `accessGranted=true` no perfil profissional/responsável; master isento.

### Relação com o slice

- Slice 005 permanece aberto até Task 013 (UI pagamento).

### Decisões técnicas

- Provider abstrato injetável (`PAYMENT_PROVIDER`, default `fake`); gateway real TBD sem hardcode.
- `amountCents=null` — valores comerciais não inventados.
- Endpoints JWT: `GET /subscriptions/me`, `GET /subscriptions/access`, `POST /subscriptions/checkout`, `POST /subscriptions/confirm`.
- Webhook simulado público: `POST /subscriptions/webhooks/fake`.
- Guard exportado para uso futuro em rotas pagas; probe em `/subscriptions/access`.
- Env vars futuras documentadas em `.env.example`.
- Nenhuma dependência de produção nova.

### Trade-offs

- Checkout exige JWT (cadastro 009/011 ainda não cria sessão) — Task 013 deve autenticar antes do pagamento ou evoluir o fluxo.
- Provider não-fake cai no fake até decisão humana do gateway.

### Contrato

- Paths/schemas de subscription adicionados em `contracts/openapi.yaml`.

### Referência visual

- nao se aplica

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/005-assinatura-liberacao-acesso.md`
- handoff `TASK-011.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002 §5 | regras | pagamento/gate/master |
| requirements 003 | NFR | acesso por perfil |
| openapi | API | paths subscription |
| ARCHITECTURE/SECURITY | back | módulo + adapter externo |

### Evitado

- design-system / front / mobile (sem UI)

## Handoff

- Caminho: `.agents/state/handoffs/TASK-012.md`
- Decisões: fake provider; guard; master isento; amount null
- Próximo contexto: Task 013 (tela pagamento web)
- Pendências: gateway/valores reais; UI 013; aplicar guard em rotas de produto

## Arquivos alterados

### backend

- `backend/src/modules/subscriptions/**`
- `backend/src/modules/professionals/**` (updateAccessGranted / grantAccess)
- `backend/src/modules/guardians/**` (findProfileByUserId / grantAccess)
- `backend/src/modules/auth/auth.module.ts` (exports Jwt/Passport)
- `backend/src/app.module.ts`
- `backend/src/database/migrations/1740000000000-CreateSubscriptionsTable.ts`
- `backend/src/database/typeorm.datasource.ts`
- `backend/.env.example`

### contrato

- `contracts/openapi.yaml`

### governança

- `tasks/012-api-assinatura-gate.md`
- `tasks/000-index.md`
- `tasks/slices/005-assinatura-liberacao-acesso.md`
- `.agents/state/handoffs/TASK-012.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok (27 tests)
- `npm run typecheck` — ok

## Aderencia ao design system

- nao se aplica (API)

## Pendencias pos-task

- Task 013 — tela pagamento web consumindo esta API
- Gateway/valores definitivos (decisão humana)
- Aplicar `AccessGrantedGuard` nas rotas de produto pós-onboarding
- Fluxo pós-cadastro sem sessão (login antes do checkout)

## Status final

done
