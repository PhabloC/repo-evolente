# Task 183 - Redesign da página de usuários admin web

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

- `contracts/openapi.yaml#/paths/~1users` (listagem por role/status)
- `contracts/openapi.yaml#/paths/~1admin~1professionals-tree` (aba Pacientes)

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

- front-end

### Tipo de referencia visual

artefato documental

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- linguagem visual já consolidada do admin web; zebra rows sutis; abas e badges discretos

## Contexto de negocio

### Por que

A página de usuários está sobrecarregada (hero, árvore, filtros embutidos). O master precisa de uma visão por categoria mais direta.

### O que

Remover o conteúdo atual da página e redesenhar com abas, badges de contagem, tabela enxuta e filtro em dropdown.

### Comportamento esperado

1. Abas: Profissionais, Pacientes, Admins
2. Botão "Novo usuário" ao lado das abas (cria master, fluxo já existente)
3. Badges: total + contagens por categoria
4. Tabela: Usuário, Perfil, Status, Ação
5. Linhas com fundo alternado (zebra)
6. Botão filtro (`FunnelPlus`) acima da tabela à direita, abrindo dropdown com opções marcáveis

### Premissas adotadas

- Aba Profissionais = `role=profissional`
- Aba Admins = `role=master`
- Aba Pacientes = pacientes da árvore `/admin/professionals-tree` (somente leitura; sem inativar por esta tela)
- Contas `responsavel` ficam fora das abas pedidas nesta entrega

### Fora de escopo

- mobile
- criar profissional/paciente por esta tela
- novo endpoint de listagem de pacientes
- árvore lateral de vínculos

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-182.md` (avatar na listagem)

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página | `front-end/src/pages/Main/AdminUsers/**` | redesign | sim |
| Workspace | `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx` | listagem/status | sim |
| Table | `front-end/src/ui/Table/**` | zebra | sim |
| Tree API | `adminService.getAdminProfessionalsTree` | aba pacientes | sim |

## Orçamento de contexto

- Risco medio
- Estratégia: reescrever só `AdminUsers` + prop striped no Table; reusar workspace/modal existentes

## Criterios de conclusao

- conteúdo antigo removido
- abas/badges/filtro/tabela conforme pedido
- lint e testes da página passam

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers`
- `cd front-end && npm run build`

## Resultado da execucao

### Resumo por stack

- **front-end**: página de usuários redesenhada com abas (Profissionais/Pacientes/Admins), botão Novo usuário, badges de contagem, tabela zebra (Usuário/Perfil/Status/Ação) e filtro dropdown com `FunnelPlus`.

### Relação com o slice

- Continua o Slice 017 refinando a UI admin dedicada de usuários.

### Decisões técnicas

- Pacientes vêm da árvore admin já existente (somente leitura).
- Filtro por status via checkboxes no dropdown; abas substituem o filtro por papel.
- `Table` ganhou prop opcional `striped`.

### Trade-offs

- Contas `responsavel` não aparecem nas abas pedidas.
- "Novo usuário" segue criando master (fluxo Task 155).

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 017, handoff 182

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `AdminUsers/**` | redesign | UI |
| `useAdminWorkspace` | listagem/status | dados |
| `ui/Table` | zebra | prop striped |
| professionals-tree | aba pacientes | flatten |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-183.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/ui/Table/index.tsx`
- `front-end/src/ui/Table/styles.module.css`
- `tasks/change-requests/183-redesign-pagina-usuarios-admin-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-183.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers` — ok (7 tests)
- `cd front-end && npm run build` — ok

## Pendencias pos-task

- nenhuma bloqueante; eventual listagem dedicada de pacientes/responsáveis se virar demanda

## Status final

done
