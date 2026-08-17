# Handoff - Task 360

## Task

- identificador: 360
- título: Deixar branco o bg do sino em Ultimos avisos mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010

## Decisões preservadas

- decisão: alterar só o fundo da pastilha do sino não lido
- motivo: o usuário pediu explicitamente bg branco sem mexer no asset nem na composição restante
- impacto: o `bell.webp` foi mantido e o ajuste ficou isolado aos estilos locais da tela

## Contexto utilizado

- `ResponsavelNotificationsScreen.tsx`
- `styles.ts` da screen
- handoff `TASK-359`

## Arquivos alterados

- `mobile/src/features/shell/screens/styles.ts`
- task/index/slice/handoff 360

## Validações executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run test` - ok (`26` suites, `90` testes)

## Pendências ou bloqueios

- `lint` e `typecheck` do mobile continuam com débitos antigos fora da tela de avisos

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-360.md`
