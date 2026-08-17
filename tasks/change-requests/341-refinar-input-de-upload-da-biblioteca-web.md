# Task 341 - Refinar input de upload da biblioteca web

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

## Slice vertical

- Slice 006 - Catálogo de conteúdos master
- `tasks/slices/006-catalogo-conteudos-master.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- refinamento incremental solicitado via chat

### Fonte primaria visual

- modal atual de criação/edição da biblioteca

### Regra de aderencia visual

- manter a semântica de upload nativo, mas substituir a aparência padrão do navegador por um controle visual alinhado ao restante do modal

## Objetivo

Melhorar o design do campo `Arquivo da atividade` no modal da biblioteca para que o upload pareça parte da interface editorial, sem perder acessibilidade nem comportamento nativo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-340.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Modal de conteúdo | `front-end/src/pages/Main/Library/ContentFormModal.tsx` | refinar o controle de upload | sim |
| Estilos da biblioteca | `front-end/src/pages/Main/Library/styles.module.css` | aplicar o novo visual do campo | sim |
| Teste da rota | `front-end/src/pages/Main/Library/index.test.tsx` | revalidar biblioteca | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar a mudança ao campo de upload do modal da biblioteca

## Criterios de conclusao

- o campo deixa de exibir a UI nativa padrão do navegador
- o novo controle comunica estado vazio, arquivo atual e arquivo recém-selecionado
- o clique continua abrindo o seletor nativo de arquivo
- teste da biblioteca continua passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: o upload do modal da biblioteca passou a usar um controle visual composto, com ícone, copy contextual, CTA e destaque para o nome do arquivo selecionado/atual.

### Relação com o slice

- refina a experiência de criação e edição do catálogo editorial do Slice 006 sem alterar regras de negócio nem integrações.

### Decisões técnicas

- o `input[type=file]` foi mantido de forma acessível e visualmente ocultado
- a interação principal passou para um `label` estilizado com estado de hover/focus
- o texto do controle varia entre arquivo atual, arquivo selecionado e estado vazio

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-340.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/ContentFormModal.tsx` | refino do upload | estrutura e estados do campo |
| `front-end/src/pages/Main/Library/styles.module.css` | refino do upload | visual e foco do controle |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | regressão da rota |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-341.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/341-refinar-input-de-upload-da-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-341.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
