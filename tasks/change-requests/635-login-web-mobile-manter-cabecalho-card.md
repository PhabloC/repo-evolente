# Task 635 - Login web mobile manter cabeçalho do card

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end (React/Vite)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (não envolvido; é responsividade da web)

## Contrato

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

- Slice 012 - Login visual e acesso livre web
- `tasks/slices/012-login-visual-acesso-livre.md`

## Referência visual

- Fonte primária: print enviado pelo usuário nesta solicitação (login mobile).
- Conteúdo obrigatório no mobile: selo, título, subtítulo, campos, ações, divisor e CTAs dentro do card branco.

## Objetivo

Corrigir a variante responsiva da Task 634: ocultar apenas a área institucional externa e manter o cabeçalho e a superfície do card de login no mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/012-login-visual-acesso-livre.md`
- `.agents/state/handoffs/TASK-634.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Ajuste visual | print enviado pelo usuário | preservar o conteúdo e o card do login mobile |
| Implementação | `front-end/src/layout/AuthLayout/**` | remover as regras responsivas incorretas |
| Regressão | `front-end/src/pages/Auth/Login/**` | manter a variante aplicada apenas ao login |
| UI web | `front-end/docs/ai/ACCESSIBILITY.md`, `QA.md` | preservar os controles e validar |

## Orçamento de contexto

- Risco: baixo; mudança CSS isolada, sem API, backend ou app nativo.

## Critérios de conclusão

- [x] Branding externo não aparece no mobile.
- [x] Selo, título, subtítulo e fundo branco do card continuam visíveis no mobile.
- [x] Controles do formulário permanecem acessíveis.

## Resultado da execucao

- A variante responsiva foi renomeada para `hideBrandingOnMobile`, descrevendo corretamente seu efeito.
- No login web até 560px, somente o bloco institucional externo é ocultado. O card preserva selo, título, subtítulo, superfície branca, campos e todas as ações, conforme o print enviado.
- O desktop e as outras telas que usam `AuthLayout` não foram alterados.

## Contexto utilizado

- Contexto mínimo: AGENTS, GUIDE, context map, índice, esta task, Slice 012 e handoff da Task 634.
- Contexto sob demanda: print enviado, `AuthLayout`, LoginPage e guias de acessibilidade e QA da stack web.
- Evitado: API, backend, app mobile nativo, OpenAPI e requisitos amplos.

## Handoff

- `.agents/state/handoffs/TASK-635.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/Login/index.test.tsx`
- esta task, Slice 012, índice e handoff.

## Validacoes executadas

- `npm run test -- --run src/pages/Auth/Login/index.test.tsx` — ok (2 testes).
- `npx eslint src/layout/AuthLayout/index.tsx src/pages/Auth/Login/index.tsx src/pages/Auth/Login/index.test.tsx` — ok.

## Pendencias pos-task

- Lint/build completos permanecem com falhas preexistentes fora deste escopo, registradas na Task 634.

## Status final

done
