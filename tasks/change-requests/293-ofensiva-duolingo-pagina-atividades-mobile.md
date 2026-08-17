# Task 293 - Ofensiva estilo Duolingo na pagina de atividades mobile

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

- não se aplica (cálculo local a partir das atividades da semana já carregadas)

## Modo de execucao

single-stack

## Slice vertical

- Slice 008 - Trilhas semanais e evolucao
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

assets locais `mobile/assets/fire.png` e `mobile/assets/fire-off.png` + pedido de ofensiva tipo Duolingo

## Objetivo

Exibir ofensiva (streak) à direita do título "Atividades": fogo aceso quando em dia, fogo apagado quando fora do dia, com o número de dias consecutivos sobre a imagem.

## Contexto mínimo

- esta task
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/components/ShellScreenTopBar/`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Cálculo | atividades da semana / completed | regra de streak | sim |
| Assets | `mobile/assets/fire.png`, `fire-off.png` | badge | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] badge de ofensiva no `rightAction` do header "Atividades"
- [x] `fire.png` quando em dia; `fire-off.png` quando não
- [x] número de dias de ofensiva sobreposto à imagem
- [x] util de cálculo com testes

## Dependencias

- Task 219 - cabeçalho Atividades igual ao Perfil — done

## Resultado da execucao

- `computeTrailStreak` calcula sequência na semana atual (dias sem atividade não quebram nem incrementam)
- em dia = sem pendência hoje e sem dia anterior incompleto
- `TrailStreakBadge` no header da tela de atividades

## Handoff

- `.agents/state/handoffs/TASK-293.md`

## Arquivos alterados

- `mobile/src/features/trail/utils/computeTrailStreak.ts`
- `mobile/src/features/trail/utils/computeTrailStreak.test.ts`
- `mobile/src/features/trail/components/TrailStreakBadge/`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `tasks/change-requests/293-ofensiva-duolingo-pagina-atividades-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
