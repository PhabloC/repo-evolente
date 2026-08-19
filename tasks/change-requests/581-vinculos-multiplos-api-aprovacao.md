# Task 581 - API de vínculos múltiplos com aprovação do responsável

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `POST /patients/link`
- `GET /guardians/me/children/{childId}/professional-links`
- `PATCH /guardians/me/children/{childId}/professional-links/{linkId}/approval`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 053 — `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Contexto mínimo

- Índice, este arquivo, Slice 053 e handoff mais recente da área de responsável.

## Contexto sob demanda

- `contracts/openapi.yaml` (paths e schemas de pacientes/guardians).
- Repositórios, serviço, controlador e migrations de pacientes.
- Módulos e serviços de guardians/users, para autorização e dados públicos do profissional.
- `backend/docs/ai/` de arquitetura e segurança, porque a regra cria novo acesso a dados sensíveis.

## Orçamento de contexto

- médio; limitar a leitura aos módulos patients, guardians, users e ao trecho do contrato afetado.

## Estratégia de redução

- Não alterar fluxos de trilha e relatório além de garantir que eles continuem aceitando somente links ativos.

## Resultado da execucao

- O vínculo profissional-criança passou a aceitar múltiplos profissionais, com unicidade apenas por profissional e criança.
- Solicitações por código passam a nascer pendentes; o responsável proprietário pode listar, aprovar ou recusar a solicitação.
- Dados e trilhas continuam protegidos até que o vínculo esteja ativo.

## Contexto utilizado

- Contrato OpenAPI, módulos de pacientes/guardians/users e diretrizes de arquitetura e segurança do backend.

## Handoff

- `.agents/state/handoffs/TASK-581.md`

## Arquivos alterados

- Contrato, entidade, repositórios, serviço/controlador de pacientes, migration e compatibilidade do admin/trilhas.

## Validacoes executadas

- `npm run build` (backend) — ok.
- `git diff --check` — ok.

## Pendencias pos-task

- Tasks 582 e 583 devem consumir os endpoints de aprovação na web e no app.

## Status final

done
