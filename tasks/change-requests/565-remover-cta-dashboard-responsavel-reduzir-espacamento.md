# Task 565 - Remover CTA do dashboard do responsável e reduzir espaçamento

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

Não se aplica.

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 052 - Dashboard analítico web do responsável

### Arquivo do slice

- `tasks/slices/052-dashboard-analitico-responsavel-web.md`

## Referencia de design system

- Stack de referência visual: front-end.
- Tipo: artefato de design system + solicitação visual do usuário.
- Fonte: `front-end/src/pages/Main/Guardian/Dashboard/`, Header e tokens de espaçamento existentes.

## Origem da solicitacao

Pedido humano: retirar “Cadastrar filho” do dashboard, mantendo o acesso somente na página Filhos, e diminuir o espaçamento do dashboard.

## Comportamento esperado

- Dashboard do responsável não exibe CTA “Cadastrar filho” no header.
- Página Filhos mantém seu CTA para cadastro de filho.
- Espaçamento entre header e conteúdo do dashboard é reduzido sem alterar a legibilidade dos indicadores e gráficos.

## Fora de escopo

- Remover CTA da página Filhos ou do empty state sem filhos.
- Alterar navegação, gráficos, notificações ou mobile.

## Criterios de aceite

- [ ] Dashboard não tem botão “Cadastrar filho” no header.
- [ ] Página Filhos continua oferecendo o CTA.
- [ ] Espaçamento vertical do dashboard é reduzido e o layout permanece responsivo.
- [ ] Lint focado passa.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e `tasks/slices/052-dashboard-analitico-responsavel-web.md`
- `.agents/state/handoffs/TASK-564.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| CTA do dashboard | `front-end/src/pages/Main/Guardian/Dashboard/index.tsx` | remover ação local sem afetar Filhos/empty state | sim |
| Espaçamento | `front-end/src/pages/Main/Guardian/styles.module.css` e layout adjacente | reduzir somente a separação afetada | sim |
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | preservar a hierarquia e ações restantes | sim |

## Orçamento de contexto

- baixo
- estratégia de redução: abrir somente dashboard, estilos locais, página Filhos para confirmação e diretriz de acessibilidade.

## Dependencias

- Task 564 - Ajustar CTA e notificações no cabeçalho do dashboard do responsável (done)

## Resultado da execucao

O dashboard do responsável não envia mais o CTA “Cadastrar filho” ao `MainLayout`; o CTA próprio da página Filhos e o do empty state sem filhos permanecem. `MainLayout` recebeu a opção `contentSpacing="compact"`, aplicada apenas ao dashboard para reduzir de `--space-4` para `--space-2` a separação entre header e conteúdo.

## Contexto utilizado

- Contexto mínimo: governança raiz, índice, esta task, Slice 052 e handoff da Task 564.
- Sob demanda: dashboard, página Filhos para confirmar o CTA independente, `MainLayout`, estilos e acessibilidade.

## Handoff

`.agents/state/handoffs/TASK-565.md`

## Arquivos alterados

- `front-end/src/pages/Main/Guardian/Dashboard/index.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/layout/MainLayout/styles.module.css`
- esta task, Slice 052, índice e handoff da Task 565

## Validacoes executadas

- eslint focado: ok.
- `git diff --check`: ok (somente avisos de normalização CRLF preexistentes).
- Vitest não foi executado: o ambiente segue sem iniciar workers, conforme Tasks 563–564.

## Pendencias pos-task

- Nenhuma.

## Status final

done
