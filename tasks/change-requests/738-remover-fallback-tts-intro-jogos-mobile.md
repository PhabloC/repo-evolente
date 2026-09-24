## Status

done

# Task 738 - Remover fallback TTS da introdução dos jogos mobile

- **Tipo**: mobile
- **Stacks envolvidos**: mobile
- **Perfil do projeto**: mobile `sim` (Expo)
- **Contrato**: não aplicável; ajuste interno da sequência de áudio.
- **Modo de execução**: single-stack
- **Slice vertical**: `tasks/slices/048-narracao-intro-conclusao-jogos.md`
- **Dependências**: Tasks 526, 700 e 727 concluídas.
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e o Slice 048.
- **Contexto sob demanda**: `mobile/AGENTS.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/QA.md`, `mobile/src/features/games/renderers/GameActivityRenderer.tsx`, `mobile/src/features/games/components/GameSessionAudio/index.tsx`, Task 727 e seu handoff; necessários para manter a decisão de usar `introAudioUrl` gravado e validar a remoção segura do ramo TTS.
- **Orçamento de contexto**: até 8 fontes de implementação; sem design system, contrato ou demais stacks.

## Objetivo

Remover a API e o ramo inalcançável de TTS para introdução no provider compartilhado, preservando a introdução gravada via `introAudioUrl` e as instruções gravadas opcionais.

## Entrega verificável

- `GameActivityRenderer` não passa mais `introText={null}`.
- `GameSessionAudioProvider` não expõe nem avalia `introText`.
- A sequência continua esperando e tocando `introAudioUrl` e/ou `introInstructionAudioUrl` quando configuradas.

## Critérios de aceite

- [x] Não há referência restante a `introText` no runtime mobile.
- [x] O tipo do provider permanece consistente com seus consumidores.
- [x] Lint, typecheck e testes mobile são executados.

## Resultado da execucao

- Removida a prop `introText={null}` do renderizador de atividades.
- Removidos `introText` e o fallback TTS do `GameSessionAudioProvider`.
- A sequência de abertura permanece baseada em `introAudioUrl` e `introInstructionAudioUrl` gravados.

## Contexto utilizado

- Contexto mínimo da raiz, Slice 048, Task 727 e seu handoff.
- Regras e QA da stack mobile, o renderizador e o provider de áudio.

## Handoff

`.agents/state/handoffs/TASK-738.md`

## Arquivos alterados

- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `mobile/src/features/games/components/GameSessionAudio/index.tsx`
- `tasks/change-requests/738-remover-fallback-tts-intro-jogos-mobile.md`
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-738.md`

## Validacoes executadas

- `rg -n "introText" mobile/src` — sem referências residuais.
- `npm run lint` — aprovado com 1 warning preexistente em `src/shared/notifications/oneSignal.ts`.
- `npm run typecheck` — bloqueado por erros preexistentes, fora dos arquivos alterados.
- `npm run test -- --runInBand` — 40 suítes e 141 testes aprovados; 1 suíte preexistente falhou ao carregar `expo-audio` (`MemoryGameRenderer`).
- `git diff --check` — aprovado.

## Pendencias pos-task

- Corrigir separadamente a configuração/mocks de `expo-audio` no Jest e os erros preexistentes de typecheck.

## Status final

done
