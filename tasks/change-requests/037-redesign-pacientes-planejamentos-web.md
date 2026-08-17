# Task 037 - Redesign de pacientes e planejamentos web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- preservar contrato e integracoes existentes

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Aplicar a nova fundacao visual aos fluxos de pacientes, cadastro, perfil, planejamentos e trilha semanal.

## Contexto mínimo

- fontes globais obrigatorias, esta task, Slice 017 e handoff da Task 036

## Contexto sob demanda

- design system desktop
- `front-end/src/pages/Main/Patients/**`
- `front-end/src/pages/Main/Plans/**`
- componentes UI diretamente utilizados e acessibilidade

## Orçamento de contexto

- medio; nao carregar biblioteca, relatorios ou admin

## Criterios de conclusao

- [x] Listas, filtros, formularios, perfil e trilhas visualmente consistentes
- [x] Estados vazios, carregamento e acoes preservados
- [x] Testes, lint e build aprovados

## Resultado da execucao

- Pacientes, cadastro, perfil e anamnese receberam filtros, campos, etapas, chips e estados vazios refinados.
- Planejamentos ganharam quadro semanal horizontal, cards de atividades e filtros coerentes.
- Table, Input e Modal compartilhados foram modernizados, beneficiando todos os fluxos internos.

## Contexto utilizado

- fontes globais, Slice 017, handoff 036, Patients, Plans e componentes UI diretos

## Handoff

- `.agents/state/handoffs/TASK-037.md`

## Arquivos alterados

- estilos de Patients e Plans; Table, Input e Modal; governanca da Task 037

## Validacoes executadas

- lint - ok
- build - ok, repetido sem warnings apos correcao CSS
- 21 arquivos e 34 testes - ok

## Pendencias pos-task

- Warnings preexistentes de `act(...)` em testes de cadastro.

## Status final

done

## Dependencias

- Task 036
