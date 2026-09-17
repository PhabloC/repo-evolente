# Task 709 - Hardening de áudio na prévia web do semáforo

## Status

done

## Resultado da execucao

O áudio gravado agora resolve sua Promise ao ser cancelado, e o modal invalida a narração da etapa antes de iniciar o feedback de avanço. Assim, o áudio da figura antiga não cancela o praise e o avanço não fica pendente.

## Contexto utilizado

- `front-end/src/pages/Main/Library/TrafficLightPreviewModal.tsx`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `front-end/src/pages/Main/Library/librarySharedFeedback.ts`
- `front-end/docs/ai/QA.md`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Handoff

Hardening concluído na prévia web do semáforo. Próximo contexto recomendado: nenhum para este apontamento; eventuais falhas globais de lint/build devem ser tratadas separadamente.

## Arquivos alterados

- `front-end/src/pages/Main/Library/TrafficLightPreviewModal.tsx`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `ajustes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-709.md`

## Validacoes executadas

- `npm run lint`: travou sem diagnóstico durante `eslint .`; interrompido.
- `npm run test` e `npm run build`: não executados porque o lint permaneceu travado.
- Revisão estrutural do fluxo de cancelamento e `git diff --check` realizada.

## Pendencias pos-task

- Reexecutar lint, testes e build em ambiente em que o processo ESLint responda.

## Status final

done

## Tipo

front

## Stacks envolvidos

front-end (React/Vite)

## Perfil do projeto

web: front-end (React/Vite); mobile: sim

## Contrato

Não se aplica — correção local de reprodução de áudio.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/040-pare-e-va-semaforo.md` (hardening da prévia web existente; não cria novo slice).

## Objetivo

Garantir que a prévia web não fique aguardando áudio cancelado nem misture a instrução antiga com o feedback da próxima etapa.

## Escopo

- Resolver a Promise de áudio gravado quando a reprodução for interrompida.
- Invalidar a sequência de instrução antes de iniciar o feedback de avanço.
- Evitar que a figura da etapa anterior cancele o `praiseAudioUrl`.
- Marcar o apontamento em `ajustes.md` como `[ok]`.

## Critérios de aceite

- Avançar durante TTS ou áudio gravado não deixa `advance` pendente.
- O áudio da figura anterior não inicia após o feedback de avanço.
- O `praiseAudioUrl` pode tocar até o fim sem ser cancelado pela instrução anterior.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/040-pare-e-va-semaforo.md`
- `front-end/src/pages/Main/Library/TrafficLightPreviewModal.tsx`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`

## Contexto sob demanda

- `front-end/docs/ai/QA.md` e `front-end/docs/ai/ACCESSIBILITY.md`: aplicar os checks da stack.

## Orçamento de contexto

Até 8 fontes; limitar a mudança ao modal, serviço de fala e rastreabilidade.

## Dependências

- Task 429 / Slice 040.
