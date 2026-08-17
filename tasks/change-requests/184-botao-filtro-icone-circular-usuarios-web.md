# Task 184 - Botão de filtro só ícone circular na página de usuários

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

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

- front-end

### Tipo de referencia visual

artefato documental

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

## Contexto de negocio

### Por que

O botão de filtro com texto ocupa espaço desnecessário; o ícone sozinho com formato circular fica mais limpo.

### O que

Remover o texto "Filtro", manter só o ícone `FunnelPlus`, com borda 100% redonda e `aria-label` para acessibilidade.

### Fora de escopo

- mudanças no dropdown de filtro
- outros botões da página

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-183.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Botão filtro | `front-end/src/pages/Main/AdminUsers/**` | ajuste visual | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- botão só com ícone, circular, acessível via aria-label
- teste atualizado

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

- Botão de filtro ficou só com ícone `FunnelPlus`, `aria-label="Filtro"` e `border-radius: 100%`.

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`

## Validacoes executadas

- lint ok
- AdminUsers tests ok (7)

## Handoff

- `.agents/state/handoffs/TASK-184.md`

## Pendencias pos-task

- nenhuma

## Status final

done
