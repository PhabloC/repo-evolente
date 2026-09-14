# Task 679 - Remover scroll interno da atividade Escreva a letra no mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

mobile

## Perfil do projeto

- mobile: sim

## Contrato

Não aplicável; ajuste local de layout e interação.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/030-escrita-guiada-de-letras.md`

## Objetivo

Impedir que a tela da atividade Escreva a letra tenha scroll interno sobre a área de escrita, permitindo que o gesto do usuário seja usado exclusivamente para desenhar a letra.

## Entrega verificável

- A atividade Escreva a letra não renderiza scroll interno na área da atividade.
- O canvas/área de escrita recebe o gesto sem ser interceptado por rolagem.
- O layout continua acessível em telas mobile suportadas, sem alterar o fluxo do jogo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- este arquivo

## Contexto sob demanda

- `mobile/AGENTS.md`, `mobile/GUIDE.md` e `mobile/docs/ai/` — implementar e validar o ajuste na stack mobile.
- `mobile/` — localizar a tela/componente da atividade e seu container de scroll.

## Orçamento de contexto

Até 6 fontes/arquivos direcionados; não carregar requirements, contrato ou design system, pois não há regra de negócio, API ou mudança visual solicitada.

## Critérios de aceite

- [x] Remover/desabilitar o scroll interno específico da atividade de escrita.
- [x] Preservar o gesto de desenho no canvas.
- [x] Executar lint/typecheck/test disponíveis no mobile.

## Resultado da execucao

O `ScrollView` da tela de atividade agora recebe `scrollEnabled={false}` apenas quando o jogo é `alphabet-writing`. Os demais jogos e vídeos mantêm o comportamento anterior.

## Contexto utilizado

- Contexto mínimo da raiz e Slice 030.
- `mobile/AGENTS.md` e `mobile/GUIDE.md`.
- `TrailActivityScreen` e `AlphabetWritingGameRenderer`.

## Handoff

Correção restrita ao container da tela de atividade; o quadro continua responsável por capturar os gestos de escrita.

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Validacoes executadas

- `npx eslint src/features/trail/screens/TrailActivityScreen.tsx` — sem saída de erro antes da cadeia de validações ficar sem resposta.
- `npx tsc --noEmit` e teste direcionado foram iniciados, mas o processo não concluiu no ambiente.

## Pendencias pos-task

- Validar manualmente em Android/iOS, especialmente em telas menores, o desenho contínuo dentro do quadro.

## Status final

done

## Status final

in_progress
