# Task 656 - Semáforo: remover instrução duplicada

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile (Expo)

## Perfil do projeto

- web: front-end
- mobile: sim

## Contrato

Não aplicável.

## Modo de execução

single-stack

## Slice vertical

- Slice 040 — `tasks/slices/040-pare-e-va-semaforo.md`

## Objetivo

Remover a repetição da instrução exibida na etapa do jogo do semáforo.

## Contexto mínimo

- `mobile/src/features/games/components/TrafficLightGameRenderer/index.tsx`
- `mobile/src/features/games/utils/trafficLightGame.ts`

## Contexto sob demanda

- `mobile/src/features/games/components/TrafficLightGameRenderer/styles.ts`, somente se o ajuste visual exigir.

## Orçamento de contexto

Carregar apenas o renderer e o parser da atividade.

## Resultado da execucao

Removida a segunda renderização de `rule.instruction`; o texto de `step.prompt` permanece como instrução visível da etapa.

## Arquivos alterados

- `mobile/src/features/games/components/TrafficLightGameRenderer/index.tsx`

## Validacoes executadas

- `git diff --check` — executado sem erro funcional.

## Pendencias pos-task

- Nenhuma.

## Status final

done
