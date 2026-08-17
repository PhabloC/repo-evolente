# Task 044 - Refinar modais web por referencia visual

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

- nao se aplica; preservar integracoes e fluxos existentes

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

imagem fornecida pelo usuario no chat

### Cobertura

- cabecalho de modal com icone destacado, titulo forte e botao de fechar em pill
- campo de busca principal com destaque visual e estado vazio em cartao suave
- rodape separado das acoes, usando a paleta oficial do produto

### Lacunas

- a imagem cobre principalmente o modal de adicionar conteudo do catalogo
- decisao: aplicar a linguagem visual ao modal base compartilhado e aos modais atuais de Planejamentos, Biblioteca e Pacientes

## Objetivo

Atualizar os modais web para o estilo da referencia enviada, reutilizando os tokens de cor da Evolente e preservando acessibilidade e comportamento.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 017 e `.agents/state/handoffs/TASK-043.md`

## Contexto sob demanda

- imagem enviada pelo usuario no chat
- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/ui/Modal/**`
- `front-end/src/pages/Main/Plans/{AddCatalogContentModal.tsx,styles.module.css}`
- `front-end/src/pages/Main/Library/{ContentFormModal.tsx,styles.module.css}`
- `front-end/src/pages/Main/Patients/{LinkPatientModal.tsx,styles.module.css}`
- `front-end/src/styles/global.css`

## Orçamento de contexto

- medio; limitado ao sistema de modal compartilhado e seus tres usos atuais

## Criterios de conclusao

- [x] modal base ganha visual coerente com a referencia e com os tokens do projeto
- [x] modal de adicionar do catalogo replica busca destacada, empty state e hierarquia visual da referencia
- [x] modais de biblioteca e pacientes herdam a mesma linguagem visual sem quebrar fluxos
- [x] foco por teclado, `Esc` e retorno de foco permanecem acessiveis
- [x] lint e build aprovados

## Resultado da execucao

- `ui/Modal` recebeu novo tratamento visual com superficie clara, gradientes suaves, icone opcional, close pill e largura configuravel
- o modal de catalogo ganhou busca destacada com icone, estado vazio em cartao informativo e rodape separado das acoes
- os modais de biblioteca e vinculo de paciente passaram a reutilizar o mesmo cabecalho visual e divisao de acoes
- o modal base passou a prender foco, restaurar foco na origem e bloquear scroll de fundo enquanto aberto

## Contexto utilizado

- fontes globais, Slice 017, handoff 043, imagem do chat, docs locais de front/acessibilidade, `ui/Modal` e modais de Plans/Library/Patients

## Handoff

- `.agents/state/handoffs/TASK-044.md`

## Arquivos alterados

- `front-end/src/ui/Modal/{index.tsx,styles.module.css}`
- `front-end/src/pages/Main/Plans/{AddCatalogContentModal.tsx,styles.module.css}`
- `front-end/src/pages/Main/Library/{ContentFormModal.tsx,styles.module.css}`
- `front-end/src/pages/Main/Patients/{LinkPatientModal.tsx,styles.module.css}`
- task, slice, indice e handoff

## Validacoes executadas

- `cd front-end && npm run lint`
- `cd front-end && npm run build`

## Pendencias pos-task

- nenhuma

## Status final

done

## Dependencias

- Task 043 - done
