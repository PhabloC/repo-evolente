# Task 283 - Icones nos status Em dia e Limpos da pagina de avisos mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

refino incremental — status com ícone como no card da home (Não lidos + Mail)

### Fonte primaria visual

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`

## Objetivo

Colocar ícones ao lado dos textos de status "Em dia" e "Limpos" na página de avisos.

## Contexto mínimo

- esta task
- `.agents/state/handoffs/TASK-282.md`
- `ResponsavelNotificationsScreen.tsx`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Props de status | `ResponsavelNotificationsScreen.tsx` | passar `statusIcon` | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] "Em dia" tem ícone ao lado
- [x] "Limpos" tem ícone ao lado

## Dependencias

- Task 282 - done

## Resultado da execucao

- resumo rápido: `CheckCircle2` quando "Em dia" (Mail continua em "Pendentes")
- card vazio: `CheckCircle2` no status "Limpos" / "Sem avisos"

## Contexto utilizado

- `ResponsavelNotificationsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-283.md`

## Arquivos alterados

- `tasks/change-requests/283-icones-status-em-dia-e-limpos-pagina-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-283.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- validação visual dependente de reload

## Pendencias pos-task

- nenhuma

## Status final

done
