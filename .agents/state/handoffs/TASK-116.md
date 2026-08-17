# Handoff - Task 116

## Task

- 116 - Remover encolhimento lateral da nuvem no login mobile
- status final: done

## Decisões

- A nuvem deixou de usar `scale` durante a animacao do teclado
- O deslocamento vertical foi preservado para manter a abertura de espaço ao teclado
- O ajuste ficou restrito ao login mobile

## Validacoes

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok
