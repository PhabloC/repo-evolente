# Task 700 - Reproduzir instrução de jogo sem intro mobile

## Status
done

## Tipo
mobile

## Stacks envolvidos
mobile

## Perfil do projeto
- mobile: sim

## Contrato
Não aplicável; campos opcionais do game config.

## Modo de execução
single-stack

## Slice vertical
`tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Objetivo
Corrigir o review do item 4 de `ajustes.md` para tocar a instrução mesmo quando não existe intro.

## Entrega verificável
O provider considera intro e instrução na inicialização, controla `isIntroReady` até o fim da sequência e toca qualquer URL configurada.

## Contexto mínimo
`AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, slice 048, `ajustes.md`.

## Contexto sob demanda
`mobile/AGENTS.md`, `GameSessionAudio`, consumidores e tipos de game config; necessários para preservar a sequência compartilhada.

## Orçamento de contexto
Até 8 arquivos; sem backend, contrato ou design system.

## Critérios de aceite
- [ ] Instrução toca sem intro.
- [ ] `isIntroReady` só libera após a sequência.
- [ ] Validações mobile executadas.

## Code review relacionado
`ajustes.md`, item 4.

## Resultado da execucao
Instrução toca mesmo sem intro e `isIntroReady` aguarda a sequência.

## Contexto utilizado
Contexto mínimo, stack mobile e provider compartilhado de áudio.

## Handoff
Estado acompanha intro e instrução.

## Arquivos alterados
Provider `GameSessionAudio`.

## Validacoes executadas
`npm run typecheck` e `npm run lint` — aprovados.

## Pendencias pos-task
Nenhuma.

## Status final
done
