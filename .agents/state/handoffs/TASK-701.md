# Handoff Task 701

- Slice: `tasks/slices/060-cartao-debito-assinatura.md`
- Status final: done
- Decisão: o checkout envia `credit_card`, então o rótulo foi corrigido para “Cartão de crédito”. O PIX local permanece removido conforme Task 696.
- Arquivos alterados: `front-end/src/pages/Auth/SubscriptionGate/index.tsx`, `ajustes.md`, `tasks/000-index.md`, Task 701.
- Validações: Vitest e ESLint iniciados, mas travaram sem saída e foram interrompidos.
- Pendência: repetir as validações automatizadas.
- Próximo contexto: apenas o gate web e seus testes.
