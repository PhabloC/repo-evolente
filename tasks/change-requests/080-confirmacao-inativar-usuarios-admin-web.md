# Task 080 - Adicionar confirmação ao inativar usuários no admin web

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

- nao altera contrato; preserva a acao atual de `PATCH /users/:id/status`

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

padrao ja consolidado em modais de confirmação

### Fonte primaria visual

- `front-end/src/pages/Main/Patients/index.tsx`

### Lacunas

- sem print dedicado
- decisao: reaproveitar o padrao textual e estrutural do modal de confirmação de inativação já usado em `Pacientes`

## Objetivo

Exigir confirmação explícita antes de inativar um usuário na tabela do admin web, reduzindo risco de ação acidental.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-079.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Fluxo de confirmação | `front-end/src/pages/Main/Patients/index.tsx` | espelhar o padrão de modal de inativação | sim |
| UI base | `front-end/src/ui/Modal/index.tsx` | integrar modal acessível na rota do admin | sim |
| Implementação atual | `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`, `front-end/src/pages/Main/AdminUsers/index.tsx` | interceptar a ação `Inativar` e exibir confirmação | sim |
| Teste | `front-end/src/pages/Main/AdminUsers/index.test.tsx` | cobrir abertura e confirmação do modal | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à ação de inativação da tabela de usuários do admin, sem tocar outras ações do módulo

## Criterios de conclusao

- [x] clicar em `Inativar` abre modal de confirmação
- [x] `Reativar` continua acionando diretamente
- [x] confirmar no modal executa a inativação real
- [x] teste da rota, lint e build aprovados

## Dependencias

- Task 077 - done
- Task 078 - done

## Resultado da execucao

- a tabela de usuários do admin agora intercepta apenas a ação de inativação com modal de confirmação
- o modal reutiliza o mesmo padrão acessível já consolidado em outras telas do produto
- a reativação permanece direta para não adicionar atrito desnecessário ao fluxo operacional
- foi adicionado teste cobrindo abertura do modal e confirmação da inativação

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-079.md`

### Sob demanda

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/ui/Modal/index.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

### Contexto evitado

- backend, mobile, overview, planos e logs do admin por nao participarem do fluxo da ação de usuário

## Handoff

- `.agents/state/handoffs/TASK-080.md`

## Arquivos alterados

- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `tasks/change-requests/080-confirmacao-inativar-usuarios-admin-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-080.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx` - ok
- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
