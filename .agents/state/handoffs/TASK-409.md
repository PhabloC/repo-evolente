# Handoff — Task 409

## Identificador

- task: 409
- título: Memória articulação: prévia web e runtime mobile
- slice: Slice 034
- status final: done

## Decisões preservadas

- Sem novo `gameType`; prompt condicional quando carta tem `instruction`
- Board trava até “Continuar” no prompt
- Aviso de material só se `requiresMaterial`

## Arquivos alterados

- `front-end/.../GamePreviewModal.tsx`, `styles.module.css`, `memoryGame.ts`
- `mobile/.../MemoryGameRenderer/*`, `utils/memoryGame.ts`, testes

## Validações

- memoryGame.test + MemoryGameRenderer tests (pass)

## Pendências

- Task 410
- Bootstrap no ambiente local ao subir o backend

## Próxima ação

Task 410 ou validar manualmente na biblioteca (aba Articulação) após restart do backend.
