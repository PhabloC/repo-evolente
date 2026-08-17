# Handoff - Task 503

## Task

- identificador: 503
- título: Mobile: abas Trilhas e Biblioteca na área Trilha
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 047-trilha-self-serve-responsavel-mobile
- objetivo: sub-abas Trilhas | Biblioteca + gerar anamnese na biblioteca
- entrega: UI com categorias e CTA

## Decisões preservadas

- decisão: sub-abas internas (não nova item no tab bar do shell)
- decisão: CTA “Gerar trilha pela anamnese” fica na aba Biblioteca (modo dono)
- decisão: após gerar, volta para aba Trilhas

## Contexto utilizado

### Contexto mínimo lido

- Task 503, slice 047, handoff 502

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| TrailTodayScreen | UI | abas |
| useTrailLibraryQuery | catálogo | categorias |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| backend/openapi | sem mudança de API |

## Resultado por stack

- mobile: sub-abas + TrailLibraryPane

## Arquivos alterados

- TrailTodayScreen, TrailLibraryPane, TrailLibraryScreen, styles, ResponsavelShellNavigator

## Validações executadas

- lints ok

## Pendências ou bloqueios

- conferir no dispositivo/emulator

## Próxima ação sugerida

- reload do app e testar abas Trilhas/Biblioteca

## Próximo contexto recomendado

- handoff 503

## Contexto que não deve ser carregado na próxima etapa

- jogos / admin
