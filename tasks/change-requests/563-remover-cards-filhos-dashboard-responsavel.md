# Task 563 - Remover cards de filhos duplicados do dashboard web do responsável

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

Não se aplica. A alteração é somente de renderização; os dados e endpoints existentes permanecem inalterados.

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 052 - Dashboard analítico web do responsável

### Arquivo do slice

- `tasks/slices/052-dashboard-analitico-responsavel-web.md`

## Referencia de design system

- Stack de referência visual: front-end
- Tipo: artefato de design system e composição existente do dashboard
- Fonte: `front-end/src/pages/Main/Guardian/Dashboard/` e `front-end/src/pages/Main/ShellHome/`
- Regra: preservar painel analítico, seletor de filho e empty state; retirar somente os cards de filho que aparecem antes do painel e repetidos ao final.

## Origem da solicitacao

Pedido humano: ao abrir o dashboard do responsável, aparece um card de criança antes de o conteúdo do dashboard carregar; também há um card de criança no final da página. Ambos devem ser removidos.

## Comportamento esperado

- Com um ou mais filhos, o dashboard abre diretamente no conteúdo analítico, sem grade de cards de filhos acima dele.
- A grade repetida de cards de filhos não é exibida ao final da página.
- O seletor de filho para contas com dois ou mais filhos permanece disponível.
- O empty state de conta sem filhos permanece disponível.

## Fora de escopo

- Alterar APIs, summary, gráficos, KPIs ou relatórios.
- Alterar a página Filhos.
- Alterar dashboard mobile.

## Criterios de aceite

- [ ] Nenhum card de criança é renderizado antes dos indicadores/gráficos quando há filhos.
- [ ] Nenhuma grade/card de criança é renderizada ao final do dashboard.
- [ ] Seletor para 2+ filhos e empty state para 0 filhos continuam funcionais e acessíveis.
- [ ] Teste do dashboard e lint dos arquivos tocados passam.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e `tasks/slices/052-dashboard-analitico-responsavel-web.md`
- `.agents/state/handoffs/TASK-562.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Renderização dos cards | `front-end/src/pages/Main/Guardian/Dashboard/index.tsx` e componentes adjacentes | remover as duas renderizações sem afetar seletor/empty state | sim |
| Cobertura de comportamento | teste do dashboard | ajustar/remover expectativa dos cards e preservar cenários de filhos | sim |
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | validar que estados e seletor preservados seguem acessíveis | sim |

## Orçamento de contexto

- baixo
- estratégia de redução: abrir somente o dashboard do responsável, seu teste e a diretriz de acessibilidade; não carregar serviços, OpenAPI, mobile nem dashboard profissional completo.

## Dependencias

- Task 562 - Dashboard analítico web do responsável (done)

## Resultado da execucao

A grade `GuardianChildrenGrid` foi removida do dashboard. Com isso, o card de filho não aparece durante o carregamento do painel e também não é repetido ao final da página. As consultas de trilha/progresso que alimentavam exclusivamente esses cards também foram removidas.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 052 e handoff da Task 562.
- Sob demanda: `front-end/src/pages/Main/Guardian/Dashboard/index.tsx`, teste adjacente e `front-end/docs/ai/ACCESSIBILITY.md`.

## Handoff

`.agents/state/handoffs/TASK-563.md`

## Arquivos alterados

- `front-end/src/pages/Main/Guardian/Dashboard/index.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/index.test.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/GuardianChildrenGrid.tsx` (removido)
- esta task, Slice 052, `tasks/000-index.md` e handoff da Task 563

## Validacoes executadas

- eslint focado em `index.tsx` e `index.test.tsx`: ok.
- vitest focado: não executou; o worker excedeu o tempo de inicialização antes de carregar o teste.
- `tsc --noEmit`: bloqueado por configuração pré-existente em `tsconfig.json` (`ignoreDeprecations` inválido para a versão instalada).

## Pendencias pos-task

- Nenhuma funcional. O runner de testes e o `tsconfig` podem ser corrigidos em task própria de ambiente, se necessário.

## Status final

done
