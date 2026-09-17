# Task 657 - Semáforo: serializar áudios do avanço

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

Evitar que a instrução da próxima etapa interrompa o áudio de feedback “Muito bem!”.

## Contexto mínimo

- `mobile/src/features/games/components/TrafficLightGameRenderer/index.tsx`
- `mobile/src/features/games/components/GameSessionAudio/index.tsx`
- `mobile/src/features/games/services/gameSpeechService.ts`

## Contexto sob demanda

- Nenhum.

## Orçamento de contexto

Somente o fluxo de avanço e os serviços de áudio envolvidos.

## Resultado da execucao

O avanço agora aguarda `announcePraise()` terminar antes de trocar a etapa. Assim, a nova instrução só é iniciada depois que “Muito bem!” for concluído.

## Arquivos alterados

- `mobile/src/features/games/components/TrafficLightGameRenderer/index.tsx`

## Validacoes executadas

- `git diff --check` — sem erros.
- `cd mobile && npx tsc --noEmit --pretty false 2>&1 | Select-String "TrafficLightGameRenderer"` — sem erros no renderer; permanecem erros preexistentes em `TrafficLightGameRenderer/styles.ts` sobre `colors.text`.

## Pendencias pos-task

- Nenhuma.

## Status final

done
