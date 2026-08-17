# Handoff - Task 365

## Task

- identificador: 365
- título: Evitar corte do check.webp na trilha e avisos mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 008

## Decisões preservadas

- decisão: adicionar `imageResizeMode` opcional à `IconPill`
- motivo: preservar a borda arredondada do `check.webp` sem crop
- impacto: só trilha e avisos usam `contain`; o resto continua como estava

## Contexto utilizado

- `IconPill/index.tsx`
- `TrailTodayScreen.tsx`
- `ResponsavelNotificationsScreen.tsx`
- handoff `TASK-364`

## Arquivos alterados

- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- task/index/slice/handoff 365

## Validações executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run test` - ok (`27` suites, `95` testes)

## Pendências ou bloqueios

- `lint` e `typecheck` do mobile continuam com débitos antigos fora da trilha e dos avisos

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-365.md`
