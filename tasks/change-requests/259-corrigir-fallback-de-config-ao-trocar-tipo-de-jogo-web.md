# Task 259 - Corrigir fallback de config ao trocar tipo de jogo web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` contents

## Modo de execucao

single-stack

## Slice vertical

- Slice 031 - Jogo caça-palavras
- `tasks/slices/031-jogo-caca-palavras.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste incremental solicitado via code review

### Fonte primaria visual

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`

## Objetivo

Impedir que a edição de um conteúdo `word-search` reutilize `gameConfig` incompatível ao trocar o jogo para `alphabet` ou `alphabet-writing`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/031-jogo-caca-palavras.md`
- `.agents/state/handoffs/TASK-164.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Tipos de config | `front-end/src/types/content.ts` | distinguir config alfabética de `word-search` | sim |
| Fallback atual | `front-end/src/pages/Main/Library/ContentFormModal.tsx` | corrigir `buildGamePayload` | sim |
| Defaults do caça-palavras | `front-end/src/pages/Main/Library/wordSearchGameDefaults.ts` | preservar fallback correto do tipo `word-search` | sim |
| Cobertura da transformação | `front-end/src/pages/Main/Library/ContentFormModal.test.ts` | validar troca entre tipos de jogo | sim |
| Padrões da stack | `front-end/docs/ai/CODE_STYLE.md` | manter tipagem e utilitários | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a mudança ao modal de edição da biblioteca e à transformação de payload de jogo

## Criterios de conclusao

- [x] `buildGamePayload` só reaproveita config anterior quando ela é compatível com jogo alfabético
- [x] trocar de `word-search` para `alphabet` ou `alphabet-writing` gera `AlphabetGameConfig` padrão
- [x] teste cobre reaproveitamento válido e fallback incompatível

## Dependencias

- Task 157 - done
- Task 164 - done
- Task 169 - done
- Task 249 - done

## Resultado da execucao

- `buildGamePayload` passou a checar `isAlphabetGameConfig` antes de reaproveitar `existingContent.gameConfig`
- ao sair de `word-search`, o modal agora envia `AlphabetGameConfig` padrão com `letters`, `locale` e `voiceMode`
- foi criada cobertura de teste para o reaproveitamento compatível e para a migração de `word-search` para jogo alfabético

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/031-jogo-caca-palavras.md`
- `.agents/state/handoffs/TASK-164.md`

### Sob demanda

- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/wordSearchGameDefaults.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.test.ts`
- `front-end/docs/ai/CODE_STYLE.md`

## Handoff

- `.agents/state/handoffs/TASK-259.md`

## Arquivos alterados

- `tasks/change-requests/259-corrigir-fallback-de-config-ao-trocar-tipo-de-jogo-web.md`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.test.ts`
- `tasks/slices/031-jogo-caca-palavras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-259.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/Library/ContentFormModal.test.ts` - ok
- `cd front-end && npm run lint` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
