# Handoff - Task 207

## Task

- identificador: 207
- título: Rota real para execução de atividade mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas semanais e evolucao
- objetivo de negócio: abrir a atividade como screen real do app em vez de simular uma página dentro da aba
- entrega verificável: `TrailActivity` virou rota da stack e o shell só navega para ela

## Decisões preservadas

- decisão: reaproveitar `TrailActivityScreen` como screen da stack, sem criar uma segunda implementação visual
- motivo: separar navegação real sem duplicar a UI já refinada nas tasks 204–206
- impacto: a tela mantém o mesmo layout, mas agora com ciclo de vida de rota real

- decisão: remover `selectedActivity` do shell do responsável
- motivo: o shell não precisa mais controlar a atividade como estado local
- impacto: a tab bar some naturalmente porque a nova screen fica acima do shell na stack

## Contexto utilizado

- `mobile/src/routes/params.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Arquivos alterados

- `mobile/src/routes/params.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `tasks/change-requests/207-rota-real-para-execucao-de-atividade-mobile.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-207.md`

## Validações executadas

- `cd mobile && npm run lint` — ok com 2 warnings antigos em `alphabetWritingGame.ts`
- `cd mobile && npm run typecheck` — ok

## Pendências ou bloqueios

- nenhuma
