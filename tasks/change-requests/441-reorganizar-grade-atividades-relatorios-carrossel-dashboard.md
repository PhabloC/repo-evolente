# Task 441 - Reorganizar grade atividades, relatórios e carrossel do dashboard

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

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Tipo

- print do chat com os 3 cards inferiores do dashboard profissional

### Cobertura

- Atividades de hoje e Relatorios na mesma linha
- Maior progresso (carrossel) na linha de baixo
- lista de atividades em 2 colunas no desktop e 1 no mobile

## Objetivo

Ajustar a grade inferior do dashboard profissional conforme layout pedido no chat.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 019, handoff 440

## Contexto sob demanda

| Gatilho | Fonte | Obrigatório? |
|---|---|---|
| Layout | `ShellHome/index.tsx`, `styles.module.css` | sim |
| Teste | `ShellHome/index.test.tsx` | sim se asserts mudarem |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] atividades + relatorios na mesma linha
- [x] carrossel na linha abaixo
- [x] atividades de hoje em 2 colunas (1 no mobile)
- [x] teste focado ok

## Dependencias

- Task 439/440 - done

## Resultado da execucao

- grade inferior reorganizada: atividades+relatorios / carrossel full-width
- lista de atividades em 2 colunas ate 900px, 1 coluna abaixo

## Handoff

- `.agents/state/handoffs/TASK-441.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- task/index

## Validacoes executadas

- teste ShellHome ok

## Pendencias pos-task

- nenhuma

## Status final

done
