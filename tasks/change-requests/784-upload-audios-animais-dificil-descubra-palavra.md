# Task 784 - Upload áudios Animais/difícil do Descubra a palavra

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Origem da solicitacao

Usuário colocou três novos MP3 em `audios-atividades/jogo_descubra_palavra/animais/dificil` (Pato amarelo, Peixe laranja, Gato laranja). Pediu upload no S3, vínculo na atividade e exclusão dos áudios anteriores dessas palavras.

## Objetivo

Publicar os três áudios novos no S3 (sobrescrevendo as chaves das palavras correspondentes) e garantir o vínculo na atividade Descubra a palavra (Animais / difícil).

## Escopo

- Atualizar labels no `_word-spell-catalog.json` para casar com os novos arquivos
- Upload S3 em `games/complete_a_palavra/audio/words/animais/dificil/{wordId}.mp3`
- Sobrescrever áudios antigos das palavras `gato_preto`, `pato_branco`, `peixe_azul`
- Reportar qual arquivo ficou em qual texto/palavra

## Fora de escopo

- Renomear IDs das palavras no catálogo
- Regravar demais áudios da categoria

## Slice vertical

- Slice 043 — `tasks/slices/043-complete-a-palavra.md`

## Contexto mínimo

- `AGENTS.md`
- `tasks/000-index.md`
- esta task
- `.agents/state/handoffs/TASK-544.md`
- `.agents/state/handoffs/TASK-731.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| upload | `backend/scripts/upload-word-spell-word-audios.mjs` | publicar MP3s | sim |
| catálogo | `backend/scripts/_word-spell-catalog.json` | match arquivo → palavra | sim |
| labels | `backend/src/modules/contents/word-spell-game-assets.ts` | confirmar textos atuais | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: só os 3 áudios de Animais/difícil; não reabrir runtime web/mobile

## Criterios de conclusao

- [x] Os 3 MP3 novos estão no S3 nas chaves das palavras correspondentes
- [x] Áudios antigos dessas palavras foram substituídos
- [x] Relatório arquivo → texto/palavra entregue ao usuário

## Dependencias

- Task 544
- Task 731

## Contexto utilizado

- `backend/scripts/upload-word-spell-word-audios.mjs`
- `backend/scripts/_word-spell-catalog.json`
- `audios-atividades/jogo_descubra_palavra/animais/dificil/`

## Resultado da execucao

- Labels do catálogo de upload atualizados: GATO LARANJA, PATO AMARELO, PEIXE LARANJA.
- Upload S3 sobrescreveu as chaves existentes (IDs preservados da Task 731):
  - `Gato-laranja.mp3` → `gato_preto.mp3` (texto **GATO LARANJA**)
  - `Pato-amarelo.mp3` → `pato_branco.mp3` (texto **PATO AMARELO**)
  - `Peixe-laranja.mp3` → `peixe_azul.mp3` (texto **PEIXE LARANJA**)
- Áudios locais antigos dessas três palavras já não estavam na pasta; no S3 o conteúdo foi substituído na mesma chave/`audioUrl`.

## Handoff

- `.agents/state/handoffs/TASK-784.md`

## Arquivos alterados

- `backend/scripts/_word-spell-catalog.json`
- `tasks/change-requests/784-upload-audios-animais-dificil-descubra-palavra.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-784.md`

## Validacoes executadas

- `npm run upload:word-spell-word-audios` — uploaded=120 unmatched=0; os 3 novos casaram com as palavras corretas

## Pendencias pos-task

- nenhuma

## Status final

done
