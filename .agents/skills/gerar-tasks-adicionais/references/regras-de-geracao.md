# Regras de geracao de change requests (raiz)

## Estrategia

1. entender solicitacao
2. mapear impacto por stack
3. mapear impacto shared/contrato
4. identificar se a demanda reusa slice existente ou cria novo slice
5. criar/atualizar arquivo do slice correspondente em `tasks/slices/`
6. decompor em 1..N tasks
7. registrar dependencias

## Qualidade

Tasks adicionais devem ser:
- executaveis
- rastreaveis
- coerentes com backlog unico

Cada task adicional deve apontar para um arquivo de slice concreto e cada slice novo deve nascer com arquivo proprio.
