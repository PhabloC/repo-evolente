# Handoff - Task 356

## Task

- identificador: 356
- título: Refinar hover e badge dos cards de jogos no modo profissional web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign interface interna web
- objetivo de negócio: alinhar os cards de jogos vistos pelo profissional ao comportamento visual solicitado no chat
- entrega verificável: badge abaixo do título e preview via hover no card de leitura

## Decisões preservadas

- decisão: aplicar overlay e botão de preview somente em `gameCardReadOnly`
- motivo: o usuário pediu explicitamente essa animação apenas nos cards do perfil do profissional
- impacto: o fluxo do master não mudou

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/356-refinar-hover-e-badge-dos-cards-de-jogos-no-modo-profissional-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-355.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/index.tsx` | card profissional | reestruturar badge e preview |
| `front-end/src/pages/Main/Library/styles.module.css` | hover/focus | aplicar overlay e ícone central |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | garantir preview funcional |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `backend/` | sem mudança de API |
| outras páginas fora da biblioteca | sem relação com o card profissional |

## Resultado por stack

- front-end: cards de jogos do profissional com badge abaixo do título e preview revelado no hover/focus
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/356-refinar-hover-e-badge-dos-cards-de-jogos-no-modo-profissional-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-356.md`

## Validações executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx` - ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente no navegador se a intensidade do overlay no hover está no nível desejado

## Próximo contexto recomendado

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, páginas fora da biblioteca
- motivo: a mudança foi isolada aos cards de jogos no modo profissional
