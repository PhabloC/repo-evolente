# Task 791 - Card Encontrar profissionais no perfil mobile

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

- `GET /professionals`
- Schema `ProfessionalDirectoryListResponse`

## Modo de execucao

single-stack

## Slice vertical

- Slice 071 - Diretório de profissionais no perfil mobile do responsável
- `tasks/slices/071-diretorio-profissionais-perfil-mobile.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato documental + UI existente do perfil

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/src/features/shell/components/HomeActionCard/`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

### Regra de aderencia visual

- O card no perfil reutiliza `HomeActionCard` (clay, colapsado, ícone + nome).
- A tela do diretório reutiliza hero, top bar e cards do perfil/relatórios.
- Sem print específico: não inventar linguagem visual nova nem copiar o layout web.

## Origem da solicitacao

Pedido humano: adicionar no app mobile o fluxo **Encontrar profissionais** já existente na web, com um card no perfil do responsável.

## Objetivo

O responsável encontra profissionais cadastrados a partir do perfil do app, sem depender só do vínculo iniciado pelo profissional via código.

## Comportamento esperado

- Card **Encontrar profissionais** no perfil, colapsável, com CTA que abre a tela do diretório.
- Tela autenticada lista `nearby` e `others` via `GET /professionals`.
- Busca por nome/especialidade e filtro por área quando houver opções.
- Loading, erro e empty cobertos.
- Toque no profissional abre contato; WhatsApp quando houver telefone público.
- Texto de orientação: o vínculo continua pelo código da criança.

## Fora de escopo

- Backend, OpenAPI e front-end web
- Solicitar vínculo a partir do card
- Alterar home, login ou cadastro

## Criterios de aceite

- [x] Card **Encontrar profissionais** visível no perfil do responsável.
- [x] CTA abre a tela do diretório.
- [x] Lista consome `GET /professionals`.
- [x] Loading, erro, empty e busca cobertos.
- [x] Contato/WhatsApp só com telefone público do contrato.
- [x] Lint e testes do escopo passam. Typecheck do app tem erros pré-existentes fora deste escopo.

## Dependências

- Task 751 — done (API do diretório)
- Task 752 — done (página web; referência de comportamento)
- Task 760 — done (telefone de contato)
- Task 773 — done (cards colapsados do perfil)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e Slice 071

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| UI do perfil | `ResponsavelProfileScreen`, `HomeActionCard` | posicionar o card | sim |
| Rotas | `mobile/src/routes/params.ts`, `RootNavigator.tsx` | nova tela | sim |
| API | `contracts/openapi.yaml` path `/professionals` | payload e seções | sim |
| Referência visual | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | tokens e cards | sim |
| Comportamento web | `front-end/src/pages/Main/Guardian/Professionals/` | busca, seções, contato | sob demanda |

## Orçamento de contexto

- médio
- estratégia: limitar à feature professionals, rota e card do perfil; não abrir backend, web além da referência de comportamento, jogos ou IAP.

## Status final

done

## Resultado da execucao

- O perfil do responsável ganhou o card colapsável **Encontrar profissionais**, com CTA **Ver profissionais**.
- A rota `ProfessionalsDirectory` lista próximos e outros via `GET /professionals`, com busca, filtro de área, loading, erro e empty.
- O toque no profissional abre o contato; WhatsApp só quando há telefone público no contrato.
- O vínculo continua pelo código da criança; a tela não cria solicitação.

## Contexto utilizado

- Mínimo: AGENTS, GUIDE, context-map, índice, Task 791 e Slice 071.
- Sob demanda: `GET /professionals` no OpenAPI, perfil/`HomeActionCard`, rotas, tela web de profissionais (comportamento), tokens/cards mobile.
- Não carregado: backend, IAP, jogos, design-system front.

## Acessibilidade aplicada

- Card do perfil com `accessibilityLabel` e CTA próprio.
- Busca com label; chips de área com `tab` e estado selecionado.
- Cards e paginação com label/hint; botão WhatsApp com label; modal com `onRequestClose`.
- Alvos de toque mínimos de 44px na paginação e nas ações do modal.

## Handoff

- `.agents/state/handoffs/TASK-791.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/routes/params.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/professionals/**`
- `tasks/slices/071-diretorio-profissionais-perfil-mobile.md`
- `tasks/change-requests/791-card-encontrar-profissionais-perfil-mobile.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx eslint` nos arquivos alterados — passou.
- `npm test` nas 5 suítes da feature — 12 testes passaram.
- `npm run typecheck` — erros pré-existentes em admin/games/trail; nenhum no escopo desta task.

## Pendencias pos-task

- Conferir no Expo (dispositivo/emulador) o card do perfil e o diretório com API real.
- Sem verificação visual em dispositivo nesta sessão.
