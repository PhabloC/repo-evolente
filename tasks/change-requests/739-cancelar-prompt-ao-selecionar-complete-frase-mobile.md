## Status

done

# Task 739 - Cancelar prompt ao selecionar no Complete a frase mobile

- **Tipo**: mobile
- **Stacks envolvidos**: mobile
- **Perfil do projeto**: mobile `sim` (Expo)
- **Contrato**: não aplicável; correção local da sequência de áudio.
- **Modo de execução**: single-stack
- **Slice vertical**: `tasks/slices/042-complete-a-frase.md`
- **Dependências**: Tasks 724 e 727 concluídas.
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e o Slice 042.
- **Contexto sob demanda**: `mobile/AGENTS.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/QA.md`, `mobile/src/features/games/components/SentenceFillGameRenderer/index.tsx`, seu teste e `mobile/src/features/games/services/gameSpeechService.ts`; necessários para cancelar a narração pendente e testar a corrida de 400 ms.
- **Orçamento de contexto**: até 8 fontes; sem API, design system ou outras stacks.

## Objetivo

Impedir que o prompt de uma rodada interrompa o áudio de feedback ou da frase correta após o usuário selecionar uma opção antes dos 400 ms iniciais.

## Entrega verificável

- O timer de prompt é cancelado após uma seleção.
- O efeito não agenda novo prompt enquanto houver opção selecionada.
- Um teste de regressão cobre a seleção antes de 400 ms.

## Critérios de aceite

- [x] Nenhum `speakGameText` do prompt ocorre após seleção antecipada.
- [x] A fala da frase correta continua sendo iniciada normalmente.
- [x] Lint, typecheck e testes mobile são executados.

## Resultado da execucao

- O efeito de narração do prompt retorna quando uma opção está selecionada.
- `selectedOptionId` foi incluído nas dependências, acionando o cleanup do timer pendente após a seleção.
- Adicionado teste de regressão para acerto antes dos 400 ms.

## Contexto utilizado

- Contexto mínimo da raiz e Slice 042.
- Regras e QA mobile, renderizador, serviço de fala e teste do componente.

## Handoff

`.agents/state/handoffs/TASK-739.md`

## Arquivos alterados

- `mobile/src/features/games/components/SentenceFillGameRenderer/index.tsx`
- `mobile/src/features/games/components/SentenceFillGameRenderer/index.test.tsx`
- `tasks/change-requests/739-cancelar-prompt-ao-selecionar-complete-frase-mobile.md`
- `tasks/slices/042-complete-a-frase.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-739.md`

## Validacoes executadas

- `npm run test -- SentenceFillGameRenderer/index.test.tsx --runInBand` — aprovado.
- `npm run lint` — aprovado com 1 warning preexistente em `src/shared/notifications/oneSignal.ts`.
- `npm run typecheck` — bloqueado por erros preexistentes fora do escopo.
- `npm run test -- --runInBand` — 41 suítes e 142 testes aprovados; 1 suíte preexistente falhou ao carregar `expo-audio` (`MemoryGameRenderer`).

## Pendencias pos-task

- Corrigir separadamente a configuração/mocks de `expo-audio` no Jest e os erros preexistentes de typecheck.

## Status final

done
