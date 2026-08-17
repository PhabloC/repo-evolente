# Task 263 - Usar asset calendar na página de atividades mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 008 - Trilhas semanais e evolucao
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

ajuste incremental solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/assets/calendar.webp`

## Objetivo

Substituir, na página de atividades, os ícones de calendário pelos assets locais `calendar.webp`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-124.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Tela de atividades | `mobile/src/features/trail/screens/TrailTodayScreen.tsx` | aplicar asset de calendário nos estados correspondentes | sim |
| Reuso da pastilha | `mobile/src/shared/components/IconPill/index.tsx` | reaproveitar suporte a asset local | sim |
| Asset local | `mobile/assets/calendar.webp` | usar a imagem fornecida | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`, `mobile/docs/ai/QA.md` | manter organização e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas os estados de calendário da tela de atividades e reaproveitar a mesma `IconPill`

## Criterios de conclusao

- [x] a página de atividades usa `calendar.webp` nos ícones de calendário do accordion semanal
- [x] o estado vazio do dia usa o mesmo asset `calendar.webp`
- [x] demais ícones da tela permanecem inalterados
- [x] validações do escopo alterado executadas

## Dependencias

- Task 020 - done
- Task 124 - done

## Resultado da execucao

- O accordion semanal da tela de atividades passou a usar `calendar.webp` quando o estado do dia é representado por calendário
- O card de dia sem atividades passou a usar o mesmo asset local
- Ícones de conclusão, mídia e demais estados da tela permaneceram vetoriais

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-124.md`

### Sob demanda

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/assets/calendar.webp`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/QA.md`

### Fontes evitadas

- `contracts/openapi.yaml`: sem mudança de API ou fluxo
- `design-system/mobile/`: troca pontual de asset sem reinterpretação visual ampla

## Handoff

- `.agents/state/handoffs/TASK-263.md`

## Arquivos alterados

- `tasks/change-requests/263-usar-asset-calendar-na-pagina-de-atividades-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-263.md`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/shared/components/IconPill/index.tsx src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/trail/screens/TrailTodayScreen.tsx` - ok
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo, conforme registrado nas tasks anteriores

## Status final

done
