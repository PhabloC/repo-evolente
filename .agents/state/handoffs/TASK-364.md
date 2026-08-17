# Handoff - Task 364

## Task

- identificador: 364
- título: Reduzir check.webp arredondado na trilha e avisos mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 008

## Decisões preservadas

- decisão: adicionar inset opcional para imagens na `IconPill`
- motivo: reduzir só o `check.webp` arredondado sem mexer no resto das imagens
- impacto: trilha e avisos passam a ter respiro interno no check

## Contexto utilizado

- `IconPill/index.tsx`
- `TrailTodayScreen.tsx`
- `ResponsavelNotificationsScreen.tsx`
- handoff `TASK-363`

## Arquivos alterados

- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- task/index/slice/handoff 364

## Validações executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run test` - ok (`27` suites, `95` testes)

## Pendências ou bloqueios

- `lint` e `typecheck` do mobile continuam com débitos antigos fora da trilha e dos avisos

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-364.md`
