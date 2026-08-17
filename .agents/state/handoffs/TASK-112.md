# Handoff - Task 112

## Task

- 112 - Remover fundo animado do auth mobile
- status final: done

## Decisões

- O componente `AuthAnimatedBackground` foi mantido apenas como ponto de extensao, mas agora retorna `null`
- O auth mobile voltou a ficar sem qualquer efeito decorativo de fundo
- Nenhuma tela auth precisou ser reescrita

## Validacoes

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok
