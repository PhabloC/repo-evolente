# Task 585 - Especialidade profissional no perfil e nos vínculos

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Perfil de usuário profissional e resposta de vínculos profissionais da criança.

## Modo de execucao

cross-stack

## Slice vertical

- Slice 053 — `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Contexto mínimo

- Índice, task, Slice 053 e handoff 584.

## Contexto sob demanda

- Entidade/DTOs/serviços de usuário, formulários de perfil profissional e cards de vínculo web/mobile.

## Orçamento de contexto

- médio; limitar ao perfil de usuário e aos consumidores dos vínculos.

## Estratégia de redução

- Uma especialidade principal com opção “Outra”; não criar catálogo administrativo separado nesta etapa.

## Resultado da execucao

- Reaproveitada a lista de especialidades que já existe no cadastro profissional.
- Os vínculos da criança passaram a retornar e exibir as especialidades do profissional na web e no app.

## Contexto utilizado

- Perfil profissional existente e consumidores dos vínculos da criança.

## Handoff

- `.agents/state/handoffs/TASK-585.md`

## Arquivos alterados

- Serviço/módulo de pacientes, contrato e cards web/mobile.

## Validacoes executadas

- `npm run build` (backend) — ok.

## Pendencias pos-task

- Nenhuma.

## Status final

done
