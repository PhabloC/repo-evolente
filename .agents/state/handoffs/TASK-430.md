# Handoff — Task 430

## Identificador

- task: 430
- slice: 041
- status final: done

## Decisões

- `gameType: odd-one-out`, categoria `raciocinio`
- 4 rounds × 4 items + `intruderId`; `criterion` opcional no config
- Shuffle Fisher-Yates das figuras **no cliente** ao iniciar (web: `startGame`; mobile: mount / jogar de novo)
- Capas e itens em `games/quem_e_o_intruso/`

## Validacoes

- Upload S3: 18 assets
- Bootstrap specs pass (catálogo length 11)

## Próxima ação

Abrir “Quem é o intruso?” na biblioteca e confirmar prévia + ordem aleatória ao começar.
