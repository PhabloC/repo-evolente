# Task 640 - Reaproveitar responsavel orfao sem assinatura

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `POST /guardians/register`

## Modo de execucao

single-stack

## Slice vertical

- Slice 049 - Cadastro publico so do responsavel (`tasks/slices/049-cadastro-responsavel-sem-filho.md`)
- Slice 039 - Gateway Asaas e ciclo de assinatura (`tasks/slices/039-gateway-asaas-assinatura.md`)

## Objetivo

Permitir que um responsavel que ficou cadastrado sem assinatura por falha no fluxo de pagamento consiga refazer o cadastro com o mesmo email e CPF e seguir novamente para pagamento, sem conflito de duplicidade.

## Comportamento esperado

- Se `POST /guardians/register` receber email e CPF de um responsavel existente, sem acesso liberado e sem filhos, o backend reaproveita a conta.
- Ao reaproveitar, o backend atualiza nome, telefone e senha informados no novo cadastro.
- Cadastro ativo, com acesso liberado, com filhos ou com CPF divergente continua retornando conflito.

## Contexto minimo

- esta task
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/users/users.service.ts`

## Contexto sob demanda

- `backend/src/modules/guardians/guardians.service.spec.ts` para teste focado
- `contracts/openapi.yaml#/paths/~1guardians~1register` para confirmar contrato

## Orcamento de contexto

- baixo - regra localizada no cadastro de responsavel.

## Criterios de aceite

- [x] Responsavel orfao sem acesso e sem filhos pode refazer cadastro com mesmo email/CPF.
- [x] Senha, nome e telefone sao atualizados no reaproveitamento.
- [x] CPF igual com email diferente ou conta com filhos/acesso continua bloqueado.
- [x] Testes backend passam.

## Resultado da execucao

- `GuardiansService.register` agora detecta responsavel existente com mesmo email e CPF, sem acesso liberado e sem filhos, e reaproveita a conta para o fluxo de pagamento.
- No reaproveitamento, nome, telefone e senha sao atualizados com os dados do novo cadastro.
- Contas com filhos, acesso liberado, CPF divergente ou outro papel continuam seguindo a validacao de conflito.
- `UsersService.update` foi corrigido para nao enviar campos opcionais `undefined` ao repository.
- O e2e de busca de usuarios passou a usar email unico da execucao, evitando colisao com dados historicos.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `contracts/openapi.yaml#/paths/~1guardians~1register`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/test/app.e2e-spec.ts`

## Handoff

- `.agents/state/handoffs/TASK-640.md`

## Arquivos alterados

- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/test/app.e2e-spec.ts`
- `tasks/change-requests/640-reaproveitar-responsavel-orfao-sem-assinatura.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `.agents/state/handoffs/TASK-640.md`

## Validacoes executadas

- `npm test -- --runInBand src/modules/guardians/guardians.service.spec.ts` - 17 testes passaram.
- `npm test -- --runInBand src/modules/users/users.service.spec.ts src/modules/subscriptions/subscriptions.service.spec.ts` - 35 testes passaram.
- `npm run test:e2e -- --runInBand test/app.e2e-spec.ts` - 3 testes passaram.
- `npm run lint` - passou.

## Pendencias pos-task

- Nenhuma.

## Status final

done
