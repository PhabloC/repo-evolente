# Handoff TASK-603

## Status

done

## Objetivo

Bloquear o login mobile de responsável sem assinatura ativa antes de abrir a área autenticada.

## Decisões

- Consulta `/subscriptions/me` com o token recém obtido antes de persistir a sessão.
- Sem acesso, a mensagem é exibida no login e nenhuma sessão é gravada.
- Master e dados demo não sofrem a verificação.

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`

## Validações

- eslint focado passou.

## Pendências

- Nenhuma.
