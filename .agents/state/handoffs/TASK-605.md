# Handoff Task 605

## Status

done

## Slice

- Slice 054 — cancelamento da conta do responsável e restrição de acesso profissional.

## Decisões preservadas

- Vínculos profissionais ativos das crianças do responsável passam a `canceled` quando a assinatura é cancelada/reembolsada ou o webhook confirma cancelamento.
- Um vínculo `canceled` não permite acesso clínico nem trilhas; só pode ser inativado/removido, nunca reativado.
- Dados da família e histórico permanecem persistidos.

## Contexto utilizado

- Contrato, subscriptions, patients, guardians, trails, segurança e testes focados.

## Arquivos alterados

- Contrato OpenAPI e módulos/testes de subscriptions e patients.

## Validações

- Lint focado e 33 testes de patients/subscriptions passaram.
- Typecheck global continua com erros preexistentes fora do escopo.

## Próximo contexto recomendado

- Task 606: tipos, serviços, lista e perfil web de pacientes; handoff TASK-604 e checklist de acessibilidade.
