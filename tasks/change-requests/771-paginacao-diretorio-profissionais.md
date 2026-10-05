# Task 771 - Paginação independente no diretório de profissionais

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /professionals` — `nearbyPage`, `othersPage`, `pageSize`
- `ProfessionalDirectoryListResponse.nearbyPage` / `othersPage`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Resultado da execucao

- API pagina `nearby` e `others` de forma independente.
- Web mostra controles de paginação em cada seção (6 itens por página).
- Busca/área reiniciam as páginas.

## Contexto utilizado

- OpenAPI, professionals.service, página Professionals, ACCESSIBILITY.md

## Handoff

- `.agents/state/handoffs/TASK-771.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/.../list-professionals-query.dto.ts`
- `backend/.../professionals.service.ts(+spec)`
- `front-end/.../useProfessionalsDirectory.ts`
- `front-end/.../Professionals/index.tsx(+test)`
- `front-end/.../styles.module.css`
- `front-end/.../professionalService.ts`
- `front-end/.../types/professional.ts`
- `front-end/.../professionalsDirectoryPagination.ts(+test)`

## Validacoes executadas

- jest professionals.service — 9 ok
- vitest Professionals + pagination util — 4 ok

## Acessibilidade

- `nav` com `aria-label` por seção
- botões Anterior/Próxima com `aria-label`
- página atual com `aria-current="page"`
- resumo com `aria-live="polite"`

## Pendencias pos-task

- Conferência visual com mais de 6 profissionais em cada seção

## Status final

done
