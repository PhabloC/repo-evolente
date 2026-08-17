# Task 486 - Hardening da biblioteca web para config de jogos e preview

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

- sem mudança de contrato; ajuste no payload web e no fluxo de preview

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/006-catalogo-conteudos-master.md`

## Objetivo

Endurecer a biblioteca web para não salvar configs inválidas ao trocar conteúdos para `emotions`/`fluency`/`dialogue` e para ignorar respostas tardias do preview quando o modal já foi fechado ou substituído.

## Criterios de aceite

- [x] `buildGamePayload` gera config inicial válida para `emotions`, `fluency` e `dialogue`
- [x] preview não reaplica resposta tardia após fechar ou trocar o item aberto
- [x] testes de regressão cobrem os dois comportamentos
- [x] handoff gerado

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/change-requests/486-hardening-biblioteca-web-config-preview.md`
- `.agents/state/handoffs/TASK-401.md`
- `.agents/state/handoffs/TASK-437.md`

## Contexto sob demanda

- `front-end/AGENTS.md` e `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/REPO_MAP.md` e `front-end/docs/ai/QA.md`
- parsers locais de `emotions`, `fluency` e `dialogue`

## Orçamento de contexto

- 8 fontes
- estratégia: limitar à biblioteca web, serviço de conteúdo e testes focados

## Resultado da execucao

O formulário da biblioteca agora cria configs mínimas válidas para `emotions`, `fluency` e `dialogue`, e o preview web passou a descartar respostas tardias de `getContent` quando o usuário fecha ou troca o item aberto.

## Contexto utilizado

- slice 006
- handoffs 401 e 437
- `ContentFormModal`, `LibraryPage`, `contentService` e testes da biblioteca

## Handoff

- `.agents/state/handoffs/TASK-486.md`

## Arquivos alterados

- `front-end/src/services/contents/contentService.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.test.ts`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- src/pages/Main/Library/ContentFormModal.test.ts --testNamePattern "gera config inicial válida"` — PASS
- `npm run test -- src/pages/Main/Library/index.test.tsx --testNamePattern "ignores a late preview response after the modal is closed"` — PASS
- `npx eslint src/services/contents/contentService.ts src/pages/Main/Library/ContentFormModal.tsx src/pages/Main/Library/ContentFormModal.test.ts src/pages/Main/Library/index.tsx src/pages/Main/Library/index.test.tsx` — PASS

## Pendencias pos-task

- `npm run lint` global do `front-end` continua falhando por erros preexistentes fora deste escopo
- `npm run build` global do `front-end` continua falhando por configuração preexistente de TypeScript em `tsconfig.json`

## Status final

done
