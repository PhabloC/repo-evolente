# Handoff - Task 033

## Task

- identificador: 033
- título: SVG animado elegante no fundo auth web
- tipo: front
- modo de execução: single-stack
- status final: done
- arquivo: `tasks/change-requests/033-svg-animado-fundo-auth-web.md`

## Decisões preservadas

- decisão: usar SVG inline no `AuthLayout`
- motivo: permite controle fino de composição, escala e camadas sem depender de asset externo
- impacto: login, cadastro e recovery/reset compartilham o mesmo fundo animado

- decisão: separar animações em orbs, linhas e pontos
- motivo: movimento mais elegante e menos chamativo do que animar tudo igual
- impacto: fundo sutil, com melhor leitura do card e do branding

- decisão: respeitar `prefers-reduced-motion`
- motivo: reduzir impacto para usuários com preferência por menos movimento
- impacto: animação desativada automaticamente quando necessário

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/033-svg-animado-fundo-auth-web.md`
- `tasks/slices/014-template-auth-unificado.md`
- `.agents/state/handoffs/TASK-032.md`

### Evitado

- backend
- mobile
- requirements
- contrato OpenAPI

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `tasks/change-requests/033-svg-animado-fundo-auth-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-033.md`

## Validações executadas

- `npm run lint` em `front-end/` — ok

## Próxima ação sugerida

- Se quiser elevar mais o acabamento visual, o próximo passo natural é ajustar opacidade, escala e posição do SVG por breakpoint após revisão visual no navegador
