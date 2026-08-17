# TASK-166 - Acoes hover nos cards de jogo da biblioteca

## Data

2026-07-24

## Decisoes

- cards de jogo do master passaram a usar overlay escurecido no hover e no foco
- ações do card usam apenas ícones Lucide: visualizar, editar e inativar/reativar
- o modal existente foi reaproveitado em modo read-only para visualização
- jogos deixaram de aparecer na tabela inferior; a tabela segue apenas para áudio e vídeo

## Contexto usado

- `tasks/change-requests/166-acoes-hover-nos-cards-de-jogo-da-biblioteca.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/166-acoes-hover-nos-cards-de-jogo-da-biblioteca.md`
- `tasks/000-index.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

## Validacoes

- `npm run lint` — ok
- `npm run build` — ok
- `npx vitest run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias

- se o card precisar abrir uma tela dedicada no futuro, o overlay já separa claramente visualizar de editar
- quando entrarem imagens reais por letra, basta trocar o placeholder atual do preview sem refazer a mecânica das ações
