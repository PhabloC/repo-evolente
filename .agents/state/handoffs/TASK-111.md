# Handoff - Task 111

## Task

- 111 - Aproximar fundo auth mobile da lava goo do sidebar
- status final: done

## Decisões

- O fundo auth mobile passou a usar `react-native-svg` com `FeGaussianBlur` + `FeColorMatrix` para simular o goo do sidebar
- Os blobs foram configurados como elipses animadas com gradientes radiais e ciclos ascendentes irregulares
- O refino ficou restrito a `AuthAnimatedBackground`, sem alterar as telas auth em si

## Validacoes

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok
