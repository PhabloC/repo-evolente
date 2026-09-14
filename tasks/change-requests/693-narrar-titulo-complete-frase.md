# Task 693 - Narrar título antes da instrução Complete a frase

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Contrato

- Não aplicável.

## Modo de execução

single-stack

## Slice vertical

- `tasks/slices/042-complete-a-frase.md`

## Objetivo

Ao entrar no Complete a frase, narrar primeiro “Complete a frase” e depois reproduzir o áudio gravado da instrução.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/042-complete-a-frase.md`

## Contexto sob demanda

- `mobile/src/features/games/components/GameSessionAudio/index.tsx`;
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`;
- testes relacionados ao áudio de sessão.

## Orçamento de contexto

- 7 fontes; carregar somente o provider, renderer e testes envolvidos.

## Status final

done

## Resultado da execucao

- O Complete a frase usa o áudio existente que anuncia a atividade como primeiro áudio.
- Em seguida, o provider reproduz o novo áudio gravado “Toque na palavra que completa a frase”.

## Contexto utilizado

- `GameSessionAudio` e `GameActivityRenderer`.

## Handoff

- Sequência de dois áudios implementada sem alterar as demais atividades.

## Arquivos alterados

- `mobile/src/features/games/components/GameSessionAudio/index.tsx`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-693.md`

## Validacoes executadas

- `npm run upload:game-session-audios` — concluído; intro antigo, instrução nova e configuração foram atualizados.
- Typecheck possui erros preexistentes em outros arquivos não relacionados.

## Pendencias pos-task

- Corrigir os erros preexistentes do typecheck em task separada.
