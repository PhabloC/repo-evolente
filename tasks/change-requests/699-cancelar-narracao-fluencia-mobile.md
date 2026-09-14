# Task 699 - Cancelar narração antiga ao avançar Fluência

## Status
done

## Tipo
mobile

## Stacks envolvidos
mobile

## Perfil do projeto
- mobile: sim

## Contrato
Não aplicável.

## Modo de execução
single-stack

## Slice vertical
`tasks/slices/045-fluencia-em-acao.md`

## Objetivo
Corrigir o review do item 3 de `ajustes.md` para impedir que a segunda fala de uma etapa antiga toque após avanço ou saída.

## Entrega verificável
Sequências assíncronas verificam um token de execução após cada await e não iniciam falas obsoletas.

## Contexto mínimo
`AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, slice 045, `ajustes.md`.

## Contexto sob demanda
`mobile/AGENTS.md`, renderer de fluência e `gameSpeechService`; necessários para implementar cancelamento seguro.

## Orçamento de contexto
Até 8 arquivos; sem backend, contrato ou design system.

## Critérios de aceite
- [ ] Fala antiga não continua após cancelamento.
- [ ] Próxima etapa permanece audível.
- [ ] Validações mobile executadas.

## Code review relacionado
`ajustes.md`, item 3.

## Resultado da execucao
Token de execução impede a segunda fala obsoleta.

## Contexto utilizado
Contexto mínimo, stack mobile e renderer/serviço de fala.

## Handoff
Avanço de etapa invalida a sequência anterior.

## Arquivos alterados
Renderer de fluência.

## Validacoes executadas
`npm run typecheck` e `npm run lint` — aprovados.

## Pendencias pos-task
Nenhuma.

## Status final
done
