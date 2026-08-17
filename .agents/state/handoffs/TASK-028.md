# Handoff - Task 028

## Task

- identificador: 028
- título: Template do login em criar conta e recuperar senha
- tipo: front
- modo de execução: single-stack
- status final: done
- arquivo: `tasks/change-requests/028-template-auth-login-cadastro-recovery.md`

## Slice vertical

- identificador: Slice 014
- status do slice: done

## Decisões preservadas

- decisão: shell visual do login vive em `AuthLayout`
- motivo: cadastro/recovery já usavam AuthLayout; herdam o template sem duplicar
- impacto: Login refatorado; Register*, PasswordRecovery, PasswordReset e SubscriptionGate no mesmo visual

- decisão: `wide` amplia o card para cadastros longos
- motivo: formulários densos (profissional/responsável)
- impacto: `cardWide` + `shellWide`

## Contexto utilizado

### Contexto mínimo lido

- AGENTS, GUIDE, context-map, index, CR-028, slice 014

### Contexto sob demanda carregado

| Fonte | Uso |
|---|---|
| Login / AuthLayout | extrair template |
| Register* / Password* | aplicar |

### Evitado

- mobile/, backend/, openapi

## Arquivos alterados

- `front-end/src/layout/AuthLayout/**`
- páginas Auth Login, Register*, PasswordRecovery, PasswordReset
- governança slice/CR/index/handoff

## Validações executadas

- test Auth / lint / build — ok

## Pendências

- Nenhuma

## Próxima ação sugerida

- Revisar visualmente `/cadastro/profissional`, `/cadastro/responsavel`, `/recuperar-senha`

## Próximo contexto recomendado

- Este handoff + AuthLayout

## Contexto que não deve ser carregado

- mobile/, backend/
