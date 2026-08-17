# Handoff - Task 168

## Task

- identificador: 168
- título: Preview jogavel no visualizar do card da biblioteca
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 029 - Catalogo inicial de jogos terapeuticos
- objetivo de negócio: permitir que o master visualize o jogo real a partir do card
- entrega verificável: o ícone de olho abre uma prévia jogável do alfabeto dentro da biblioteca
- status do slice: done

## Decisões preservadas

- decisão: `visualizar` deixou de abrir metadados e passou a abrir o jogo em si
- motivo: o objetivo do card é revisar a experiência real do conteúdo
- impacto: preview e edição agora têm superfícies separadas

- decisão: usar voz nativa do navegador na prévia web
- motivo: manter o mesmo princípio adotado no mobile de não depender de upload de áudio
- impacto: o preview continua útil mesmo sem mídia gravada

## Contexto utilizado

- `tasks/change-requests/168-preview-jogavel-no-visualizar-do-card-da-biblioteca.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `.agents/state/handoffs/TASK-166.md`
- `.agents/state/handoffs/TASK-167.md`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/168-preview-jogavel-no-visualizar-do-card-da-biblioteca.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run build` — ok
- `npx vitest run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias ou bloqueios

- sem bloqueio
- navegadores podem variar na voz disponível; o preview já tem fallback visual/textual

## Proxima acao sugerida

- quando entrarem novos jogos, seguir o mesmo padrão: preview local dedicado por `gameType`, sem misturar com o modal de edição
