# Task 623 - Refinar formulário de cadastro de filho mobile

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

- não altera contrato; preserva `POST /guardians/me/children`

## Modo de execucao

single-stack

## Slice vertical

- Slice 055 - Cadastro de filho no perfil mobile
- `tasks/slices/055-cadastro-filho-perfil-mobile.md`

## Objetivo

Refinar a primeira etapa do cadastro de filho para melhorar a orientação de preenchimento e a continuidade visual da tela.

## Comportamento esperado

- Aproximar a seção `Dados da criança` do topo da tela, reduzindo apenas a folga visual excessiva.
- Adicionar placeholders úteis aos campos de texto.
- Aplicar máscaras aos campos que possuem formato previsível, sem alterar o payload enviado à API.
- Substituir o ícone atual do botão `Continuar` por uma seta apontando para a direita.

## Fora de escopo

- Alterar contrato, backend, validações de negócio, anamnese ou fluxo de navegação.

## Referência visual

- Mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`.
- Sem print específico: preservar os campos, botões e linguagem existentes da tela de cadastro.

## Critérios de aceite

- [ ] A seção `Dados da criança` fica visualmente mais próxima do topo.
- [ ] Campos textuais mostram placeholders coerentes e acessíveis.
- [ ] CPF e data de nascimento aceitam apenas o formato mascarado esperado, mantendo a validação existente.
- [ ] `Continuar` usa ícone Lucide de seta para a direita.
- [ ] Typecheck e lint do escopo passam.

## Dependências

- Task 621 — done

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 055 e `.agents/state/handoffs/TASK-621.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI do formulário | `mobile/src/features/children/screens/CreateChildScreen.tsx`, `mobile/src/features/children/screens/createChildStyles.ts` | espaçamento, placeholders, máscara e ícone |
| Componentes de entrada | `mobile/src/shared/components/TextField*` | confirmar suporte a placeholder e teclado |
| Referência visual | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | consistência visual |
| Convenções mobile | `mobile/docs/ai/AGENTS.md`, `CODE_STYLE.md`, `COMPONENT_REUSE.md`, `MOBILE_PATTERNS.md`, `QA.md` | organização, ícones e validação |

## Orçamento de contexto

- baixo
- estratégia: restringir a alteração à tela e ao estilo local, reutilizando componentes existentes e sem carregar contrato completo, backend ou outras features.

## Resultado da execucao

- A primeira etapa do cadastro agora tem uma folga leve entre o cabeçalho e o bloco `Dados da criança`.
- Foram adicionados placeholders aos campos textuais do cadastro e da anamnese.
- Data de nascimento usa a máscara `DD/MM/AAAA` e CPF usa `000.000.000-00`; antes do envio, os valores seguem normalizados para o contrato atual.
- O botão `Continuar` passou a usar o ícone Lucide `ArrowRight`.

## Contexto utilizado

- Mínimo: AGENTS, GUIDE, context-map, índice, Task 623, Slice 055 e handoff Task 621.
- Sob demanda: tela e estilos do cadastro, `TextField`, `Button`, design system mobile e convenções locais necessárias de mobile.
- Não carregado: backend, web, contrato completo, jogos ou outras features.

## Handoff

- `.agents/state/handoffs/TASK-623.md`

## Arquivos alterados

- `mobile/src/features/children/screens/CreateChildScreen.tsx`
- `mobile/src/features/children/screens/createChildStyles.ts`
- `mobile/src/features/children/utils/childFormInput.ts`
- `mobile/src/features/children/utils/childFormInput.test.ts`
- backlog, Slice 055 e handoff desta task

## Validacoes executadas

- `npm test -- --runInBand src/features/children/utils/childFormInput.test.ts` — passou (1 suíte, 2 testes).
- `npm run typecheck` — passou.
- `npx eslint src/features/children/screens/CreateChildScreen.tsx src/features/children/screens/createChildStyles.ts src/features/children/utils/childFormInput.ts src/features/children/utils/childFormInput.test.ts` — passou.
- `git diff --check` — passou.

## Pendencias pos-task

- Nenhuma.

## Status final

done
