# Handoff - Task 769

## Task

- identificador: 769
- título: Opções de área a partir das especialidades cadastradas
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 063
- objetivo de negócio: filtrar profissionais por área real
- entrega verificável: select alimentado por `availableSpecialties`

## Decisões preservadas

- decisão: especialidades únicas dos elegíveis, antes de search/specialty
- motivo: o select não pode colapsar ao filtrar
- impacto: lista reflete o cadastro, não um catálogo fixo

## Contexto utilizado

### Contexto mínimo lido

- task 769, Slice 063, handoffs 767/768

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| OpenAPI | schema | `availableSpecialties` |
| professionals.service | extração | uniqueSpecialties |
| página Professionals | UI | opções do select |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile | fora de escopo |

## Resultado por stack

- contracts/backend: campo na listagem
- front-end: select dinâmico; constante removida

## Arquivos alterados

- openapi, service, util, types, hook, página, teste; delete professionalAreas.ts

## Validações executadas

- jest 12 ok; vitest 2 ok

## Pendências ou bloqueios

- Conferir `/profissionais` logado como responsável

## Próxima ação sugerida

- Nenhuma task extra

## Próximo contexto recomendado

- `/profissionais` autenticado

## Contexto que não deve ser carregado na próxima etapa

- cadastro profissional e Asaas
