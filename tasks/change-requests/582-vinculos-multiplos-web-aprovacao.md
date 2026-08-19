# Task 582 - Aprovação de vínculos de profissionais na web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Depende da Task 581: endpoints de links profissionais da criança.

## Modo de execucao

single-stack

## Slice vertical

- Slice 053 — `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Contexto mínimo

- Índice, task, Slice 053 e handoff da Task 581.

## Contexto sob demanda

- Perfil web da criança, serviço/tipos de guardian e `front-end/docs/ai/ACCESSIBILITY.md`.
- `design-system/front/Design_System_Evolente_Desktop.md` para cards e ações.

## Orçamento de contexto

- baixo.

## Estratégia de redução

- Reutilizar o card e os botões já usados no perfil da criança; não alterar dashboard nem listagem de filhos.

## Resultado da execucao

- O perfil web da criança lista profissionais ativos, pendentes, recusados e inativos.
- Solicitações pendentes têm ações de aprovar e recusar, com atualização local após a resposta da API.

## Contexto utilizado

- Perfil da criança, tipos/serviço de guardian e checklist de acessibilidade web.

## Handoff

- `.agents/state/handoffs/TASK-582.md`

## Arquivos alterados

- Tipos/serviço de guardian, perfil da criança e estilos locais.

## Validacoes executadas

- `npm run lint` (front-end) — bloqueado por erros preexistentes fora dos arquivos desta task; a nova regra de cast no serviço foi corrigida.

## Pendencias pos-task

- Nenhuma.

## Status final

done
