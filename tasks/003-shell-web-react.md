# Task 003 - Shell web React com tokens e rotas por perfil

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

- nao se aplica

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

- Tokens (cores, Nunito, espacamentos) e sidebar/layout do DS desktop.

## Contexto de negocio

### Por que

Base visual e roteamento por perfil.

### O que

Shell web com tokens Evolente, layout e guards por role.

### Comportamento esperado

- Rotas protegidas
- Layout com identidade Evolente

### Fora de escopo

- Login completo
- Dashboards de negocio

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: guards por role
- Casos de erro: rota sem permissao
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: role desconhecida

## Especificacao tecnica

### Deve

- React/Vite
- Tokens alinhados ao DS

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Usar next-js
- Gamificacao

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`

## Dependencias

- Task 001

## Slice vertical

### Identificador do slice

Slice 001 - Fundacao e contrato base

### Arquivo do slice

- `tasks/slices/001-fundacao-contrato-base.md`

### Objetivo de negócio

Shell web.

### Entrega verificável do slice

App web com shell.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/001-fundacao-contrato-base.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Tokens aplicados
- Guard stub por role
- build/lint ok

## Instrucoes de implementacao

- Sidebar conforme DS
- Copy multi-especialidade

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- Shell web

## Riscos ou ambiguidades

- Sem prints

## Resultado da execucao

Shell web Evolente no `front-end/` com tokens do DS Desktop, sidebar por perfil, `RoleGuard` stub e placeholders sem dashboard de negócio.

### Por stack

- front-end: tokens CSS (paleta, Nunito, spacing/radius), MainLayout/Sidebar/Header, rotas protegidas por role, página shell + placeholders, preview de sessão em `/entrar`

### Slice

- Slice 001 permanece `in_progress`: Task 003 done; Task 004 (shell mobile) ainda planned

### Decisoes tecnicas

- Roles: master | profissional | responsavel (alinhado ao contrato/backend)
- Sidebar DS: Dashboard, Adicionar Paciente, Pacientes, Planejamentos, Biblioteca, Configurações — filtrada por role
- Responsável: apenas dashboard + configurações no desktop shell
- Sem login real: stub de preview + seletor de perfil no header
- Sem novas dependências npm
- Amarelo do DS mantido como token semântico; sem UI de gamificação

### Trade-offs

- Sem prints: aderência baseada no artefato documental do DS
- Dashboard scaffold antigo removido em favor do shell mínimo

### Contrato

- nao se aplica (sem integração API nesta task)

### Referencia visual

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md`
- Tokens e sidebar aplicados; sem desvios críticos registrados

## Contexto utilizado

### Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 001, handoff Task 002

### Contexto sob demanda carregado

- `design-system/front/Design_System_Evolente_Desktop.md` — tokens/sidebar
- `front-end/docs/ai/ARCHITECTURE.md` — rotas/layout/stores
- `front-end/docs/ai/CODE_STYLE.md` — types/utils
- `front-end/docs/ai/ACCESSIBILITY.md` — UI (nav/main/focus/labels)

### Contexto nao carregado

- design-system/mobile, mobile docs, backend docs, openapi (contrato nao se aplica)

## Handoff

- `.agents/state/handoffs/TASK-003.md`
- Proximo: Task 004 shell mobile

## Arquivos alterados

- `front-end/index.html`
- `front-end/src/styles/global.css`
- `front-end/src/types/role.ts`
- `front-end/src/types/api.ts`
- `front-end/src/types/user.ts`
- `front-end/src/constants/routes.ts`
- `front-end/src/constants/navigation.ts`
- `front-end/src/utils/roleAccess.ts`
- `front-end/src/utils/roleAccess.test.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/hooks/useAuth.ts`
- `front-end/src/routes/**`
- `front-end/src/layout/**`
- `front-end/src/pages/Main/ShellHome/**`
- `front-end/src/pages/Main/PlaceholderPage/**`
- `front-end/src/pages/Main/Forbidden/**`
- `front-end/src/pages/Public/SessionPreview/**`
- `front-end/src/ui/Button/styles.module.css`
- `front-end/src/ui/Card/styles.module.css`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- removidos: `front-end/src/pages/Main/Dashboard/**`
- `tasks/003-shell-web-react.md`
- `tasks/000-index.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-003.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — 3 passed
- `npm run build` — ok

## Aderencia ao design system

- Fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md`
- Tipo: artefato documental
- Evidencias: paleta (#FF8A00, #E981AD, #459662, #DE4E38, #2D7FBE, #F5B300, #F3E4C2), Nunito, spacing 8–40, sidebar com logo/itens DS, item ativo em azul
- Acessibilidade: `nav`/`main`, label no select de perfil, `:focus-visible`, hierarquia h1
- Lacuna: sem prints — estados visuais finos (drawer mobile) ficam para refinamento futuro
- Desvios: nenhum crítico; gamificação do amarelo não implementada (fora de escopo)

## Pendencias pos-task

- Task 004 shell mobile
- Login completo (slice autenticação)
- Dashboards de negócio e telas reais das rotas placeholder

## Status final

done
