# Task 702 - Preservar áudios de instrução dos jogos

## Status

done

## Resultado da execucao

`instructionAudioUrl` foi adicionado ao contrato e preservado pelo builder de `sentence-fill`; o validator de `fluency` agora valida e copia o URL por etapa em criação e atualização. Os dois comentários de review foram marcados como `[ok]` em `ajustes.md`.

## Contexto utilizado

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/sentence-fill-game-assets.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/scripts/upload-game-session-audios.mjs`
- `backend/docs/ai/QA.md`

## Handoff

Hardening concluído nos dois fluxos de persistência de áudio. Próximo contexto recomendado: reexecutar build/testes do backend em ambiente sem o travamento do processo Nest.

## Arquivos alterados

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/sentence-fill-game-assets.ts`
- `backend/src/modules/contents/contents.service.ts`
- `ajustes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-702.md`

## Validacoes executadas

- `npm run build` (iniciado, sem saída por aproximadamente 20 segundos; interrompido por travamento observado).

## Pendencias pos-task

- Reexecutar `npm run lint`, `npm run test`, `npm run test:e2e` e `npm run build` em ambiente com o toolchain respondendo.

## Status final

done

## Tipo

back

## Stacks envolvidos

backend

## Contrato

Interno — atualizar os tipos/configurações de `sentence-fill` e `fluency`; sem mudança de endpoint.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/042-complete-a-frase.md` e `tasks/slices/045-fluencia-em-acao.md` (escopo de hardening dos slices existentes; não cria novo slice).

## Objetivo

Impedir que o bootstrap ou a API apaguem os áudios de instrução gravados dos jogos após reinício ou edição.

## Escopo

- Adicionar e preservar `instructionAudioUrl` no contrato e no builder de `sentence-fill`.
- Validar e copiar `instructionAudioUrl` em cada etapa de `fluency` durante criação e atualização.
- Cobrir regressão com testes automatizados dos fluxos afetados.
- Marcar os dois comentários correspondentes em `ajustes.md` como `[ok]`.

## Critérios de aceite

- URL de instrução existente em `sentence-fill` sobrevive ao bootstrap.
- URL de instrução existente em etapas `fluency` sobrevive à normalização da API.
- URL vazia ou inválida continua sendo rejeitada conforme as regras do validator.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/042-complete-a-frase.md`
- `tasks/slices/045-fluencia-em-acao.md`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/sentence-fill-game-assets.ts`
- `backend/src/modules/contents/contents.service.ts`

## Contexto sob demanda

- `backend/scripts/upload-game-session-audios.mjs`: confirmar o shape produzido pelo upload.
- testes específicos de contents/bootstrap: adicionar cobertura mínima de persistência.
- `backend/docs/ai/QA.md`: aplicar os checks locais da stack.

## Orçamento de contexto

Até 8 fontes; limitar a mudança aos tipos, builder, validator, testes, review e rastreabilidade.

## Dependências

- Tasks 436 e 483 (fluency).
- Tasks 432 e 547 (sentence-fill e áudio).
