# Task 001 - Contrato OpenAPI base (auth, users, roles)

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` (paths base)

## Modo de execucao

cross-stack

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

Contrato vazio bloqueia integracoes.

### O que

Schemas/paths base de auth, users e roles no OpenAPI.

### Comportamento esperado

- User/Role documentados
- Status ativo/inativo previsto

### Fora de escopo

- Endpoints de dominio (pacientes, trilhas, pagamento)

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: nao se aplica
- Casos de erro: schema incompleto
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: OpenAPI 3.1

## Especificacao tecnica

### Deve

- Atualizar contracts/openapi.yaml
- Documentar roles master/profissional/responsavel

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Implementar codigo de produto

## Entradas

- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`

## Dependencias

Nenhuma

## Slice vertical

### Identificador do slice

Slice 001 - Fundacao e contrato base

### Arquivo do slice

- `tasks/slices/001-fundacao-contrato-base.md`

### Objetivo de negócio

Fundar contrato e identidade.

### Entrega verificável do slice

Contrato base versionado.

### Fora do slice

- UI
- Persistencia

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/001-fundacao-contrato-base.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| API | `contracts/openapi.yaml` | API | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia: so auth/users/roles

## Criterios de conclusao

- paths auth/users preenchidos
- roles documentados
- status inativo no schema

## Instrucoes de implementacao

- Partir do OpenAPI atual
- Nao incluir gamificacao

## Validacao esperada

- Validar YAML OpenAPI

## Entregaveis esperados

- contracts/openapi.yaml

## Riscos ou ambiguidades

- Payloads podem evoluir

## Resultado da execucao

Contrato OpenAPI 3.1 preenchido com paths e schemas base de auth, users e roles. Sem codigo de produto nas stacks.

### Por stack

- front-end: contrato compartilhado disponivel; sem implementacao nesta task
- backend: contrato compartilhado disponivel; sem implementacao nesta task
- mobile: contrato compartilhado disponivel; sem implementacao nesta task

### Slice

- Slice 001 permanece em andamento: Task 001 concluida; Tasks 002/003/004 ainda planned
- Entrega verificavel parcial do slice: contrato base versionado

### Decisoes tecnicas

- Roles autenticaveis: `master`, `profissional`, `responsavel`
- Paciente/crianca documentado como sem login (fora do enum Role)
- Status de conta: `active` | `inactive` (inativacao, sem exclusao)
- Auth: login, logout, password-recovery, password-reset
- Users: me, list, get by id, patch status
- Roles: GET /roles com definicoes documentadas
- Endpoints publicos de auth com `security: []`
- Sem endpoints de dominio (pacientes, trilhas, pagamento, gamificacao)

### Trade-offs

- Server URL permanece `https://api.example.com` como placeholder ate ambiente real
- `refreshToken` opcional no schema de tokens (payloads podem evoluir)

### Contrato

- `contracts/openapi.yaml` e a fonte de verdade atualizada

### Referencia visual

- nao se aplica (sem UI)

## Contexto utilizado

### Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, `tasks/slices/001-fundacao-contrato-base.md`

### Contexto sob demanda carregado

- `requirements/001-escopo-produto.md` — papeis e escopo
- `requirements/002-regras-de-negocio.md` — login, recuperacao, inativacao
- `contracts/openapi.yaml` — partida e entrega

### Contexto nao carregado

- `design-system/front/` e `design-system/mobile/` — sem UI
- docs locais de stacks — sem implementacao de codigo
- `ACCESSIBILITY.md` — sem UI

## Handoff

- `.agents/state/handoffs/TASK-001.md`
- Proximo contexto recomendado: Task 002 (fundacao backend identidade) com este contrato

## Arquivos alterados

- `contracts/openapi.yaml`
- `tasks/001-contrato-openapi-base.md`
- `tasks/000-index.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-001.md`

## Validacoes executadas

- `npx @redocly/cli lint contracts/openapi.yaml --extends=minimal` — valido; warning residual de server example.com (placeholder)

## Aderencia ao design system

- nao se aplica (sem UI)

## Pendencias pos-task

- Task 002 deve implementar fundacao backend alinhada a este contrato
- Tasks 003/004 (shells) dependem do contrato + fundacao backend
- Substituir URL de server placeholder quando ambiente existir
- Payloads de token/auth podem evoluir em tasks futuras

## Status final

done
