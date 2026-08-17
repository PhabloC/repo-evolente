# Handoff - Task 007

## Task

- identificador: 007
- título: Telas de autenticacao mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002 - Autenticacao
- objetivo de negócio: Auth web/mobile
- entrega verificável: telas auth mobile (slice completo com 005+006+007)
- status do slice: done

## Decisões preservadas

- decisão: adapter OpenAPI camelCase (`tokens.accessToken` + `user.name`)
- motivo: contrato Task 001/005
- impacto: removido snake_case legado do shell

- decisão: profissional autenticado → UnsupportedRoleScreen (orientar web)
- motivo: SCOPE_EXCLUSIONS + task
- impacto: sem shell profissional no app

- decisão: remoção dos chips de previewRole
- motivo: auth real do Slice 002
- impacto: demo data fixa role responsavel

- decisão: recovery + reset no stack anônimo com deep link `redefinir-senha`
- motivo: paridade com API/web
- impacto: linking + params tipados

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/007-telas-auth-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-006.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Mobile | UI | toque/sem gamificação |
| openapi auth | API | login/recovery/reset |
| ARCHITECTURE/CODE_STYLE | mobile | camadas feature |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| DS Desktop / front-end | Task 007 é mobile |
| backend docs | API já na 005 |

## Resultado por stack

- mobile: auth concluída
- front/back: n/a

## Arquivos alterados

- `mobile/src/features/auth/**`, apiClient, routes, linking, .env.example
- task/index/slice/handoff

## Validações executadas

- lint/typecheck/test: ok (5 tests)

## Pendências ou bloqueios

- SMTP real; cadastros domínio (008+)

## Próxima ação sugerida

- Executar Task 008 (`tasks/008-api-cadastro-profissional.md`) se for a próxima do backlog

## Próximo contexto recomendado

- task 008 + openapi users/profissional + backend docs

## Contexto que não deve ser carregado na próxima etapa

- fonte: DS mobile / telas auth mobile
- motivo: Task 008 é API backend de cadastro
