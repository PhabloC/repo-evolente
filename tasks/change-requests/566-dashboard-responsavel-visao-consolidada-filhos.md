# Task 566 - Dashboard do responsável: visão consolidada e filtro por filho

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
- `GET /patients/{patientId}/trails`
- `GET /patients/{patientId}/progress`
- relatórios e conteúdos já liberados ao responsável

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 052 - Dashboard analítico web do responsável

### Arquivo do slice

- `tasks/slices/052-dashboard-analitico-responsavel-web.md`

## Referencia de design system

- Stack de referência visual: front-end.
- Tipo: artefato de design system e composição existente do dashboard.
- Fonte: `front-end/src/pages/Main/Guardian/Dashboard/`, builders de dashboard e seletor existente.

## Origem da solicitacao

Pedido humano: por padrão, os gráficos precisam mostrar a evolução de todos os filhos; deve ser possível filtrar individualmente cada filho.

## Comportamento esperado

- Com 2+ filhos, o filtro inicia em “Todos os filhos”.
- A visão consolidada agrega os dados disponíveis de todos os filhos da conta nos indicadores e gráficos.
- Cada filho continua sendo opção individual no seletor e altera o dashboard para sua evolução.
- Com 1 filho, o dashboard continua mostrando seus dados sem filtro; com 0, mantém o empty state.

## Fora de escopo

- Novos endpoints, dashboard mobile ou persistir o filtro.
- Alterar permissões e dados de filhos fora da conta.

## Criterios de aceite

- [ ] Seletor de 2+ filhos tem “Todos os filhos” como valor padrão.
- [ ] Visão consolidada soma/combina corretamente dados dos filhos nos painéis existentes.
- [ ] Selecionar um filho mostra apenas seus dados.
- [ ] Estados sem filhos, um filho e falhas parciais permanecem acessíveis.
- [ ] Lint e testes focados, quando o runner permitir, passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 052 e `.agents/state/handoffs/TASK-565.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Seleção e render | dashboard do responsável e teste | criar opção consolidada e preservar seleção individual | sim |
| Dados consolidados | `useGuardianDashboardSummary`, `getGuardianDashboardSummary`, tipos e testes | agregar summaries dos filhos sem novo endpoint | sim |
| Gráficos | `GuardianDashboardPanels` e builders de séries | fornecer copy e séries para todos vs filho | sim |
| UI | `front-end/docs/ai/ACCESSIBILITY.md` | seletor e estados anunciados | sim |

## Orçamento de contexto

- médio
- estratégia de redução: limitar à cadeia de summary do responsável e seus componentes; não abrir dashboard profissional completo, mobile, backend nem OpenAPI inteiro.

## Dependencias

- Tasks 562–565 (dashboard analítico e refinamentos do responsável)

## Resultado da execucao

Com dois ou mais filhos, o seletor inicia em “Todos os filhos” e o dashboard agrega trilhas, progresso, atividades, séries e relatórios de todos os perfis da conta. A adesão consolidada usa a razão entre itens concluídos e itens planejados da família. Ao escolher um filho, a mesma cadeia carrega somente os dados daquele perfil. Para uma conta com um filho, o comportamento segue individual e sem seletor.

## Contexto utilizado

- Contexto mínimo: governança raiz, índice, esta task, Slice 052, handoff Task 565 e acessibilidade.
- Sob demanda: dashboard, hook e service de summary do responsável, tipos, builders/painéis e testes adjacentes.

## Handoff

`.agents/state/handoffs/TASK-566.md`

## Arquivos alterados

- `front-end/src/types/dashboard.ts`
- `front-end/src/services/dashboard/getGuardianDashboardSummary.ts`
- `front-end/src/services/dashboard/getGuardianDashboardSummary.test.ts`
- `front-end/src/hooks/useGuardianDashboardSummary.ts`
- `front-end/src/pages/Main/Guardian/Dashboard/index.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/index.test.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/GuardianDashboardPanels.tsx`
- esta task, Slice 052, índice e handoff da Task 566

## Validacoes executadas

- prettier nos arquivos alterados: ok.
- eslint focado: ok.
- `git diff --check`: ok (somente avisos CRLF preexistentes).
- Vitest focado não executou neste ambiente porque os workers não iniciam, condição já registrada nas Tasks 563–565.

## Pendencias pos-task

- Nenhuma funcional.

## Status final

done
