# Task 802 - Master que também atua como profissional, sem mensalidade

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

Substituir a troca de perfil (papel) da edição administrativa por uma opção, só para contas master, de também atuar como profissional. O master mantém o cargo, ganha o modo profissional (pacientes, planejamentos, relatórios) e não paga mensalidade.

## Decisões humanas confirmadas

- Pedido humano: "essa parte de poder mudar o perfil do usuario pode desconsiderar isso, mantem a possibilidade de excluir, visualizar inativar e editar"
- Pedido humano: "no usuario admin no editar coloca a possibilidade de marcar o admin para que ele possa ser um profissional também, só que o valor da mensalidade não vai ser cobrado para ele. Ele mantem o cargo de master"

## Premissas adotadas

- O papel continua único no usuário; o master marcado alterna o **modo de atuação** pela sidebar ("Atuar como profissional" / "Voltar ao modo master")
- No modo profissional o cliente envia `X-Acting-Role: profissional`; o backend só aceita o header para master com `actsAsProfessional`, e a requisição passa a valer como de profissional (guards e escopos existentes ficam intactos)
- Ao ativar a flag é criado/garantido um perfil profissional mínimo (`specialties: []`, `individual`, `access_granted = true`)
- O gate de assinatura trata a conta real master como isenta mesmo em modo profissional
- O master que atua como profissional aparece no diretório de profissionais dos responsáveis

## Dependências

- Task 800 — done
- Task 801 — done

## Contexto mínimo

- esta task e o Slice 072
- `backend/src/modules/users/`
- `backend/src/modules/auth/strategies/jwt.strategy.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `front-end/src/stores/authStore.ts`, `front-end/src/services/http/apiClient.ts`
- `front-end/src/layout/Sidebar/`, `front-end/src/layout/MainLayout/`
- `front-end/src/pages/Main/AdminUsers/EditUserModal.tsx`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Checagens por papel | `backend/src/common/guards/roles.guard.ts` | confirmar que o papel efetivo basta |
| Diretório | `backend/src/modules/professionals/professionals.service.ts` | incluir master profissional |
| Rotas web por papel | `front-end/src/constants/navigation.ts`, `front-end/src/routes/index.tsx` | menu e guarda seguem o papel efetivo |

## Orçamento de contexto

- médio
- estratégia: papel efetivo por requisição, sem multi-papel no domínio; sem mobile

## Critérios de aceite

- [x] Edição administrativa não altera mais o papel (`role` removido do `UpdateUserRequest`)
- [x] Excluir, visualizar, inativar e editar continuam disponíveis
- [x] Editar um master mostra "Também atua como profissional"; editar profissional/responsável mostra a isenção
- [x] Master marcado alterna para o modo profissional e acessa as rotas de profissional
- [x] Master em modo profissional não é cobrado
- [x] Header de atuação é ignorado para master sem a flag e para outros papéis

## Fora de escopo

- Mobile
- Completar perfil clínico (especialidades, registro) do master profissional

## Resultado da execucao

- Backend: coluna `users.acts_as_professional` (migration 1960000000000), DTO sem `role` e com `actsAsProfessional`, validações `FEE_EXEMPT_NOT_APPLICABLE` e `ACTS_AS_PROFESSIONAL_MASTER_ONLY`, `buildRequestUser` com papel efetivo via `X-Acting-Role`, perfil profissional mínimo ao ativar, gate de assinatura isento para conta master, diretório incluindo master profissional
- Front: modal de edição sem seletor de perfil; checkbox de atuação profissional para master; selo "Também profissional" na tabela; store com `actingAsProfessional` e papel efetivo persistido; header enviado pelo `apiClient`; alternância de modo no menu do usuário da sidebar

## Contexto utilizado

- Task 802, Slice 072, guards/strategy de auth, subscriptions, authStore, Sidebar, MainLayout, AdminUsers

## Handoff

- `.agents/state/handoffs/TASK-802.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/database/migrations/1960000000000-AddActsAsProfessionalToUsers.ts`
- `backend/src/modules/users/entities/user.entity.ts`
- `backend/src/modules/users/dto/update-user.dto.ts`
- `backend/src/modules/users/users.repository.ts`
- `backend/src/modules/users/users.typeorm.repository.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `backend/src/modules/auth/strategies/jwt.strategy.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/stores/authStore.test.ts`
- `front-end/src/services/http/apiClient.ts`
- `front-end/src/services/adapters/adaptAuthResponse.ts`
- `front-end/src/hooks/useAuth.ts`
- `front-end/src/types/auth.ts`
- `front-end/src/types/admin.ts`
- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/styles.module.css`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/AdminUsers/EditUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/editUserModal.module.css`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validacoes executadas

- Backend: `users.service.spec` 20/20 e `subscriptions.service.spec` 26/26; `npm run build` ok; migration aplicada localmente
- Front: `tsc` e `eslint` sem erros nos arquivos alterados; Vitest com `--pool=threads`: `authStore.test` 7/7, novos testes de edição/exclusão em AdminUsers passando
- 4 falhas antigas (Sidebar `/baixar-app`, AdminUsers "consultar perfil" e 2 de "criar usuário master") reproduzem igual no código sem esta task

## Pendencias pos-task

- Validar no browser: marcar um master, alternar modo pela sidebar, cadastrar/vincular paciente
- Corrigir as 4 falhas antigas de teste em task própria

## Status final

done
