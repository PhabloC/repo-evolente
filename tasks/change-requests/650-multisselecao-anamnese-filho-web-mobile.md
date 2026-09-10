# Task 650 - Multisseleção de motivo principal e comunicação na anamnese

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- mobile
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Atualiza o contrato de `POST /guardians/me/children` para arrays nos dois campos; o armazenamento continua no JSON da anamnese.

## Modo de execucao

cross-stack

## Slice vertical

- Slice 060 - Multisseleção na anamnese do filho
- `tasks/slices/060-multisselecao-anamnese-filho.md`

## Objetivo

Permitir selecionar mais de uma opção nos campos `Motivo principal` e `Comunicação` durante o cadastro de filho, tanto na web quanto no mobile.

## Comportamento esperado

- Substituir a semântica de seleção única por seleção múltipla apenas nesses dois campos.
- Permitir adicionar e remover opções sem perder as demais seleções.
- Persistir e reidratar todas as opções selecionadas no formato já suportado pelo backend.
- Usar controles acessíveis com indicação clara de selecionado/não selecionado.

## Fora de escopo

- Novas opções ou mudanças de texto.
- Alterações no backend, OpenAPI ou sugestão de trilha.
- Mudanças em outras perguntas da anamnese.

## Referência visual

- Web: `design-system/front/Design_System_Evolente_Desktop.md` e padrões do wizard existente.
- Mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md` e componentes do cadastro existente.
- A imagem enviada pelo usuário governa o comportamento da seção web `Motivo principal`; não cobre mobile nem o campo `Comunicação`, que devem preservar a linguagem da própria stack.

## Critérios de aceite

- [x] Web permite selecionar múltiplos motivos principais.
- [x] Web permite selecionar múltiplas formas de comunicação.
- [x] Mobile oferece o mesmo comportamento nos dois campos.
- [x] Payload e tipos preservam todas as seleções.
- [x] Backend valida e retorna arrays, sem migração adicional.
- [x] Build/typecheck do escopo, lint backend e `git diff --check` passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 060 e handoffs `TASK-560.md`, `TASK-621.md`, `TASK-623.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Implementação web | `front-end/src/pages/Auth/RegisterGuardian/**` e arquivos do cadastro autenticado | estado, schemas e renderização |
| Implementação mobile | `mobile/src/features/children/**` | estado, payload e renderização |
| Contrato | `contracts/openapi.yaml`, `POST /guardians/me/children` | validar formato persistido |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | aderência visual |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | aderência visual |
| Acessibilidade web | `front-end/docs/ai/ACCESSIBILITY.md` | grupos e estados acessíveis |
| Convenções locais | docs `front-end/docs/ai/` e `mobile/docs/ai/` dos arquivos envolvidos | organização e validação |

## Orçamento de contexto

- médio; executar em duas frentes independentes, lendo somente formulário, tipos, utilitários, serviços e testes relacionados.

## Dependências

- Task 560 — done
- Task 621 — done
- Task 623 — done

## Resultado da execucao

- `motivoPrincipal` e `comunicacao` passaram a ser arrays no contrato, DTOs e tipos compartilhados.
- Web e mobile usam checkboxes/multisseleção com estado acessível; outras perguntas permanecem de seleção única.
- Leituras de perfil e relatórios formatam múltiplas respostas; registros novos preservam todas as escolhas.

## Contexto utilizado

- Task, Slice 060, índice e handoffs 560/621/623.
- Formulários web/mobile, tipos, DTO/serviço backend, OpenAPI, design-system e acessibilidade web.

## Handoff

- `.agents/state/handoffs/TASK-650.md`

## Arquivos alterados

- `front-end/src/pages/Main/Guardian/ChildRegister/**`, tipos/schema e perfis/testes relacionados.
- `mobile/src/features/children/**`.
- `backend/src/modules/guardians/**`, `backend/src/modules/reports/reports.service.ts`.
- `contracts/openapi.yaml`, task, slice, índice e handoff.

## Validacoes executadas

- `npx tsc --noEmit` em `front-end` — passou para a mudança; build completo ainda acusa pendências preexistentes em Patients/Plans.
- `npx tsc --noEmit` em `mobile` — mudança sem erro; projeto completo mantém erros preexistentes em admin/auth/games/trail.
- `npm run build` em `backend` — passou.
- lint backend e ESLint do formulário mobile — passaram.
- `git diff --check` — passou.

## Pendencias pos-task

- Nenhuma funcional. Permanecem erros preexistentes de typecheck fora do escopo nas stacks web/mobile.

## Status final

done



