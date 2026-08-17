# Task 198 - Visualizar jogo no perfil profissional da biblioteca

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

nao se aplica

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

- O card de jogo do profissional deve manter a mesma linguagem de hover já existente no catálogo, expondo apenas a ação de visualizar.

## Contexto de negocio

### Por que

O profissional também precisa inspecionar o jogo publicado na biblioteca antes de usá-lo na trilha.

### O que

Habilitar no perfil profissional da biblioteca o hover com ícone de olho nos cards de jogo e abrir o preview jogável em modo somente leitura.

### Comportamento esperado

- profissional vê o card de jogo com efeito de hover
- o hover/foco revela o ícone do olho
- clicar no olho abre o mesmo preview jogável já usado pelo master
- ações de editar, inativar e reativar continuam exclusivas do master

### Fora de escopo

- mudanças no backend
- novas ações para o profissional na biblioteca
- mudanças na execução mobile do jogo

## Slice vertical

### Identificador do slice

Slice 029 - Catalogo inicial de jogos terapeuticos

### Arquivo do slice

- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `.agents/state/handoffs/TASK-176.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | preservar a linguagem visual dos cards e ações | sim |
| Front-end | `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` e `ACCESSIBILITY.md` | implementação e acessibilidade do hover/preview | sim |
| Biblioteca web | `front-end/src/pages/Main/Library/index.tsx`, `styles.module.css` e `index.test.tsx` | alteração e validação localizadas | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: restringir a mudança à rota `/biblioteca`, sem reabrir contrato, backend ou mobile

## Criterios de conclusao

- card de jogo no perfil profissional mostra hover/foco com ícone de olho
- profissional consegue abrir o preview jogável a partir da biblioteca
- profissional continua sem ações de editar/inativar
- lint e teste da biblioteca passam

## Dependencias

- Task 176

## Resultado da execucao

- O card de jogo do profissional passou a reutilizar o overlay da biblioteca com a ação de visualizar.
- O preview jogável segue sendo aberto no mesmo `GamePreviewModal`, preservando o modo somente leitura.
- As ações de editar e inativar/reativar permanecem restritas ao master.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 198, slice 029 e `TASK-176`
- contexto sob demanda: `design-system/front/Design_System_Evolente_Desktop.md`; `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`; `front-end/src/pages/Main/Library/index.tsx`, `styles.module.css`, `index.test.tsx`
- contexto evitado: `contracts/openapi.yaml`, `backend/`, `mobile/`

## Handoff

- `.agents/state/handoffs/TASK-198.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/198-visualizar-jogo-no-perfil-profissional-da-biblioteca.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-198.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
