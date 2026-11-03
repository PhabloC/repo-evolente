## Status

done

## Título

Reproduzir vídeo do YouTube na trilha mobile

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica (consome `mediaUrl` já persistida).

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/006-catalogo-conteudos-master.md`

## Objetivo

Permitir que atividades de vídeo com URL do YouTube sejam reproduzidas no app mobile, em vez de falhar no `expo-video`.

## Entrega verificável

Ao abrir uma atividade de vídeo com `mediaUrl` do YouTube, o player mobile exibe o embed e permite assistir; uploads diretos (mp4 etc.) continuam no `expo-video`.

## Fora de escopo

- Alterar criação/validação de conteúdo na web ou backend.
- Alterar capa de vídeo da biblioteca.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `mobile/src/features/trail/components/TrailVideoPlayer.tsx`
- `front-end/src/utils/youtubeMedia.ts` (referência de parsing)

## Contexto sob demanda

- docs Expo `react-native-webview` se houver dúvida de instalação.

## Orçamento de contexto

Baixo; player + util YouTube + dependência WebView.

## Dependências

- Task 636 (URL YouTube no catálogo) — done.

## Status final

done

## Resultado da execucao

- Util `youtubeMedia` no mobile para detectar URL e montar embed.
- `TrailVideoPlayer` usa WebView para YouTube e mantém `expo-video` para arquivos.
- Dependência `react-native-webview@13.16.1` instalada.
- Testes do util passaram.
