# Handoff — Task 484

## Identificador

- task: 484
- slice: 009
- status final: done

## Decisões

- dashboard master mobile não trata falha de assinaturas como zero real
- `Ativas` e `Pendentes` usam métricas confiáveis do dashboard quando necessário
- `Em atraso` e `Encerradas / outras` ficam como indisponíveis se `/admin/subscriptions` falhar
- enriquecimento dos logs limita a 4 lookups paralelos de usuário

## Próxima ação

Validar o dashboard master mobile contra uma API com falha simulada em `/admin/subscriptions`.
