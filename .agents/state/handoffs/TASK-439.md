# Handoff - Task 439

- task: `439`
- título: Redesenhar dashboard profissional web
- slice: `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- status final: done

## Decisões preservadas

- manter os 4 cards de métricas, sem mini-barras decorativas
- evolução geral em linha com 3 séries (concluídas / engajamento / evolução média) nas últimas 6 semanas
- pizza por área a partir das atividades das trilhas ativas + catálogo de conteúdos
- status de hoje: concluída (progresso do item), em andamento (paciente já concluiu algo hoje), pendente
- carrossel horizontal com maior progresso da trilha de referência
- card de relatórios lista os mais recentes já existentes
- sem novos endpoints

## Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 439, slice 019

## Contexto sob demanda carregado

- ShellHome, summary/dashboard types, ACCESSIBILITY, PatientAvatar, padrão recharts

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/**`
- `front-end/src/services/dashboard/**`
- `front-end/src/types/dashboard.ts`
- task/index/slice/handoff

## Validações executadas

- testes focados ShellHome + buildDashboardPanels ok
- eslint quiet no escopo ok

## Pendências

- nenhuma

## Próxima ação sugerida

- validar visualmente no browser com dados reais do profissional

## Próximo contexto recomendado

- apenas ShellHome se houver ajuste visual fino

## Contexto que não deve ser carregado

- backend, mobile, openapi, demais páginas autenticadas
