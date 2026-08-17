# Task 384 - Restaurar botões nativos da nav bar Android mobile

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

não se aplica

## Modo de execução

single-stack

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Referência visual

- mobile; reversão funcional pedida na conversa para voltar a exibir os botões nativos do Android

## Objetivo

Reverter a ocultação global da navigation bar nativa no Android para os botões do sistema voltarem a aparecer.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-149.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Config Android | `mobile/app.json` | reverter a configuração do plugin que esconde a nav bar | sim |
| Runtime Android | `mobile/src/app/providers/AppProviders.tsx` | remover a ocultação programática da nav bar | sim |

## Orçamento de contexto

- baixo
- estratégia: reversão localizada na configuração e no provider global do app

## Critérios de conclusão

- [x] app não oculta mais a nav bar nativa no Android
- [x] runtime não força mais `NavigationBar.setHidden(true)`
- [x] `npm run typecheck` segue sem diagnósticos

## Resultado da execucao

- `mobile/app.json` deixou de pedir `hidden: true` ao plugin `expo-navigation-bar`
- `AppProviders` não importa mais `expo-navigation-bar` nem força ocultação da nav bar no runtime Android
- os botões nativos do sistema voltam a depender do comportamento padrão do Android/device

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 022 e handoff `TASK-149`
- contexto sob demanda: `mobile/app.json`, `mobile/src/app/providers/AppProviders.tsx`
- contexto evitado: telas da trilha, shell visual e outras stacks, porque o pedido era só reverter a ocultação global da nav bar

## Handoff

- `.agents/state/handoffs/TASK-384.md`

## Arquivos alterados

- `mobile/app.json`
- `mobile/src/app/providers/AppProviders.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- validar em device Android; a mudança de `app.json` pode exigir novo build nativo para o plugin refletir totalmente

## Status final

done
