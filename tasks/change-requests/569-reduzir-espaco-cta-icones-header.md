# Task 569 - Reduzir espaço entre CTA e ícones do header

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
- Tipo: captura fornecida pelo usuário no chat.
- Fonte: Header e seu CSS. A captura governa a redução do espaço entre CTA e controles de busca/notificações.

## Origem da solicitacao

Pedido humano: retirar o espaço excessivo entre o botão “Cadastrar filho” e os ícones do header.

## Comportamento esperado

- CTA e ícones ficam no mesmo grupo compacto.
- A pesquisa mantém expansão e foco funcionais.
- O layout responsivo existente permanece.

## Fora de escopo

- Alterar texto, ação do CTA ou comportamento do sino.

## Criterios de aceite

- [ ] Sem grande espaço vazio entre CTA e ícones no desktop.
- [ ] Busca e notificações continuam acessíveis.
- [ ] Lint focado passa.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 050 e `.agents/state/handoffs/TASK-568.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Layout do header | `front-end/src/layout/Header/styles.module.css` e teste | remover largura reservada pela busca fechada | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | preservar foco e nomes dos controles | sim |

## Orçamento de contexto

- baixo
- estratégia de redução: ajustar somente o CSS do header e validar o componente correspondente.

## Dependencias

- Task 564 - Ajustar CTA e notificações no cabeçalho do dashboard do responsável (done)

## Resultado da execucao

A área da busca não reserva mais a largura do campo expandido enquanto está fechada. Assim, o CTA da página Filhos fica junto aos ícones de busca e notificações; ao acionar a busca, o campo continua expandindo normalmente.

## Contexto utilizado

- Contexto mínimo: governança raiz, índice, esta task, Slice 050, handoff Task 568 e acessibilidade.
- Sob demanda: CSS e testes do Header.

## Handoff

`.agents/state/handoffs/TASK-569.md`

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- esta task, Slice 050, índice e handoff da Task 569

## Validacoes executadas

- prettier: ok.
- eslint focado: ok.
- `git diff --check`: ok (somente avisos CRLF preexistentes).

## Pendencias pos-task

- Nenhuma.

## Status final

done
