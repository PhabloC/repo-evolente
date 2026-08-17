# Task 552 - Bootstrap Descubra a palavra: mesclar palavras por ID

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Contrato

- nao se aplica (builder interno do catálogo)

## Modo de execucao

single-stack

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora de escopo)

## Referencia de design system

### Stack de referencia visual

nao se aplica

## Origem da solicitacao

Code review em `ajustes_backend.md` item 2: se a categoria existe, o bootstrap troca `words` pelo template e apaga palavras/ajustes do admin.

## Objetivo

Mesclar palavras por ID como fluency/jigsaw (Task 488): preservar valores atuais e só adicionar palavras ou URLs ausentes.

## Escopo

- `buildDefaultWordSpellGameConfig` em `word-spell-game-assets.ts`
- Teste de regressão no merge

## Fora de escopo

- UI da biblioteca
- Reupload S3

## Slice vertical

### Identificador do slice

Slice 043 - Complete a palavra (leitura e escrita)

### Arquivo do slice

- `tasks/slices/043-complete-a-palavra.md`

### Objetivo de negocio

Jogo Descubra a palavra no catálogo, sem wipe no bootstrap.

### Entrega verificavel do slice

Palavras e URLs editadas pelo admin sobrevivem à reinicialização.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 043

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Builder | `word-spell-game-assets.ts` | merge | sim |
| Padrão | `jigsaw-game-assets.ts` / Task 488 | mescla por ID | sim |
| Teste | `catalog-config-merge.spec.ts` | regressão | sim |

## Orçamento de contexto

- baixo; um builder + um teste

## Dependencias

- Task 488, Task 544 (done)

## Criterios de conclusao

- Categoria existente não substitui a lista inteira por `template.words`
- Palavra custom (ID novo) permanece
- Palavra do template ausente é acrescentada
- `imageUrl`/`audioUrl` vazios recebem fallback do template

## Instrucoes de implementacao

- Mapear palavras atuais; `preferNonEmpty` nos URLs; append das palavras do template sem ID correspondente
- Append de categorias do template que ainda não existem

## Validacao esperada

- Jest do merge
- Lint

## Entregaveis esperados

- Builder + teste + handoff

## Resultado da execucao

- `mergeWordSpellWords` mescla por ID: preserva palavra atual, `preferNonEmpty` em image/audio, append do template sem ID correspondente
- Categorias atuais permanecem; categorias do template ausentes são acrescentadas
- Teste: `pulga` custom + `palavra-admin` sobrevivem; lista cresce com o template
- Slice 043 permanece done

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 043

### Contexto sob demanda carregado

- `word-spell-game-assets.ts` — merge por ID
- `catalog-config-merge.ts` / padrão jigsaw (Task 488) — `preferNonEmpty`
- `catalog-config-merge.spec.ts` — regressão word-spell

### Contexto não carregado

- `contracts/openapi.yaml`, UI web/mobile — builder interno

## Handoff

- `.agents/state/handoffs/TASK-552.md`
- Próximo contexto: smoke bootstrap com catálogo já editado no admin

## Arquivos alterados

- `backend/src/modules/contents/word-spell-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/552-bootstrap-descubra-palavra-mesclar-por-id.md`
- `tasks/slices/043-complete-a-palavra.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest `catalog-config-merge.spec.ts` (filtro word-spell): PASS
- eslint `word-spell-game-assets.ts` e spec: 0 erros

## Pendencias pos-task

- Smoke: reiniciar backend com palavra admin extra em Descubra a palavra e confirmar que não some

## Status final

done
