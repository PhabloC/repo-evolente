# Handoff - Task 031

## Task

- identificador: 031
- título: Atalho dev na raiz para backend + frontend
- tipo: shared
- modo de execução: cross-stack
- status final: done
- arquivo: `tasks/change-requests/031-atalho-dev-raiz-backend-frontend.md`

## Decisões preservadas

- decisão: usar `concurrently` na raiz
- motivo: permitir um comando unico sem alterar scripts existentes das stacks
- impacto: `npm run dev` passa a subir backend e frontend juntos

- decisão: reaproveitar `backend:start:dev` e `front-end:dev`
- motivo: manter cada stack como fonte de verdade do seu fluxo local
- impacto: baixo risco e sem duplicar comandos

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `tasks/000-index.md`
- packages da raiz/backend/front-end

### Evitado

- requirements
- design-system
- mobile
- contrato OpenAPI

## Arquivos alterados

- `package.json`
- `package-lock.json`
- `tasks/000-index.md`
- `tasks/change-requests/031-atalho-dev-raiz-backend-frontend.md`

## Validações executadas

- `npm install` na raiz — ok
- `npm run dev` com timeout de teste — o encerramento forçado gerou `EPIPE` do `concurrently`; nao indica falha funcional do atalho em uso normal

## Próxima ação sugerida

- Rodar `npm run dev` na raiz sem timeout para usar backend e frontend juntos
