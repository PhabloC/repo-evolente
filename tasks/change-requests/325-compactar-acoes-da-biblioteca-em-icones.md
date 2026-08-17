# Task 325 - Compactar acoes da biblioteca em icones

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

- `contracts/openapi.yaml#/paths/~1contents`

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- A tabela da biblioteca deve ficar mais compacta, com ações icon-only e contraste claro para ação destrutiva.

## Contexto de negocio

### Por que

O master precisa de ações mais compactas na tabela da biblioteca.

### O que

Transformar os botões de editar e inativar/reativar em ações apenas por ícone, destacando a inativação em vermelho.

### Comportamento esperado

- editar vira ícone de lápis
- inativar vira ícone vermelho
- reativar mantém ícone semântico de retorno
- nomes acessíveis continuam disponíveis por `aria-label`

### Fora de escopo

- exclusão real de conteúdos
- alterações de contrato/backend

## Dependencias

- Task 324

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/Library/` | implementar as ações da tabela | sim |
| Front-end | `front-end/docs/ai/CODE_STYLE.md e ACCESSIBILITY.md` | manter padrão e nomes acessíveis | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia de redução: limitar a mudança à tabela da biblioteca e ao teste isolado da página

## Resultado da execucao

### Resumo por stack

- **front-end**: as ações da tabela da biblioteca foram compactadas para ícones, com `Editar` em estilo neutro e `Inativar` em vermelho.

### Decisões técnicas

- os botões ficaram icon-only com `aria-label`
- a ação de inativar usa estilo destrutivo em vermelho
- a exclusão não foi implementada porque o slice vigente continua com decisão de `inativar, não excluir` e o contrato atual não expõe `DELETE /contents`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/325-compactar-acoes-da-biblioteca-em-icones.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok

## Status final

done
