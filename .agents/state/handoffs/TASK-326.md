# Handoff - Task 326

## Task

- identificador: 326
- título: Excluir conteúdos da biblioteca master
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catalogo
- objetivo de negócio: permitir exclusão real de conteúdos pelo master sem quebrar itens já usados
- entrega verificável: lixeira funcional na biblioteca web e endpoint de exclusão com trava para conteúdo em uso
- status do slice: done

## Decisões preservadas

- decisão: excluir de verdade, não apenas inativar
- motivo: a demanda do catálogo pediu lixeira operacional
- impacto: o slice deixa de ter a restrição anterior de “inativar, não excluir”

- decisão: bloquear exclusão quando houver uso em trilhas ou evolução
- motivo: evitar órfãos operacionais no produto
- impacto: o backend responde erro claro e a UI exibe feedback sem apagar o item

- decisão: apagar a mídia do storage ao excluir
- motivo: evitar lixo no bucket para conteúdos já removidos
- impacto: o delete do catálogo também faz limpeza do arquivo associado

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/326-excluir-conteudos-da-biblioteca-master.md`
- `tasks/slices/006-catalogo-conteudos-master.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | contrato | adicionar `DELETE /contents/{contentId}` |
| `backend/src/modules/contents/` | backend | service, repository, controller e testes |
| `front-end/src/pages/Main/Library/` | UI web | lixeira, modal e teste |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile e demais áreas fora do catálogo | não envolvidas nesta exclusão |

## Resultado por stack

- backend: done
- front-end: done

## Arquivos alterados

- `backend/src/modules/contents/contents.controller.ts`
- `backend/src/modules/contents/contents.repository.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/src/modules/contents/contents.typeorm.repository.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `front-end/src/services/contents/contentService.ts`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `contracts/openapi.yaml`
- `tasks/change-requests/326-excluir-conteudos-da-biblioteca-master.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-326.md`

## Validações executadas

- `cd backend && npm run test -- contents.service.spec.ts` — ok
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok

## Pendências ou bloqueios

- sem bloqueio para exclusão unitária
- restauração, exclusão em lote e novas regras de retenção seguem fora do escopo

## Próxima ação sugerida

- abrir nova task apenas se o produto quiser reciclagem/restauração, exclusão em lote ou ampliar as travas de dependência
