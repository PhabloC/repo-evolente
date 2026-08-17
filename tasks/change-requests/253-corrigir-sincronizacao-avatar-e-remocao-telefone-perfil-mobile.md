# Task 253 - Corrigir sincronização do avatar e remoção de telefone no perfil mobile

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `PATCH /guardians/me`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Dependencias

- Task 243
- Task 247

## Objetivo

Corrigir regressões na edição de perfil do responsável para que a troca de avatar não sobrescreva silenciosamente campos já editados e para que a remoção do telefone seja persistida de forma explícita no contrato, backend e app mobile.

## Entrega verificavel

- Troca de avatar não reinicializa nome, parentesco ou telefone já alterados localmente na tela
- Formulário do responsável é inicializado apenas no primeiro carregamento útil ou preserva edição local durante refetch
- Remoção do telefone envia um valor explícito aceito pelo contrato para limpar o campo
- Backend aplica limpeza do telefone sem restaurar o valor anterior no refetch
- Testes cobrindo sincronização do cache/perfil e remoção de telefone

## Fora de escopo

- Redesign das telas de perfil
- Crop, remoção ou novos fluxos de avatar
- Alterações no perfil da criança além do que for estritamente compartilhado

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-243.md`
- `.agents/state/handoffs/TASK-247.md`

## Contexto sob demanda

- `contracts/openapi.yaml` no path `PATCH /guardians/me`
- `backend/src/modules/guardians/**`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/src/features/profile/**`

## Orcamento de contexto

medio

## Estrategia de reducao

Limitar a leitura ao contrato de edição do responsável, ao módulo `guardians` e à feature mobile de perfil, sem reabrir outras áreas do app do responsável.

## Referencia visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md` apenas se algum ajuste visual mínimo for necessário para preservar a tela existente

## Resultado da execucao

- O upload de avatar do responsável e da criança deixou de invalidar/refetchar o perfil inteiro e passou a atualizar apenas o cache relevante da query
- A tela `EditGuardianProfileScreen` inicializa o formulário apenas no primeiro carregamento útil, preservando edições locais durante atualizações de avatar
- A remoção do telefone agora envia `phone: null` no app mobile
- Contrato e backend passaram a aceitar `null` para limpar o telefone do responsável sem restaurar o valor anterior
- Foram adicionados testes para limpeza de telefone no backend e para atualização seletiva do cache no mobile

## Contexto utilizado

- `contracts/openapi.yaml` no path `PATCH /guardians/me`
- `backend/src/modules/guardians/**`
- `backend/src/modules/users/**`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/src/features/profile/**`

## Handoff

- `.agents/state/handoffs/TASK-253.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/dto/update-my-guardian-profile.dto.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `backend/src/modules/users/dto/update-user.dto.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/modules/users/users.repository.ts`
- `mobile/src/features/profile/hooks/useResponsavelProfile.ts`
- `mobile/src/features/profile/hooks/useResponsavelProfile.test.ts`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/services/profileService.ts`

## Validacoes executadas

- `cd backend && npm run test -- guardians.service.spec.ts` — ok
- `cd mobile && npm run test -- useResponsavelProfile` — ok
- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- Validar em dispositivo o fluxo completo de apagar telefone existente e salvar
- Validar visualmente no app que a troca de avatar não interfere em edição local já preenchida

## Status final

done
