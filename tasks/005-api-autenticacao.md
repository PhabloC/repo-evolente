# Task 005 - API de autenticacao e recuperacao de senha

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

- `contracts/openapi.yaml#/paths` auth

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

Porta de entrada de todos os perfis.

### O que

Login e-mail/senha, recovery e reset por link.

### Comportamento esperado

- Login retorna sessao
- Recovery por e-mail
- Reset com token
- Inativo nao autentica

### Fora de escopo

- Cadastro
- OAuth

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: qualquer role ativa
- Casos de erro: 401; token invalido; inativo
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: recovery nao enumeravel

## Especificacao tecnica

### Deve

- Alinhar OpenAPI
- SECURITY.md

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Revelar se e-mail existe

## Entradas

- `contracts/openapi.yaml`
- `backend/docs/ai/SECURITY.md`
- `requirements/002-regras-de-negocio.md`

## Dependencias

- Task 002

## Slice vertical

### Identificador do slice

Slice 002 - Autenticacao

### Arquivo do slice

- `tasks/slices/002-autenticacao.md`

### Objetivo de negócio

Autenticar.

### Entrega verificável do slice

API auth.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API | `contracts/openapi.yaml` | API | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| NFR | `requirements/003-requisitos-nao-funcionais.md` | LGPD/storage | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Testes auth
- Reset funcional

## Instrucoes de implementacao

- E-mail configuravel

## Validacao esperada

- npm run test
- npm run lint
- npm run build

## Entregaveis esperados

- API auth

## Riscos ou ambiguidades

- SMTP por ambiente

## Resultado da execucao

API de autenticação alinhada ao OpenAPI: login (AuthResponse), logout 204, password-recovery 202 não enumerável, password-reset 204 com token hasheado.

### Por stack

- backend: AuthController/Service; MailAdapter; repositório de reset tokens (in-memory + TypeORM + migration); testes de auth

### Slice

- Slice 002 `in_progress`: Task 005 done; Tasks 006/007 (UI) planned

### Decisoes tecnicas

- Login retorna `{ user, tokens: { accessToken, tokenType, expiresIn } }`
- Conta inativa → 403; credenciais inválidas → 401
- Recovery sempre mesma mensagem; e-mail via MailAdapter (log configurável; SMTP real por ambiente)
- Token de reset: random + SHA-256; TTL via `PASSWORD_RESET_TTL_MINUTES`
- Logout JWT stateless (204); sem blacklist nesta fase
- Sem novas dependências npm

### Trade-offs

- SMTP real não integrado — adapter registra envio; configurar provedor depois
- Logout sem revogação server-side (JWT)

### Contrato

- Paths `/auth/login|logout|password-recovery|password-reset` cobertos

### Referencia visual

- nao se aplica

## Contexto utilizado

### Contexto minimo

- AGENTS, GUIDE, context-map, 000-index, esta task, slice 002, handoff 004

### Contexto sob demanda carregado

- `contracts/openapi.yaml` (auth)
- `backend/docs/ai/SECURITY.md`, `ARCHITECTURE.md`
- `requirements/002` (auth), `003` (NFR), trechos 001

### Contexto nao carregado

- design-system, front/mobile docs

## Handoff

- `.agents/state/handoffs/TASK-005.md`
- Próximo: Task 006 telas auth web

## Arquivos alterados

- `backend/src/modules/auth/**`
- `backend/src/common/utils/auth-token.util.ts`
- `backend/src/patterns/adapters/mailAdapter.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/config/app.config.ts`
- `backend/src/database/typeorm.datasource.ts`
- `backend/src/database/migrations/1710000000000-CreatePasswordResetTokensTable.ts`
- `backend/.env.example`
- `tasks/005-api-autenticacao.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-005.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — 9 passed (5 auth + 4 users)
- `npm run build` — ok

## Aderencia ao design system

- nao se aplica

## Pendencias pos-task

- Telas auth web (006) e mobile (007)
- Integrar SMTP real no MailAdapter
- Opcional: blacklist/refresh token strategy

## Status final

done
