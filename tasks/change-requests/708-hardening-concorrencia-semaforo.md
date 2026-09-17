# Task 708 - Hardening de concorrência no jogo Pare e Vá

## Status

done

## Resultado da execucao

O renderer agora invalida operações de fala no cleanup e nas trocas manuais, interrompe o áudio ativo, verifica o token antes da segunda fala e desabilita os controles durante `announcePraise()`. Os dois comentários de `ajustes.md` foram marcados como `[ok]`.

## Contexto utilizado

- `mobile/src/features/games/components/TrafficLightGameRenderer/index.tsx`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/docs/ai/QA.md`
- `tasks/slices/040-pare-e-va-semaforo.md`

## Handoff

Hardening concluído no runtime mobile do semáforo. Próximo contexto recomendado: corrigir os erros preexistentes do typecheck mobile caso o projeto queira uma validação global limpa.

## Arquivos alterados

- `mobile/src/features/games/components/TrafficLightGameRenderer/index.tsx`
- `ajustes.md`
- `tasks/000-index.md`
- `tasks/slices/040-pare-e-va-semaforo.md`
- `.agents/state/handoffs/TASK-708.md`

## Validacoes executadas

- `npm run typecheck`: executado; falhou por erros preexistentes em outros módulos e em `TrafficLightGameRenderer/styles.ts`, sem erro novo no `index.tsx` alterado.
- `npm run lint`: iniciado, mas travou no `expo lint` sem produzir diagnóstico; interrompido.
- `npx eslint src/features/games/components/TrafficLightGameRenderer/index.tsx --no-cache`: travou sem produzir diagnóstico; interrompido.
- `npm test -- --runInBand`: não executado porque o processo anterior de lint permaneceu travado.

## Pendencias pos-task

- Sanear os erros preexistentes do typecheck/lint global do mobile em task própria.

## Status final

done

## Tipo

mobile

## Stacks envolvidos

mobile

## Perfil do projeto

web: front-end (React/Vite); mobile: sim

## Contrato

Não se aplica — correção local de runtime e áudio no app mobile.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/040-pare-e-va-semaforo.md` (hardening do runtime existente; não cria novo slice).

## Objetivo

Evitar que falas e transições obsoletas do jogo Pare e Vá alterem a etapa atual ou continuem reproduzindo áudio depois de sair da tela.

## Escopo

- Invalidar a sequência de instrução quando a etapa mudar ou o componente desmontar.
- Interromper o áudio ativo no cleanup antes de permitir nova fala.
- Ignorar a continuação de `announcePraise()` quando Reiniciar, outra casa ou desmontagem invalidar a operação.
- Desabilitar os controles durante a transição assíncrona.
- Marcar os dois apontamentos correspondentes em `ajustes.md` como `[ok]`.

## Critérios de aceite

- A segunda fala de uma instrução antiga nunca é reproduzida após mudança de etapa ou desmontagem.
- Reiniciar ou selecionar outra casa durante o elogio não é sobrescrito pelo `next` antigo.
- Os controles ficam desabilitados durante a transição e voltam ao estado normal ao finalizar ou invalidar.
- `npm run lint`, `npm run typecheck` e `npm run test` passam, ou eventual limitação fica registrada.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/040-pare-e-va-semaforo.md`
- `mobile/src/features/games/components/TrafficLightGameRenderer/index.tsx`
- `mobile/src/features/games/services/gameSpeechService.ts`

## Contexto sob demanda

- `mobile/docs/ai/QA.md`: aplicar os checks locais da stack.
- Testes existentes de renderers de jogos: adicionar regressão somente se o harness já cobrir o fluxo sem ampliar o escopo.

## Orçamento de contexto

Até 8 fontes; limitar a mudança ao renderer, serviço de parada de áudio, testes diretamente relacionados, review e rastreabilidade.

## Dependências

- Task 429 / Slice 040.
