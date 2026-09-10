# Gravuras do jogo “Quem é o intruso?”

Este documento lista todas as gravuras usadas nas rodadas padrão do jogo.

Os arquivos ficam no storage sob o prefixo:

`games/quem_e_o_intruso/items/`

## Rodadas

### 1. Frutas e legumes

- Maçã — `maca.webp`
- Banana — `banana.webp`
- Uva — `uva.webp`
- Cenoura — `cenoura.webp` **(intruso)**

Critério: cenoura é legume; os demais são frutas.

### 2. Animais

- Cachorro — `cachorro.webp`
- Gato — `gato.webp`
- Tartaruga — `tartaruga.webp`
- Árvore — `arvore.webp` **(intruso)**

Critério: árvore não é animal; os demais são animais.

### 3. Meios de transporte

- Carro — `carro.webp`
- Ônibus — `onibus.webp`
- Bicicleta — `bicicleta.webp`
- Árvore — `arvore.webp` **(intruso)**

Critério: árvore não é meio de transporte; os demais são meios de transporte.

### 4. Roupas

- Camiseta — `camiseta.webp`
- Shorts — `shorts.webp`
- Meias — `meias.webp`
- Banana — `banana.webp` **(intruso)**

Critério: banana é fruta; os demais são peças de vestir.

### 5. Material escolar

- Lápis — `lapis.webp`
- Borracha — `borracha.webp`
- Caderno — `caderno.webp`
- Bola — `bola.webp` **(intruso)**

Critério: bola é brinquedo; os demais são materiais escolares.

### 6. Natureza

- Árvore — `arvore.webp`
- Flor — `flor.webp`
- Folha — `folha.webp`
- Sapato — `sapato.webp` **(intruso)**

Critério: sapato não faz parte da natureza; os demais crescem na terra.

### 7. Doces

- Sorvete — `sorvete.webp`
- Bolo — `bolo.webp`
- Biscoito — `biscoito.webp`
- Brócolis — `brocolis.webp` **(intruso)**

Critério: brócolis é vegetal; os demais são guloseimas.

### 8. Fundo do mar

- Peixe — `peixe.webp`
- Polvo — `polvo.webp`
- Caranguejo — `caranguejo.webp`
- Gato — `gato.webp` **(intruso)**

Critério: gato vive em terra; os demais vivem na água.

### 9. Móveis

- Cadeira — `cadeira.webp`
- Mesa — `mesa.webp`
- Cama — `cama.webp`
- Banana — `banana.webp` **(intruso)**

Critério: banana é fruta; os demais são móveis.

## Observações

- Árvore, banana e gato aparecem em mais de uma rodada com funções diferentes.
- As rodadas devem sempre conter três itens da categoria principal e um item claramente externo a ela.
- Alterações nas gravuras devem ser refletidas no seed em `backend/src/modules/contents/odd-one-out-game-assets.ts`.
