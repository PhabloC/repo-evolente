# Handoff - Task 001

## Task

- identificador: 001
- título: Contrato OpenAPI base (auth, users, roles)
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 001 - Fundacao e contrato base
- objetivo de negócio: Fundar contrato e identidade
- entrega verificável: Contrato base versionado (parcial do slice; shells e backend ainda pendentes)

## Decisões preservadas

- decisão: Roles autenticáveis = master | profissional | responsavel
- motivo: requisitos de perfis; criança sem login
- impacto: enum `Role` e path `/roles`

- decisão: UserStatus = active | inactive
- motivo: inativar, não excluir
- impacto: schema User + PATCH `/users/{userId}/status`

- decisão: só paths auth/users/roles nesta versão
- motivo: fora de escopo de domínio e gamificação
- impacto: contrato enxuto para desbloquear Task 002+

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/001-contrato-openapi-base.md`
- `tasks/slices/001-fundacao-contrato-base.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `requirements/001-escopo-produto.md` | regras | papéis e escopo |
| `requirements/002-regras-de-negocio.md` | regras | login, recovery, inativação |
| `contracts/openapi.yaml` | API | partida e entrega |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `design-system/front/` | sem UI |
| `design-system/mobile/` | sem UI |
| docs locais de stacks | sem código de produto |

## Resultado por stack

- front-end: contrato compartilhado; sem implementação
- backend: contrato compartilhado; sem implementação
- mobile: contrato compartilhado; sem implementação

## Arquivos alterados

- `contracts/openapi.yaml`
- `tasks/001-contrato-openapi-base.md`
- `tasks/000-index.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-001.md`

## Validações executadas

- Redocly lint (`--extends=minimal`): válido; warning de server example.com

## Pendências ou bloqueios

- implementar fundação backend (Task 002) alinhada ao contrato
- shells web/mobile (003/004) ainda planned no slice
- URL de server placeholder

## Próxima ação sugerida

- Executar Task 002 (`tasks/002-fundacao-backend-identidade.md`)

## Próximo contexto recomendado

- `tasks/002-fundacao-backend-identidade.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `contracts/openapi.yaml` (paths auth/users/roles)
- `backend/docs/ai/` conforme a Task 002 declarar

## Contexto que não deve ser carregado na próxima etapa

- fonte: `design-system/front/` e `design-system/mobile/`
- motivo: Task 002 é backend; UI só nas 003/004
