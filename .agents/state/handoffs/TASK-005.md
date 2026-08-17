# Handoff - Task 005

## Task

- identificador: 005
- título: API de autenticacao e recuperacao de senha
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002 - Autenticacao
- objetivo de negócio: Autenticar
- entrega verificável: API auth (parcial do slice; UI 006/007 pendentes)

## Decisões preservadas

- decisão: AuthResponse OpenAPI com tokens.Bearer + expiresIn
- motivo: contrato Task 001
- impacto: AuthService.signIn

- decisão: recovery não enumerável + MailAdapter configurável
- motivo: requisitos + SECURITY
- impacto: password-recovery sempre 202 com mesma mensagem

- decisão: reset token hasheado (SHA-256) com TTL env
- motivo: segurança mínima sem nova dep
- impacto: password_reset_tokens + in-memory/TypeORM

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/005-api-autenticacao.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-004.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| openapi auth paths | API | contrato |
| SECURITY/ARCHITECTURE | back | JWT/hash/adapters |
| requirements 002/003 | regras/NFR | login/recovery |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system | sem UI |
| front/mobile docs | stack não envolvida |

## Resultado por stack

- backend: API auth concluída
- front/mobile: n/a

## Arquivos alterados

- `backend/src/modules/auth/**`, mail adapter, migration reset tokens
- task/index/slice/handoff

## Validações executadas

- lint/test/build: ok (9 tests)

## Pendências ou bloqueios

- UI auth web/mobile; SMTP real

## Próxima ação sugerida

- Executar Task 006 (`tasks/006-telas-auth-web.md`) se existir no backlog

## Próximo contexto recomendado

- task 006 + DS front (login) + openapi auth + front-end docs

## Contexto que não deve ser carregado na próxima etapa

- fonte: mobile docs / DS mobile
- motivo: Task 006 é web
