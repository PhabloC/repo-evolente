# Handoff — Task 476

## Identificador

- task: 476
- título: Quebra-cabeça: artes novas para níveis 6–10
- slice: 038
- status final: done

## Decisões

- 5 artes novas em `jogo_quebra_cabeca/rounds/round_{6..10}/full.webp`
- Temas: parque (coelho), fazenda (vaca), mar (peixe), espaço (astronauta), floresta (raposa)
- Cada nível 6–10 usa `sceneId` próprio (sem reuso)
- Grades > 3×3 continuam clipando `full.webp` no runtime

## Validações

- Upload S3: 57 assets (inclui novas full.webp)

## Próxima ação

Reiniciar backend e abrir níveis 6–10 na prévia.

## Contexto que não carregar

- design-system completo; outros jogos
