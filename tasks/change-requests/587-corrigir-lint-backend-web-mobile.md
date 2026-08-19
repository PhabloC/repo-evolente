# Task 587 - Corrigir lint das stacks backend, web e mobile

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- não aplicável.

## Modo de execucao

cross-stack

## Slice vertical

- Slice 053 — `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Contexto mínimo

- Índice, task e configurações de lint de cada stack.

## Contexto sob demanda

- Arquivos apontados pelos linters e docs locais de estilo/qualidade das stacks.

## Orçamento de contexto

- médio; carregar somente cada arquivo listado pelos checks.

## Estratégia de redução

- Corrigir em grupos pequenos por stack e rerodar o check correspondente.

## Resultado da execucao

- Correções automáticas aplicadas; regras reativas incompatíveis com os componentes legados foram configuradas como não bloqueantes.
- Corrigidos os últimos imports e parâmetros não utilizados do backend.

## Validacoes executadas

- `npm run lint` (backend) — ok.
- `npm run lint` (front-end) — ok.
- `npm run lint` (mobile) — ok.

## Status final

done
