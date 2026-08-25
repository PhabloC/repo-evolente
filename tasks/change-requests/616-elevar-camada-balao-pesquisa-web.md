# Task 616 - Elevar camada do balão da pesquisa web

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

Elevar a camada de empilhamento do balão de resultados da pesquisa acima de qualquer CTA do conteúdo.

## Dependências

- Task 615 — done

## Contexto mínimo

- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-615.md`
- `front-end/src/layout/Header/styles.module.css`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Sobreposição visual | pedido do usuário nesta conversa | elevar apenas os contextos de empilhamento do header e do balão. |

## Orçamento de contexto

- baixo
- estratégia: ajuste isolado de CSS, sem alterar comportamento ou dados da busca.

## Critérios de aceite

- [x] Header e balão usam camadas elevadas sobre o conteúdo e CTAs.
- [x] Não há alteração no comportamento da pesquisa.

## Resultado da execução

- Header elevado a `z-index: 100` e balão de resultados a `z-index: 1000`.

## Contexto utilizado

- Task 616, Slice 017, handoff Task 615 e CSS do Header.

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- `tasks/000-index.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-616.md`

## Validações executadas

- Inspeção do contexto de empilhamento: o Header fica acima dos irmãos do conteúdo e o balão acima dos controles internos.

## Pendências pós-task

- Smoke visual do balão sobre qualquer CTA customizado futuro.

## Handoff

- Criado em `.agents/state/handoffs/TASK-616.md`.

## Status final

done
