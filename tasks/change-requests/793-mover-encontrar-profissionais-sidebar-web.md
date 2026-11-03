# Task 793 - Mover Encontrar profissionais para a sidebar web do responsável

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora de escopo)

## Contrato

- n/a (reusa `GET /professionals` e a rota `/profissionais` já existentes)

## Modo de execucao

single-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Referencia de design system

- Stack de referência visual: front-end
- Tipo: artefato de design system + sidebar existente da área do responsável
- Fonte primária: `design-system/front/Design_System_Evolente_Desktop.md`
- Fontes adjacentes: `front-end/src/constants/navigation.ts`, `front-end/src/layout/Sidebar/`, página Filhos
- Lacuna: sem print do item novo — reutilizar o padrão de nav da sidebar; não inventar CTA visual novo

## Origem da solicitacao

Pedido humano: na versão web da área do responsável, o botão **Encontrar profissionais** da página Filhos deve ir para a sidebar.

## Comportamento esperado

- A sidebar do responsável ganha o item **Profissionais**, apontando para `/profissionais`.
- O item fica entre **Filhos** e **Relatórios**, só no papel `responsavel`.
- O botão **Encontrar profissionais** some do cabeçalho da página Filhos.
- **Cadastrar filho** permanece no cabeçalho de Filhos.
- A página do diretório e a API não mudam.

## Fora de escopo

- Mobile
- Backend / OpenAPI
- Alterar listagem, filtros ou modal de contato do diretório
- Redesign da sidebar

## Criterios de aceite

- [x] Sidebar do responsável exibe o item **Profissionais** com destino `/profissionais`.
- [x] O item não aparece para master nem profissional.
- [x] Página Filhos não tem mais o botão **Encontrar profissionais**.
- [x] **Cadastrar filho** continua visível em Filhos.
- [x] Testes de navegação e da página Filhos passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 063 e handoff da Task 752

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Itens da sidebar | `front-end/src/constants/navigation.ts` | incluir item só para responsável | sim |
| Ícone do item | `front-end/src/layout/Sidebar/index.tsx` | mapear label → ícone Lucide | sim |
| CTA de Filhos | `front-end/src/pages/Main/Guardian/Children/` | remover o botão do cabeçalho | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | link de nav com texto visível | sim |

## Orçamento de contexto

- baixo

## Estratégia de redução

- Não recarregar requirements, OpenAPI nem mobile.
- Não reler o design system inteiro: só o padrão já usado na sidebar.
- Não alterar a página `/profissionais`.

## Dependências

- Task 752 — done

## Resultado da execucao

- O responsável acessa o diretório pelo item **Profissionais** na sidebar (entre Filhos e Relatórios).
- O botão **Encontrar profissionais** saiu do cabeçalho de Filhos; **Cadastrar filho** permanece.
- Master e profissional não veem o item.

## Contexto utilizado

- Contexto mínimo da task, Slice 063, handoff 752, `navigation.ts`, Sidebar, Children e ACCESSIBILITY.md.

## Handoff

- `.agents/state/handoffs/TASK-793.md`

## Arquivos alterados

- `front-end/src/constants/navigation.ts`
- `front-end/src/constants/navigation.test.ts`
- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.test.tsx`
- `tasks/slices/063-diretorio-profissionais-responsavel-web.md`
- `tasks/000-index.md`
- `tasks/change-requests/793-mover-encontrar-profissionais-sidebar-web.md`

## Validacoes executadas

- `npx vitest run` navigation + Children — 4 testes ok
- Sidebar test `shows the app download callout only for guardians` falhou por href das lojas (`/baixar-app` vs URLs reais) — falha pré-existente, fora desta task
- ReadLints nos arquivos alterados — sem erros
- Browser em `/filhos` redirecionou para login; sem conta autenticada nesta sessão para validar o sidebar visualmente

## Acessibilidade aplicada

- Item da sidebar é `NavLink` com texto visível **Profissionais**
- Ícone `Search` com `aria-hidden="true"`
- Destino descrito pelo `title` do item (`Encontrar profissionais cadastrados na Evolente`)

## Pendencias pos-task

- Nenhuma

## Status final

done
