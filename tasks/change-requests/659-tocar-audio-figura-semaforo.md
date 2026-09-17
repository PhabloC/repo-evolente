# Task 659 - Semáforo: tocar áudio da figura após instrução

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end (React/Vite)
- mobile (Expo)

## Contrato

Não aplicável.

## Modo de execução

cross-stack

## Slice vertical

- Slice 040 — `tasks/slices/040-pare-e-va-semaforo.md`

## Resultado da execucao

Após o áudio da instrução da cor, a atividade toca o áudio gravado da figura da etapa atual, sem sobreposição.

## Arquivos alterados

- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/trafficLightGame.ts`
- `mobile/src/features/games/components/TrafficLightGameRenderer/index.tsx`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/trafficLightGame.ts`
- `front-end/src/pages/Main/Library/TrafficLightPreviewModal.tsx`

## Validacoes executadas

- Typecheck filtrado do Semáforo — sem erros nos componentes/parsers alterados; permanecem dois erros preexistentes em `styles.ts` sobre `colors.text`.
- `git diff --check` — sem erros funcionais.

## Pendencias pos-task

- Nenhuma funcional.

## Status final

done
