# Handoff - Task 244

## Task

- identificador: 244
- título: Bolhas decorativas no fundo do app mobile
- tipo: mobile
- status final: done

## Decisões preservadas

- Bolhas globais no `AppGate` (persistentes, como a lava do sidebar)
- Gradiente pink → orange + highlight, opacidade ~0.4
- Animação de subida suave com `Animated`
- Shell/navigator/`Screen` padrão transparentes para revelar o fundo
- Telas com `backgroundColor` sólido (ex. `colors.surface`) cobrem as bolhas

## Arquivos alterados

- `AppBackgroundBubbles`, `AppGate`, `Screen`, `RootNavigator`, shell `styles.ts`

## Validações

- typecheck mobile ok

## Próximo contexto

- Ajuste fino visual se necessário no device
