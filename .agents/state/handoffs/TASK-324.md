# Handoff - Task 324

## Task

- identificador: 324
- título: Reabrir criacao de atividades audio e video na biblioteca master
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catalogo
- objetivo de negócio: restaurar a criação operacional de áudio/vídeo na biblioteca web do master
- entrega verificável: master cria atividade de áudio/vídeo com upload no bucket e profissional segue read-only
- status do slice: done

## Decisões preservadas

- decisão: reabrir apenas `audio` e `video` na criação
- motivo: o pedido reabre o fluxo editorial, mas não pede autoria de jogos
- impacto: o modo `create` do modal remove `game`, enquanto a edição existente segue suportando jogos

- decisão: manter `ageMinYears`, `ageMaxYears` e `difficulty` no formulário
- motivo: o contrato de `POST /contents` ainda exige esses campos
- impacto: o modal atende o pedido sem assumir defaults de produto fora da task

- decisão: exigir arquivo no modo `create`
- motivo: a entrega precisa garantir que áudio/vídeo realmente siga para o bucket
- impacto: o fluxo usa `createContent` seguido de `uploadContentMedia`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/324-reabrir-criacao-audio-video-na-biblioteca-master.md`
- `tasks/slices/006-catalogo-conteudos-master.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | preservar padrão visual da biblioteca e do modal |
| `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementação | estrutura, a11y e padrão de código |
| `contracts/openapi.yaml` | API | confirmar `POST /contents` e `POST /contents/{contentId}/media` |
| `.agents/state/handoffs/TASK-164.md` | histórico | reabrir com segurança o fluxo antes removido |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| backend/mobile docs | stacks não envolvidas |

## Resultado por stack

- front-end: done

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/324-reabrir-criacao-audio-video-na-biblioteca-master.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-324.md`

## Validações executadas

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npm run lint` — falhou por erro pré-existente fora do escopo em `src/components/PatientAvatar/*`

## Pendências ou bloqueios

- sem bloqueio para a biblioteca
- lint global do front-end segue falhando por dívida pré-existente em `PatientAvatar`

## Próxima ação sugerida

- se quiser simplificar o modal removendo idade/dificuldade, abrir task separada para revisar contrato e/ou defaults de criação

## Próximo contexto recomendado

- `tasks/change-requests/324-reabrir-criacao-audio-video-na-biblioteca-master.md`
- `.agents/state/handoffs/TASK-324.md`
- `front-end/src/pages/Main/Library/`
