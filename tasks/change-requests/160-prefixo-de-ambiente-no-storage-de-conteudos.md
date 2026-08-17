# Task 160 - Prefixo de ambiente no storage de conteudos

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

O bucket já está funcional, mas os objetos ainda não seguem uma convenção com isolamento por ambiente e pasta `original`.

### O que

Ajustar o backend para gravar conteúdos no padrão `prefixo/contents/{contentId}/original/{uuid}.{ext}`.

### Comportamento esperado

- uploads usam prefixo configurável por env
- conteúdos ficam organizados por ambiente
- provider local e S3 seguem o mesmo key pattern

### Fora de escopo

- migração de objetos antigos
- UI

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master continua único ator de upload
- Casos de erro: prefixo com barras extras; compatibilidade com storage local
- Decisoes humanas confirmadas: padrão com pasta por ambiente e `original`
- Casos de borda: prefixo vazio continua funcional

## Especificacao tecnica

### Deve

- introduzir env de prefixo para storage
- manter compatibilidade com bucket publico atual
- preservar key aleatória por arquivo

### Nao deve

- nao hardcodar `dev` no código
- nao quebrar testes existentes de upload

## Entradas

- `backend/.env.example`
- `backend/.env.local`
- `backend/docs/ai/ARCHITECTURE.md`

## Dependencias

- Task 159

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

### Objetivo de negócio

Organizar os objetos do catálogo em prefixos previsíveis por ambiente.

### Entrega verificável do slice

Keys novas no padrão `prefixo/contents/{contentId}/original/{uuid}.{ext}`.

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
| Backend | `backend/docs/ai/ARCHITECTURE.md` | ajustar geração de key | sim |
| Env | `backend/.env.example e .env.local` | refletir prefixo | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a mudanca ao fluxo de geração de key e envs do storage

## Criterios de conclusao

- nova env de prefixo documentada
- uploads usam `prefixo/contents/{contentId}/original/...`
- lint e test do backend passam

## Instrucoes de implementacao

- normalizar o prefixo para evitar barras duplicadas
- usar `dev` no `.env.local` atual

## Validacao esperada

- `npm run lint`
- `npm run test`

## Entregaveis esperados

- ajuste de geração de key
- envs atualizadas

## Riscos ou ambiguidades

- objetos antigos permanecem onde já foram gravados; apenas novos uploads seguem o padrão novo

## Resultado da execucao

### Resumo por stack

- **backend**: o upload de conteúdos agora gera keys no padrão `prefixo/contents/{contentId}/original/{uuid}.{ext}`, com `STORAGE_KEY_PREFIX=dev` configurado no ambiente local.

### Relação com o slice

- Slice 006 foi refinado sem mudar comportamento de negócio; apenas a organização física dos objetos no storage foi endurecida.

### Decisões técnicas

- Nova env `STORAGE_KEY_PREFIX` para isolar ambiente sem hardcode no código.
- Geração de key centralizada no `ContentsService`.
- Prefixo normalizado para evitar barras duplicadas.
- Padrão final das novas keys: `dev/contents/{contentId}/original/{uuid}.{ext}` no ambiente local atual.

### Trade-offs

- Objetos antigos permanecem no path anterior.
- Só novos uploads passam a seguir a convenção nova.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-159.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `backend/.env.example` e `backend/.env.local` | env | documentar e aplicar prefixo |
| `backend/src/modules/contents/contents.service.ts` | storage | ajustar geração de key |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-160.md`
- Próximo contexto recomendado: validação manual de upload real via biblioteca ou API

## Arquivos alterados

### Backend

- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `backend/.env.example`
- `backend/.env.local`

### Governança

- `tasks/change-requests/160-prefixo-de-ambiente-no-storage-de-conteudos.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-160.md`

## Validacoes executadas

- `cd backend && npm run lint` — ok
- `cd backend && npm run test` — ok (17 suites / 64 tests)

## Aderencia ao design system

- nao se aplica (sem UI)

## Pendencias pos-task

- validar manualmente um upload real para confirmar escrita em `dev/contents/.../original/...`
- eventualmente migrar objetos antigos se você quiser uniformizar o bucket inteiro

## Status final

done
