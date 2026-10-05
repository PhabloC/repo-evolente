# Handoff - Task 768

## Task

- identificador: 768
- título: Filtro por área no diretório de profissionais (web)
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 063
- objetivo de negócio: responsável filtra profissionais por área
- entrega verificável: seletor Área em `/profissionais`

## Decisões preservadas

- decisão: catálogo canônico no front (fono, psico, TO, fisio, psicopedagogia)
- motivo: especialidade no cadastro é texto livre
- impacto: áreas fora da lista ainda são acháveis pela busca

## Contexto utilizado

### Contexto mínimo lido

- task 768, Slice 063, ACCESSIBILITY.md

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| página Professionals | UI | select na toolbar |
| hook/serviço | query | `specialty` |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile | fora de escopo |

## Resultado por stack

- front-end: Busca + Área na toolbar; empty state considera filtro

## Arquivos alterados

- constants/professionalAreas, types, service, hook, página, CSS, teste

## Validações executadas

- vitest Professionals: 2 ok
- eslint: ok

## Pendências ou bloqueios

- Confirmar visual com sessão de responsável no browser

## Próxima ação sugerida

- Nenhuma task de follow-up

## Próximo contexto recomendado

- `/profissionais` autenticado como responsável

## Contexto que não deve ser carregado na próxima etapa

- backend do diretório, salvo regressão da query
