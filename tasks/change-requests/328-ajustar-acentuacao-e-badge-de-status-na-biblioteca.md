# Task 328 - Ajustar acentuacao e badge de status na biblioteca

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

- A tabela da biblioteca deve manter texto legível em português e badge de status consistente com o padrão visual das demais telas internas.

## Contexto de negocio

### Por que

O catálogo precisa exibir informações da tabela com acentuação correta e o status ativo com indicador visual mais claro.

### O que

Corrigir a renderização dos labels acentuados da biblioteca e adicionar a bolinha à esquerda na badge de status da tabela.

### Comportamento esperado

- dificuldade aparece como `Fácil`, `Médio` e `Difícil`
- chips de dificuldade no preview também usam acentuação correta
- badge de `Ativo` e `Inativo` da tabela mostra bolinha à esquerda

### Fora de escopo

- mudanças de backend
- alterações fora da biblioteca

## Dependencias

- Task 324
- Task 325
- Task 326
- Task 327

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
- `.agents/state/handoffs/TASK-327.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/Library/` | ajustar tabela, preview e badge de status | sim |
| Labels compartilhados | `front-end/src/constants/contentOptions.ts` | reaproveitar labels acentuados por helper central | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia de redução: manter a mudança limitada ao catálogo web e reaproveitar padrões já existentes de label e badge

## Criterios de conclusao

- dificuldade com acentuação correta na tabela
- dificuldade com acentuação correta no preview de mídia
- badge de status da tabela com bolinha à esquerda
- teste da biblioteca atualizado

## Validacao esperada

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: a biblioteca passou a exibir os labels de dificuldade com acentuação correta e a badge de status da tabela ganhou o indicador circular à esquerda.

### Relação com o slice

- O Slice 006 recebeu um refino visual e textual no catálogo sem alterar o comportamento funcional das ações.

### Decisões técnicas

- a acentuação foi centralizada em helper de dificuldade compartilhado
- a badge da biblioteca passou a seguir o mesmo padrão visual de status já usado em outras telas web

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-327.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/constants/contentOptions.ts` | labels | helper de dificuldade |
| `front-end/src/pages/Main/Library/` | UI web | tabela, preview, estilos e testes |

### Contexto evitado

- backend, contrato e mobile, por não haver impacto de integração

## Handoff

- Caminho: `.agents/state/handoffs/TASK-328.md`
- Próximo contexto recomendado: reutilizar esta task se o catálogo pedir padronização adicional de badges ou labels em outras áreas da biblioteca.

## Arquivos alterados

- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/MediaPreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/328-ajustar-acentuacao-e-badge-de-status-na-biblioteca.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-328.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok em **quarta-feira, 29 de julho de 2026**

## Pendencias pos-task

- sem pendências

## Status final

done
