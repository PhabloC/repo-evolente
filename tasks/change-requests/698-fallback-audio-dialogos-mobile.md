# Task 698 - Garantir fallback individual de áudio em Diálogos

## Status
done

## Tipo
mobile

## Stacks envolvidos
mobile

## Perfil do projeto
- mobile: sim

## Contrato
Não aplicável; comportamento do game config.

## Modo de execução
single-stack

## Slice vertical
`tasks/slices/046-dialogos-em-acao.md`

## Objetivo
Corrigir o review do item 2 de `ajustes.md` para que URLs parciais não silenciem trechos da situação.

## Entrega verificável
Cada trecho usa áudio gravado quando disponível e TTS individualmente quando ausente; sequência gravada integral só é usada quando completa.

## Contexto mínimo
`AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, slice 046, `ajustes.md`.

## Contexto sob demanda
`mobile/AGENTS.md`, renderer de diálogo e `gameSpeechService`; necessários para preservar o contrato de fala.

## Orçamento de contexto
Até 8 arquivos; sem backend, contrato ou design system.

## Critérios de aceite
- [ ] Nenhum trecho é omitido com URLs parciais.
- [ ] Fallback TTS é individual.
- [ ] Validações mobile executadas.

## Code review relacionado
`ajustes.md`, item 2.

## Resultado da execucao
Cada trecho usa áudio gravado ou TTS individualmente.

## Contexto utilizado
Contexto mínimo, stack mobile e serviço/renderer de fala.

## Handoff
Fallback granular implementado.

## Arquivos alterados
Serviço de fala e renderer de diálogo.

## Validacoes executadas
`npm run typecheck` e `npm run lint` — aprovados.

## Pendencias pos-task
Nenhuma.

## Status final
done
