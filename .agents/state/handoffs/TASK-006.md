# Handoff - Task 006

## Task

- identificador: 006
- título: Telas de autenticacao web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002 - Autenticacao
- objetivo de negócio: Auth web/mobile
- entrega verificável: telas auth web (parcial do slice; 007 mobile pendente)

## Decisões preservadas

- decisão: sessão real via authStore + localStorage (`evolente:web-auth`); hydrate no boot
- motivo: substituir preview da Task 003
- impacto: PrivateRoutes/RoleGuard redirecionam para `/entrar`

- decisão: CTAs cadastro profissional/responsável como placeholders
- motivo: fora de escopo desta task
- impacto: rotas `/cadastro/*` sem formulários de domínio

- decisão: `@hookform/resolvers` adicionado para zodResolver
- motivo: formulários auth + lint/typecheck
- impacto: dependência nova justificada na task

- decisão: gate de assinatura não implementado
- motivo: slice 005 ainda inexistente; task proíbe pular
- impacto: pós-login vai ao dashboard

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/006-telas-auth-web.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-005.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | tokens/inputs |
| openapi auth | API | login/recovery/reset |
| ACCESSIBILITY + ARCHITECTURE | front/UI | a11y e estrutura |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| DS/mobile docs | Task 006 é web |
| backend docs | API já entregue na 005 |

## Resultado por stack

- front-end: auth web concluída
- backend/mobile: n/a

## Arquivos alterados

- `front-end/src/pages/Auth/**`, AuthLayout, authStore/service/adapter/types
- rotas, apiClient, .env.example, @hookform/resolvers
- task/index/slice/handoff

## Validações executadas

- lint/test/build: ok (5 tests)

## Pendências ou bloqueios

- Task 007 auth mobile; SMTP real; cadastros domínio; gate assinatura

## Próxima ação sugerida

- Executar Task 007 (`tasks/007-telas-auth-mobile.md`) se existir no backlog

## Próximo contexto recomendado

- task 007 + DS mobile (login) + openapi auth + mobile docs

## Contexto que não deve ser carregado na próxima etapa

- fonte: front-end docs / DS Desktop inteiro
- motivo: Task 007 é mobile; reutilizar apenas contrato auth se necessário
