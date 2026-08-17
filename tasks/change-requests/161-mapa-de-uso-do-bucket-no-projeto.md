# Task 161 - Mapear uso do bucket no projeto

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` de `contents`, `reports` e `admin/reports`

## Modo de execucao

cross-stack

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

Com o bucket MinIO/S3 já configurado para conteúdos, falta um inventário objetivo do que realmente precisa ir para o bucket no sistema e do que ainda não existe.

### O que

Mapear no código e no contrato todos os fluxos atuais de arquivos e consolidar isso em um documento Markdown na raiz.

### Comportamento esperado

- documento raiz lista o que vai para bucket hoje
- documento raiz lista o que não vai para bucket hoje
- documento raiz propõe um padrão de pastas para expansões futuras

### Fora de escopo

- mover relatórios atuais para bucket
- implementar upload de avatar
- implementar anexos clínicos

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: documento descritivo, sem mudança funcional
- Casos de erro: diferenciar fluxo existente de recomendação futura
- Decisoes humanas confirmadas: manter bucket público atual e padrão por pastas
- Casos de borda: evitar inferir avatar/anexo onde o sistema ainda não tem suporte

## Especificacao tecnica

### Deve

- inspecionar backend, contrato e pontos visuais relevantes do app/web
- registrar evidências de código para cada conclusão
- deixar explícito o padrão recomendado de organização no bucket

### Nao deve

- não afirmar uploads inexistentes
- não alterar comportamento do storage atual

## Entradas

- `tasks/change-requests/159-storage-s3-compativel-minio-backend.md`
- `tasks/change-requests/160-prefixo-de-ambiente-no-storage-de-conteudos.md`
- `.agents/state/handoffs/TASK-160.md`

## Dependencias

- Task 159
- Task 160

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

### Objetivo de negócio

Dar visibilidade operacional para o uso do bucket já conectado ao catálogo e para futuras expansões de storage.

### Entrega verificável do slice

Documento raiz listando usos atuais e recomendados do bucket.

### Fora do slice

- novas features de upload

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
| Handoff de storage | `.agents/state/handoffs/TASK-160.md` | reaproveitar decisão do bucket atual | sim |
| API/storage | `contracts/openapi.yaml` | confirmar endpoints com arquivo | sim |
| Backend | `backend/src/modules/contents/**` | confirmar mídia em bucket | sim |
| Backend | `backend/src/modules/reports/**` e `backend/src/modules/admin/**` | separar exports/relatórios de bucket | sim |
| Domínio | `backend/src/modules/users/**`, `guardians/**`, `professionals/**` | confirmar ausência de avatar/anexos | sim |
| Mobile | `mobile/src/features/shell/components/HomeHeader/**` | confirmar avatar visual sem upload | nao |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a leitura a entidades, services e paths de contrato com potencial real de arquivo

## Criterios de conclusao

- backlog atualizado com a nova task
- documento criado na raiz
- documento diferencia estado atual e recomendação futura

## Instrucoes de implementacao

- usar linguagem objetiva
- incluir convenção de pastas alinhada ao prefixo por ambiente já adotado

## Validacao esperada

- revisão manual do conteúdo
- busca por termos de upload/anexo/avatar para sustentar o inventário

## Entregaveis esperados

- `STORAGE_BUCKET_MAP.md`

## Riscos ou ambiguidades

- requisitos futuros podem introduzir novos tipos de arquivo; o documento deve ser tratado como fotografia do código atual

## Resultado da execucao

### Resumo por stack

- **backend**: confirmado que apenas mídias de conteúdos `audio` e `video` usam storage/bucket hoje; relatórios e exports seguem fora do bucket.
- **front-end**: confirmado que a web consome downloads de relatórios/exportações, mas não possui upload de avatar ou anexos.
- **mobile**: confirmado que o avatar atual é apenas visual por iniciais, sem imagem persistida.

### Relação com o slice

- Slice 006 foi reaberto apenas para documentar o uso operacional do storage já implantado, sem alterar comportamento.

### Decisões técnicas

- O documento raiz distingue evidência confirmada de recomendação futura.
- O padrão recomendado preserva a convenção `prefixo/entidade/id/original/...` já adotada em conteúdos.
- Relatórios e exports foram marcados explicitamente como candidatos futuros, não como uso atual do bucket.

### Trade-offs

- O inventário cobre o estado atual do repositório em 2026-07-24.
- Novas features de arquivos exigirão atualização manual do documento.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-160.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | arquivos na API | confirmar upload e downloads |
| `backend/src/modules/contents/**` | storage atual | confirmar mídia em bucket |
| `backend/src/modules/reports/**` | relatórios | confirmar persistência no banco |
| `backend/src/modules/admin/**` | exports | confirmar geração em memória/stream |
| `backend/src/modules/users/**`, `guardians/**`, `professionals/**` | perfis | confirmar ausência de avatar |
| `mobile/src/features/shell/components/HomeHeader/**` | avatar mobile | confirmar iniciais sem upload |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-161.md`
- Próximo contexto recomendado: qualquer futura task de avatar, anexos clínicos ou migração de relatórios para storage

## Arquivos alterados

### Documentação

- `STORAGE_BUCKET_MAP.md`

### Governança

- `tasks/change-requests/161-mapa-de-uso-do-bucket-no-projeto.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-161.md`

## Validacoes executadas

- busca dirigida por `upload`, `media`, `avatar`, `attachment`, `anexo`, `pdf`, `csv` — ok
- revisão manual de entidades, services e contrato relevantes — ok

## Aderencia ao design system

- nao se aplica (sem UI)

## Pendencias pos-task

- atualizar este inventário quando avatar, anexos clínicos ou arquivos de relatórios passarem a existir

## Status final

done
