# Task 556 - Contrato e requisitos: cadastro só do responsável + filhos autenticados

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts (openapi)
- requirements

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml`

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- `nao se aplica`

## Contexto de negocio

### Por que

O onboarding público hoje cria responsável + criança + anamnese de uma vez. O produto passa a cadastrar só o responsável, pagar, e só então cadastrar N filhos dentro da plataforma.

### O que

Atualizar requisitos e OpenAPI: register sem filho; novo POST autenticado de filho com anamnese e código único; parentesco no filho.

### Comportamento esperado

- `POST /guardians/register` exige só `guardian` (sem `child`/`anamnese`)
- Resposta do register não inclui criança; `accessGranted` permanece false
- `POST /guardians/me/children` (bearer + `responsavel` + `accessGranted`) cria filho + anamnese + `patientCode` + `suggestedTrailCategories`
- `GET /guardians/me/children` continua listando todos os filhos
- `POST /patients` do profissional **permanece** atômico (responsável + criança + anamnese)
- Requirements 001 e 002 descrevem o novo fluxo

### Fora de escopo

- Implementar backend ou UI
- Mudar preços/Asaas
- Cadastro de filho no mobile

## Slice vertical

### Identificador do slice

Slice 049 - Cadastro público só do responsável

### Arquivo do slice

- `tasks/slices/049-cadastro-responsavel-sem-filho.md`

## Permissoes

- Register: público
- POST children: `responsavel` autenticado com `accessGranted`

## Casos de erro mapeados

- 400 validação / menoridade / CPF inválido / anamnese incompleta
- 401/403 no POST children
- 409 CPF/e-mail duplicado
- Register legado (payload com child) deixa de ser aceito — breaking change documentada

## Decisoes humanas confirmadas

- Cadastro público só do responsável
- Depois do cadastro → pagamento
- Depois do acesso → N filhos, cada um com perfil, trilha e código único
- Web do responsável liberada; cadastro do filho dentro da plataforma

## Premissas adotadas pela IA

- Parentesco sai do register público e entra no filho (`Child.kinship`); `GuardianProfile.kinship` fica opcional/legado
- Sem teto de filhos
- Assinatura continua por conta, não por filho
- Trilha individual = categorias da pergunta 6 da anamnese daquele filho (já é o modelo por `childId`)

## Criterios de aceite

- [x] `RegisterGuardianRequest` contém apenas `guardian`
- [x] Novo schema `CreateGuardianChildRequest` (`child` + `anamnese` + parentesco)
- [x] `POST /guardians/me/children` documentado (201 com `Child` + `Anamnese`)
- [x] `POST /patients` documentado como fluxo profissional separado, ainda atômico
- [x] `requirements/001-escopo-produto.md` §4.3 e §7 atualizados
- [x] `requirements/002-regras-de-negocio.md` §3 separado em cadastro do responsável vs cadastro do filho autenticado
- [x] Breaking change do register registrada na descrição do path

## Casos de borda

- Contas já existentes com um filho criado no register antigo
- Responsável recém-pago sem filhos

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos atuais | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | reescrever fluxo | sim |
| Contrato | `contracts/openapi.yaml` schemas Guardian/Child/Anamnese e path `/guardians/register` | breaking change | sim |

## Orçamento de contexto

- medio
- estrategia de reducao: só paths/schemas de guardians/patients/register; não reler trilhas/jogos

## Dependencias

- Nenhuma task nova. Histórico: Tasks 010/011 (done)

## Resultado da execucao

### Resumo por stack

- **contracts**: `POST /guardians/register` agora exige só `guardian` (breaking change documentada). Novo `POST /guardians/me/children` com `CreateGuardianChildRequest`/`CreateGuardianChildResponse`. `POST /patients` usa `CreatePatientRequest` e permanece atômico. `Child.kinship` canônico; `GuardianProfile.kinship` legado/nullable.
- **requirements**: escopo 4.3/7 e regras §3/§5.2 descrevem cadastro público só do responsável, filhos autenticados e seleção no mobile.

### Relação com o slice

- Slice 049: contrato pronto para a Task 557. Slice permanece `todo` (API e wizard pendentes).

### Decisões técnicas

- Payload legado com `child`/`anamnese` no register deve ser 400.
- Profissional não reutiliza mais `RegisterGuardianRequest`.
- Sem teto de filhos no contrato.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slices 049 e 050

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `requirements/001-escopo-produto.md` | reescrever 4.3 e 7 | novo fluxo |
| `requirements/002-regras-de-negocio.md` | reescrever §3 e 5.2 | cadastro vs filho |
| `contracts/openapi.yaml` paths/schemas guardians/patients | breaking change | contrato |

### Evitado

- backend, front-end, mobile, trilhas, jogos

## Handoff

- Caminho: `.agents/state/handoffs/TASK-556.md`
- Próximo contexto: Task 557 (`backend/src/modules/guardians/**` + contrato atualizado)

## Arquivos alterados

- `contracts/openapi.yaml`
- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`
- `tasks/change-requests/556-contrato-cadastro-responsavel-sem-filho.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-556.md`

## Validacoes executadas

- Revisão manual dos paths `/guardians/register`, `/guardians/me/children` (GET+POST) e `/patients` POST
- Critérios de aceite da task conferidos contra o YAML e os requirements

## Pendencias pos-task

- Task 557 implementar a API
- Task 558 wizard web

## Status final

done
