# Task 090 - Sincronizar dropdowns do sidebar web

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

- nao se aplica; ajuste de comportamento local do shell autenticado

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

correcao funcional sem impacto visual estrutural

### Fonte primaria visual

- `front-end/src/layout/Sidebar/index.tsx`

### Lacunas

- sem print novo; decisao: preservar o visual atual e corrigir apenas a exclusao mutua entre os menus do sidebar

## Objetivo

Garantir que o dropdown de Configuracoes e o menu do usuario no rodape do sidebar nao fiquem abertos ao mesmo tempo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-075.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste de UI no shell autenticado | `front-end/docs/ai/ARCHITECTURE.md` | confirmar organizacao local do front-end antes de alterar o layout compartilhado | sim |
| Ajuste de UI no shell autenticado | `front-end/docs/ai/CODE_STYLE.md` | preservar padrao TypeScript/imports do componente | sim |
| Ajuste de UI no shell autenticado | `front-end/docs/ai/REPO_MAP.md` | validar local apropriado para teste do sidebar | sim |
| Ajuste de UI no shell autenticado | `front-end/docs/ai/ACCESSIBILITY.md` | preservar interacao por teclado e uso correto de `aria-expanded` | sim |
| Exclusao mutua entre menus | `front-end/src/layout/Sidebar/index.tsx` | implementar o fechamento reciproco entre grupo Configuracoes e menu do usuario | sim |
| Cobertura de regressao | testes do `front-end` para componentes/layout | adicionar ou ajustar teste para validar a interacao entre os dois menus | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a leitura ao shell autenticado, aos guias locais do front-end e ao handoff mais proximo do sidebar

## Criterios de conclusao

- [x] clicar em Configuracoes fecha o menu do usuario quando ele estiver aberto
- [x] clicar no usuario fecha o grupo Configuracoes quando ele estiver aberto
- [x] componente continua expondo estados corretos via `aria-expanded`
- [x] testes direcionados do front-end aprovados

## Dependencias

- Task 075 - done

## Resultado da execucao

- o `Sidebar` passou a fechar explicitamente o menu do usuario ao abrir grupos de navegacao com filhos
- o clique no resumo do usuario agora colapsa os grupos expansivos do sidebar antes de alternar o menu de saida
- foi adicionada cobertura de regressao para garantir a exclusao mutua entre Configuracoes e o menu do usuario

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-075.md`

### Sob demanda

- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/REPO_MAP.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/index.test.tsx`

### Contexto evitado

- demais páginas do shell autenticado e referências visuais externas por não serem necessárias para um ajuste local de interação

## Handoff

- `.agents/state/handoffs/TASK-090.md`

## Arquivos alterados

- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/index.test.tsx`
- `tasks/change-requests/090-sincronizar-dropdowns-sidebar-web.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-090.md`

## Validacoes executadas

- `cd front-end && npm run test -- src/layout/Sidebar/index.test.tsx` - ok
- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok (mantido warning preexistente de chunk grande do Vite)

## Pendencias pos-task

- nenhuma

## Status final

done
