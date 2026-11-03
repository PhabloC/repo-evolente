# Handoff - Task 785

## Task

- identificador: 785
- título: Capa exclusiva para cards de vídeo na biblioteca mobile
- slice: `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`
- status final: done

## Decisões preservadas

- somente mobile; web fora de escopo;
- capa local em `mobile/assets/covers/capa-video-biblioteca.jpg`;
- aplicada via `ContentCoverThumb` quando `mediaType === 'video'` e não há `coverUrl` remoto.

## Contexto utilizado

- `mobile/src/features/admin/contents/components/ContentCoverThumb/index.tsx`
- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`

## Arquivos alterados

- `mobile/assets/covers/capa-video-biblioteca.jpg`
- `mobile/src/features/admin/contents/components/ContentCoverThumb/index.tsx`
- `tasks/change-requests/785-capa-exclusiva-video-biblioteca-mobile.md`
- `tasks/000-index.md`

## Validações executadas

- inspeção de path do asset e wiring do `ContentCoverThumb`.

## Pendências

- validação visual no app (reload Metro).

## Próximo contexto recomendado

- `mobile/src/features/trail/screens/TrailLibraryPane.tsx` para checar cards de vídeo na biblioteca.
