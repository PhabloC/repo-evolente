## Status

done

## Tipo

back

## Stacks envolvidos

- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica. O formato do conteúdo permanece o mesmo; a correção ajusta o bootstrap do catálogo.

## Modo de execucao

cross-stack

## Slice vertical

`tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Objetivo

Garantir que o conteúdo real do jogo Alfabeto falado entregue A–Z para o aplicativo, usando as imagens já publicadas no S3.

## Entrega verificável

O bootstrap substitui uma lista incompleta persistida por A–Z e preserva/atualiza as 26 URLs de imagens do S3 no `gameConfig`.

## Fora de escopo

- Alterar o renderer mobile.
- Fazer novo upload das imagens.
- Alterar o contrato público do conteúdo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/alphabet-game-assets.ts`

## Contexto sob demanda

- testes do bootstrap: validar atualização de conteúdo já existente.
- entidade/configuração de conteúdo: confirmar que a alteração não muda o contrato.

## Orçamento de contexto

Baixo; correção localizada no bootstrap e nos testes do backend.

## Resultado da execucao

- O bootstrap do backend normaliza para A–Z só o jogo padrão "Alfabeto falado". Um jogo `ALPHABET` com outro título mantém `letters`.
- Capa e imagens já gravadas permanecem. O catálogo só preenche `coverUrl` e `letterImages` quando esses campos estão vazios.
- O bootstrap mantém as URLs das 26 imagens geradas a partir do prefixo S3 configurado.
- O app mobile também inclui as letras presentes em `letterImages`, permitindo renderizar as imagens disponíveis mesmo antes da persistência ser atualizada pelo bootstrap.
- Teste do bootstrap reproduz a configuração incompleta A–L + N e espera A–Z após a inicialização.

## Contexto utilizado

- Contexto mínimo da raiz e do slice 026.
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts` e testes.
- `backend/src/modules/contents/alphabet-game-assets.ts`.
- `mobile/src/features/games/utils/alphabetGame.ts` e testes.

## Handoff

- Identificador: Task 746.
- Slice: `tasks/slices/026-jogos-terapeuticos-alfabeto.md`.
- Decisão: corrigir a origem persistida no bootstrap e adicionar fallback defensivo no app para aproveitar todas as imagens recebidas.
- Próximo contexto: reiniciar/republicar o backend para executar o bootstrap; depois abrir o jogo no app e confirmar A–Z.

## Arquivos alterados

- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `mobile/src/features/games/utils/alphabetGame.ts`
- `mobile/src/features/games/utils/alphabetGame.test.ts`

## Validacoes executadas

- `git diff --check` na raiz, backend e mobile — ok.
- Jest direcionado do bootstrap backend — interrompido após não emitir saída dentro da janela disponível.
- Typecheck/lint completos — não repetidos nesta rodada por duração do ambiente.

## Pendencias pos-task

- O backend precisa ser reiniciado/republicado para o bootstrap atualizar o registro existente no banco.
- Repetir o Jest direcionado em CI ou janela local mais longa.

## Critérios de aceite

- [x] O jogo padrão "Alfabeto falado" com letras incompletas passa a usar A–Z.
- [x] Um jogo de alfabeto com outro título mantém a lista de letras gravada.
- [x] As 26 imagens continuam apontando para `games/alphabet/letters/{letra}.webp` no S3.
- [x] Teste do bootstrap cobre a correção de conteúdo existente.

## Status final

done
