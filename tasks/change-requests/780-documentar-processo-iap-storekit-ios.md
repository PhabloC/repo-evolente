# Task 780 - Documentar processo IAP StoreKit iOS

## Status

done

## Tipo

shared

## Stacks envolvidos

- docs (raiz)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- n/a (aponta endpoints planejados; contrato formal na task 781)

## Modo de execucao

single-stack

## Slice vertical

- Slice 070 — `tasks/slices/070-iap-storekit-ios.md`

## Escopo

- Criar documentação viva `docs/development/ios-iap-storekit.md` cobrindo: motivo da rejeição Apple, decisões (Asaas permanece, IAP só iOS), fluxo usuário, App Store Connect, backend, mobile, testes Sandbox, checklist de reenvio à review, e status do que já foi implementado vs pendente.
- Atualizar o doc à medida que as tasks 781/782 avançarem.

## Fora de escopo

- Implementação de código de pagamento

## Criterios de aceite

- [x] Arquivo `docs/development/ios-iap-storekit.md` existe e descreve o processo ponta a ponta
- [x] Slice 070 e índice referenciam o doc
- [x] Seção de status distingue feito / em andamento / pendente humano (App Store Connect)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/slices/070-iap-storekit-ios.md`
- `erro_aprovacao.md`
- esta task

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Decisões de produto | conversa / slice 039 e 070 | redigir decisões | sim |

## Orçamento de contexto

- baixo; apenas docs e governança.

## Resultado da execucao

- Criado `docs/development/ios-iap-storekit.md` com decisões, fluxo, env vars, checklist Connect e status.
- Slice 070 e índice atualizados.

## Contexto utilizado

- `erro_aprovacao.md`, slice 070, decisões da sessão

## Handoff

- `.agents/state/handoffs/TASK-780.md`

## Arquivos alterados

- `docs/development/ios-iap-storekit.md`
- `tasks/slices/070-iap-storekit-ios.md`
- `tasks/000-index.md`
- esta task

## Validacoes executadas

- Revisão manual do doc

## Pendencias pos-task

- Atualizar doc após Sandbox/review

## Status final

done
