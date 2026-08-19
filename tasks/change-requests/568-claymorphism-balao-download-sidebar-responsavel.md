# Task 568 - Aplicar claymorphism ao balão de download da sidebar

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

Slice 050 - Área web do responsável e cadastro de filhos

### Arquivo do slice

- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Referencia de design system

- Stack de referência visual: front-end.
- Tipo: refinamento visual solicitado pelo usuário.
- Fonte: `front-end/src/layout/Sidebar/styles.module.css` e balão entregue na Task 567.
- Aderência: claymorphism com volumes suaves, bordas grandes, sombras claras/escuras em camadas e controles táteis, mantendo contraste e forma de balão.

## Origem da solicitacao

Pedido humano: colocar o balão no estilo claymorphism.

## Comportamento esperado

- Balão e botões das lojas ganham profundidade de claymorphism sem alterar conteúdo, destino ou regra por papel.
- Ponta inferior permanece integrada visualmente ao balão.
- Estados hover/foco preservam contraste e visibilidade.

## Fora de escopo

- Alterar links, texto, ícones, navegação ou sidebar mobile.

## Criterios de aceite

- [ ] Balão tem volume claymorphism coerente com a sidebar.
- [ ] Controles de loja têm estados acessíveis e táteis.
- [ ] Lint focado passa.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 050 e `.agents/state/handoffs/TASK-567.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Estilo do balão | `front-end/src/layout/Sidebar/styles.module.css` | aplicar volumes, sombras e ponta claymorphism | sim |
| Estrutura | Sidebar atual | preservar classes e semântica | sim |
| UI | `front-end/docs/ai/ACCESSIBILITY.md` | garantir foco e contraste | sim |

## Orçamento de contexto

- baixo
- estratégia de redução: alterar apenas os estilos do balão e validar a sidebar; não carregar serviços ou outras telas.

## Dependencias

- Task 567 - Balão de download do app na sidebar do responsável (done)

## Resultado da execucao

O balão e sua ponta agora usam claymorphism: superfície em degradê claro, bordas suaves, realces internos e sombras de volume. Os botões de App Store e Google Play receberam o mesmo tratamento tátil, com estado de hover/foco visível e contraste preservado.

## Contexto utilizado

- Contexto mínimo: governança raiz, índice, esta task, Slice 050, handoff Task 567 e acessibilidade.
- Sob demanda: estilos e estrutura da Sidebar.

## Handoff

`.agents/state/handoffs/TASK-568.md`

## Arquivos alterados

- `front-end/src/layout/Sidebar/styles.module.css`
- esta task, Slice 050, índice e handoff da Task 568

## Validacoes executadas

- prettier: ok.
- eslint focado: ok.
- `git diff --check`: ok (somente avisos CRLF preexistentes).

## Pendencias pos-task

- Nenhuma.

## Status final

done
