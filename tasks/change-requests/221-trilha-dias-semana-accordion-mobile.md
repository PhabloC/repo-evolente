# Task 221 - Trilha: dias da semana em accordion

## Status

done

## Tipo

mobile

## Stacks envolvidos

mobile

## Modo de execucao

single-stack

## Slice vertical

`tasks/slices/010-app-responsavel-home-notificacoes.md` (refino da trilha do responsavel)

## Objetivo

Na página de trilha, listar todos os dias da semana como accordion; ao expandir, mostrar as atividades do dia.

## Entrega verificavel

- Seg–Dom aparecem como itens de accordion
- Dia atual expandido por padrao
- Ao tocar, expande/colapsa e lista atividades do dia (ou estado vazio)
- Hero e atalho “proxima atividade” continuam focados no dia atual

## Fora de escopo

- Alterar contrato OpenAPI
- Redesign completo da trilha
- Backend

## Contexto minimo

- Esta task
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/adapters/adaptDayTrail.ts`
- `mobile/src/features/trail/services/trailService.ts`

## Contexto sob demanda

- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/trail/utils/week.ts`

## Orcamento de contexto

baixo

## Resultado

- Adapter passa a retornar a semana inteira quando `weekday` e omitido
- Servico demo/API carrega atividades de todos os dias da semana
- UI com accordion Seg–Dom (hoje expandido; contagem concluídas/total)
