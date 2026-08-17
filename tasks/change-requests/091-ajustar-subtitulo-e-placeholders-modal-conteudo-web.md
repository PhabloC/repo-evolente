# Task 091 - Ajustar subtitulo e placeholders no modal de conteudo web

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

- nao se aplica; ajuste textual e de usabilidade no formulario local do modal

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

imagem fornecida pelo usuario no chat

### Fonte primaria visual

- captura do modal "Novo conteudo" enviada no chat nesta solicitacao

### Lacunas

- a captura cobre apenas o estado de criacao do modal
- decisao: aplicar os placeholders ao formulario compartilhado e atualizar o subtitulo sem alterar fluxos de edicao nem integracao de upload

## Objetivo

Ajustar o subtitulo do modal de conteudo para remover a mencao a Base64 e adicionar placeholders nos campos textuais do formulario.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-044.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste de UI em modal existente | `front-end/docs/ai/AGENTS.md` | confirmar padrao estrutural do front-end antes de alterar componente de pagina | sim |
| Ajuste de UI em modal existente | `front-end/docs/ai/ACCESSIBILITY.md` | preservar rotulagem e navegacao do formulario ao introduzir placeholders | sim |
| Ajuste textual e de formulario no modal de conteudo | `front-end/src/pages/Main/Library/ContentFormModal.tsx` | alterar subtitulo e placeholders do formulario | sim |
| Ajuste visual fino no formulario | `front-end/src/pages/Main/Library/styles.module.css` | somente se o placeholder exigir ajuste visual adicional | nao |

## Orçamento de contexto

- baixo
- estrategia: limitar a execucao ao modal de conteudo da biblioteca, ao handoff do refino anterior e aos guias locais estritamente necessarios

## Criterios de conclusao

- [x] subtitulo do modal deixa de mencionar Base64
- [x] campos textuais do formulario exibem placeholders coerentes com seus labels
- [x] acessibilidade do formulario permanece preservada
- [x] validacoes locais do front-end aprovadas

## Dependencias

- Task 044 - done

## Resultado da execucao

- o subtitulo do modal de criacao passou a orientar o anexo de audio ou video sem mencionar Base64
- os campos `Titulo`, `Descricao`, `Idade minima`, `Idade maxima` e `Objetivo terapeutico` passaram a expor placeholders alinhados aos respectivos labels
- o ajuste ficou restrito ao formulario de conteudo da biblioteca, sem alterar upload, contrato ou fluxo de edicao

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-044.md`

### Sob demanda

- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`

### Contexto evitado

- `design-system/front/`, `contracts/openapi.yaml` e demais modais/paginas internas por nao serem necessarios para um ajuste textual localizado

## Handoff

- `.agents/state/handoffs/TASK-091.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `tasks/change-requests/091-ajustar-subtitulo-e-placeholders-modal-conteudo-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-091.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok (warning preexistente de chunk grande do Vite mantido)

## Pendencias pos-task

- nenhuma

## Status final

done
