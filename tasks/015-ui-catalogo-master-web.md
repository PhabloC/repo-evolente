# Task 015 - UI do catalogo de conteudos do master

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` contents

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- Biblioteca: tabelas/cards/filtros DS.

## Contexto de negocio

### Por que

Master opera catalogo.

### O que

CRUD visual com upload e filtros.

### Comportamento esperado

- Criar/editar/listar
- Upload
- Estados vazio/loading

### Fora de escopo

- Jogos

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master
- Casos de erro: upload falho
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: lista vazia

## Especificacao tecnica

### Deve

- Preferir inativar conteudo

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Profissional criar

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`

## Dependencias

- Task 014

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

### Objetivo de negócio

UI catalogo.

### Entrega verificável do slice

Biblioteca web.

### Fora do slice

- Mobile

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
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |
| API | `contracts/openapi.yaml` | API | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Master cria audio/video
- Profissional sem mutacao

## Instrucoes de implementacao

- Inativar em vez de hard delete

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- UI catalogo

## Riscos ou ambiguidades



## Resultado da execucao

### Resumo por stack

- **front-end**: `/biblioteca` com listagem, filtros, loading/vazio; master cria/edita/upload Base64/inativa; profissional somente leitura.

### Relação com o slice

- Slice 006 concluído (API 014 + UI 015).

### Decisões técnicas

- Consome API 014 (`list/create/update/upload` Base64).
- Mutação só se `role === 'master'`; profissional vê lista sem ações.
- Inativar/reativar via `status` (sem hard delete).
- Categorias reutilizam opções da pergunta 6.
- Nenhuma dependência nova.

### Trade-offs

- Sem prints: Card + Table + Modal + filtros no topo (DS documental).
- Upload Base64 conforme handoff 014.

### Contrato

- Paths `/contents` da Task 014.

### Referência visual

- DS Desktop: tabela/lista, filtros no topo, status pills, estados loading/vazio.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 006
- handoff `TASK-014.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | biblioteca/tabela/filtros |
| openapi contents | API | payloads |
| ARCHITECTURE/ACCESSIBILITY | front | estrutura + a11y |

### Evitado

- mobile / backend docs

## Handoff

- Caminho: `.agents/state/handoffs/TASK-015.md`
- Decisões: master muta; profissional read-only; inativar; Base64
- Próximo contexto: Task 016 (API pacientes)
- Pendências: multipart futuro; S3

## Arquivos alterados

### front-end

- `front-end/src/pages/Main/Library/**`
- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/services/contents/contentService.ts`
- `front-end/src/utils/fileToBase64.ts`
- `front-end/src/routes/index.tsx`

### governança

- `tasks/015-ui-catalogo-master-web.md`
- `tasks/000-index.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-015.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok (16 tests)
- `npm run build` — ok

## Qualidade estrutural

- Tipos em `types/content.ts`
- Service em `services/contents/`
- Utils `fileToBase64` em `utils/`
- Form modal separado da page

## Acessibilidade aplicada

- Filtros com labels; search region; status `role="status"`; erros `role="alert"`; `aria-busy` no form; modal dialog; tabela com headers

## Aderencia ao design system

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md`
- Evidências: Card, Table, filtros no topo, status pills, MainLayout
- Lacuna: sem prints de biblioteca

## Pendencias pos-task

- Multipart upload (quando autorizado)
- Provider S3
- Próximo slice pacientes (016)

## Status final

done
