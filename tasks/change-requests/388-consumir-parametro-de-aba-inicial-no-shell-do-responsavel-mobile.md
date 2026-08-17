# Task 388 - Consumir parâmetro de aba inicial no shell do responsável mobile

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

- não se aplica

## Modo de execução

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referência visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

correção funcional de navegação, sem mudança de layout

### Fonte primaria visual

- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`

## Objetivo

Fazer o shell do responsável consumir `initialTab` como aba de entrada, liberando a navegação interna do shell logo depois, em vez de deixar o parâmetro prevalecer sobre o estado local.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Estado das abas do shell | `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx` | corrigir a precedência entre parâmetro e estado local | sim |
| Origem do parâmetro | `mobile/src/features/shell/components/ResponsavelStackScreenFrame.tsx` | confirmar quem navega com `initialTab` | sim |
| Tipagem da rota | `mobile/src/routes/params.ts` | confirmar que `initialTab` é opcional | não |

## Orçamento de contexto

- baixo
- estratégia: manter a mudança no navigator do shell do responsável

## Critérios de conclusão

- [x] `initialTab` deixa de prevalecer sobre o estado local após ser aplicado
- [x] o botão `Voltar` das telas de trilha, perfil e avisos volta a trocar a tela
- [x] a tab bar do shell continua refletindo a aba visível
- [x] `npm run lint` executado no arquivo alterado
- [x] `npm run test` executado

## Origem

- comentário de code review (`P2 MÉDIO`) apontando que `initialTab` continuava prevalecendo sobre `activeKey`, deixando `setActiveKey('home')` sem efeito visível

## Resultado da execucao

- removida a derivação `resolvedActiveKey = routeInitialTab ?? activeKey`; a renderização e a tab bar passaram a usar apenas `activeKey`
- `initialTab` passou a ser sincronizado com o estado local durante a render (padrão de ajuste de estado quando a prop muda), cobrindo também navegações para um shell já montado
- o parâmetro é limpo em efeito (`navigation.setParams({ initialTab: undefined })`) assim que aplicado, o que também permite repetir a mesma aba em navegações posteriores
- a limpeza do parâmetro deixou de depender do toque na tab bar

## Decisao tecnica

- a sincronização ficou em render, e não em `useEffect`, porque a regra `react-hooks/set-state-in-effect` do lint local proíbe `setState` síncrono dentro de efeito
- o efeito restante só atualiza o estado externo da navegação, sem `setState`

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 010
- contexto sob demanda: `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`, `mobile/src/features/shell/components/ResponsavelStackScreenFrame.tsx`, `mobile/src/routes/params.ts`
- contexto evitado: backend, front-end web e design system, porque a correção é local à navegação do shell mobile

## Handoff

- `.agents/state/handoffs/TASK-388.md`

## Arquivos alterados

- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `cd mobile && npm run test`
- `cd mobile && npm run typecheck`

## Pendencias pos-task

- o projeto não tem biblioteca de teste de componente instalada, então a regressão foi coberta por revisão manual do fluxo e não por teste automatizado

## Status final

done
