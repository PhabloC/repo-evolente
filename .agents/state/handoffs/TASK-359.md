# Handoff - Task 359

## Task

- identificador: 359
- título: Alinhar sino de Ultimos avisos ao Resumo rapido mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010

## Decisões preservadas

- decisão: alinhar apenas o sino do item não lido em "Ultimos avisos", sem reabrir os demais estados da lista
- motivo: o pedido era estritamente visual e o asset `bell.webp` já estava consolidado na tela
- impacto: a lista reaproveita a linguagem do "Resumo rápido" só na pastilha do sino

## Contexto utilizado

- `ResponsavelNotificationsScreen.tsx`
- `styles.ts` da screen
- `HomeActionCard/index.tsx`
- handoff `TASK-283`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- task/index/slice/handoff 359

## Validações executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run test` - ok (`26` suites, `90` testes)

## Pendências ou bloqueios

- `lint` e `typecheck` do mobile continuam com débitos antigos fora da tela de avisos

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-359.md`
