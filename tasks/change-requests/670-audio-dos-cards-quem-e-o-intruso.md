## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica; o payload de item foi estendido com `audioUrl` opcional.

## Modo de execução

cross-stack

## Slice vertical

`tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Objetivo

Reproduzir o áudio correspondente ao card ao selecioná-lo no jogo Quem é o intruso.

## Entrega verificável

Cada item recebe URL de áudio e o mobile reproduz a pronúncia ao toque, com fallback para voz do dispositivo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `backend/src/modules/contents/odd-one-out-game-assets.ts`
- `mobile/src/features/games/components/OddOneOutGameRenderer/`

## Contexto sob demanda

- `mobile/src/features/games/services/gameSpeechService.ts`: reprodução e fallback.

## Orçamento de contexto

Baixo.

## Status final

done
