# Task 767 - Filtro por área no diretório de profissionais (API)

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /professionals` — query opcional `specialty`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Referencia de design system

- Sem UI nesta task

## Origem da solicitacao

Pedido humano: no diretório de profissionais do responsável, filtrar pela área do profissional.

## Objetivo

Permitir filtrar `GET /professionals` pela especialidade/área de atuação, combinável com a busca por nome já existente.

## Dependências

- Task 751 (diretório)
- Task 758 (próximos / others)

## Comportamento esperado

- Query `specialty` opcional (string, max 80).
- Mantém profissionais cuja lista `specialties` contém a área (comparação sem acento e sem maiúsculas; aceita correspondência parcial).
- Combina com `search`, `page` e `pageSize`; `nearby`/`others` continuam após o filtro.
- Sem `specialty` (vazio), o diretório não restringe por área.

## Fora de escopo

- UI web (Task 768)
- Mobile
- Catálogo rígido de especialidades no cadastro
- Alterar campos públicos do item

## Criterios de aceite

- [x] OpenAPI declara `specialty` em `GET /professionals`.
- [x] Backend aplica o filtro no diretório.
- [x] Teste cobre área correspondente vs não correspondente.
- [x] Lint/testes focados do módulo passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e Slice 063

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Contrato | `contracts/openapi.yaml` (`GET /professionals`) | query `specialty` | sim |
| Listagem | `backend/src/modules/professionals/` | filtro após busca | sim |

## Orçamento de contexto

- baixo

## Estratégia de redução

- Não reabrir cadastro, assinatura nem modal de WhatsApp além do diretório.

## Resultado da execucao

- `GET /professionals` aceita `specialty` e filtra especialidades com normalização de acento/caixa.
- `nearby`/`others` permanecem após o recorte.

## Contexto utilizado

- OpenAPI `GET /professionals`, DTO e service do diretório, SECURITY.md (validação de query).

## Handoff

- `.agents/state/handoffs/TASK-767.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/professionals/dto/list-professionals-query.dto.ts`
- `backend/src/modules/professionals/professionals.service.ts`
- `backend/src/modules/professionals/professionals.service.spec.ts`
- `backend/src/modules/professionals/utils/specialty-filter.util.ts`
- `backend/src/modules/professionals/utils/specialty-filter.util.spec.ts`

## Validacoes executadas

- `npx jest --runInBand professionals.service.spec specialty-filter.util.spec --no-coverage` — 11 testes ok
- eslint nos arquivos do módulo alterados — ok

## Pendencias pos-task

- Task 768 (UI)

## Acessibilidade

- Não se aplica (API)

## Status final

done
