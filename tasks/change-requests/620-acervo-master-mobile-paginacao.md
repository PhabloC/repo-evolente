# Task 620 - Paginação do Acervo master mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /contents` com filtros atuais; paginação local quando a resposta não expõe metadados paginados.

## Modo de execução

single-stack

## Slice vertical

- Slice 006 — `tasks/slices/006-catalogo-conteudos-master.md`

## Objetivo

Adicionar paginação à grade do Acervo master mobile, preservando filtros por tipo e status.

## Dependências

- nenhuma

## Contexto mínimo

- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `mobile/src/features/admin/contents/{screens/AdminContentsScreen.tsx,hooks/useAdminContents.ts,services/adminContentsService.ts,types/content.ts}`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI mobile | `mobile/src/features/admin/contents/screens/listStyles.ts` | integrar controles de paginação no padrão do acervo. |

## Orçamento de contexto

- baixo
- estratégia: paginação na lista já filtrada, sem ampliar API.

## Critérios de aceite

- [x] Exibe uma página por vez com anterior/próxima e indicador de página.
- [x] Trocar filtros retorna à primeira página.
- [x] Estado vazio e acessibilidade permanecem preservados.

## Resultado da execução

- Paginação local de 8 itens aplicada após os filtros do Acervo.

## Contexto utilizado

- Task 620, Slice 006, AdminContentsScreen e listStyles.

## Arquivos alterados

- `mobile/src/features/admin/contents/screens/{AdminContentsScreen.tsx,listStyles.ts}`.

## Validações executadas

- Typecheck mobile executado; os erros restantes são preexistentes em MasterProfile, Auth, jogos e Trail.

## Pendências pós-task

- Smoke em dispositivo para controles da grade.

## Handoff

- Criado em `.agents/state/handoffs/TASK-620.md`.

## Status final

done
