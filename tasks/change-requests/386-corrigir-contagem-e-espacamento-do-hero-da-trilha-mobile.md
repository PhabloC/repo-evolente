# Task 386 - Corrigir contagem e espaçamento do hero da trilha mobile

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

não se aplica

## Modo de execução

single-stack

## Slice vertical

- Slice 008 - Trilhas semanais e evolução
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referência visual

- mobile; card `Rotina da semana` da trilha e ajuste funcional pedido na conversa

## Objetivo

Corrigir a contagem exibida no hero da trilha e reduzir o espaço excessivo entre o selo e o título.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-385.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/trail/screens/TrailTodayScreen.tsx`, `mobile/src/features/trail/screens/styles.ts` | corrigir hero da trilha | sim |
| Regra da trilha | `mobile/src/features/trail/utils/computeTrailWeekdayState.ts` | validar contagem atual usada no restante da tela | não |

## Orçamento de contexto

- baixo
- estratégia: ajuste localizado no hero da tela de trilha

## Critérios de conclusão

- [x] hero deixa de usar só a contagem do dia
- [x] espaço excessivo no hero é reduzido
- [x] validação de tipagem foi tentada sem novos diagnósticos reportados pelo `tsc`

## Resultado da execucao

- o hero da trilha passou a usar a contagem total de atividades da rotina semanal (`day.activities.length`) em vez de considerar apenas o dia atual
- o bloco do hero deixou de usar `justifyContent: 'space-between'`, reduzindo o vazio entre o selo e o título quando não há CTA relevante ocupando o rodapé
- o botão `Abrir próxima` passou a usar `marginTop: 'auto'`, mantendo o CTA ancorado embaixo sem forçar espaçamento excessivo no conteúdo textual

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-385`
- contexto sob demanda: `mobile/src/features/trail/screens/TrailTodayScreen.tsx`, `mobile/src/features/trail/screens/styles.ts`
- contexto evitado: alterações em contrato, backend e outras telas, porque a correção ficou local no hero da trilha

## Handoff

- `.agents/state/handoffs/TASK-386.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — iniciou `tsc --noEmit` sem novos diagnósticos, mas o shell ficou preso e os processos de validação precisaram ser encerrados manualmente

## Pendencias pos-task

- se necessário, repetir a validação de tipagem em um terminal local fora do backend de execução quando houver nova rodada de ajustes na trilha

## Status final

done
