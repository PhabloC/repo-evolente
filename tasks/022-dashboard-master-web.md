# Task 022 - Dashboard master web

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

- `contracts/openapi.yaml#/paths` admin

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- Cards metricas, tabelas, sidebar DS.

## Contexto de negocio

### Por que

Admin na web.

### O que

Metricas, usuarios/planos, logs.

### Comportamento esperado

- Cards
- Tabelas
- Inativar
- Logs

### Fora de escopo

- Excluir

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master
- Casos de erro: falha carga
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: zero profissionais

## Especificacao tecnica

### Deve

- Estados vazio/loading
- Sem exclusao

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- UI infantil

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`

## Dependencias

- Task 021

## Slice vertical

### Identificador do slice

Slice 009 - Admin master

### Arquivo do slice

- `tasks/slices/009-administracao-master.md`

### Objetivo de negócio

UI admin web.

### Entrega verificável do slice

Dashboard master web.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/009-administracao-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |
| API | `contracts/openapi.yaml` | API | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- Metricas
- Inativar
- Logs

## Instrucoes de implementacao

- Densidade profissional DS

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- Dashboard master web

## Riscos ou ambiguidades



## Resultado da execucao

Dashboard master em `/dashboard` quando o papel é `master`:

- Cards de métricas (`GET /admin/metrics`)
- Tabela de usuários com filtros + inativar/reativar (`GET/PATCH /users`) — bloqueio de auto-inativação na UI
- Planos/assinaturas com ativar/recusar (`/admin/subscriptions`)
- Árvore profissionais → pacientes (`/admin/professionals-tree`) com estado vazio
- Logs de auditoria (`/admin/audit-logs`)
- Loading/erro/sucesso/vazio; sem exclusão; densidade profissional (Nunito/tokens DS)

Profissional/responsável continuam no ShellHome em `/dashboard`.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-021.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | cards, tabelas, sidebar, densidade |
| openapi admin/users | API | payloads |
| ARCHITECTURE + ACCESSIBILITY | front | estrutura + a11y |

### Contexto não carregado

- mobile / backend docs (single-stack front)

## Handoff

- `.agents/state/handoffs/TASK-022.md`

## Arquivos alterados

- `front-end/src/pages/Main/Admin/**`
- `front-end/src/pages/Main/Dashboard/index.tsx`
- `front-end/src/services/admin/adminService.ts`
- `front-end/src/services/users/userService.ts`
- `front-end/src/types/admin.ts`
- `front-end/src/constants/adminOptions.ts`
- `front-end/src/utils/formatDateTime.ts` (+ test)
- `front-end/src/routes/index.tsx`
- `front-end/src/constants/navigation.ts`
- task/index/slice/handoff

## Validacoes executadas

- `npm run lint` ok
- `npm run test` ok
- `npm run build` ok

## Aderencia ao design system

- Cards de resumo para métricas; tabelas com filtros e pills de status; sidebar Dashboard existente
- Tom profissional (sem UI infantil); bege/tokens do shell
- Acessibilidade: `role="status"|"alert"`, labels em filtros, botões com texto, headings via MainLayout

## Pendencias pos-task

- Task 023 dashboard master mobile
- Criar usuário master via UI (POST /users) não foi priorizado nesta tela — inativar/listar cobertos

## Status final

done
