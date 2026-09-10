## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica; alteração no conteúdo seed do jogo.

## Modo de execução

cross-stack

## Slice vertical

`tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Objetivo

Garantir que as rodadas do jogo Quem é o intruso tenham um elemento semanticamente fora da categoria.

## Entrega verificável

A rodada Roupas usa banana como intruso, mantendo meia, camiseta e shorts como peças de vestir. A mesma regra deve orientar novas rodadas.

Correção posterior: o merge do catálogo agora substitui configurações antigas que ainda usam Boné como intruso, permitindo que instalações existentes recebam a correção no bootstrap.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `backend/src/modules/contents/odd-one-out-game-assets.ts`

## Contexto sob demanda

- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`: persistência do seed.
- parsers mobile/web do jogo: compatibilidade do payload.

## Orçamento de contexto

Baixo; ajuste de conteúdo seed, sem alterar contrato.

## Status final

done
