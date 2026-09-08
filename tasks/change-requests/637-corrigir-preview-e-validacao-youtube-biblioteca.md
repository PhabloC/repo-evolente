# Task 637 - Corrigir preview e validação YouTube na biblioteca

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end (React/Vite)
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (não envolvido nesta task)

## Contrato

- Não altera contrato OpenAPI.

## Modo de execução

cross-stack

## Slice vertical

- Slice 006 - Catalogo de conteudos do master
- `tasks/slices/006-catalogo-conteudos-master.md`

## Origem

- `ajustes.md`, itens 1, 2 e 3 do code review sobre URLs do YouTube em conteúdos de vídeo.

## Objetivo

Corrigir a reprodução e a validação de vídeos externos do YouTube na biblioteca master, garantindo que apenas URLs com identificador de vídeo sejam aceitas e que o preview web use player compatível.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI web | `front-end/docs/ai/AGENTS.md`, `front-end/docs/ai/ACCESSIBILITY.md` | manter padrões do modal de preview e acessibilidade do iframe |
| Backend | `backend/docs/ai/AGENTS.md` | validar update/create no módulo de conteúdos |
| Code review | `ajustes.md` | confirmar escopo dos defeitos apontados |
| Testes | specs do módulo de conteúdos e testes da biblioteca | cobrir URLs válidas/inválidas e preview YouTube |

## Orçamento de contexto

- Risco: médio; mudança cruza front-end e backend, mas fica restrita ao fluxo de conteúdo de vídeo por URL externa.
- Estratégia de redução: não alterar contrato, runtime mobile, upload de arquivo, nem catálogo de jogos.

## Critérios de conclusão

- [x] Preview web renderiza URL do YouTube em iframe/player incorporável, sem repassar página `watch`/`youtu.be` diretamente para `<video>`.
- [x] Criação backend aceita apenas URLs do YouTube que contenham identificador de vídeo em formatos `watch?v=`, `youtu.be/`, `shorts/` ou `embed/`.
- [x] Atualização backend não preserva URL externa incompatível quando o conteúdo deixa de ser vídeo.
- [x] Testes focados cobrem os cenários corrigidos ou registram bloqueio objetivo.

## Resultado da execucao

- Front-end: criado utilitário `youtubeMedia` para extrair ID, validar URL reproduzível e gerar URL de embed; o formulário passou a rejeitar páginas/canais sem vídeo e o preview renderiza YouTube em `iframe` com título acessível.
- Backend: a validação de `mediaUrl` passou a exigir ID de vídeo nos formatos aceitos; ao alterar conteúdo com URL externa para tipo não vídeo, os campos de mídia externa são limpos.
- Contrato: sem alteração, pois `mediaUrl` já existia no contrato da Task 636.
- Slice 006 permanece `done`; a task corrige lacunas do code review sem ampliar o escopo de catálogo ou mobile.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/006-catalogo-conteudos-master.md`.
- Contexto sob demanda: `ajustes.md`, `front-end/docs/ai/AGENTS.md`, `front-end/docs/ai/ACCESSIBILITY.md`, `backend/docs/ai/AGENTS.md`, `.agents/state/handoffs/TASK-636.md`, arquivos do módulo de biblioteca web e service/spec de conteúdos.
- Contexto evitado: contrato OpenAPI e runtime mobile, porque a correção não alterou schema nem reprodução no app nativo.

## Handoff

- `.agents/state/handoffs/TASK-637.md`
- Decisão preservada: URL do YouTube continua persistida como `mediaUrl`; a conversão para embed fica no consumo web.
- Próximo contexto recomendado: carregar esta task, `front-end/src/utils/youtubeMedia.ts`, `MediaPreviewModal.tsx` e `backend/src/modules/contents/contents.service.ts` se houver nova manutenção em mídia externa.

## Arquivos alterados

- `front-end/src/utils/youtubeMedia.ts`
- `front-end/src/utils/youtubeMedia.test.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/MediaPreviewModal.tsx`
- `front-end/src/pages/Main/Library/MediaPreviewModal.test.tsx`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `tasks/change-requests/637-corrigir-preview-e-validacao-youtube-biblioteca.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-637.md`

## Validacoes executadas

- `cd backend && npm run test -- contents.service.spec.ts` — ok, 16 testes.
- `cd front-end && cmd /c node_modules\\.bin\\vitest.cmd run src/utils/youtubeMedia.test.ts src/pages/Main/Library/ContentFormModal.test.ts src/pages/Main/Library/MediaPreviewModal.test.tsx --pool=vmThreads` — ok, 12 testes.
- `cd front-end && cmd /c node_modules\\.bin\\tsc.cmd --noEmit --pretty false` — falhou por erros preexistentes em `Patients` e `Plans`; sem erro nos arquivos alterados.
- `cd backend && cmd /c node_modules\\.bin\\tsc.cmd --noEmit --pretty false` — falhou por erros preexistentes em specs de admin, contents bootstrap, patients, reports, trails e e2e; filtro posterior não encontrou erro em `contents.service.ts` ou `contents.service.spec.ts`.

## Pendencias pos-task

- Persistem falhas globais preexistentes de TypeScript fora do escopo desta task.
- Reprodução de YouTube no app mobile continua fora do escopo, conforme pendência preservada da Task 636.

## Status final

done
