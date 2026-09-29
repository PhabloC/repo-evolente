# Task 749 - Remover o bloco de pagamento da política de privacidade

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

- Slice 062 — `tasks/slices/062-contato-politica-privacidade-web.md`

## Objetivo

Retirar da política de privacidade o bloco que descreve dados de pagamento.

## Dependências

- Task 748 — done

## Contexto mínimo

- esta task
- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

## Contexto sob demanda

Não se aplica. A alteração é só a remoção do bloco “Pagamento”.

## Orçamento de contexto

- baixo
- estratégia: editar um bloco do conteúdo público já conhecido.

## Critérios de aceite

- [x] A seção “Dados que coletamos” não tem mais o subtítulo “Pagamento” nem o parágrafo de Asaas, cartão e PIX.

## Fora de escopo

- menções pontuais a assinatura, cobrança ou Asaas em outras seções
- app mobile

## Resultado da execucao

O bloco “Pagamento” saiu da lista de dados coletados. As demais seções permanecem.

## Contexto utilizado

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

## Handoff

- `.agents/state/handoffs/TASK-749.md`

## Arquivos alterados

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`
- `tasks/slices/062-contato-politica-privacidade-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- página `/politica-de-privacidade`: o subtítulo “Pagamento” não aparece

## Pendencias pos-task

- nenhuma

## Status final

done
