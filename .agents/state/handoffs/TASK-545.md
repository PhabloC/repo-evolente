# Handoff — Task 545

## Identificador

Task 545

## Título

Alinhar opções da anamnese (tópico 6) às categorias da biblioteca

## Slice vertical

Slice 004 - Onboarding responsavel, crianca e anamnese

## Status final

done

## Decisões preservadas

- Pergunta 6 reusa `CONTENT_CATEGORY_FORM_OPTIONS` (mesmas 9 categorias/labels da biblioteca).
- Valores internos do enum (`linguagem`, `fala`, etc.) não mudaram.
- Legados `memoria`/`matematica` exibem como Cognição via `getContentCategoryLabel` / `CATEGORY_LABELS`.
- Enum OpenAPI / persistência backend de anamnese não foram alterados.

## Contexto mínimo lido

- `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, slice 004

## Contexto sob demanda carregado

- `contentOptions.ts`, `guardianOptions.ts`, RegisterGuardian, PatientProfile, reports.service

## Arquivos alterados

- `front-end/src/constants/guardianOptions.ts`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `backend/src/modules/reports/reports.service.ts`

## Validações executadas

- lints front: ok

## Pendências

- nenhuma

## Próximo contexto recomendado

- nenhum; mudança isolada de labels/opções

## Não carregar na próxima etapa

- `design-system/`, `mobile/`, contrato OpenAPI completo
