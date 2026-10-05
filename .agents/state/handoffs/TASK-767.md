# Handoff - Task 767

## Task

- identificador: 767
- título: Filtro por área no diretório de profissionais (API)
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 063
- objetivo de negócio: responsável descobre profissionais
- entrega verificável: query `specialty` em `GET /professionals`

## Decisões preservadas

- decisão: filtro por string em `specialties`, sem enum no cadastro
- motivo: especialidades já são texto livre
- impacto: UI escolhe valores canônicos; API aceita qualquer termo

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- Slice 063 e esta task

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | query | `specialty` |
| módulo professionals | filtro | service + DTO |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile | fora de escopo |
| design-system | API |

## Resultado por stack

- backend: filtro aplicado antes de nearby/others
- contracts: parâmetro documentado

## Arquivos alterados

- openapi + DTO + service + util de specialty

## Validações executadas

- jest professionals + specialty-filter: 11 ok
- eslint: ok

## Pendências ou bloqueios

- Task 768

## Próxima ação sugerida

- UI do seletor de área

## Próximo contexto recomendado

- `front-end/src/pages/Main/Guardian/Professionals/`
- hook `useProfessionalsDirectory`

## Contexto que não deve ser carregado na próxima etapa

- cadastro profissional e Asaas
