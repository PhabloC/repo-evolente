# Task 621 - Cadastro de filho no perfil do responsável mobile

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

- `POST /guardians/me/children`
- `GET /guardians/me/children`
- Schema `CreateGuardianChildRequest`

## Modo de execucao

single-stack

## Slice vertical

- Slice 055 - Cadastro de filho no perfil mobile
- `tasks/slices/055-cadastro-filho-perfil-mobile.md`

## Objetivo

No perfil do responsável, disponibilizar o cadastro completo de um filho pelo aplicativo.

## Comportamento esperado

- Exibir CTA `Cadastrar filho` no perfil do responsável, para primeiro ou próximo filho.
- Abrir um formulário em etapas para dados da criança e anamnese obrigatória (Q1–Q8).
- Validar dados obrigatórios, CPF e ao menos uma categoria na pergunta 6 antes de enviar.
- Criar com `POST /guardians/me/children`; em sucesso invalidar a listagem, selecionar o filho criado e voltar ao perfil com feedback.
- Exibir erros de validação, de acesso e de CPF já cadastrado sem descartar o preenchimento.

## Fora de escopo

- Mudanças no backend, no OpenAPI, em pagamento, edição de anamnese ou montagem da trilha.

## Referência visual

- Mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`.
- Sem print específico: reutilizar `HomeActionCard`, campos, botões e a linguagem do perfil mobile; não copiar o wizard web.

## Critérios de aceite

- [x] CTA acessível no perfil, inclusive sem filhos.
- [x] Dados da criança + anamnese completa são enviados no contrato vigente.
- [x] Sucesso atualiza a lista e torna o filho recém-criado o selecionado.
- [x] Estados de loading, erro e envio repetido são tratados.
- [x] Testes e lint do escopo passam.

## Dependências

- Task 560 — done (contrato de criação autenticada)
- Task 561 — done (lista e seleção de filhos)
- Task 601 — done (perfil/seletor atual)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e Slice 055
- `.agents/state/handoffs/TASK-560.md`, `.agents/state/handoffs/TASK-561.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI de perfil/formulário | `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`, `mobile/src/features/profile/**`, `mobile/src/shared/components/**` | CTA, rota e formulário |
| Criação/cache/seleção | `mobile/src/features/children/**` | service, mutation e invalidação |
| API | `contracts/openapi.yaml` (paths e schemas de filhos) | payload e respostas |
| Referência visual | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | componentes e estados |

## Orçamento de contexto

- médio
- estratégia: limitar a implementação à feature children, rota e card do perfil; não abrir web, backend, jogos ou trilha.

## Status final

done

## Resultado da execucao

- O perfil do responsável agora permite cadastrar o primeiro filho pelo card vazio e outros filhos por um CTA próprio.
- A nova rota `CreateChild` apresenta duas etapas: dados da criança e anamnese Q1–Q8.
- O app usa o `POST /guardians/me/children` existente; após sucesso, atualiza caches de perfil/listagem, persiste e seleciona o filho criado.
- Foram tratados preenchimento obrigatório, CPF inválido, estado de envio e falhas retornadas pela API, preservando os dados preenchidos.

## Contexto utilizado

- Mínimo: AGENTS, GUIDE, context-map, índice, Task 621, Slice 055 e handoffs 560/561.
- Sob demanda: contrato `CreateGuardianChildRequest`, design system mobile, perfil do responsável, feature children, rotas e componentes de formulário compartilhados.
- Não carregado: backend, web, jogos e trilha.

## Handoff

- `.agents/state/handoffs/TASK-621.md`

## Arquivos alterados

- `mobile/src/features/children/types/child.ts`
- `mobile/src/features/children/services/childrenService.ts`
- `mobile/src/features/children/hooks/useCreateChildMutation.ts`
- `mobile/src/features/children/screens/CreateChildScreen.tsx`
- `mobile/src/features/children/screens/createChildStyles.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/routes/params.ts`
- `mobile/src/routes/RootNavigator.tsx`
- backlog, slice e handoff desta task

## Validacoes executadas

- `npm run typecheck` — passou.
- `npx eslint` nos arquivos alterados — passou.
- `npm test -- --runTestsByPath src/features/children/hooks/useGuardianChildrenQuery.test.ts src/features/children/utils/resolveSelectChildViewState.test.ts src/features/children/store/useSelectedChildStore.test.ts` — 3 suítes, 7 testes passaram.

## Pendencias pos-task

- Nenhuma.
