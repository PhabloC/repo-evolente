# Handoff - Task 686

## Task

- identificador: 686
- status final: done

## Decisões preservadas

- situação e pergunta são tocadas em sequência ao iniciar a etapa;
- áudio de opção toca ao selecionar a opção;
- `voiceMode` removido do nível raiz do config de diálogo, pois o parser mobile o rejeita;
- associação dos 10 arquivos de situação usa a ordem oficial das etapas, pois os nomes locais são truncados.

## Arquivos alterados

- `backend/scripts/upload-game-session-audios.mjs`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/components/DialogueGameRenderer/index.tsx`

## Validações executadas

- Upload S3 + atualização do catálogo concluídos.

## Pendências

- Nenhuma.
