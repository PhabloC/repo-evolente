# Task 751 - API do diretório de profissionais para o responsável

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

- `GET /professionals`
- schemas de listagem/item do diretório (campos públicos)

## Modo de execucao

cross-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Objetivo

Expor listagem autenticada de profissionais elegíveis para o responsável consultar no diretório web.

## Dependências

- Nenhuma task bloqueante; baseia-se no cadastro profissional e na área do responsável já entregues.

## Comportamento esperado

- Endpoint autenticado com bearer; papel `responsavel` com acesso liberado.
- Retorna apenas profissionais com usuário `active`, `accessGranted=true` e perfil profissional existente.
- Query opcional de busca por nome/especialidade e paginação (`page`, `pageSize`).
- Payload público: id, nome, avatarUrl, specialties, professionalRegistry, practiceType, clinicName/clinicPhone quando clínica.
- Não retorna e-mail pessoal, CPF, CNPJ, senha nem dados de assinatura.

## Fora de escopo

- UI web (Task 752)
- Mobile
- Criação/aprovação de vínculo
- Endpoint público sem autenticação

## Criterios de aceite

- [x] `contracts/openapi.yaml` declara `GET /professionals` e schemas.
- [x] Backend implementa o endpoint com autorização do responsável.
- [x] Filtro exclui inativos / sem acesso / sem perfil.
- [x] Busca e paginação funcionam conforme contrato.
- [x] Build do backend passa.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e Slice 063

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Contrato | `contracts/openapi.yaml` (professionals/users) | path, schemas e segurança | sim |
| Persistência | módulo de profissionais/users no backend | query e filtros | sim |
| Segurança | `backend/docs/ai/SECURITY.md` | campos públicos vs sensíveis | sim |

## Orçamento de contexto

- médio

## Estratégia de redução

- Ler só módulos de professionals/users e o trecho do OpenAPI; não reabrir Slice 053 inteiro além da regra de vínculo fora de escopo.

## Resultado da execucao

- Contrato e backend de `GET /professionals` entregues para o responsável autenticado com acesso liberado.
- Listagem filtra `accessGranted` + usuário ativo profissional, com busca e paginação.
- Dependência circular com assinaturas resolvida via `forwardRef`.

## Contexto utilizado

- OpenAPI (professionals), módulo professionals, UsersService, SECURITY.md, SubscriptionsModule.

## Handoff

- `.agents/state/handoffs/TASK-751.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/professionals/dto/list-professionals-query.dto.ts`
- `backend/src/modules/professionals/professionals.controller.ts`
- `backend/src/modules/professionals/professionals.service.ts`
- `backend/src/modules/professionals/professionals.service.spec.ts`
- `backend/src/modules/professionals/professionals.repository.ts`
- `backend/src/modules/professionals/professionals.in-memory.repository.ts`
- `backend/src/modules/professionals/professionals.typeorm.repository.ts`
- `backend/src/modules/professionals/professionals.module.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/subscriptions/subscriptions.module.ts`
- `tasks/slices/063-diretorio-profissionais-responsavel-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx jest --runInBand professionals.service.spec --no-coverage` — ok (6 testes)
- `npm run build` (backend) — ok

## Pendencias pos-task

- Task 752: botão e página web.

## Status final

done
