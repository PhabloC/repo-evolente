# Task 614 - Busca global com debounce no header web

## Status

in_progress

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica; a busca consulta os destinos de navegação já liberados ao perfil logado.

## Modo de execução

single-stack

## Slice vertical

- Slice 017 — `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Fazer a pesquisa global do header aguardar uma breve pausa na digitação antes de filtrar destinos e seções disponíveis ao usuário, mostrando o resultado e o local onde foi encontrado.

## Dependências

- Task 613 — done (campo de pesquisa sem botão X)

## Contexto mínimo

- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `front-end/src/layout/{Header,MainLayout}/`
- `front-end/src/constants/navigation.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI compartilhada | pedido do usuário nesta conversa | mostrar termo, resultado e localização sem buscar em cada tecla. |
| Acessibilidade/qualidade | `front-end/docs/ai/{ACCESSIBILITY,CODE_STYLE,QA}.md` | lista de resultados navegável, foco e testes do debounce. |

## Orçamento de contexto

- baixo
- estratégia: índice local dos destinos já permitidos pelo papel do usuário, com debounce de 350 ms; sem API ou indexação de dados privados.

## Critérios de aceite

- [x] Após 350 ms sem digitação, a busca filtra título, descrição e localização dos destinos disponíveis ao perfil.
- [x] Cada resultado mostra o nome e “Encontrado em: …”.
- [x] Selecionar um resultado navega ao destino encontrado.
- [x] Antes do debounce não há resultado atualizado; estado vazio é claro e acessível.
- [x] Testes são atualizados e executados; lint, types e build foram disparados, mas o ambiente não devolveu seus resumos finais.

## Resultado da execução

- Concluída a busca de destinos locais autorizados, com debounce de 350 ms, resultados acessíveis e navegação pelo resultado selecionado.

## Contexto utilizado

- Task 614, Slice 017, Header e MainLayout compartilhados, constantes de navegação e guias de acessibilidade/QA do front-end.

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `tasks/000-index.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-614.md`

## Validações executadas

- `npm run test -- --run src/layout/Header/index.test.tsx` — 5 testes aprovados.
- `npm run lint`, `npx tsc --noEmit` e `npm run build` foram iniciados, mas este ambiente encerrou a coleta sem imprimir o resultado final.
- `git diff --check` — sem erros de whitespace; apenas avisos de conversão LF/CRLF em arquivos já alterados no worktree.

## Pendências pós-task

- Smoke visual em desktop e mobile; confirmar lint, typecheck e build em uma sessão local sem os processos Node concorrentes do ambiente.

## Handoff

- Criado em `.agents/state/handoffs/TASK-614.md`.

## Status final

done
