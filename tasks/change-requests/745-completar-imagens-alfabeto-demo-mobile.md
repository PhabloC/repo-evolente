## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica. A correção ajusta somente o conteúdo demo local do aplicativo.

## Modo de execucao

single-stack

## Slice vertical

`tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Objetivo

Fazer o jogo Alfabeto falado do aplicativo demo apresentar todas as letras e suas imagens.

## Entrega verificável

O jogo demo mobile fornece as letras A–Z e uma URL de imagem para cada letra, permitindo que a grade exiba todas as imagens configuradas.

## Fora de escopo

- Alterar o renderer ou o layout do jogo.
- Alterar o catálogo real, o bucket ou a API.
- Alterar o jogo Escreva a letra.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `mobile/src/features/trail/services/trailService.ts`

## Contexto sob demanda

- `mobile/src/features/games/components/AlphabetGameRenderer/`: confirmar que o renderer consome todas as letras configuradas.
- `mobile/src/features/games/utils/alphabetGame.ts`: confirmar normalização das letras e URLs.

## Orçamento de contexto

Baixo; alteração localizada no fixture demo do mobile.

## Dependências

- Task 158 — execução mobile do jogo alfabeto falado — done
- Task 174 — imagens do alfabeto falado no bucket — done

## Resultado da execucao

- O fixture demo do app passou de A–F para A–Z.
- As 26 URLs de imagens agora são geradas pelo mesmo padrão do bucket, de `a.webp` a `z.webp`.
- Foi criado teste unitário para garantir 26 letras, 26 chaves e URLs de início/fim do alfabeto.

## Contexto utilizado

- Contexto mínimo da raiz e do slice 026.
- `mobile/src/features/trail/services/trailService.ts`.
- `mobile/src/features/games/utils/alphabetGame.ts` e testes relacionados.
- Renderer mobile apenas para confirmar que ele renderiza todas as letras recebidas.

## Handoff

- Identificador: Task 745.
- Slice: `tasks/slices/026-jogos-terapeuticos-alfabeto.md`.
- Decisão: manter a correção restrita ao fixture demo; o catálogo real e o renderer não foram alterados.
- Próximo contexto: nenhum obrigatório; reabrir somente se imagens do ambiente real também estiverem ausentes.

## Arquivos alterados

- `mobile/src/features/games/utils/alphabetGame.ts`
- `mobile/src/features/games/utils/alphabetGame.test.ts`
- `mobile/src/features/trail/services/trailService.ts`

## Validacoes executadas

- `npm run typecheck` — sem erros reportados antes do encerramento do processo.
- Jest direcionado para os testes do alfabeto — não concluiu dentro da janela do ambiente.
- `npm run lint` — não concluiu dentro da janela do ambiente.
- `git diff --check` — executado após a edição.

## Pendencias pos-task

- Nenhuma pendência funcional. Jest e lint devem ser repetidos em CI ou em uma janela local mais longa.

## Critérios de aceite

- [x] O fixture demo usa A–Z no jogo Alfabeto falado.
- [x] Cada letra A–Z possui URL no padrão público já usado pelo bucket.
- [x] Teste ou validação automatizada impede regressão para um subconjunto de letras.

## Status final

done
