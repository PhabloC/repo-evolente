# Handoff TASK-640

## Slice vertical

Slice 049 - Cadastro publico so do responsavel; Slice 039 - Gateway Asaas e ciclo de assinatura

## Status final

done

## Decisoes preservadas

- Recadastro so reaproveita conta de responsavel quando email e CPF batem, `accessGranted=false` e nao existem filhos.
- O reaproveitamento atualiza nome, telefone e senha para o usuario conseguir seguir ao pagamento com a senha recem-informada.
- Contas com filhos, acesso liberado, CPF divergente ou papel diferente continuam protegidas por conflito.

## Contexto efetivamente usado

- Task 640, slices 049/039, contrato de `/guardians/register`, services de guardians/users e specs focadas.

## Arquivos alterados

- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/test/app.e2e-spec.ts`
- `tasks/change-requests/640-reaproveitar-responsavel-orfao-sem-assinatura.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`

## Validacoes executadas

- `npm test -- --runInBand src/modules/guardians/guardians.service.spec.ts` - 17 testes passaram.
- `npm test -- --runInBand src/modules/users/users.service.spec.ts src/modules/subscriptions/subscriptions.service.spec.ts` - 35 testes passaram.
- `npm run test:e2e -- --runInBand test/app.e2e-spec.ts` - 3 testes passaram.
- `npm run lint` - passou.

## Pendencias ou bloqueios

- Nenhuma.

## Proximo contexto recomendado

- Se ainda houver travas de cadastro no front, carregar `front-end/src/pages/Auth/RegisterGuardian/` e o retorno de erro real da API.
