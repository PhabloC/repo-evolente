# Task 077 - Refinar design da pagina de usuarios do admin web

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

- nao se aplica; preservar a listagem e as acoes atuais do modulo admin

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- reforcar clareza operacional, hierarquia visual e confianca clinica na rota dedicada de usuarios do admin
- preservar a linguagem acolhedora e profissional ja consolidada na area autenticada

## Objetivo

Melhorar o design da pagina de usuarios do perfil admin para deixar a operacao de contas e vinculos mais clara, organizada e coerente com o restante da area interna.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-039.md`
- `.agents/state/handoffs/TASK-043.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | orientar hierarquia, densidade e estados visuais | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | manter coerencia estrutural, icones e acessibilidade | sim |
| Implementacao atual | `front-end/src/pages/Main/AdminUsers/index.tsx`, `front-end/src/pages/Main/Admin/sections.tsx`, `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`, `front-end/src/pages/Main/Admin/styles.module.css` | aplicar o redesign no menor escopo possivel | sim |
| UI base | `front-end/src/ui/Card/**`, `front-end/src/ui/Table/**` | confirmar limites dos componentes compartilhados reutilizados | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca a rota dedicada `/admin/usuarios`, reutilizando dados, hooks e componentes existentes do modulo admin

## Criterios de conclusao

- [x] pagina de usuarios ganha hierarquia visual mais clara para operacao do admin
- [x] listagem e filtros ficam mais legiveis sem alterar contrato nem fluxo de inativacao/reativacao
- [x] bloco de vinculos profissionais/pacientes fica visualmente mais organizado
- [x] lint e build do front-end aprovados

## Dependencias

- Task 039 - done
- Task 043 - done

## Resultado da execucao

- a rota `AdminUsers` ganhou um hero operacional com indicadores honestos sobre o recorte atual e os vinculos carregados
- a listagem de usuarios passou a exibir identidade, papel, status e acoes com melhor hierarquia, chips e metadados auxiliares
- os filtros foram agrupados em um painel mais claro, com feedback sobre total filtrado e limite visualizado quando aplicavel
- a arvore de profissionais foi reorganizada com resumo, contagem de pacientes vinculados e cards mais legiveis

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-039.md`
- `.agents/state/handoffs/TASK-043.md`

### Sob demanda

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/ARCHITECTURE.md`, `front-end/docs/ai/CODE_STYLE.md`, `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/types/admin.ts`
- `front-end/src/ui/Card/index.tsx`
- `front-end/src/ui/Card/styles.module.css`
- `front-end/src/ui/Table/index.tsx`
- `front-end/src/ui/Table/styles.module.css`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/utils/formatDateTime.ts`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver mudanca de integracao
- backend, mobile, overview, planos e logs do admin por nao fazerem parte deste refino visual

## Handoff

- `.agents/state/handoffs/TASK-077.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `tasks/change-requests/077-refinar-usuarios-admin-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-077.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
