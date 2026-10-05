# Task 761 - Modal de contato WhatsApp no diretório web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- Depende da Task 760

## Modo de execucao

single-stack

## Slice vertical

- Slice 067 — `tasks/slices/067-modal-contato-profissional-diretorio.md`

## Criterios de aceite

- [x] Clique no card abre modal
- [x] Modal mostra infos do profissional
- [x] WhatsApp abre em nova aba
- [x] Teste da página ok

## Resultado da execucao

- Modal com detalhes + link `wa.me` (`target=_blank`, `rel=noopener noreferrer`).

## Handoff

- `.agents/state/handoffs/TASK-761.md`

## Arquivos alterados

- Professionals page/styles/test
- `utils/whatsapp.ts(+test)`
- types professional

## Validacoes executadas

- vitest Professionals + whatsapp — ok

## Pendencias pos-task

- Nenhuma

## Status final

done
