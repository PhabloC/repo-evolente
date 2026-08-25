# Slice 039 - Gateway Asaas e ciclo de assinatura

## Status

done

## Objetivo de negocio

Substituir o provider fake pelo Asaas com planos mensais reais, meios de pagamento definidos e regras de atraso, cancelamento e reembolso.

## Entrega verificavel

- Checkout Asaas (cartão, PIX, boleto) libera acesso após confirmação.
- Atraso > 3 dias inativa a conta.
- Cancelamento e reembolso (até 3 dias de uso) bloqueiam na hora.
- Master permanece isento.

## Fora de escopo

- Notificações push de cobrança
- Planos anuais
- Portal Asaas avançado para o master (além do status já listado em admin)
- Migração de assinaturas fake históricas para Asaas (tratar caso a caso na execução)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend
- mobile (somente mensagem/gate quando acesso bloqueado; checkout permanece na web)

## Contrato

- `contracts/openapi.yaml#/paths` de subscription (checkout, webhook Asaas, cancel, refund)
- remover ou restringir webhook fake a `PAYMENT_PROVIDER=fake`

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (assinatura)
- lacunas: meios PIX/cartão/boleto, cancelamento e reembolso sem print dedicado — copiar tokens e layout do gate atual

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- escopo: apenas estados de assinatura sem acesso (sem checkout no app nesta fase)

## Permissoes e atores

- Profissional e responsável: pagam e gerenciam própria assinatura
- Master: isento; pode listar status via admin existente

## Casos de erro e borda

- Pagamento pendente (PIX/boleto)
- Pagamento recusado
- Webhook duplicado ou fora de ordem
- Atraso no limite de 3 dias
- Reembolso após janela de 3 dias (deve recusar)
- Tentativa de checkout por master

## Decisoes humanas confirmadas

- Gateway: Asaas
- Valores: profissional R$ 79/mês; responsável R$ 49/mês
- Periodicidade: mensal
- Meios: cartão, PIX, boleto
- Master isento
- Ciclo: `PENDING` → `ACTIVE` → `OVERDUE` → `SUSPENDED` → `CANCELED`
- Atraso: `OVERDUE` (3 dias) → `SUSPENDED` (inativa conta)
- Cancelamento/reembolso: → `CANCELED` com bloqueio imediato
- Reembolso: até 3 dias de uso
- Sem inadimplência aberta além de `OVERDUE`

## Premissas adotadas

- Checkout e gestão financeira na web; mobile só consome `accessGranted`
- Valores em centavos: `7900` e `4900`; moeda BRL
- Conta Asaas sandbox primeiro; produção via env

## Tasks relacionadas

- `tasks/change-requests/419-contrato-openapi-asaas-assinatura.md`
- `tasks/change-requests/420-provider-asaas-checkout-mensal.md`
- `tasks/change-requests/421-webhook-ciclo-atraso-cancel-refund-asaas.md`
- `tasks/change-requests/422-tela-checkout-asaas-web.md`
- `tasks/change-requests/423-cancelamento-reembolso-web-e-gate-mobile.md`
- `tasks/change-requests/599-cancelar-reembolsar-assinatura-perfil-mobile.md`
- `tasks/change-requests/600-simplificar-cta-confirmacao-cancelamento-mobile.md`
- `tasks/change-requests/603-gate-assinatura-antes-login-mobile.md`
- `tasks/change-requests/424-pagina-planos-master-valores-asaas.md`
- `tasks/change-requests/425-gate-assinatura-confirmacao-e-valores.md`

## Dependencias do slice

- Slice 005 (gate fake) — done
- Tasks 012 e 013 — done

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- `requirements/001-escopo-produto.md` (seção 8)
- `requirements/002-regras-de-negocio.md` (seção 5)

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Contrato | `contracts/openapi.yaml` paths subscription | alterar API | sim se API |
| Provider atual | `backend/src/modules/subscriptions/` | implementar Asaas | sim se back |
| UI gate | `front-end/src/pages/Auth/SubscriptionGate/` | checkout web | sim se front |
| Admin assinaturas | paths `/admin/subscriptions` | só se status admin | nao |
| Docs Asaas | documentação oficial Asaas (API + webhooks) | integração | sim se back |
| Mobile perfil | `mobile/src/features/profile/` | gate sem acesso | sim se mobile |

## Risco de contexto

- medio
- estrategia: uma task por camada (contrato → provider → webhook/ciclo → UI web → UI cancel/mobile); não carregar jogos nem admin completo

## Observacoes de rastreabilidade

- Substitui a abstração fake do Slice 005 sem reabrir o slice inteiro.
- Decisões registradas em `requirements/001` e `002`.

## Progresso das tasks relacionadas

- `tasks/change-requests/419-contrato-openapi-asaas-assinatura.md` — done
- `tasks/change-requests/420-provider-asaas-checkout-mensal.md` — done
- `tasks/change-requests/421-webhook-ciclo-atraso-cancel-refund-asaas.md` — done
- `tasks/change-requests/422-tela-checkout-asaas-web.md` — done
- `tasks/change-requests/423-cancelamento-reembolso-web-e-gate-mobile.md` — done
- `tasks/change-requests/599-cancelar-reembolsar-assinatura-perfil-mobile.md` — done
- `tasks/change-requests/600-simplificar-cta-confirmacao-cancelamento-mobile.md` — done
- `tasks/change-requests/603-gate-assinatura-antes-login-mobile.md` — done
- `tasks/change-requests/424-pagina-planos-master-valores-asaas.md` — done
- `tasks/change-requests/425-gate-assinatura-confirmacao-e-valores.md` — done
- `tasks/change-requests/487-hardening-supersede-checkout-asaas.md` — done
- `tasks/change-requests/597-layout-gate-assinatura-login-e-pagamento.md` — done
- `tasks/change-requests/598-layout-aguardando-pagamento-e-botao-ja-paguei.md` — done

## Status final

done
