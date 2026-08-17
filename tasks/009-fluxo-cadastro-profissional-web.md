# Task 009 - Fluxo de cadastro profissional na web

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

- `contracts/openapi.yaml#/paths` register professional

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

- Formularios/estados DS desktop.

## Contexto de negocio

### Por que

Onboarding web do profissional.

### O que

Cadastro com toggle individual/clinica e redirect pagamento.

### Comportamento esperado

- Validacao
- Redirect ao gate

### Fora de escopo

- Gateway real

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: publico
- Casos de erro: duplicidade; clinica
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: tipo clinica

## Especificacao tecnica

### Deve

- Consumir Task 008
- Nao liberar dashboard

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada


## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`
- `requirements/002-regras-de-negocio.md`

## Dependencias

- Task 008

## Slice vertical

### Identificador do slice

Slice 003 - Onboarding profissional

### Arquivo do slice

- `tasks/slices/003-onboarding-profissional.md`

### Objetivo de negócio

UI cadastro.

### Entrega verificável do slice

Fluxo ate pagamento.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/003-onboarding-profissional.md`

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

- Campos do requisito
- Redirect pagamento

## Instrucoes de implementacao

- Copy multi-especialidade

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- UI cadastro

## Riscos ou ambiguidades



## Resultado da execucao

### Resumo por stack

- **front-end**: formulário completo em `/cadastro/profissional` (individual/clínica, multi-especialidade); consome `POST /professionals/register`; após sucesso redireciona para `/assinatura` (gate placeholder) **sem** criar sessão nem liberar dashboard.

### Relação com o slice

- Slice 003 concluído (API 008 + UI 009).

### Decisões técnicas

- Não chama `setSession` após cadastro (API não retorna tokens; evita liberar dashboard).
- Gate `/assinatura` público com CTA de pagamento desabilitado (“em breve”); gateway real fora de escopo.
- Especialidades via texto separado por vírgula (`parseSpecialties`).
- Default `VITE_API_BASE_URL` corrigido para `http://localhost:3000/api` (prefixo Nest).
- Nenhuma dependência de produção nova.

### Trade-offs

- Sem prints: formulário alinhado a tokens/Input/Button do DS + AuthLayout.
- Login pós-cadastro ainda pode acessar dashboard até Tasks 012/013 (gate real) — fluxo de cadastro em si não libera.

### Contrato

- Consome `POST /professionals/register` conforme OpenAPI Task 008.

### Referência visual

- DS Desktop documental; formulários com labels, erros e estados loading.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/003-onboarding-profissional.md`
- handoff `TASK-008.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | formulários/estados |
| openapi professionals/register | API | payload |
| ARCHITECTURE/ACCESSIBILITY | front | estrutura + a11y |
| requirements 002 | regras | campos |

### Evitado

- mobile / backend docs (single-stack front)

## Handoff

- Caminho: `.agents/state/handoffs/TASK-009.md`
- Decisões: redirect gate sem sessão; multi-especialidade; clínica condicional
- Próximo contexto: Task 010 (API cadastro responsável) ou próxima do index
- Pendências: gateway real (012/013); gate no login

## Arquivos alterados

### front-end

- `front-end/src/types/professional.ts`
- `front-end/src/services/professionals/professionalService.ts`
- `front-end/src/services/adapters/adaptProfessionalRegistration.ts`
- `front-end/src/services/adapters/adaptProfessionalRegistration.test.ts`
- `front-end/src/utils/parseSpecialties.ts`
- `front-end/src/utils/parseSpecialties.test.ts`
- `front-end/src/pages/Auth/RegisterProfessional/**`
- `front-end/src/pages/Auth/SubscriptionGate/**`
- `front-end/src/layout/AuthLayout/**`
- `front-end/src/constants/routes.ts`
- `front-end/src/routes/index.tsx`
- `front-end/src/services/http/apiClient.ts`
- `front-end/.env.example`

### governança

- `tasks/009-fluxo-cadastro-profissional-web.md`
- `tasks/000-index.md`
- `tasks/slices/003-onboarding-profissional.md`
- `.agents/state/handoffs/TASK-009.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok (9 tests)
- `npm run build` — ok

## Qualidade estrutural

- Tipos em `types/professional.ts`
- Service + adapter separados
- Utils `parseSpecialties` em `utils/`
- Pages RegisterProfessional e SubscriptionGate

## Acessibilidade aplicada

- Labels nos inputs; radiogroup para tipo de atuação; erros com `role="alert"`; status no gate com `role="status"`; `aria-busy` no form; hierarquia h1 no AuthLayout

## Aderencia ao design system

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md`
- Evidências: AuthLayout, Input, Button, tokens
- Lacuna: sem prints de registro

## Pendencias pos-task

- Tasks 012/013 — API/tela de assinatura real
- Gate de acesso no login para profissional sem `accessGranted`
- Cadastro responsável (slice 004)

## Status final

done
