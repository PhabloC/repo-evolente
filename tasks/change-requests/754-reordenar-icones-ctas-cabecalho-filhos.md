# Task 754 - Reordenar ícones e CTAs do cabeçalho Filhos

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

## Modo de execucao

single-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Origem da solicitacao

Print: lupa e sino ficaram embaixo; usuário pediu ícones em cima e botões “Encontrar profissionais” / “Cadastrar filho” embaixo.

## Comportamento esperado

- Lupa e sino no topo à direita, alinhados ao título.
- Botões de ação na linha de baixo, à direita, sem sobrepor conteúdo.
- Sem regressão nas demais páginas que usam o header padrão.

## Fora de escopo

- Mudar copy ou rotas dos botões.

## Criterios de aceite

- [x] Ícones de pesquisa e notificação no topo.
- [x] CTAs abaixo dos ícones.
- [x] Sem overlap com o card de filhos.
- [x] Teste focado Filhos passa.

## Contexto mínimo

- esta task, Header CSS/JSX, página Filhos

## Orçamento de contexto

- baixo

## Dependências

- Task 753 — done

## Resultado da execucao

- Grid `below-heading` com áreas: título | ícones (topo); CTAs na segunda linha à direita.

## Contexto utilizado

- `front-end/src/layout/Header/styles.module.css`
- captura do usuário

## Handoff

- `.agents/state/handoffs/TASK-754.md`

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- `tasks/000-index.md`
- `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Validacoes executadas

- Vitest Header + Children — 8 ok

## Pendencias pos-task

- Nenhuma

## Status final

done
