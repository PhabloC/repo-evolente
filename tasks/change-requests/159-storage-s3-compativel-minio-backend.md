# Task 159 - Storage S3-compativel com MinIO no backend

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` contents

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- `nao se aplica`

### Regra de aderencia visual

- Sem UI.

## Contexto de negocio

### Por que

O catálogo já persiste metadados de mídia, mas o provider real ainda cai no adapter local e impede uso do bucket público já criado no MinIO.

### O que

Implementar adapter S3-compativel real para MinIO, selecionar via env e configurar o backend local para usar o bucket público informado.

### Comportamento esperado

- `STORAGE_PROVIDER=s3` passa a usar client S3/MinIO real
- upload de mídia salva no bucket `evolente`
- URL pública resolvida para leitura direta
- provider local continua disponível para desenvolvimento alternativo

### Fora de escopo

- UI web
- URLs assinadas
- proxy de leitura pelo backend

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: somente master continua fazendo upload
- Casos de erro: credencial invalida; bucket ausente; endpoint indisponivel
- Decisoes humanas confirmadas: bucket público; endpoint HTTPS; região `us-east-1`
- Casos de borda: provider local preservado; remoção de objeto remoto

## Especificacao tecnica

### Deve

- manter compatibilidade com adapter local
- encapsular integração externa em adapter próprio
- aceitar endpoint S3-compativel customizado do MinIO

### Nao deve

- nao salvar blob no banco
- nao hardcodar segredos no codigo fonte
- nao quebrar testes existentes de `contents`

## Entradas

- `backend/.env.example`
- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/SECURITY.md`

## Dependencias

- Task 014

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

### Objetivo de negócio

Trocar o storage local opcional por provider S3-compativel real.

### Entrega verificável do slice

Uploads do catálogo apontando para o bucket público do MinIO.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | implementar adapter externo | sim |
| API/storage | `backend/.env.example` | refletir envs | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a mudança ao adapter de storage, módulo `contents` e configuração local do backend

## Criterios de conclusao

- Adapter S3/MinIO funcional
- Seleção do provider respeita `STORAGE_PROVIDER`
- `.env.local` do backend criado com bucket público configurado
- `npm run lint` e `npm run test` do backend passam

## Instrucoes de implementacao

- preferir `@aws-sdk/client-s3` por compatibilidade com MinIO
- para bucket público, resolver URL direta sem assinatura
- registrar no handoff que segredos locais foram colocados em arquivo ignorado pelo git

## Validacao esperada

- `npm run lint`
- `npm run test`

## Entregaveis esperados

- adapter S3/MinIO
- wiring do provider no módulo `contents`
- `.env.local` do backend

## Riscos ou ambiguidades

- alguns MinIOs exigem `forcePathStyle=true`; essa compatibilidade precisa ficar explícita no adapter

## Resultado da execucao

### Resumo por stack

- **backend**: provider S3-compativel real implementado com `@aws-sdk/client-s3`, seleção por `STORAGE_PROVIDER`, URL pública resolvida para bucket público e `.env.local` do backend criado para o MinIO informado.

### Relação com o slice

- Slice 006 foi reaberto apenas para endurecer o storage e volta a `done` com suporte a provider local ou S3/MinIO real.

### Decisões técnicas

- Adapter novo em `patterns/adapters/s3-media-storage.adapter.ts`.
- Seleção do provider no `ContentsModule`: `local` ou `s3`.
- Compatibilidade explícita com MinIO via `STORAGE_S3_FORCE_PATH_STYLE=true`.
- URL pública resolvida por `STORAGE_S3_PUBLIC_BASE_URL` ou fallback `endpoint/bucket/key`.
- Credenciais gravadas apenas em `backend/.env.local`, arquivo já ignorado pelo git.

### Trade-offs

- Sem URL assinada; bucket público entrega leitura direta.
- Sem proxy/backend de download nesta fase.
- Testes continuam usando adapter local onde já estavam acoplados e cobrem o adapter S3 por spec isolada.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-156.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `backend/.env.example` | storage | refletir variáveis do provider |
| `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/SECURITY.md` | integração externa | encaixar adapter e preservar segredos fora do código |

### Contexto evitado

- contratos OpenAPI e UI web/mobile ficaram fora do escopo porque a tarefa foi puramente de infraestrutura do backend

## Handoff

- Caminho: `.agents/state/handoffs/TASK-159.md`
- Próximo contexto recomendado: Task 158 ou validação manual de upload real no ambiente local

## Arquivos alterados

### Backend

- `backend/src/patterns/adapters/s3-media-storage.adapter.ts`
- `backend/src/patterns/adapters/s3-media-storage.adapter.spec.ts`
- `backend/src/modules/contents/contents.module.ts`
- `backend/.env.example`
- `backend/.env.local`
- `backend/package.json`
- `backend/package-lock.json`

### Governança

- `tasks/change-requests/159-storage-s3-compativel-minio-backend.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-159.md`

## Validacoes executadas

- `cd backend && npm run lint` — ok
- `cd backend && npm run test` — ok (17 suites / 64 tests)

## Aderencia ao design system

- nao se aplica (sem UI)

## Pendencias pos-task

- validar upload real contra o bucket `evolente` no ambiente local com o backend rodando
- ideal rotacionar a `secret key` informada em conversa após a configuração

## Status final

done
