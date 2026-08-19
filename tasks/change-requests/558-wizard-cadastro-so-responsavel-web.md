# Task 558 - Wizard web: cadastro só do responsável e redirect ao pagamento

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

- `POST /guardians/register` (contrato da Task 556)

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

- Manter `AuthLayout`, tokens, Input/Button e steps do wizard atual
- Remover etapas Criança / Motivo / Perfil
- Lacuna: sem print novo; não redesenhar o auth

## Contexto de negocio

### Por que

O wizard público ainda pede criança e anamnese antes do pagamento.

### O que

Deixar `/cadastro/responsavel` só com dados do responsável + acesso (e-mail/senha) e, no sucesso, ir para `/assinatura`.

### Comportamento esperado

- Etapas: Responsável → Acesso (ou uma página só, se couber sem perder validação)
- Campos: nome, nascimento (18+), CPF, telefone, sexo, e-mail, senha forte
- Sem parentesco, sem dados da criança, sem anamnese
- Não chama `setSession`
- Redirect `/assinatura` com `audience: 'responsavel'`, e-mail e `fromRegistration`; **sem** `patientCode`
- Link “Já tenho conta” permanece

### Fora de escopo

- Área autenticada (Task 559)
- Cadastro de filho (Task 560)
- Checkout Asaas (já existe)

## Slice vertical

### Identificador do slice

Slice 049 - Cadastro público só do responsável

### Arquivo do slice

- `tasks/slices/049-cadastro-responsavel-sem-filho.md`

## Permissoes

- Visitante; autenticado é redirecionado para o pós-login já existente

## Casos de erro mapeados

- Validação por etapa
- 409 e-mail/CPF
- Falha de rede no submit (`role="alert"`)

## Decisoes humanas confirmadas

- Cadastro público só do responsável
- Finalizou → pagamento

## Premissas adotadas pela IA

- Duas etapas (identidade + acesso) em vez de uma, para não inflar a tela; se o layout atual compactar bem, uma etapa única é aceitável desde que a validação cubra todos os campos
- Gate `/assinatura` já funciona sem `patientCode` (hoje é opcional)

## Criterios de aceite

- [x] Wizard não coleta criança nem anamnese
- [x] Payload alinhado ao novo `RegisterGuardianRequest`
- [x] Sucesso navega para `/assinatura` sem sessão
- [x] Lint, testes do RegisterGuardian e build ok
- [x] Acessibilidade: labels, erros, `aria-current` nas etapas restantes

## Casos de borda

- Voltar etapa
- Usuário já autenticado no cadastro

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 049, Tasks 556/557
- `front-end/docs/ai/ACCESSIBILITY.md` (UI)

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI | `design-system/front/Design_System_Evolente_Desktop.md` | wizard | sim |
| Página atual | `front-end/src/pages/Auth/RegisterGuardian/**` | reduzir etapas | sim |
| Service | `front-end/src/services/guardians/guardianService.ts` | payload | sim |
| Gate | `front-end/src/pages/Auth/SubscriptionGate/**` | state sem patientCode | sim se quebrar |

## Orçamento de contexto

- baixo/medio
- estrategia de reducao: só RegisterGuardian + service + types; não abrir o dashboard

## Dependencias

- Task 556
- Task 557

## Resultado da execucao

### Resumo por stack

- **front-end**: `/cadastro/responsavel` ficou com duas etapas (Responsável → Acesso). Removidos parentesco, criança e anamnese. Submit envia só `{ guardian }` e redireciona para `/assinatura` sem `setSession` e sem `patientCode`. Schemas de criança/anamnese permaneceram no arquivo para reuso na Task 560.

### Relação com o slice

- Slice 049: entrega web verificável concluída. Com 556/557/558 done, o slice fecha.

### Decisões técnicas

- Duas etapas para não inflar a tela; validação por etapa.
- `GuardianProfile.kinship` no tipo front passou a `string | null`.
- Adapter de cadastro deixa de mapear `child`/`anamnese`.
- CSS de anamnese no wizard público ficou intacto para o cadastro autenticado de filho.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 049, Tasks 556/557, `front-end/docs/ai/ACCESSIBILITY.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI | AuthLayout, tokens, wizard |
| `front-end/src/pages/Auth/RegisterGuardian/**` | reduzir etapas | implementação |
| `front-end/src/services/guardians/guardianService.ts` | payload | `{ guardian }` |
| `front-end/docs/ai/AGENTS.md` / `FRONTEND_PATTERNS.md` / `SECURITY.md` | padrões front | page → service → adapter |
| `contracts/openapi.yaml` RegisterGuardianRequest/Response | payload | alinhamento |

### Evitado

- dashboard do responsável, mobile, checkout Asaas, backend

## Handoff

- Caminho: `.agents/state/handoffs/TASK-558.md`
- Próximo contexto: Task 559 (Slice 050 — área web do responsável)

## Arquivos alterados

- `front-end/src/pages/Auth/RegisterGuardian/index.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/index.test.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`
- `front-end/src/constants/guardianOptions.ts`
- `front-end/src/types/guardian.ts`
- `front-end/src/services/adapters/adaptGuardianRegistration.ts`
- `tasks/change-requests/558-wizard-cadastro-so-responsavel-web.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-558.md`

## Validacoes executadas

- `npx eslint` nos arquivos do wizard — passou
- `npx vitest run src/pages/Auth/RegisterGuardian/index.test.tsx` — 3 testes passaram
- `npx vite build` — passou
- `npx tsc --noEmit` — falha pré-existente em `tsconfig.json` (`ignoreDeprecations`), fora do escopo

## Qualidade estrutural

- Tipos reutilizáveis permaneceram em `src/types/guardian.ts`
- Adapter em `services/adapters/`
- Schemas de criança/anamnese mantidos em `schemas.ts` para a Task 560; não extraídos para página nova nesta task

## Aderencia ao design system

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md` (artefato)
- Mantidos AuthLayout, Input/Button, tokens e steps do wizard
- Lacuna: sem print novo do cadastro só do responsável; etapas de criança removidas sem redesenhar o auth

## Acessibilidade aplicada

- Labels nos campos; erros em texto; `role="alert"` na falha de submit
- `aria-current="step"` nas etapas restantes; `aria-busy` no envio
- Ícones decorativos com `aria-hidden="true"`
- Link “Já tenho conta — entrar” com destino explícito

## Pendencias pos-task

- Nenhuma no Slice 049
- Próxima: Task 559 (shell web do responsável)

## Status final

done
