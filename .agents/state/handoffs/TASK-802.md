# Handoff TASK-802

## Status

done

## Decisões

- Troca de papel removida do PATCH `/users/{id}` (contrato e DTO)
- Master + `actsAsProfessional` = papel efetivo `profissional` quando a requisição traz `X-Acting-Role: profissional`; sem multi-papel no domínio
- Perfil profissional mínimo criado ao ativar; gate de assinatura isenta a conta master real
- Front: `authStore.role` é o papel efetivo; `actingAsProfessional` persistido; alternância no menu do usuário da sidebar navega para o dashboard

## Validações

- Backend specs users (20) e subscriptions (26) ok; build ok; migration 1960000000000 aplicada
- Front: tsc/eslint limpos nos arquivos alterados; Vitest (`--pool=threads`) ok nos testes novos; 4 falhas pré-existentes não relacionadas

## Pendências

- Teste manual no browser do modo profissional do master
- Task própria para as 4 falhas antigas de Vitest

## Próximo contexto recomendado

- `tasks/change-requests/802-master-atua-como-profissional-sem-mensalidade.md`
- `front-end/src/stores/authStore.ts`, `backend/src/modules/users/users.service.ts`
