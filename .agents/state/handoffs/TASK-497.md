# Handoff - Task 497

## Task

- TASK-497 - Igualar fundo do sidebar ao background da página
- status final: done

## Decisões

- Sidebar: `background: var(--color-bg)` (mesmo token da página/shell)
- Removido véu de vidro (`::after`) que deixava o tom diferente
- Lava permanece visível sobre o fundo

## Arquivos

- `front-end/src/layout/Sidebar/styles.module.css`

## Próxima ação

- Validar visualmente no shell autenticado
