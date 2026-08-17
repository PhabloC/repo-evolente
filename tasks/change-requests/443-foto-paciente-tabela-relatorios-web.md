# Task 443 - Exibir foto do paciente na tabela de relatórios web

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

- nao se aplica; `avatarUrl` ja vem em `ChildProfile` via listagem de pacientes

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

- padrao de `PatientAvatar` ja usado na tabela de pacientes

## Objetivo

Na coluna Paciente da tabela de relatorios, exibir foto de perfil (com fallback) ao lado do nome.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 011

## Contexto sob demanda

| Gatilho | Fonte | Obrigatório? |
|---|---|---|
| UI | `Reports/index.tsx`, `Reports/styles.module.css` | sim |
| Avatar | `components/PatientAvatar` | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] coluna Paciente mostra avatar + nome
- [x] sem foto, fallback do PatientAvatar

## Dependencias

- Task 442 / Slice 027 (fotos em bucket) — dados ja disponiveis

## Resultado da execucao

- coluna Paciente usa `PatientAvatar` + nome/código
- listagem de pacientes sem filtro de status para resolver avatar tambem de vinculos inativos; geracao continua so com ativos

## Handoff

- `.agents/state/handoffs/TASK-443.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

## Validacoes executadas

- lints no arquivo Reports ok

## Pendencias pos-task

- nenhuma

## Status final

done
