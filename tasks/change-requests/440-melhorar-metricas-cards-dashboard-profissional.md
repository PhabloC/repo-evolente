# Task 440 - Melhorar métricas dos cards do dashboard profissional

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

- nao se aplica; reutilizar campos ja presentes no summary do dashboard

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- print de tela enviado no chat (cards de metricas do `/dashboard`)

### Fonte primaria visual

- print anexado na solicitacao da Task 440 (4 cards superiores do dashboard profissional)

### Cobertura / lacunas

- governa apenas o conteudo informacional dos 4 cards
- layout/estrutura visual dos cards permanece; troca de titulos, valores e detalhes

## Objetivo

Substituir as metricas pouco operacionais (novos vinculos / inativos genericos) por indicadores uteis ao dia a dia: pacientes com contexto de progresso, atividades de hoje, engajamento medio e pendencias de relatorios.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-439.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI cards | `front-end/src/pages/Main/ShellHome/index.tsx` | trocar topStats | sim |
| Teste | `front-end/src/pages/Main/ShellHome/index.test.tsx` | atualizar asserts | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar aos 4 cards do ShellHome sem reabrir graficos/paineis

## Criterios de conclusao

- [x] 4 cards com metricas operacionais alinhadas ao dashboard redesenhado
- [x] detalhes secundarios trazem contexto acionavel (nao frases genericas)
- [x] teste do ShellHome atualizado

## Dependencias

- Task 439 - done

## Fora de escopo

- novos endpoints
- redesign visual completo dos cards
- demais secoes do dashboard

## Resultado da execucao

- cards superiores passaram a: Pacientes ativos, Atividades de hoje, Engajamento medio, Relatorios pendentes
- detalhes secundarios usam progresso da semana, breakdown de status do dia, baixa adesao/conclusao e compartilhamento de relatorios

## Contexto utilizado

### Mínimo

- fontes globais, task, slice 019, handoff 439

### Sob demanda

- ShellHome index + teste

## Handoff

- `.agents/state/handoffs/TASK-440.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- task/index/slice/handoff

## Validacoes executadas

- teste focado ShellHome ok

## Pendencias pos-task

- nenhuma

## Status final

done
