# Task 156 - API de jogos terapeuticos e conteudos jogaveis

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

- `contracts/openapi.yaml#/paths` contents/trails/progress

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

O catalogo atual aceita apenas audio e video e nao representa atividades interativas.

### O que

Expandir o dominio de conteudos para suportar jogos terapeuticos e permitir que esses itens sejam usados com seguranca nas trilhas.

### Comportamento esperado

- Master cria/edita/inativa conteudo jogavel
- Profissional continua apenas leitura no catalogo
- Trilhas aceitam conteudo jogavel como item atribuivel
- Leitura mobile recebe metadados suficientes para abrir o jogo correto

### Fora de escopo

- UI web
- Execucao do jogo
- Motor generico de jogos

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master escreve; profissional e responsavel consomem conforme fluxo atual
- Casos de erro: tipo de jogo invalido; manifest ausente; jogo inativo em trilha
- Decisoes humanas confirmadas: primeiro jogo = alfabeto; sem gamificacao; sem login infantil
- Casos de borda: trilha com item legado audio/video + item jogavel

## Especificacao tecnica

### Deve

- manter compatibilidade com audio/video ja publicados
- explicitar no contrato quando um conteudo e `game`
- permitir um manifest/configuracao minima por jogo

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao quebrar leitura atual de trilhas no mobile
- nao criar endpoints paralelos sem necessidade se a extensao do dominio atual for suficiente

## Entradas

- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/`

## Dependencias

- Task 014
- Task 018
- Task 020

## Slice vertical

### Identificador do slice

Slice 026 - Jogos terapeuticos

### Arquivo do slice

- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

### Objetivo de negócio

Modelagem backend e contrato para conteudos jogaveis.

### Entrega verificável do slice

API pronta para cadastrar e distribuir o jogo do alfabeto.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Regras de negocio | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | fluxo de envio e execução | sim |
| API | `contracts/openapi.yaml` | modelagem contents/trails/progress | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | implementação backend | sim |

## Orçamento de contexto

- Risco medio
- Estrategia de reducao: limitar leitura aos paths de `contents`, `trails` e `progress`, sem recarregar slices não envolvidos

## Criterios de conclusao

- Conteudo jogavel documentado no contrato
- Backend persiste tipo/configuracao do jogo
- Trilhas e leitura mobile expõem metadados suficientes para abrir o alfabeto
- Testes cobrindo compatibilidade com audio/video legados

## Instrucoes de implementacao

- Preferir extensao do modulo `contents` antes de criar um modulo novo
- Registrar claramente a suposicao de que a execução do paciente ocorre no app do responsavel

## Validacao esperada

- `npm run lint`
- `npm run test`

## Entregaveis esperados

- dominio/DTOs/entidades para conteudo jogavel
- contrato OpenAPI atualizado
- testes do backend

## Riscos ou ambiguidades

- decidir entre TTS em runtime ou manifest de audios por letra pode impactar o shape final do config do jogo

## Resultado da execucao

### Resumo por stack

- **backend**: `contents` passou a suportar `mediaType=game`, `gameType=alphabet` e `gameConfig` persistido em `jsonb`, com validacao de payload, bloqueio de upload de midia para jogo e compatibilidade mantida para audio/video.

### Relação com o slice

- Slice 026 aberto com a primeira camada concluída: modelagem e contrato para conteúdo jogável já suportam o jogo do alfabeto e seu uso em trilhas.

### Decisões técnicas

- Extensão mínima do domínio existente de `contents`, sem criar módulo novo.
- `gameType` inicial restrito a `alphabet`.
- `gameConfig` mínimo do alfabeto: `letters`, `locale`, `voiceMode`.
- Trilhas continuam referenciando `contentId`; os metadados do jogo passam a sair em `GET /contents`.
- `POST /contents/{id}/media` agora rejeita conteúdos `game`.

### Trade-offs

- Sem endpoint novo de execução; o app continuará resolvendo o renderer via catálogo.
- Sem modelagem genérica de engine de jogos nesta fase; apenas discriminador suficiente para o primeiro jogo.

### Contrato

- `contracts/openapi.yaml`: `ContentMediaType` inclui `game`; `Content` e requests de criação/edição incluem `gameType` e `gameConfig`.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-020.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | regras do fluxo | confirmar master/profissional/responsavel e trilha |
| `contracts/openapi.yaml` | contrato | estender `contents` sem novo endpoint |
| `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/SECURITY.md` | implementação backend | validar extensão de módulo, DTOs e migration |

### Contexto evitado

- `design-system/front/` e `design-system/mobile/` ficaram fora desta task por não haver UI
- docs de stacks web/mobile não foram carregadas

## Handoff

- Caminho: `.agents/state/handoffs/TASK-156.md`
- Próximo contexto recomendado: `Task 157` + `contracts/openapi.yaml` (`contents/trails`) + `front-end` docs/ai

## Arquivos alterados

### Backend

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.repository.ts`
- `backend/src/modules/contents/contents.typeorm.repository.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/src/modules/contents/dto/create-content.dto.ts`
- `backend/src/modules/contents/dto/update-content.dto.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `backend/src/modules/trails/trails.service.spec.ts`
- `backend/src/database/migrations/1780000000000-AddGameFieldsToContents.ts`

### Contrato e governança

- `contracts/openapi.yaml`
- `tasks/change-requests/156-api-jogos-terapeuticos-e-conteudos-jogaveis.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-156.md`

## Validacoes executadas

- `cd backend && npm run lint` — ok
- `cd backend && npm run test` — ok (16 suites / 62 tests)

## Aderencia ao design system

- nao se aplica (sem UI)

## Pendencias pos-task

- Task 157 — adaptar biblioteca e planejamentos web para `mediaType=game`
- Task 158 — abrir renderer mobile do jogo `alphabet`
- Decisao de execução do áudio permanece aberta entre TTS do dispositivo e fallback gravado no app

## Status final

done
