# Handoff - Task 614

## Task

- TASK-614 - Busca global com debounce no header web
- Slice 017 — Redesign da interface interna web
- status final: done

## Decisões preservadas

- A pesquisa usa somente os destinos de navegação já permitidos ao perfil autenticado; não faz chamadas de API nem expõe conteúdo de outras áreas.
- O filtro aguarda 350 ms sem alteração no input e compara título, descrição e localização sem diferenciar acentos.
- Cada resultado mostra `Encontrado em: ...`; ao selecioná-lo, o usuário navega ao destino e o campo é recolhido.

## Contexto efetivamente usado

- Task 614, Slice 017, Header e MainLayout compartilhados, navegação por perfil e guias de acessibilidade/QA do front-end.

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`

## Validações

- `npm run test -- --run src/layout/Header/index.test.tsx` — 5 testes aprovados.
- `git diff --check` — sem erros de whitespace; apenas avisos de conversão LF/CRLF no worktree.
- Lint, typecheck e build foram iniciados, mas o ambiente não imprimiu os resultados antes do limite de execução.

## Pendências ou bloqueios

- Fazer smoke visual da lista de resultados e executar lint/typecheck/build em sessão sem processos Node concorrentes.

## Próximo contexto recomendado

- `front-end/src/layout/Header/`, caso a busca global passe a precisar consultar dados dinâmicos da API.
