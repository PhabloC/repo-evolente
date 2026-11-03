## Status

done

## Título

Capa exclusiva para cards de vídeo na biblioteca mobile

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Objetivo

Substituir o placeholder tipográfico “VÍDEO” nos cards da biblioteca mobile por uma capa ilustrada exclusiva de vídeo.

## Entrega verificável

Cards de conteúdo `mediaType === 'video'` na biblioteca mobile exibem a imagem `mobile/assets/covers/capa-video-biblioteca.jpg` no topo do card.

## Fora de escopo

- Alterar a biblioteca web.
- Preview/frame do arquivo de vídeo ou thumbnail YouTube.
- Capa exclusiva de áudio.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `mobile/src/features/admin/contents/components/ContentCoverThumb/index.tsx`
- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`

## Contexto sob demanda

- `design-system/mobile/`: somente se precisar validar tipografia/cor do card.

## Orçamento de contexto

Baixo; apenas o thumb compartilhado e o asset local.

## Dependências

- Slice 047 / biblioteca mobile existentes.

## Status final

done

## Resultado da execucao

Asset local de capa de vídeo adicionado e ligado no `ContentCoverThumb` para `mediaType === 'video'`, sem mudanças na web.
