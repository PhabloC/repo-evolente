# Handoff - Task 428

## Task

- identificador: 428
- título: Capa e vidro nas telas auth de cadastro e recovery
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 014
- objetivo de negócio: template auth unificado
- entrega verificável: mesma capa/vidro em cadastro e recovery

## Decisões preservadas

- decisão: reutilizar prop `coverBackground` (sem novo CSS)
- motivo: login já define o visual
- impacto: SubscriptionGate também usa capa

## Contexto utilizado

### Contexto mínimo lido

- Task 428, índice, Auth pages

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| páginas Auth | criar conta / recovery | `coverBackground` |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| OpenAPI / mobile | n/a |

## Resultado por stack

- front-end: capa+vidro em 4 telas auth
- backend: n/a
- mobile: n/a

## Arquivos alterados

- RegisterProfessional, RegisterGuardian, PasswordRecovery, PasswordReset
- task/index/handoff 428

## Validações executadas

- revisão de prop nas quatro páginas

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- aplicar no gate de assinatura se desejado

## Próximo contexto recomendado

- `AuthLayout` `coverBackground`

## Contexto que não deve ser carregado na próxima etapa

- requirements / OpenAPI
