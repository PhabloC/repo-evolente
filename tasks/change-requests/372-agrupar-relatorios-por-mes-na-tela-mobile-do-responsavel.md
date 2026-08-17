# Task 372 - Agrupar relatórios por mês na tela mobile do responsável

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

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

refino incremental da leitura da lista de relatórios

### Fonte primaria visual

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/shell/screens/guardianReportsStyles.ts`

## Objetivo

Separar os relatórios novos e antigos por mês na tela mobile do responsável, deixando os blocos mensais em ordem do mais recente para o mais antigo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-371.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Lista atual da tela | `mobile/src/features/shell/screens/GuardianReportsScreen.tsx` | reorganizar a apresentação dos relatórios | sim |
| Estilos da tela | `mobile/src/features/shell/screens/guardianReportsStyles.ts` | criar cabeçalhos mensais e blocos da lista | sim |

## Orçamento de contexto

- baixo
- estratégia: manter o mesmo card de relatório e apenas agrupar a lista em seções mensais ordenadas pelo mês mais recente

## Criterios de conclusao

- [x] a tela separa relatórios por mês
- [x] os meses mais recentes aparecem primeiro
- [x] os relatórios antigos ficam separados dos novos por bloco mensal
- [x] `npm run test` executado
- [x] `npm run typecheck` executado

## Dependencias

- Task 369 - done
- Task 371 - done

## Resultado da execucao

- a tela de relatórios passou a agrupar os arquivos por mês de compartilhamento/criação
- cada grupo mensal ganhou cabeçalho próprio, mantendo os cards atuais dentro de cada seção
- a ordem da tela preserva os relatórios mais novos no topo e empurra os antigos para baixo por mês

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-371.md`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/shell/screens/guardianReportsStyles.ts`

## Handoff

- `.agents/state/handoffs/TASK-372.md`

## Arquivos alterados

- `tasks/change-requests/372-agrupar-relatorios-por-mes-na-tela-mobile-do-responsavel.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-372.md`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/shell/screens/guardianReportsStyles.ts`

## Validacoes executadas

- `cd mobile && npm run test` — passou
- `cd mobile && npm run typecheck` — falhou por erros preexistentes em `MemoryGameRenderer` e `TrailActivityScreen`

## Pendencias pos-task

- erros preexistentes de typecheck no app mobile seguem fora do escopo desta task

## Status final

done
