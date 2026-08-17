# Handoff - Task 165

## Task

- identificador: 165
- título: Bootstrap do primeiro jogo e card na biblioteca
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 029 - Catalogo inicial de jogos terapeuticos
- objetivo de negócio: disponibilizar o primeiro jogo no catálogo e torná-lo visível na biblioteca
- entrega verificável: jogo do alfabeto criado por código e exibido em card na biblioteca
- status do slice: done

## Decisões preservadas

- decisão: bootstrap do jogo no backend em vez de depender da UI
- motivo: a criação saiu da biblioteca
- impacto: o jogo agora existe automaticamente no catálogo

- decisão: bootstrap apenas cria quando o jogo ainda não existe
- motivo: não sobrescrever edição ou status definidos pelo master
- impacto: a inicialização é idempotente e não destrutiva

- decisão: “Conheça o alfabeto” é categoria visual da biblioteca
- motivo: evitar extensão prematura do contrato só para apresentação
- impacto: o conteúdo segue com categoria terapêutica compatível (`linguagem`)

- decisão: placeholder visual do card usa letras simples
- motivo: imagens por letra ainda não foram fornecidas
- impacto: a UI já identifica o jogo sem bloquear a próxima etapa visual

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/165-bootstrap-do-primeiro-jogo-e-card-na-biblioteca.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `.agents/state/handoffs/TASK-164.md`
- `.agents/state/handoffs/TASK-163.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `proposta.md` | jogo | comportamento do alfabeto |
| openapi contents | API | garantir reaproveitamento do contrato |
| backend docs/ai | backend | bootstrap do catálogo |
| front-end docs/ai | web | biblioteca e acessibilidade |
| DS desktop | UI | card e biblioteca |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile docs/DS | execução mobile já concluída |

## Resultado por stack

- backend: done
- front-end: done

## Arquivos alterados

- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.module.ts`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- task/slice/index/handoff

## Validações executadas

- backend lint: ok
- backend test: ok (`18 suites`, `68 tests`)
- front-end lint: ok
- front-end build: ok
- teste isolado da biblioteca: ok (`src/pages/Main/Library/index.test.tsx`)

## Pendências ou bloqueios

- sem bloqueio
- imagens reais por letra ainda pendentes
- se “Conheça o alfabeto” virar categoria persistida, isso exigirá nova task

## Próxima ação sugerida

- quando as imagens por letra chegarem, atualizar o card da biblioteca e, se necessário, a execução mobile

## Próximo contexto recomendado

- `tasks/change-requests/165-bootstrap-do-primeiro-jogo-e-card-na-biblioteca.md`
- `.agents/state/handoffs/TASK-165.md`
- `front-end/src/pages/Main/Library/`
- `mobile/src/features/games/`

## Contexto que não deve ser carregado na próxima etapa

- fonte: fluxos antigos de criação via UI
- motivo: a criação de conteúdo na biblioteca já foi removida
