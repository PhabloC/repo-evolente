# Task 393 - Reverter criação de atividade quando o upload falhar na biblioteca web

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

- `contracts/openapi.yaml#/paths/~1contents/post`
- `contracts/openapi.yaml#/paths/~1contents~1{contentId}~1media/post`
- `contracts/openapi.yaml#/paths/~1contents~1{contentId}/delete`

## Modo de execução

single-stack

## Slice vertical

- Slice 006 - Catalogo de conteudos do master
- `tasks/slices/006-catalogo-conteudos-master.md`

## Referência visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

correção funcional de fluxo, sem mudança de layout

### Fonte primaria visual

- `front-end/src/pages/Main/Library/index.tsx`

## Objetivo

Evitar atividades órfãs sem mídia na biblioteca quando `createContent` conclui e o upload posterior falha.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Fluxo de create + upload | `front-end/src/pages/Main/Library/index.tsx` | adicionar rollback com `deleteContent` | sim |
| Serviço HTTP | `front-end/src/services/contents/contentService.ts` | confirmar APIs já disponíveis | sim |
| Cobertura | `front-end/src/pages/Main/Library/index.test.tsx` | regressão do rollback | sim |

## Orçamento de contexto

- baixo
- estratégia: rollback no front com as APIs já existentes; sem mudar o contrato nem o backend nesta task

## Critérios de conclusão

- [x] falha de upload após criação remove a atividade recém-criada
- [x] edição com falha de upload não exclui o conteúdo existente
- [x] o erro exibido ao usuário continua sendo o do upload
- [x] regressão coberta por teste
- [x] suíte da Library executada

## Origem

- comentário de code review (`P2 MÉDIO`) apontando que create + upload não são atômicos e deixam atividade órfã sem mídia

## Resultado da execucao

- o `handleSubmit` passou a guardar o `id` criado e, se o upload falhar, chama `deleteContent` em melhor esforço antes de repropagar o erro
- falha no `buildMediaUploadPayload` também dispara o mesmo rollback, porque o `try` interno cobre as duas etapas
- no modo edição, o rollback não roda — o conteúdo já existia e não deve ser apagado
- teste novo cobre create → upload rejeitado → `deleteContent(contentId)` e mensagem de erro no modal

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 006
- contexto sob demanda: página Library, `contentService`, teste da Library
- contexto evitado: backend e atomicidade no servidor — a correção pedida no review foi o rollback no cliente

## Handoff

- `.agents/state/handoffs/TASK-393.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx`
- `cd front-end && npx eslint src/pages/Main/Library/index.tsx src/pages/Main/Library/index.test.tsx`

## Pendencias pos-task

- o eslint ainda aponta `Card` não usado em `Library/index.tsx` (pré-existente, fora do escopo)
- atomicidade real no backend (transação create+upload) continua fora de escopo; o rollback no cliente cobre o caso órfão

## Status final

done
