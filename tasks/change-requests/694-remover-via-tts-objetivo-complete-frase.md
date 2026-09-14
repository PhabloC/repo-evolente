# Task 694 - Remover “via TTS” do objetivo terapêutico

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Contrato

- Não aplicável.

## Modo de execução

single-stack

## Slice vertical

- `tasks/slices/042-complete-a-frase.md`

## Objetivo

Atualizar o objetivo terapêutico do Complete a frase para não mencionar TTS.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/042-complete-a-frase.md`

## Contexto sob demanda

- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`: objetivo terapêutico padrão.

## Orçamento de contexto

- 6 fontes; carregar apenas o bootstrap e configuração relacionada.

## Status final

done

## Resultado da execucao

- Objetivo atualizado para: “Estimular vocabulário, construção de frases e compreensão auditiva com feedback oral.”
- Registro existente de Complete a frase atualizado no banco.

## Contexto utilizado

- Bootstrap do catálogo e registro persistido da atividade.

## Handoff

- Alteração concluída.

## Arquivos alterados

- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-694.md`

## Validacoes executadas

- SQL de atualização retornou `Complete a frase`.
- Busca no bootstrap confirmou a nova frase.

## Pendencias pos-task

- Nenhuma.
