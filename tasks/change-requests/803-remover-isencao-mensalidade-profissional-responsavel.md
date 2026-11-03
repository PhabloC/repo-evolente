# Task 803 - Remover isenção de mensalidade de profissional e responsável

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (não envolvido)

## Contrato

- `contracts/openapi.yaml#/paths/~1users~1{userId}` (PATCH)
- `contracts/openapi.yaml#/components/schemas/UpdateUserRequest`
- `contracts/openapi.yaml#/components/schemas/User`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 072 — `tasks/slices/072-gestao-operacional-usuarios-master.md`

## Objetivo

Retirar a isenção administrativa de mensalidade (`feeExempt`) de profissional e responsável. Master continua sem cobrança pelo papel, inclusive quando atua como profissional (Task 802).

## Decisão humana confirmada

- Pedido humano: "Pode tirar a isenção de mensalidade do profissional e paciente"

## Premissas adotadas

- Como nada foi publicado, a migration `1950000000000-AddFeeExemptToUsers` foi removida em vez de compensada; no banco local a coluna foi descartada e o registro da migration apagado (nenhum usuário estava isento)

## Dependências

- Tasks 800, 801 e 802 — done

## Contexto mínimo

- esta task e o Slice 072
- `backend/src/modules/users/`, `backend/src/modules/subscriptions/subscriptions.service.ts`
- `front-end/src/pages/Main/AdminUsers/`, `front-end/src/types/admin.ts`

## Contexto sob demanda

- nenhum

## Orçamento de contexto

- baixo

## Critérios de aceite

- [x] Contrato, DTO, entidade e resposta sem `feeExempt`
- [x] Gate de assinatura isenta apenas a conta master
- [x] Edição de profissional/responsável só altera nome, e-mail e telefone
- [x] Tabela e perfil sem selo/linha de isenção

## Fora de escopo

- Mobile

## Resultado da execucao

- Backend: removidos coluna, DTO, `syncBillingExemption`, validação `FEE_EXEMPT_NOT_APPLICABLE`, checagens no gate de assinatura e testes da isenção
- Front: removidos checkbox de isenção, selo "Isento da mensalidade", linha "Mensalidade" do perfil e campo nos tipos; selo "Também profissional" mantido

## Handoff

- `.agents/state/handoffs/TASK-803.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/database/migrations/1950000000000-AddFeeExemptToUsers.ts` (removido)
- `backend/src/modules/users/entities/user.entity.ts`
- `backend/src/modules/users/dto/update-user.dto.ts`
- `backend/src/modules/users/users.repository.ts`
- `backend/src/modules/users/users.typeorm.repository.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `front-end/src/types/admin.ts`
- `front-end/src/pages/Main/AdminUsers/EditUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/editUserModal.module.css`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validacoes executadas

- Backend: `users.service.spec` 19/19; `npm run build` ok
- Front: tsc/eslint sem erros nos arquivos alterados; testes de edição, master profissional e exclusão passando
- Falhas antigas de AdminUsers ("consultar perfil", 2× "criar usuário master") seguem iguais; testes da página sofrem timeout intermitente sob carga

## Pendencias pos-task

- Nenhuma específica

## Status final

done
