# Handoff - Task 183

## Task

- identificador: 183
- título: Redesign da página de usuários admin web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- status do slice: done

## Decisões preservadas

- Abas: Profissionais (`role=profissional`), Pacientes (árvore admin), Admins (`role=master`)
- Novo usuário continua abrindo o modal de criação de master
- Filtro dropdown com checkboxes de status + ícone `FunnelPlus`
- Tabela com colunas Usuário / Perfil / Status / Ação e zebra via `Table striped`
- Pacientes são somente leitura nesta tela

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/change-requests/183-redesign-pagina-usuarios-admin-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-182.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `AdminUsers/**` | redesign | UI |
| `useAdminWorkspace` | dados | listagem/status |
| `ui/Table` | zebra | prop striped |

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/**`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/ui/Table/**`

## Validações executadas

- lint ok
- AdminUsers tests ok (7)
- build ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- só reabrir se precisar criar profissional/paciente nesta tela ou listar responsáveis

## Próximo contexto recomendado

- `front-end/src/pages/Main/AdminUsers/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- backend/storage
- motivo: entrega só de UI web
