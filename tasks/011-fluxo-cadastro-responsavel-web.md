# Task 011 - Fluxo multi-etapa de cadastro responsavel na web

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

- `contracts/openapi.yaml#/paths` register guardian/child/anamnese

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

- Wizard com estados DS.

## Contexto de negocio

### Por que

Onboarding web antes do app.

### O que

Wizard responsavel → crianca → anamnese → pagamento.

### Comportamento esperado

- Etapas
- Pergunta 6 multi-select
- Redirect pagamento

### Fora de escopo

- App

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: publico
- Casos de erro: validacao por etapa
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: voltar etapa

## Especificacao tecnica

### Deve

- Perguntas 1-8

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Dashboard web do responsavel pos-pagamento

## Entradas

- `requirements/002-regras-de-negocio.md`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`

## Dependencias

- Task 010

## Slice vertical

### Identificador do slice

Slice 004 - Onboarding responsavel

### Arquivo do slice

- `tasks/slices/004-onboarding-responsavel-anamnese.md`

### Objetivo de negócio

UI onboarding.

### Entrega verificável do slice

Wizard web.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/004-onboarding-responsavel-anamnese.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |
| API | `contracts/openapi.yaml` | API | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- Wizard completo
- Redirect pagamento

## Instrucoes de implementacao

- Mostrar codigo do paciente se API retornar

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- UI wizard

## Riscos ou ambiguidades

- Sem prints

## Resultado da execucao

### Resumo por stack

- **front-end**: wizard em `/cadastro/responsavel` (responsável → criança → anamnese Q1–8); consome `POST /guardians/register`; após sucesso redireciona para `/assinatura` com `patientCode` e `audience: 'responsavel'`, **sem** criar sessão nem liberar dashboard.

### Relação com o slice

- Slice 004 concluído (API 010 + UI 011).

### Decisões técnicas

- Não chama `setSession` após cadastro (API não retorna tokens; evita liberar dashboard).
- Payload atômico alinhado à Task 010 (guardian + child + anamnese).
- Pergunta 6 multi-select → áreas enviadas no payload; personalização de trilha no backend.
- Gate `/assinatura` exibe `patientCode` quando presente; CTA de pagamento permanece placeholder.
- Validação por etapa (zod); CPF e maioridade no front antes do submit.
- Nenhuma dependência de produção nova.

### Trade-offs

- Sem prints: wizard alinhado a tokens/Input/Button do DS + AuthLayout; lacuna registrada.
- Login pós-cadastro ainda pode acessar áreas até Tasks 012/013 (gate real) — fluxo de cadastro em si não libera.

### Contrato

- Consome `POST /guardians/register` conforme OpenAPI Task 010.

### Referência visual

- DS Desktop documental; wizard com steps, labels, erros e estados loading.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/004-onboarding-responsavel-anamnese.md`
- handoff `TASK-010.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | formulários/estados wizard |
| openapi guardians/register | API | payload/response |
| ARCHITECTURE/ACCESSIBILITY | front | estrutura + a11y |
| requirements 002 | regras | campos Q1–8 |

### Evitado

- mobile / backend docs (single-stack front)

## Handoff

- Caminho: `.agents/state/handoffs/TASK-011.md`
- Decisões: redirect gate sem sessão; Q6 multi-select; exibir patientCode
- Próximo contexto: Task 012 (API assinatura/gate)
- Pendências: gateway real (012/013); gate no login

## Arquivos alterados

### front-end

- `front-end/src/types/guardian.ts`
- `front-end/src/constants/guardianOptions.ts`
- `front-end/src/utils/cpf.ts`
- `front-end/src/utils/cpf.test.ts`
- `front-end/src/utils/age.ts`
- `front-end/src/services/guardians/guardianService.ts`
- `front-end/src/services/adapters/adaptGuardianRegistration.ts`
- `front-end/src/pages/Auth/RegisterGuardian/**`
- `front-end/src/pages/Auth/SubscriptionGate/**`
- `front-end/src/routes/index.tsx`
- removido placeholder de cadastro responsável

### governança

- `tasks/011-fluxo-cadastro-responsavel-web.md`
- `tasks/000-index.md`
- `tasks/slices/004-onboarding-responsavel-anamnese.md`
- `.agents/state/handoffs/TASK-011.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok (11 tests)
- `npm run build` — ok

## Qualidade estrutural

- Tipos em `types/guardian.ts`
- Service + adapter separados
- Utils `cpf` e `age` em `utils/`
- Constantes de opções em `constants/guardianOptions.ts`
- Page RegisterGuardian com schemas por etapa

## Acessibilidade aplicada

- Labels nos inputs; radiogroup onde aplicável; steps com `aria-current`; erros com `role="alert"`; `aria-busy` no submit; hierarquia h1 no AuthLayout; nav de etapas com label acessível

## Aderencia ao design system

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md`
- Evidências: AuthLayout, Input, Button, tokens, wizard multi-etapa
- Lacuna: sem prints de registro responsável — layout documental; decisão: seguir padrão do cadastro profissional + estados DS

## Pendencias pos-task

- Tasks 012/013 — API/tela de assinatura real
- Gate de acesso no login para responsável sem `accessGranted`
- Montagem de trilha de conteúdo a partir de `suggestedTrailCategories` (catálogo)

## Status final

done
