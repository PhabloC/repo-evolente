# Handoff - Task 393

## Task

- identificador: 393
- título: Reverter criação de atividade quando o upload falhar na biblioteca web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catalogo de conteudos do master

## Decisões preservadas

- criação + upload continuam em duas chamadas HTTP; a atomicidade prática ficou no cliente via rollback com `deleteContent`
- o rollback só roda no modo `create`; falha de upload na edição não apaga o conteúdo existente
- se o próprio `deleteContent` falhar no rollback, o erro exibido continua sendo o do upload (melhor esforço)

## Contexto utilizado

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/services/contents/contentService.ts`
- `front-end/src/pages/Main/Library/index.test.tsx`

## Arquivos alterados

- página Library, teste, task, slice, índice e handoff

## Validações executadas

- suíte `Library/index.test.tsx` (11 testes)
- eslint nos arquivos alterados (erro pré-existente de `Card` não usado)

## Pendências ou bloqueios

- atomicidade no backend continua opcional / fora desta task
- import `Card` não usado na Library (pré-existente)

## Próximo contexto recomendado

- nenhum; correção localizada no fluxo de create da Library
