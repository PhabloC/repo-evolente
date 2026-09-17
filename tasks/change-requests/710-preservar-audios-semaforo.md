# Task 710 - Preservar e validar áudios do semáforo

## Status

done

## Resultado da execucao

`audioUrl` foi incluído no tipo e preservado pelo normalizador de configurações traffic-light. O script de upload agora valida o catálogo completo de figuras e aborta antes do UPDATE quando houver arquivos faltantes ou duplicados. Os dois itens de `ajustes.md` foram marcados como `[ok]`.

## Contexto utilizado

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/scripts/upload-traffic-light-prompt-audios.mjs`
- `backend/docs/ai/QA.md`

## Handoff

Hardening de persistência e upload concluído. Próximo contexto recomendado: criar testes focados do normalizador/upload quando o backend estiver com a suíte tipada estabilizada.

## Arquivos alterados

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/scripts/upload-traffic-light-prompt-audios.mjs`
- `ajustes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-710.md`

## Validacoes executadas

- `npm run typecheck`: falhou por erros preexistentes em specs e tipos não relacionados.
- `npm run lint -- --no-cache`: interrompido após travamento sem diagnóstico.
- Revisão estrutural e `git diff --check` realizados.

## Pendencias pos-task

- Reexecutar lint/testes globais e adicionar teste focado quando a suíte estiver compilável.

## Status final

done

## Tipo

back

## Stacks envolvidos

backend

## Contrato

Interno — configuração e script de assets; sem alteração de endpoint.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/040-pare-e-va-semaforo.md` (hardening do slice existente; não cria novo slice).

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/040-pare-e-va-semaforo.md`
- arquivos de tipo, normalizador e script listados acima

## Contexto sob demanda

- `backend/docs/ai/QA.md`: checks locais da stack.

## Orçamento de contexto

Até 8 fontes; limitar a tipos, normalizador, script, validação e rastreabilidade.
