# Task 752 - Botão e página Encontrar profissionais na web do responsável

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

- Depende da Task 751: `GET /professionals`

## Modo de execucao

single-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Referencia de design system

- Stack de referência visual: front-end
- Tipo: artefato de design system + UI existente da área do responsável
- Fonte primária: `design-system/front/Design_System_Evolente_Desktop.md`
- Fontes adjacentes: `front-end/src/pages/Main/Guardian/Children/`, `MainLayout`, cards do responsável
- Lacuna: sem prints do diretório — reutilizar shell/tokens; não inventar linguagem visual nova

## Origem da solicitacao

Pedido humano: na área Filhos do dashboard do responsável, adicionar botão **Encontrar profissionais** que leva a uma página com os profissionais cadastrados no sistema.

## Comportamento esperado

- Na página Filhos, cabeçalho ganha ação **Encontrar profissionais** (além de Cadastrar filho).
- A ação navega para rota autenticada do responsável (ex.: `/profissionais`).
- A página lista profissionais via `GET /professionals`, com busca simples, loading, erro e empty state.
- Cada item mostra nome, avatar, especialidades e dados públicos acordados na Task 751.
- Orientação textual de que o vínculo continua pelo código da criança (sem CTA de vincular nesta tela).

## Fora de escopo

- Mobile
- Solicitar vínculo a partir do card
- Alterar perfil do filho ou fluxo de aprovação existente
- Implementar a API (Task 751)

## Criterios de aceite

- [x] Botão **Encontrar profissionais** visível na página Filhos.
- [x] Navegação abre a nova página do diretório.
- [x] Lista consome o endpoint da Task 751.
- [x] Loading, erro, empty e busca cobertos.
- [x] Rota restrita ao responsável autenticado.
- [x] Lint/testes focados da página passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 063 e handoff da Task 751

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| UI Filhos | `front-end/src/pages/Main/Guardian/Children/` | posicionar botão no header | sim |
| Rotas | `front-end/src/constants/routes` + router | nova rota e guard | sim |
| Serviço | services/hooks de professionals/guardians | consumir listagem | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | botão, lista e estados | sim |
| Visual | DS desktop + estilos Guardian | cards/listagem coerentes | sim |

## Orçamento de contexto

- baixo a médio

## Estratégia de redução

- Reutilizar `MainLayout`, `PageActionButton` e padrões de cards da área do responsável; não redesenhar o shell.

## Dependências

- Task 751 — done

## Resultado da execucao

- Página Filhos ganhou o botão **Encontrar profissionais**.
- Nova rota `/profissionais` lista o diretório com busca, loading, erro e empty state.
- Texto orienta que o vínculo segue pelo código da criança.

## Contexto utilizado

- Handoff 751, rotas/guardian pages, ACCESSIBILITY.md, estilos Guardian.

## Handoff

- `.agents/state/handoffs/TASK-752.md`

## Arquivos alterados

- `front-end/src/constants/routes.ts`
- `front-end/src/routes/index.tsx`
- `front-end/src/types/professional.ts`
- `front-end/src/services/professionals/professionalService.ts`
- `front-end/src/hooks/useProfessionalsDirectory.ts`
- `front-end/src/pages/Main/Guardian/Children/index.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.test.tsx`
- `front-end/src/pages/Main/Guardian/Professionals/index.tsx`
- `front-end/src/pages/Main/Guardian/Professionals/index.test.tsx`
- `front-end/src/pages/Main/Guardian/styles.module.css`
- `tasks/slices/063-diretorio-profissionais-responsavel-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx vitest run` Children + Professionals — 4 testes ok
- ReadLints nos arquivos alterados — sem erros

## Acessibilidade aplicada

- Botões com texto visível + ícones `aria-hidden`
- Campo de busca com `aria-label` e `type=search`
- Loading com `role=status`; erro com `role=alert`
- Hierarquia de títulos h1 (layout) → h2 (seções) → h3 (cards)
- Lista em `<ul>/<li>` com artigos nomeados

## Pendencias pos-task

- Nenhuma

## Status final

done
