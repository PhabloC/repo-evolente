# Task 713 - Cancelar áudio de instrução ao abandonar exercício na prévia web

## Status

done

## Tipo

front

## Stacks envolvidos

front-end (React/Vite)

## Perfil do projeto

web: front-end (React/Vite); mobile: sim

## Contrato

Não se aplica — correção local do ciclo de vida de áudio.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/034-jogo-memoria-articulacao.md` (hardening da prévia web existente; não cria novo slice).

## Objetivo

Impedir que o áudio de instrução de um exercício continue ou comece depois que a criança abandonou aquele exercício na prévia web do jogo da memória.

## Escopo

- Invalidar a sequência elogio → instrução ao continuar, trocar categoria ou fechar o modal.
- Interromper áudio gravado e TTS nessas transições.
- Manter o elogio e a instrução encadeados enquanto o exercício continuar ativo.

## Fora de escopo

- Alteração do catálogo, contrato ou arquivos de áudio.
- Runtime mobile.
- Mudança visual.

## Critérios de aceite

- Clicar em `Continuar` durante o elogio não inicia a instrução depois.
- Trocar categoria durante o elogio/instrução não deixa áudio tocar na tela de configuração.
- Fechar o modal interrompe a sequência de áudio pendente.
- O fluxo normal ainda reproduz `Muito bem!` antes da instrução.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/034-jogo-memoria-articulacao.md`
- `tasks/change-requests/712-audio-exercicio-memoria-articulacao.md`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`

## Contexto sob demanda

- `front-end/docs/ai/QA.md` e `front-end/docs/ai/ACCESSIBILITY.md`: validar estado dinâmico de áudio no modal.
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts` e `librarySharedFeedback.ts`: confirmar a API de interrupção existente.

## Orçamento de contexto

Até 8 fontes; limitar a implementação ao modal de memória e à rastreabilidade da correção.

## Dependências

- Task 712 — done.

## Resultado da execucao

O `MemoryPreviewModal` agora atribui uma geração à sequência elogio → instrução e ignora a continuação quando a geração foi invalidada. Continuar, trocar categoria, fechar o modal e desmontar o componente interrompem TTS/áudio gravado por meio de `stopBrowserGameSpeech()`.

## Contexto utilizado

- `tasks/000-index.md`, Slice 034 e Task 712.
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`.
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts` e `librarySharedFeedback.ts`.
- `front-end/docs/ai/QA.md` e `ACCESSIBILITY.md`.

## Handoff

O cancelamento é local ao `MemoryPreviewModal`; não foi necessário alterar o serviço de fala compartilhado. Próximo contexto recomendado: smoke manual da prévia acertando um par e abandonando o exercício durante o elogio e durante a instrução.

## Arquivos alterados

- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `tasks/change-requests/713-cancelar-audio-instrucao-memoria-web.md`
- `tasks/slices/034-jogo-memoria-articulacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-713.md`

## Validacoes executadas

- `npm run lint -- --no-warn-ignored src/pages/Main/Library/GamePreviewModal.tsx` — passou.
- `git diff --check` — passou.
- `npm run build` — falhou em erros TypeScript preexistentes em `Patients`, `Plans` e `PatientTrail`; nenhum erro apontou o arquivo alterado.
- `npm run test -- src/pages/Main/Library/index.test.tsx --run` — interrompido após permanecer sem progresso além do banner inicial do Vitest.

## Pendencias pos-task

- Smoke manual da prévia web com cancelamento durante elogio/instrução.
- Corrigir os erros TypeScript preexistentes para liberar o build global.

## Status final

done
