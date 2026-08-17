# Task 469 - Modal de confirmação para cancelar assinatura

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica; endpoints de cancel/refund preservados

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Substituir a confirmação inline no rodapé do card de assinatura por um modal de confirmação no perfil do profissional.

## Criterios de conclusao

- [x] Cancelar assinatura abre modal
- [x] Solicitar reembolso também usa o mesmo modal
- [x] caixa de confirmação inferior removida
- [x] layout alinhado aos demais modais sensíveis

## Resultado da execucao

- `SubscriptionManagementCard` com Modal split para cancel/refund
- `confirmBox` removido do CSS do card

## Arquivos alterados

- `front-end/src/pages/Main/Settings/SubscriptionManagementCard.tsx`
- `front-end/src/pages/Main/Settings/subscriptionManagement.module.css`
- `tasks/000-index.md`

## Status final

done
