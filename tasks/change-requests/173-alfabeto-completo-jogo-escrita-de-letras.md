# Task 173 - Alfabeto completo no jogo de escrita de letras

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

nao se aplica

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/030-escrita-guiada-de-letras.md`

## Referencia de design system

- sem mudança visual de layout

## Contexto de negocio

### Por que

O jogo “Escreva a letra” só pedia vogais. O pedido é expandir para o alfabeto completo.

### O que

- templates de validação A–Z no web e no mobile
- default do bootstrap com A–Z
- sincronizar o jogo padrão já existente no catálogo para A–Z

### Fora de escopo

- biblioteca `$P`/TensorFlow.js
- calibração fina letra a letra além do necessário para templates básicos

## Contexto mínimo

- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-172.md`

## Contexto sob demanda

| Gatilho | Fonte | Obrigatorio? |
|---|---|---|
| templates | utilitarios web/mobile | sim |
| default letters | bootstrap backend | sim |

## Orçamento de contexto

- medio-baixo

## Criterios de aceite

- [x] jogo padrão pede letras de A a Z
- [x] bootstrap atualiza jogo existente “Escreva a letra” se ainda estiver só com vogais
- [x] templates cobrem A–Z
- [x] testes essenciais passam

## Resultado da execucao

Templates A–Z adicionados no web/mobile. Bootstrap cria e sincroniza o jogo “Escreva a letra” com 26 letras. Demo mobile da trilha também atualizado.

## Arquivos alterados

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.test.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `tasks/change-requests/173-alfabeto-completo-jogo-escrita-de-letras.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-173.md`

## Validacoes executadas

- bootstrap tests — ok
- letterWritingGame web — ok
- alphabetWritingGame mobile — ok

## Pendencias pos-task

- reiniciar/aguardar reload do backend para o bootstrap expandir letras no banco local
- calibração fina de consoantes pode precisar de ajuste após uso real

## Status final

done
