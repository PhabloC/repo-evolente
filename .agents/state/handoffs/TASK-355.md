# Handoff - Task 355

## Task

- identificador: 355
- título: Adicionar ação de visualizar na tabela editorial da biblioteca web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign interface interna web
- objetivo de negócio: permitir preview direto dos conteúdos editoriais da biblioteca também para o profissional
- entrega verificável: coluna de ações com ícone de visualizar visível na tabela de áudio e vídeo em modo leitura

## Decisões preservadas

- decisão: manter a coluna `Ações` sempre visível, mas renderizar apenas `visualizar` para perfis sem permissão de mutação
- motivo: o problema era de acesso ao preview, não de ampliação de permissão
- impacto: a tabela fica consistente entre perfis sem liberar edição indevida

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/355-adicionar-acao-de-visualizar-na-tabela-editorial-da-biblioteca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-354.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/index.tsx` | tabela editorial | expor a ação de visualizar no modo leitura |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | cobrir o profissional com botão de preview |
| `front-end/src/ui/Table/index.tsx` | tabela compartilhada | confirmar a composição da coluna |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `backend/` | sem mudança de API |
| outras páginas da biblioteca | sem relação com a tabela editorial |

## Resultado por stack

- front-end: tabela editorial com preview disponível para profissional e ações de mutação ainda restritas ao master
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/355-adicionar-acao-de-visualizar-na-tabela-editorial-da-biblioteca-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-355.md`

## Validações executadas

- `cd front-end && npm test -- --run src/pages/Main/Library/index.test.tsx` - ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente se o alinhamento da coluna `Ações` segue adequado com poucos itens por linha no modo profissional

## Próximo contexto recomendado

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, outras páginas fora da biblioteca
- motivo: a mudança foi isolada à tabela editorial
