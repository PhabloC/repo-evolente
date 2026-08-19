# Task 584 - Exibir avatar do profissional nos vínculos da criança

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Consome `avatarUrl` já exposto em `GuardianProfessionalLink` pela Task 581.

## Modo de execucao

cross-stack

## Slice vertical

- Slice 053 — `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Contexto mínimo

- Índice, task, Slice 053 e handoff das Tasks 582 e 583.

## Contexto sob demanda

- Cards de vínculo no perfil web e móvel; componentes utilitários de avatar já existentes em cada stack.

## Orçamento de contexto

- baixo.

## Estratégia de redução

- Reutilizar fallback de avatar existente; não alterar o contrato nem o fluxo de aprovação.

## Resultado da execucao

- Os cards de vínculo exibem a foto do profissional na web e no app móvel.
- Sem foto, ambos preservam um fallback circular com a inicial do nome.

## Contexto utilizado

- Cards de vínculo e utilitários de avatar das duas stacks.

## Handoff

- `.agents/state/handoffs/TASK-584.md`

## Arquivos alterados

- Perfil web da criança, estilos locais e tela móvel de perfil da criança.

## Validacoes executadas

- `git diff --check` — ok.

## Pendencias pos-task

- Nenhuma.

## Status final

done
