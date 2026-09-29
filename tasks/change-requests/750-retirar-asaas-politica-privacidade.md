# Task 750 - Retirar Asaas da política de privacidade

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

Retirar o compartilhamento com o Asaas e a menção ao Asaas na transferência internacional.

## Dependências

- Task 749 — done

## Contexto mínimo

- esta task
- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

## Contexto sob demanda

Não se aplica.

## Orçamento de contexto

- baixo

## Critérios de aceite

- [x] O item “Asaas, para processar a assinatura por cartão ou PIX” saiu de “Com quem compartilhamos”.
- [x] A seção “Transferência internacional” não cita mais o Asaas.

## Fora de escopo

- a finalidade de cobrança da assinatura na seção 5
- a menção a registros de pagamento na seção 8

## Resultado da execucao

As duas frases do Asaas saíram. A seção 7 ficou só com OneSignal e armazenamento de mídia.

## Contexto utilizado

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`

## Handoff

- `.agents/state/handoffs/TASK-750.md`

## Arquivos alterados

- `front-end/src/pages/Public/PrivacyPolicy/content.ts`
- `tasks/slices/062-contato-politica-privacidade-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- página `/politica-de-privacidade` sem as frases do Asaas

## Pendencias pos-task

- nenhuma

## Status final

done
