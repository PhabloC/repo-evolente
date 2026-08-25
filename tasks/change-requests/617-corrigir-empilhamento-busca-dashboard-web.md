# Task 617 - Corrigir empilhamento da busca sobre dashboard web

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

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

- Slice 017 — `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Garantir que o Header e seu balão de pesquisa sejam pintados acima do conteúdo do dashboard.

## Dependências

- Task 616 — done

## Contexto mínimo

- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-616.md`
- `front-end/src/layout/MainLayout/styles.module.css`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Balão atrás do dashboard | CSS do MainLayout | corrigir a ordem de empilhamento entre Header e `main`. |

## Orçamento de contexto

- baixo
- estratégia: ajustar apenas a camada do `main`, mantendo a camada do header já elevada.

## Critérios de aceite

- [x] O conteúdo de `main` fica abaixo do Header no mesmo contexto de empilhamento.
- [x] O balão da pesquisa permanece acima do dashboard e dos CTAs.

## Resultado da execução

- O `main` do shell passou a usar camada base (`z-index: 0`), enquanto o Header preserva sua camada elevada.

## Contexto utilizado

- Task 617, Slice 017, handoff Task 616 e CSS do MainLayout.

## Arquivos alterados

- `front-end/src/layout/MainLayout/styles.module.css`
- `tasks/000-index.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-617.md`

## Validações executadas

- Inspeção do contexto de empilhamento do shell: Header em camada 100 e `main` em camada 0.

## Pendências pós-task

- Smoke visual no dashboard.

## Handoff

- Criado em `.agents/state/handoffs/TASK-617.md`.

## Status final

done
