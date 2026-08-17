# Task 346 - Reposicionar CTA do dashboard profissional abaixo do header

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

nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste orientado por print enviado pelo usuario no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- print do dashboard profissional enviado no chat em 2026-07-29

### Regra de aderencia visual

- preservar o header do shell autenticado e mover apenas o CTA `Criar planejamento` para uma linha abaixo do heading no dashboard profissional

## Contexto de negocio

### Por que

No perfil profissional, o CTA do header passou a quebrar a composição superior e reduzir a legibilidade do bloco de título/subtítulo.

### O que

Reposicionar o botão `Criar planejamento` para baixo do heading do dashboard profissional, sem alterar o comportamento das ações de busca e notificações nem reabrir outros headers.

### Comportamento esperado

- o dashboard profissional mantém título e subtítulo legíveis
- o botão `Criar planejamento` aparece abaixo do heading
- busca e notificações continuam no topo do shell
- outros headers do produto mantêm o layout atual

### Fora de escopo

- alterações de contrato ou backend
- redesenho global do header web
- mudanças em telas fora do dashboard profissional

## Slice vertical

### Identificador do slice

Slice 019 - Reproducao de shell dashboard por referencia externa

### Arquivo do slice

- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-055.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | preservar linguagem do shell e do CTA | sim |
| Front-end | `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` e `ACCESSIBILITY.md` | implementar o ajuste com isolamento e acessibilidade | sim |
| Implementacao atual | `front-end/src/layout/Header/index.tsx`, `styles.module.css`, `index.test.tsx`; `front-end/src/layout/MainLayout/index.tsx`; `front-end/src/pages/Main/ShellHome/index.tsx` e `index.test.tsx` | aplicar o ajuste no menor escopo possivel | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a mudanca ao header compartilhado e habilitar o novo layout apenas no `ShellHome`

## Criterios de conclusao

- [x] CTA `Criar planejamento` renderiza abaixo do heading no dashboard profissional
- [x] busca e notificacoes permanecem no topo do shell
- [x] outros headers permanecem no layout atual
- [x] teste focado passa
- [x] lint dos arquivos alterados passa
- [ ] lint global do front-end passa

## Dependencias

- Task 055
- Task 298
- Task 308

## Resultado da execucao

- o `Header` ganhou uma opcao explicita de layout para renderizar a acao customizada abaixo do heading
- o `ShellHome` passou a usar essa opcao apenas no dashboard profissional
- o topo continua com busca e notificacoes na primeira linha, evitando a quebra visual do CTA

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-055.md`

### Sob demanda

- print enviado pelo usuario no chat em 2026-07-29
- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao
- `backend/` e `mobile/` por estarem fora do escopo
- outras paginas autenticadas por nao exigirem esse reposicionamento

## Handoff

- `.agents/state/handoffs/TASK-346.md`

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `tasks/change-requests/346-reposicionar-cta-do-dashboard-profissional-abaixo-do-header.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-346.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/layout/Header/index.test.tsx src/pages/Main/ShellHome/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx src/layout/MainLayout/index.tsx src/pages/Main/ShellHome/index.tsx src/pages/Main/ShellHome/index.test.tsx` - ok
- `cd front-end && npm run lint` - falhou por erros preexistentes fora do escopo em `src/components/PatientAvatar/*`, `src/pages/Main/Library/*`

## Pendencias pos-task

- o `npm run lint` global do front-end continua falhando por erros preexistentes fora do escopo desta CR

## Status final

done
