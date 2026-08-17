# Handoff — Task 540

## Identificador

TASK-540

## Título

Prévia web Fluência: Ouvir usa áudio gravado da etapa

## Slice vertical

`tasks/slices/045-fluencia-em-acao.md`

## Status final

done

## Decisões preservadas

- `stages[].audioUrl` do catálogo (Task 536); botão Ouvir usa `voiceMode: recorded` quando houver URL
- Fallback TTS se `audioUrl` ausente

## Arquivos alterados

- `FluencyPreviewModal.tsx`, `fluencyGame.ts`, `content.ts`

## Próxima ação sugerida

- Abrir Fluência em Ação, clicar Ouvir e confirmar a voz gravada
