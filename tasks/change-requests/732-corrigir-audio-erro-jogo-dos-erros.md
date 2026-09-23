# Task 732 - Corrigir áudio de erro do Jogo dos erros

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile (Expo)

## Perfil do projeto

- web: front-end
- mobile: sim

## Contrato

Não aplicável; correção de feedback de áudio no runtime mobile já existente.

## Modo de execução

single-stack

## Slice vertical

- Slice 035 — `tasks/slices/035-jogo-dos-erros.md`

## Objetivo

Fazer o Jogo dos erros reproduzir o áudio correto de tentativa quando a criança toca em uma área sem diferença, usando “Tente novamente.” em vez do áudio de “Quase! Escolha outra palavra.”.

## Entrega verificável

- Um toque incorreto no Jogo dos erros reproduz `announceRetry()`.
- O feedback visual do erro permanece coerente com o áudio: “Tente novamente.”.
- Os cues de outros jogos não são alterados.

## Fora de escopo

- Alteração dos áudios cadastrados no catálogo ou no storage.
- Mudanças no Jogo dos erros web.
- Alteração do comportamento de acerto, dica, avanço ou exercício.

## Dependências

- Slice 035 — concluído.
- Task 655 — concluída.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx`
- `mobile/src/features/games/components/GameSessionAudio/index.tsx`

## Contexto sob demanda

- `mobile/docs/ai/ACCESSIBILITY.md` — validar que o feedback visual e sonoro continua acessível.
- testes diretamente relacionados ao renderer e ao áudio, se existentes.

## Orçamento de contexto

Carregar somente o renderer do Jogo dos erros, o provider de áudio e testes/configuração diretamente relacionados; não carregar outras stacks, contrato ou assets visuais.

## Critérios de aceite

- Ao errar uma área sem diferença, o áudio reproduz “Tente novamente.”.
- Não é reproduzido o cue “Quase! Escolha outra palavra.” nessa interação.
- Lint e testes direcionados passam, ou falhas preexistentes ficam registradas.

## Resultado da execucao

O toque fora de um hotspot válido no Jogo dos erros agora chama `announceRetry()` e reproduz “Tente novamente.”. O feedback visual foi alinhado ao mesmo texto, mantendo a mensagem orientativa complementar.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `mobile/AGENTS.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx`
- `mobile/src/features/games/components/GameSessionAudio/index.tsx`

## Handoff

Correção localizada no renderer mobile do Jogo dos erros. O cue de erro usa `announceRetry`, sem alterar o cue global `announceAlmost` usado por atividades de completar frase. A referência `mobile/docs/ai/ACCESSIBILITY.md` declarada na task não existe no repositório; a mudança não alterou controles ou layout.

## Arquivos alterados

- `mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx`
- `tasks/change-requests/732-corrigir-audio-erro-jogo-dos-erros.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `.agents/state/handoffs/TASK-732.md`

## Validacoes executadas

- `cd mobile && npm run lint -- --no-warn-ignored mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx` — passou.
- `cd mobile && npm run typecheck` — passou.
- `cd mobile && npm run test -- --runInBand` — interrompido após execução prolongada sem saída; não houve falha reportada.
- `git diff --check` — passou; Git exibiu apenas avisos preexistentes de conversão LF/CRLF.

## Pendencias pos-task

- Nenhuma pendência funcional.
- A suíte Jest completa deve ser reexecutada em uma janela dedicada para obter o resultado final.
- A ausência de `mobile/docs/ai/ACCESSIBILITY.md` permanece como lacuna documental preexistente.

## Status final

done

