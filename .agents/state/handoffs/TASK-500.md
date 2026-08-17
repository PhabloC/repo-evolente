# Handoff - Task 500

## Task

- identificador: 500
- título: Contrato: trilha self-serve do responsável
- tipo: shared
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 047-trilha-self-serve-responsavel-mobile
- objetivo de negócio: responsável sem vínculo monta trilha no mobile
- entrega verificável: OpenAPI com ownership nullable + canManage

## Decisões preservadas

- decisão: `TrailListResponse.canManage` em vez de só `hasActiveProfessionalLink` no Child
- motivo: modo dono/execução vem direto da listagem da semana
- impacto: mobile consome `canManage` no adapter

## Contexto utilizado

### Contexto mínimo lido

- slice 047
- `contracts/openapi.yaml` (trails)

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| openapi trails | contrato | professionalUserId nullable, canManage |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system | sem UI nesta task |

## Resultado por stack

- contracts: atualizado
- backend: n/a nesta task
- mobile: n/a nesta task

## Arquivos alterados

- `contracts/openapi.yaml`

## Validações executadas

- revisão manual do schema TrailListResponse / WeeklyTrail

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- Task 501 (já concluída na mesma fatia)

## Próximo contexto recomendado

- handoff 501/502 se retomar UI/API

## Contexto que não deve ser carregado na próxima etapa

- specs de jogos / Asaas
