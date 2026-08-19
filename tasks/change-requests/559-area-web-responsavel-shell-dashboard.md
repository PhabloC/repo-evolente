# Task 559 - Área web do responsável: shell, dashboard, relatórios e configuração

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

- `GET /guardians/me/children`
- `GET /guardians/me`
- paths de reports já liberados ao responsável
- `PATCH /guardians/me` / `PATCH /users/me` já existentes para perfil

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md` (shell autenticado, cards, tabelas, empty states)

### Regra de aderencia visual

- Reutilizar `MainLayout` / sidebar / header atuais
- Navegação do responsável **somente**: Dashboard, Filhos, Relatórios, Configuração (perfil)
- Sem prints da área do responsável: não copiar o dashboard profissional (métricas clínicas, planejamentos, biblioteca)
- Lacuna registrada: composição dos cards do dashboard é decisão de implementação fiel aos tokens, não a um print inexistente

## Contexto de negocio

### Por que

Hoje o responsável pago é mandado para `/baixar-app` e não tem área web.

### O que

Liberar a web do responsável com dashboard dos filhos, listagem de filhos, relatórios disponibilizados e configuração de perfil.

### Comportamento esperado

- `resolvePostAuthPath` para `responsavel` + `accessGranted` → dashboard (não `/baixar-app`)
- Sem `accessGranted` → `/assinatura`
- Dashboard: resumo dos filhos (nome, código, status de trilha se já houver dado; empty state com CTA “Cadastrar filho”)
- Filhos: listagem + atalho para cadastrar (UI do cadastro é a Task 560) + abrir perfil do filho
- Relatórios: só os disponibilizados, filtráveis por filho
- Configuração: perfil do responsável
- Sidebar/menu não mostra Pacientes, Planejamentos, Biblioteca nem Admin

### Fora de escopo

- Wizard de cadastro do filho (Task 560)
- Editar trilha na web
- Jogos na web do responsável
- Redesign geral do shell para master/profissional

## Slice vertical

### Identificador do slice

Slice 050 - Área web do responsável e cadastro de filhos

### Arquivo do slice

- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Permissoes

- Papel `responsavel` + `accessGranted`
- Relatórios: regra já existente (só após disponibilização)

## Casos de erro mapeados

- Loading / erro de lista de filhos
- Zero filhos
- 403 em relatório não liberado
- Conta sem assinatura redirecionada ao gate

## Decisoes humanas confirmadas

- Web do responsável: dashboard com filhos, filhos, relatórios e configuração (perfil)

## Premissas adotadas pela IA

- `/baixar-app` deixa de ser o destino padrão; pode permanecer como link opcional em configuração
- Perfil da criança vive em Filhos, não em Configuração
- Dashboard não replica métricas do profissional

## Criterios de aceite

- [x] Responsável pago entra no shell web, não no gate do app
- [x] Menu só com os 4 destinos confirmados
- [x] Dashboard lista filhos ou empty state
- [x] Relatórios e perfil acessíveis
- [x] Master/profissional não mudam de navegação
- [x] Lint, testes de rota/shell do responsável e build ok
- [x] Acessibilidade mínima do shell e empty states

## Casos de borda

- Conta antiga com 1 filho
- Conta nova sem filhos
- Troca de papel (não aplicável na mesma sessão)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 050, Task 557
- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| DS | `design-system/front/Design_System_Evolente_Desktop.md` | shell | sim |
| Rotas | `front-end/src/routes/index.tsx`, `resolvePostAuthPath.ts` | pós-login | sim |
| Layout | `front-end/src/layout/**` | menu por papel | sim |
| Reports UI | páginas de relatórios existentes | reuso para responsável | sim |
| Settings | `front-end/src/pages` de configurações/perfil | reuso | sim |

## Orçamento de contexto

- medio
- estrategia de reducao: não abrir biblioteca/planejamentos/jogos; só shell + home + reports + settings

## Dependencias

- Task 557
- Task 558 (para o funil completo cadastro → pagamento → dashboard; o shell em si só precisa da 557)

## Resultado da execucao

### Resumo por stack

- **front-end**: responsável com `accessGranted` entra no dashboard web. Sidebar só com Dashboard, Filhos, Relatórios e Configuração (perfil). Dashboard lista filhos (nome, código, status de trilha) ou empty state com CTA. Relatórios reutilizam a API já existente em modo somente leitura. Perfil reutiliza a tela de configurações. `/baixar-app` permanece como página opcional.

### Relação com o slice

- Slice 050: shell e navegação prontos. Slice permanece `todo` (wizard de cadastro do filho é a Task 560). `/filhos/cadastrar` é um placeholder explícito até a 560.

### Decisões técnicas

- `resolvePostAuthPath` do responsável pago aponta para `/dashboard`.
- Relatórios do responsável são uma página própria, sem gerar/compartilhar/excluir.
- Status de trilha no dashboard usa `GET /patients/:id/trails` e progresso já liberados ao responsável.
- Desvio do design system desktop (que reservava a área autenticada a master/profissional): a decisão humana da task prevalece; a navegação foi reduzida aos 4 destinos, sem copiar métricas clínicas.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 050, handoff 558
- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | shell/cards/empty | tokens e estados |
| `front-end/src/routes/index.tsx`, `resolvePostAuthPath.ts` | pós-login | destino do responsável |
| `front-end/src/layout/**`, `constants/navigation.ts` | menu por papel | 4 destinos |
| `front-end/src/pages/Main/Reports/**` | reuso | filtro/download |
| `front-end/src/pages/Main/Settings/**` | perfil | conta do responsável |
| `contracts/openapi.yaml` `/guardians/me/children` e `/reports` | API | listagem |

### Evitado

- wizard de filho (560), biblioteca, planejamentos, jogos, mobile

## Handoff

- Caminho: `.agents/state/handoffs/TASK-559.md`
- Próximo contexto: Task 560 (`POST /guardians/me/children` + wizard em `/filhos/cadastrar`)

## Arquivos alterados

- `front-end/src/utils/resolvePostAuthPath.ts`
- `front-end/src/utils/resolvePostAuthPath.test.ts`
- `front-end/src/utils/formatGuardianTrailStatus.ts`
- `front-end/src/constants/routes.ts`
- `front-end/src/constants/navigation.ts`
- `front-end/src/constants/navigation.test.ts`
- `front-end/src/routes/index.tsx`
- `front-end/src/types/guardian.ts`
- `front-end/src/services/guardians/guardianService.ts`
- `front-end/src/hooks/useGuardianChildren.ts`
- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/pages/Main/Dashboard/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Settings/index.tsx`
- `front-end/src/pages/Main/Settings/styles.module.css`
- `front-end/src/pages/Main/Guardian/**`
- `front-end/src/pages/Auth/GuardianAppGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `tasks/change-requests/559-area-web-responsavel-shell-dashboard.md`
- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-559.md`

## Validacoes executadas

- eslint dos arquivos alterados — passou
- vitest: resolvePostAuthPath, navigation, Sidebar, ShellHome, Guardian dashboard/filhos, SubscriptionGate — passou
- `npx vite build` — passou

## Qualidade estrutural

- Listagem de filhos no hook `useGuardianChildren` e no service `guardianService`
- Status de trilha em `utils/formatGuardianTrailStatus.ts`
- Páginas do responsável em `pages/Main/Guardian/`

## Aderencia ao design system

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md` (artefato)
- Reuso de MainLayout, sidebar, cards, empty states e tokens
- Lacuna: sem prints da área do responsável; não foi copiado o dashboard profissional
- Desvio documentado: DS dizia que responsável não acessa desktop; decisão humana da task libera shell reduzido

## Acessibilidade aplicada

- `nav` existente com `aria-label`; empty states com `aria-label` e CTA nomeado
- Loading com `role="status"`; erros com `role="alert"`
- Cards de filho são links com nome visível; ícones decorativos com `aria-hidden`

## Pendencias pos-task

- Task 560: wizard autenticado em `/filhos/cadastrar`

## Status final

done
