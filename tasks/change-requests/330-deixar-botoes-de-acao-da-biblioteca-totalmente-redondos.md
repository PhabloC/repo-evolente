# Task 330 - Deixar botoes de acao da biblioteca totalmente redondos

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

- `nao se aplica`

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

- As ações icon-only da biblioteca devem usar silhueta circular completa.

## Contexto de negocio

### Por que

Os botões de ação da biblioteca precisam ficar visualmente mais coerentes com o tratamento de ícones compactos.

### O que

Ajustar os botões de visualizar, editar, inativar/reativar e excluir para borda 100% redonda.

### Comportamento esperado

- ações da tabela aparecem em formato circular
- estados hover e cores atuais permanecem

### Fora de escopo

- mudanças funcionais nas ações
- alterações em outras tabelas

## Dependencias

- Task 325
- Task 326
- Task 327
- Task 328

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
- `.agents/state/handoffs/TASK-329.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/Library/` | ajustar o shape dos botões de ação | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia de redução: limitar a mudança ao CSS local da biblioteca

## Resultado da execucao

### Resumo por stack

- **front-end**: os botões icon-only da tabela da biblioteca passaram a usar borda totalmente circular.

### Decisões técnicas

- o ajuste ficou restrito à classe compartilhada dos botões de ação da tabela
- tamanhos, ícones e cores existentes foram preservados

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-329.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/styles.module.css` | UI web | shape circular dos botões |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-330.md`
- Próximo contexto recomendado: reutilizar esta task se o mesmo shape circular precisar ser padronizado em outras tabelas.

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/330-deixar-botoes-de-acao-da-biblioteca-totalmente-redondos.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-330.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok em **quarta-feira, 29 de julho de 2026**

## Pendencias pos-task

- sem pendências

## Status final

done
