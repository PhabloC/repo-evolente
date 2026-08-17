# Task 471 - Efeito de vidro no sidebar igual ao login

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Aplicar no sidebar o véu de vidro translúcido usado na tela de login (`AuthLayout` pageCover).

## Criterios de conclusao

- [x] overlay translúcido com highlight/borda como no login
- [x] bolhas continuam visíveis atrás do véu
- [x] mobile sem overlay (lava já desligada)

## Resultado da execucao

- `.sidebar::after` com gradiente/borda no padrão do login
- fundo do sidebar mais translúcido; lava um pouco mais visível

## Arquivos alterados

- `front-end/src/layout/Sidebar/styles.module.css`
- `tasks/000-index.md`

## Status final

done
