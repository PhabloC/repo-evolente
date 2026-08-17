# Task 013 - Tela de pagamento web e orientacao ao app

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` subscription

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- Tela assinatura DS; estados loading/erro/sucesso.

## Contexto de negocio

### Por que

Pagar e orientar responsavel ao app.

### O que

Gate; profissional → dashboard; responsavel → CTA app.

### Comportamento esperado

- Status pendente/ativo
- CTA mobile
- Redirect gate

### Fora de escopo

- SDK gateway definitivo

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: sem assinatura
- Casos de erro: falha pagamento
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: retorno checkout

## Especificacao tecnica

### Deve

- Fake/abstracao Task 012
- Valor TBD na copy

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Preco definitivo inventado

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`
- `requirements/001-escopo-produto.md`

## Dependencias

- Task 012

## Slice vertical

### Identificador do slice

Slice 005 - Assinatura

### Arquivo do slice

- `tasks/slices/005-assinatura-liberacao-acesso.md`

### Objetivo de negócio

UI pagamento.

### Entrega verificável do slice

Gate web.

### Fora do slice

- Mobile checkout

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
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Gate bloqueia
- Fake sucesso libera

## Instrucoes de implementacao

- Copy valor TBD

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- UI pagamento

## Riscos ou ambiguidades

- Gateway TBD

## Resultado da execucao

### Resumo por stack

- **front-end**: `/assinatura` com login no gate (JWT), checkout+confirm fake, copy “valor a definir”; profissional liberado → dashboard; responsável → CTA app; `PrivateRoutes` + login redirecionam sem `accessGranted`.

### Relação com o slice

- Slice 005 concluído (API 012 + UI 013).

### Decisões técnicas

- Checkout exige JWT → formulário de login no gate pós-cadastro (e-mail pré-preenchido).
- `completeFakeSubscriptionPayment` = checkout + confirm success.
- `accessGranted` persistido no `authStore`; `resolvePostAuthPath` centraliza redirect.
- Valor não inventado (“a definir”); botão “Concluir pagamento (simulado)”.
- Nenhuma dependência nova.

### Trade-offs

- Sem prints/DS específico de checkout: AuthLayout + tokens + estados loading/erro/sucesso.
- Links de store do app ainda TBD — CTA textual.
- Responsável pode abrir área web opcional após pagamento (acesso liberado).

### Contrato

- Consome `/subscriptions/me`, `/checkout`, `/confirm`.

### Referência visual

- DS Desktop documental; estados de formulário/status.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 005
- handoff `TASK-012.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | tokens/estados |
| openapi subscriptions | API | endpoints |
| ARCHITECTURE/ACCESSIBILITY | front | estrutura + a11y |
| requirements 001/002 | regras | pós-pagamento app |

### Evitado

- mobile / backend docs

## Handoff

- Caminho: `.agents/state/handoffs/TASK-013.md`
- Decisões: login no gate; fake pay; redirect por perfil; accessGranted no store
- Próximo contexto: Task 014 (API conteúdos/storage) conforme index
- Pendências: gateway real; links das stores

## Arquivos alterados

### front-end

- `front-end/src/pages/Auth/SubscriptionGate/**`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/services/subscriptions/subscriptionService.ts`
- `front-end/src/types/subscription.ts`
- `front-end/src/utils/resolvePostAuthPath.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/hooks/useAuth.ts`
- `front-end/src/routes/PrivateRoutes.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`

### governança

- `tasks/013-tela-pagamento-web.md`
- `tasks/000-index.md`
- `tasks/slices/005-assinatura-liberacao-acesso.md`
- `.agents/state/handoffs/TASK-013.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok
- `npm run build` — ok

## Qualidade estrutural

- Tipos em `types/subscription.ts`
- Service em `services/subscriptions/`
- Util `resolvePostAuthPath` em `utils/`

## Acessibilidade aplicada

- Labels no login do gate; erros `role="alert"`; status `role="status"`; `aria-busy` em loading/submit; hierarquia h1 AuthLayout

## Aderencia ao design system

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md`
- Evidências: AuthLayout, Input, Button, tokens, estados
- Lacuna: sem print de checkout — layout documental

## Pendencias pos-task

- Gateway/valores reais
- Links das app stores
- Aplicar guard em mais rotas de produto conforme evolução

## Status final

done
