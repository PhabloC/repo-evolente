# Handoff — Task 486

## Identificador

- task: 486
- slice: 006
- status final: done

## Decisões

- a biblioteca web passa a gerar config mínima válida ao trocar um conteúdo para `emotions`, `fluency` ou `dialogue`
- o review falava em "criar", mas o caminho real hoje é principalmente edição/troca de tipo, já que criação com `mediaType=game` continua bloqueada no modal
- o preview usa `AbortController` + token local para ignorar respostas tardias de `getContent`

## Próxima ação

Se o fluxo de autoria de jogos for reaberto no futuro, reaproveitar esses defaults como base do editor dedicado.
