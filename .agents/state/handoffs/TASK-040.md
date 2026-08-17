# Handoff - Task 040

## Task

- identificador: 040
- slice vertical: Slice 018 - Fidelidade visual dashboard e pacientes web
- status final: done

## Decisoes preservadas

- Prints do usuario sao referencia primaria para o shell, dashboard e pacientes.
- Linguagem adotada: sidebar clara, ativo azul, fundo creme, busca superior e cards densos.
- Nao inventar agenda, fotos, notificacoes, graficos ou metricas sem dados reais.
- Indicadores de pacientes sao calculados da resposta existente e a busca filtra nome/codigo localmente.

## Contexto utilizado

- Dois prints internos, shell, ShellHome, Patients e acessibilidade.

## Arquivos alterados

- prints em `design-system/front/prints/`
- Header, Sidebar CSS, MainLayout CSS, ShellHome e Patients
- governanca da Task 040 e Slice 018

## Validacoes executadas

- lint e build - ok
- 21 arquivos e 34 testes - ok

## Pendencias

- Busca global e notificacao aguardam escopo de integracao.
- Warnings preexistentes de `act(...)` em dois testes auth.

## Proximo contexto recomendado

- Capturas reais da aplicacao apos uso, caso haja refinamento de fidelidade por viewport.
