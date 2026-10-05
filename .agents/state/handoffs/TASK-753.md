# TASK-753

## Slice

Slice 063

## Status

done

## Decisões preservadas

- Ações `below-heading` deixaram de usar `position: absolute` (causava overlap no card).
- Grupo `headerActions` com flex em linha e wrap controlado.

## Contexto usado

- Header CSS, Children page, print do usuário.

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/pages/Main/Guardian/Children/index.tsx`
- `front-end/src/pages/Main/Guardian/styles.module.css`

## Validações

- Vitest Children — ok

## Pendências

- Nenhuma

## Próximo contexto

- Validar visualmente em `/filhos` no browser.
