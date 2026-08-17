# Handoff - Task 160

## Task

- identificador: 160
- título: Prefixo de ambiente no storage de conteudos
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catalogo
- objetivo de negócio: organizar as keys do storage por ambiente
- entrega verificável: novas keys em `prefixo/contents/{contentId}/original/{uuid}.{ext}`
- status do slice: done

## Decisões preservadas

- decisão: nova env `STORAGE_KEY_PREFIX`
- motivo: separar ambiente sem hardcode
- impacto: o mesmo backend pode gravar em `dev`, `staging` ou `prod`

- decisão: pasta fixa `original/`
- motivo: deixar espaço para derivados futuros sem redesenhar a convenção
- impacto: novos uploads entram em `.../original/...`

- decisão: prefixo atual do ambiente local é `dev`
- motivo: convenção pedida para o bucket
- impacto: uploads reais agora devem cair em `dev/contents/...`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/160-prefixo-de-ambiente-no-storage-de-conteudos.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-159.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `.env.example` / `.env.local` | env | prefixo |
| `contents.service.ts` | upload | geração de key |

## Resultado por stack

- backend: done

## Arquivos alterados

- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `backend/.env.example`
- `backend/.env.local`
- task/slice/index/handoff

## Validações executadas

- backend lint: ok
- backend test: ok (17 suites / 64 tests)

## Pendências ou bloqueios

- nenhuma bloqueante
- falta apenas validação manual de upload real no bucket

## Próxima ação sugerida

- subir o backend e testar um upload na biblioteca

## Próximo contexto recomendado

- rota `/biblioteca` ou chamada direta de `POST /contents/{id}/media`

## Contexto que não deve ser carregado na próxima etapa

- fonte: refactors de storage não relacionados
- motivo: padrão das keys já foi definido
