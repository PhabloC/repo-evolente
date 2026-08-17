# Handoff - Task 109

## Task

- 109 - Background animado nas telas de login e recuperacao mobile
- status final: done

## Decisões

- Fundo animado extraido para `AuthAnimatedBackground` reutilizado por login e recovery
- Movimento lento e orgânico com `Animated` nativo, sem piscadas e sem Reanimated
- `formSection` ficou levemente translucida para deixar o background aparecer sem perder legibilidade
- Layout, navegacao e formularios existentes foram preservados

## Validacoes

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok
