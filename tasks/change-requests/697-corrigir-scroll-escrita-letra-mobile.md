# Task 697 - Restaurar scroll acessível na escrita de letras mobile

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
`tasks/slices/030-escrita-guiada-de-letras.md`

## Objetivo
Corrigir o review do item 1 de `ajustes.md`: manter os controles acessíveis em telas pequenas sem deixar o canvas perder seus gestos.

## Entrega verificável
Remover o bloqueio global de scroll da tela e preservar a captura de desenho somente na área apropriada.

## Contexto mínimo
`AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, slice 030, `ajustes.md`.

## Contexto sob demanda
`mobile/AGENTS.md`, `mobile/GUIDE.md`, `TrailActivityScreen.tsx` e renderer de escrita; necessários para implementar e validar o gesto/layout.

## Orçamento de contexto
Até 8 arquivos; não carregar backend, contrato ou design system.

## Critérios de aceite
- [ ] Scroll permanece habilitado e botões alcançáveis.
- [ ] Canvas continua desenhando.
- [ ] Lint/typecheck/test direcionado executados.

## Code review relacionado
`ajustes.md`, item 1.

## Resultado da execucao
Scroll restaurado; o quadro mantém seus responders de desenho.

## Contexto utilizado
Contexto mínimo, stack mobile e arquivos da tela/renderer.

## Handoff
Correção restrita ao container da atividade.

## Arquivos alterados
`mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Validacoes executadas
`npm run typecheck` e `npm run lint` — aprovados.

## Pendencias pos-task
Nenhuma.

## Status final
done
