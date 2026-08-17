# Task 223 - Capa do jogo no ícone da trilha mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

mobile

## Modo de execucao

single-stack

## Slice vertical

`tasks/slices/010-app-responsavel-home-notificacoes.md`

## Objetivo

No card de atividade da trilha, o ícone à esquerda de jogos deve exibir a foto de capa (`gameConfig.coverUrl`) em vez do ícone genérico de gamepad.

## Entrega verificavel

- Atividades `game` com `coverUrl` mostram a capa
- Sem capa ou falha de carga: fallback para o ícone Lucide atual
- Áudio/vídeo permanecem com ícones de mídia

## Fora de escopo

- Backend / OpenAPI
- Catálogo web de conteúdos

## Contexto minimo

- Esta task
- `TrailTodayScreen.tsx`
- `IconPill`
- `getAlphabetCoverUrl`

## Contexto sob demanda

- `trailService` demo (já possui coverUrl)

## Orcamento de contexto

baixo

## Dependencias

- Task 221
