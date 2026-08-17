# Handoff - Task 388

## Task

- identificador: 388
- título: Consumir parâmetro de aba inicial no shell do responsável mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010 - App do responsavel: home, perfil e notificacoes

## Decisões preservadas

- `initialTab` volta a ter semântica de aba de entrada: é aplicado ao estado local e limpo em seguida, em vez de prevalecer sobre `activeKey` enquanto existir
- a renderização das telas e a `ShellTabBar` usam apenas `activeKey`; a derivação `resolvedActiveKey` foi removida
- a sincronização do parâmetro acontece durante a render, porque o lint local (`react-hooks/set-state-in-effect`) proíbe `setState` síncrono dentro de `useEffect`
- limpar o parâmetro também garante que navegar de novo para a mesma aba a partir de `ResponsavelStackScreenFrame` continue funcionando

## Contexto utilizado

- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/shell/components/ResponsavelStackScreenFrame.tsx`
- `mobile/src/routes/params.ts`

## Arquivos alterados

- navigator do shell do responsável, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npx eslint src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `cd mobile && npm run test`
- `cd mobile && npm run typecheck`

## Pendências ou bloqueios

- sem teste automatizado de componente no projeto; a regressão de navegação não está coberta por teste

## Próximo contexto recomendado

- `mobile/src/features/shell/components/ResponsavelStackScreenFrame.tsx`, caso as telas em stack precisem preservar a aba anterior ao voltar
