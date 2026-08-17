# Handoff - Task 049

## Task

- identificador: 049
- título: Gitignore local nas stacks backend, front-end e mobile
- tipo: shared
- modo de execução: cross-stack
- status final: done
- arquivo: `tasks/change-requests/049-gitignore-stacks-backend-front-end-mobile.md`

## Decisões preservadas

- decisao: criar apenas o `.gitignore` ausente no `backend/`
- motivo: `front-end/` e `mobile/` ja possuíam arquivos locais validos
- impacto: cada stack passa a manter seu proprio ignore local sem alterar comportamento do produto

- decisao: complementar o `.gitignore` do `front-end/` com regras de `.env`
- motivo: o arquivo existente nao ignorava variaveis de ambiente locais
- impacto: reduz risco de versionar segredos do front, preservando `.env.example`

- decisao: complementar o `.gitignore` do `mobile/` com regras de `.env`
- motivo: o arquivo existente ignorava apenas `.env*.local`
- impacto: reduz risco de versionar segredos do mobile, preservando `.env.example`

- decisao: mapear o pedido `frontend` para o diretório real `front-end/`
- motivo: o monorepo usa `front-end/` como stack web React/Vite
- impacto: evita criar caminho incorreto ou duplicado

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `tasks/change-requests/049-gitignore-stacks-backend-front-end-mobile.md`

### Sob demanda

- `.gitignore`
- `front-end/.gitignore`
- `mobile/.gitignore`
- `backend/package.json`
- `.agents/state/handoffs/TASK-031.md`

### Evitado

- requirements
- design-system
- contrato OpenAPI
- docs locais de stack fora do necessario

## Arquivos alterados

- `backend/.gitignore`
- `front-end/.gitignore`
- `mobile/.gitignore`
- `tasks/change-requests/049-gitignore-stacks-backend-front-end-mobile.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-049.md`

## Validações executadas

- leitura e verificacao dos `.gitignore` das tres stacks

## Próxima ação sugerida

- se quiser padronizacao ainda mais estrita entre stacks, revisar depois os `.gitignore` de `front-end/` e `mobile/` em uma CR separada
