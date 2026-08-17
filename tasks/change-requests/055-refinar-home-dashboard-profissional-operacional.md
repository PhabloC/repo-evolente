# Task 055 - Refinar home do dashboard profissional para uso operacional

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

- nao se aplica; preservar integracoes existentes e sem abrir novo escopo de backend

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Tipo

ajuste funcional orientado por decisao do usuario no chat

### Cobertura

- manter a composicao base do dashboard profissional
- priorizar apenas informacoes que o profissional usa no trabalho diario

### Lacunas

- a solicitacao nao redefine um novo print
- decisao: reaproveitar a estrutura atual do dashboard e substituir/remover apenas os blocos de conteudo

## Objetivo

Manter no `/dashboard` apenas os paineis operacionais aprovados pelo usuario: resumo operacional, prioridades, planejamentos, acompanhamento clinico, alertas, relatorios, agenda clinica resumida e atalhos reais.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-053.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | historico da decisao do usuario no chat | confirmar os blocos que permanecem e o que deve ser removido | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | manter coerencia estrutural e acessibilidade | sim |
| Implementacao atual | `front-end/src/pages/Main/ShellHome/index.tsx`, `styles.module.css`, `index.test.tsx` | aplicar o refino no menor escopo possivel | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao `ShellHome` e aos arquivos diretamente ligados ao dashboard profissional

## Criterios de conclusao

- [x] dashboard profissional exibe apenas os blocos aprovados pelo usuario
- [x] widgets genericos ou pouco uteis sao removidos
- [x] layout segue navegavel em desktop e mobile
- [x] lint, build e teste focado aprovados

## Dependencias

- Task 053 - done

## Resultado da execucao

- a home do profissional foi reduzida aos paineis de uso real aprovados no chat
- foram removidos blocos genericos como frentes clinicas/uso da plataforma e preferencias como atalho principal
- o dashboard agora destaca resumo operacional, prioridades, planejamentos, acompanhamento clinico, alertas, relatorios, agenda resumida e atalhos reais

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-053.md`

### Sob demanda

- decisao do usuario no chat para definir os blocos mantidos
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver alteracao de integracao
- backend e mobile por estarem fora do escopo deste refino
- outras telas autenticadas por nao fazerem parte da home do profissional

## Handoff

- `.agents/state/handoffs/TASK-055.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `tasks/change-requests/055-refinar-home-dashboard-profissional-operacional.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-055.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
