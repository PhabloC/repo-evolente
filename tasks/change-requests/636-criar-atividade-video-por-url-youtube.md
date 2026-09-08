# Task 636 - Criar atividade de vídeo por URL do YouTube

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end (React/Vite)
- backend
- contrato OpenAPI

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (não envolvido nesta task)

## Contrato

- `contracts/openapi.yaml#/paths/~1contents`
- `contracts/openapi.yaml#/components/schemas/CreateContentRequest`
- `contracts/openapi.yaml#/components/schemas/Content`

## Modo de execução

cross-stack

## Slice vertical

- Slice 006 - Catalogo de conteudos do master
- `tasks/slices/006-catalogo-conteudos-master.md`

## Referência visual

- Fonte primária: print enviado pelo usuário nesta solicitação (modal Nova atividade).
- Fonte complementar: `design-system/front/Design_System_Evolente_Desktop.md`.

## Objetivo

Permitir que o master crie uma atividade do tipo vídeo informando uma URL do YouTube no modal Nova atividade, como alternativa ao upload de arquivo.

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
| UI web | print enviado pelo usuário, `design-system/front/Design_System_Evolente_Desktop.md` | adicionar a opção no modal preservando layout |
| Front-end | `front-end/docs/ai/AGENTS.md`, `ACCESSIBILITY.md` | manter padrões de formulário e acessibilidade |
| API | `contracts/openapi.yaml` | declarar `mediaUrl` opcional no create |
| Backend | `backend/docs/ai/AGENTS.md` | validar e persistir URL sem upload |

## Orçamento de contexto

- Risco: médio; mudança cruza contrato, backend e modal, mas fica restrita ao fluxo de criação de conteúdo.
- Estratégia de redução: não alterar runtime mobile nem visualização completa de vídeo fora do modal.

## Critérios de conclusão

- [x] Modal Nova atividade permite escolher entre upload de arquivo e URL do YouTube para vídeo.
- [x] URL do YouTube é validada no front e no backend.
- [x] `POST /contents` aceita `mediaUrl` para conteúdo `video`.
- [x] Criação por URL não exige upload posterior nem cria órfão.
- [x] Testes focados foram adicionados; backend executado com sucesso e front bloqueado por runner.

## Resultado da execucao

- Contrato `POST /contents` documenta `mediaUrl` opcional para vídeo com URL HTTPS do YouTube.
- Backend valida que `mediaUrl` externa só é aceita para `video` e apenas em hosts do YouTube (`youtube.com`, `m.youtube.com`, `youtu.be`), persistindo na coluna `media_url` existente sem `mediaStorageKey`.
- Modal Nova atividade passou a exibir, quando `Tipo = Vídeo`, um seletor de origem entre `Arquivo` e `URL do YouTube`.
- Criação por URL envia `mediaUrl` no `createContent` e não chama `uploadContentMedia`.
- Criação por arquivo continua preservada para áudio e vídeo.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e Slice 006.
- Contexto sob demanda: print enviado no chat, `design-system/front/Design_System_Evolente_Desktop.md`, `front-end/docs/ai/AGENTS.md`, `front-end/docs/ai/ACCESSIBILITY.md`, `backend/docs/ai/AGENTS.md`, `contracts/openapi.yaml` e arquivos do módulo de conteúdos.
- Evitado: runtime mobile e mudanças de player fora do modal/criação.

## Handoff

- `.agents/state/handoffs/TASK-636.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/contents/dto/create-content.dto.ts`
- `backend/src/modules/contents/contents.repository.ts`
- `backend/src/modules/contents/contents.typeorm.repository.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- esta task, `tasks/slices/006-catalogo-conteudos-master.md`, `tasks/000-index.md`

## Validacoes executadas

- `cd backend && npm run test -- contents.service.spec.ts` — ok, 14 testes.
- `cd front-end && cmd /c node_modules\\.bin\\vitest.cmd run src/pages/Main/Library/index.test.tsx --pool=vmThreads` — falhou antes de executar testes por incompatibilidade ESM do `react-router` com `vmThreads`.
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx src/pages/Main/Library/ContentFormModal.test.ts` — falhou antes de executar testes por timeout ao iniciar worker.
- `cd front-end && cmd /c node_modules\\.bin\\tsc.cmd --noEmit --pretty false` — falhou por erros preexistentes em `Patients` e `Plans`, sem erro nos arquivos desta task.
- `cd backend && cmd /c node_modules\\.bin\\tsc.cmd --noEmit` — falhou por erros preexistentes em specs de admin/contents bootstrap/patients/reports/trails/e2e, sem erro nos arquivos desta task.

## Pendencias pos-task

- A reprodução nativa de URLs do YouTube no mobile pode exigir task própria caso o runtime atual espere somente arquivo direto de vídeo.
- O runner de testes front precisa de ajuste de configuração para `react-router`/ESM ou estabilidade dos workers antes de validar este teste no ambiente local.

## Status final

done
