# Context map

Este arquivo define como agentes devem carregar contexto neste scaffold usando progressive disclosure.

## Objetivo

Evitar carregamento excessivo de contexto e reduzir risco de dumb zone. Agentes devem começar por contexto mínimo, identificar o slice/task atual e carregar contexto sob demanda apenas quando houver gatilho explícito.

Este arquivo é um índice de decisão. Ele deve apontar onde buscar contexto, não substituir requirements, tasks, handoffs ou guias locais de stack.

## Contexto sempre permitido

Ler no início de fluxos globais:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`

Ler no início de execução de task:

- `tasks/000-index.md`
- arquivo da task atual em `tasks/*.md`
- arquivo do slice atual em `tasks/slices/*.md`
- handoff relacionado em `.agents/state/handoffs/`, quando existir e a task continuar trabalho anterior

## Contexto sob demanda

Antes de carregar qualquer fonte sob demanda, declarar:

- gatilho concreto na task, no slice, no contrato ou na referência visual;
- decisão, implementação ou validação que depende da fonte;
- menor arquivo, seção, path de contrato ou trecho suficiente.

Se a fonte desejada nao tiver gatilho concreto, nao carregar.

### Referências de processo da raiz

Carregar `.agents/references/context-engineering.md` somente quando:

- houver duvida sobre como fatiar vertical slices;
- uma conversa longa precisar ser resumida em handoff;
- uma task exigir decisao sobre orçamento de contexto ou bloqueio por excesso de contexto;
- for preciso ajustar skills/modelos de governança.

### Requirements

Carregar `requirements/` somente durante planejamento, geração de change request ou quando a task indicar requisito concreto.

Preferir arquivos específicos dentro de `requirements/` em vez do diretório inteiro.

### Design system front

Carregar `design-system/front/` somente quando:

- a task tiver UI web;
- a task declarar `Stack de referência visual: front-end` ou `multiplas stacks`;
- a task apontar caminhos concretos dentro de `design-system/front/`.

Não usar `design-system/front/` para inferir UI mobile.

### Design system mobile

Carregar `design-system/mobile/` somente quando:

- o projeto tiver mobile confirmado;
- a task tiver UI mobile;
- a task apontar caminhos concretos dentro de `design-system/mobile/`.

Não usar `design-system/mobile/` para inferir UI web.

### Contrato OpenAPI

Carregar `contracts/openapi.yaml` somente quando:

- a task envolver API;
- a task declarar endpoint ou path do contrato;
- a execução precisar validar integração cliente-servidor.

Quando possível, consultar apenas o path relevante.

### Docs locais de stack

Carregar docs locais somente da stack afetada:

- `front-end/docs/ai/` quando `Stacks envolvidos` incluir `front-end`;
- `next-js/docs/ai/` quando `Stacks envolvidos` incluir `next-js`;
- `backend/docs/ai/` quando `Stacks envolvidos` incluir `backend`;
- `mobile/docs/ai/` quando `Stacks envolvidos` incluir `mobile`.

Não carregar docs de stack não envolvida.

### Acessibilidade

Carregar `ACCESSIBILITY.md` somente quando houver UI web ou mobile.

### Segurança

Carregar docs ou skills de segurança quando:

- a task envolver autenticação, autorização, permissões, dados sensíveis ou exposição externa;
- a task declarar risco de segurança;
- a task exigir review de segurança.

## Orçamento de contexto

Antes de executar uma task, o agente deve listar o contexto que pretende carregar.

Se a lista tiver mais de 8 fontes obrigatórias, o agente deve reduzir o escopo, usar handoff existente ou bloquear pedindo fatiamento da task.

Nunca carregar diretórios inteiros de forma preventiva quando a task já aponta arquivos ou trechos específicos.

Se uma spec grande for a origem da demanda, planejar primeiro slices e tasks. O executor deve receber apenas a task atual, o slice atual, handoffs relevantes e fontes sob demanda justificadas.

## Regra de bloqueio

Bloquear a task quando não for possível identificar o contexto mínimo necessário sem inferir escopo, stack, contrato ou referência visual.
