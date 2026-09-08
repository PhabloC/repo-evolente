# Handoff - Task 635

## Task

- identificador: 635
- título: Login web mobile manter cabeçalho do card
- slice: 012 - Login visual e acesso livre web
- status final: done

## Decisões preservadas

- Em mobile, ocultar apenas o branding externo ao card.
- Selo, título, subtítulo, superfície branca, formulário e CTAs permanecem visíveis, seguindo o print enviado.
- A prop passou a se chamar `hideBrandingOnMobile` para refletir esse comportamento.

## Contexto efetivamente usado

- Task/handoff 634, Slice 012, print do usuário, `AuthLayout`, LoginPage e guias de acessibilidade/QA web.

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/Login/index.test.tsx`
- task, slice e índice.

## Validações executadas

- Teste da LoginPage: ok (2 testes).
- Lint dos arquivos alterados: ok.

## Pendências

- Lint/build completos têm falhas preexistentes fora do escopo, registradas na Task 634.

## Próximo contexto recomendado

- Para outro ajuste de login responsivo: este handoff, a Task 635 e `front-end/src/layout/AuthLayout/**`.
