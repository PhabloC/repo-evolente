# Handoff - Task 204

## Task

- identificador: 204
- título: Tela imersiva para execução de atividade no mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas semanais e evolucao
- objetivo de negócio: abrir a atividade em uma superfície dedicada, sem header extra
- entrega verificável: atividade abre sem cabeçalho superior e sem tab bar

## Decisões preservadas

- decisão: ocultar a tab bar do shell quando uma atividade estiver aberta
- motivo: transformar a execução em uma tela dedicada sem recriar a navegação inteira
- impacto: voltar para a lista restaura o shell normal

- decisão: remover hero e `ScreenHeader` da `TrailActivityScreen`
- motivo: o usuário quer focar apenas na atividade
- impacto: jogo, mídia, feedback e ações continuam, mas sem chrome superior

## Contexto utilizado

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/shell/navigators/styles.ts`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/shell/navigators/styles.ts`
- `tasks/change-requests/204-tela-imersiva-para-execucao-de-atividade-mobile.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-204.md`

## Validações executadas

- `cd mobile && npm run lint` — ok
- `cd mobile && npm run typecheck` — ok

## Pendências ou bloqueios

- nenhuma
