# Task 165 - Bootstrap do primeiro jogo e card na biblioteca

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` contents

## Modo de execucao

cross-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- A biblioteca deve manter tabela/filtros e ganhar uma apresentação visual simples para jogos, sem criar fluxo paralelo.

## Contexto de negocio

### Por que

Agora que a criação saiu da UI, o primeiro jogo precisa existir automaticamente no catálogo para que o master e o profissional possam vê-lo e usá-lo.

### O que

Criar por código o primeiro jogo do alfabeto no catálogo e exibi-lo como card na biblioteca, sob a categoria visual “Conheça o alfabeto”.

### Comportamento esperado

- O jogo “Alfabeto falado” existe no catálogo sem uso da UI de criação
- A biblioteca mostra uma seção/categoria “Conheça o alfabeto”
- Dentro dessa seção, o jogo aparece como card com identificação visual simples e nome abaixo
- O restante da biblioteca continua funcionando

### Fora de escopo

- Imagens reais por letra
- Novos jogos
- Mudanças na execução mobile
- Mudanças na trilha além do conteúdo já disponível

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master gerencia; profissional só consome; responsavel executa no mobile
- Casos de erro: duplicação do conteúdo; catálogo vazio; card não renderizar
- Decisoes humanas confirmadas: primeiro jogo, criação em código, categoria visual “Conheça o alfabeto”
- Casos de borda: placeholder sem imagem por letra; item inativo; reinício idempotente do backend

## Especificacao tecnica

### Deve

- garantir bootstrap idempotente do primeiro jogo no backend
- manter o conteúdo modelado como `mediaType=game` e `gameType=alphabet`
- mostrar card do jogo na biblioteca com nome abaixo
- usar placeholder textual simples enquanto não houver imagens por letra

### Nao deve

- nao reabrir fluxo de criação por UI
- nao quebrar a tabela/listagem atual
- nao alterar o contrato além do necessário

## Entradas

- `proposta.md`
- `design-system/front/Design_System_Evolente_Desktop.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/`
- `front-end/docs/ai/`

## Dependencias

- Task 156
- Task 157
- Task 164

## Slice vertical

### Identificador do slice

Slice 029 - Catalogo inicial de jogos terapeuticos

### Arquivo do slice

- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

### Objetivo de negócio

Disponibilizar o primeiro jogo jogável no catálogo e torná-lo visível de forma clara na biblioteca.

### Entrega verificável do slice

O jogo do alfabeto aparece automaticamente no catálogo e na biblioteca web com card e nome.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API | `contracts/openapi.yaml` | shape de `contents` | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | biblioteca/card | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | bootstrap do catálogo | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md e ACCESSIBILITY.md` | biblioteca web | sim |

## Orçamento de contexto

- Risco medio
- Estrategia de reducao: limitar o trabalho ao módulo de conteúdos no backend e à rota `/biblioteca` no front-end

## Criterios de conclusao

- Primeiro jogo disponível automaticamente no catálogo
- Biblioteca mostra categoria “Conheça o alfabeto”
- Card do jogo aparece com nome abaixo
- Validações backend e front-end executadas

## Instrucoes de implementacao

- Preferir bootstrap idempotente dentro do backend em vez de depender de ação manual pela UI
- Enquanto não houver imagens por letra, usar placeholder textual claro no card

## Validacao esperada

- `cd backend && npm run lint`
- `cd backend && npm run test`
- `cd front-end && npm run lint`
- `cd front-end && npm run build`
- `cd front-end && npm run test`

## Entregaveis esperados

- bootstrap do primeiro jogo no backend
- card do jogo na biblioteca web
- testes ajustados por stack

## Riscos ou ambiguidades

- a categoria “Conheça o alfabeto” será tratada como categoria visual da biblioteca, preservando por enquanto a categoria terapêutica existente no contrato

## Resultado da execucao

### Resumo por stack

- **backend**: o catálogo agora garante por código a existência do primeiro jogo `alphabet`, com bootstrap idempotente no módulo de conteúdos.
- **front-end**: a biblioteca ganhou uma seção visual “Conheça o alfabeto” com card do jogo e nome abaixo, mantendo a tabela operacional existente.

### Relação com o slice

- Slice 029 foi concluído: o primeiro jogo passou a existir automaticamente no catálogo e a biblioteca web agora o apresenta como card identificável.

### Decisões técnicas

- Criação de `ContentsCatalogBootstrapService` no backend para criar o jogo do alfabeto apenas quando ele ainda não existir.
- O bootstrap não sobrescreve edição nem status já definidos pelo master após a criação inicial.
- O conteúdo continua usando `category='linguagem'` no contrato atual.
- A categoria “Conheça o alfabeto” foi implementada como categoria visual da biblioteca, sem reabrir o contrato.
- A biblioteca continua com tabela/filtros e ganhou uma seção adicional de cards para jogos.

### Trade-offs

- A apresentação visual de “Conheça o alfabeto” vive apenas na UI web por enquanto; ela não virou novo campo persistido no backend.
- O placeholder do card usa letras simples (`A B C`) até a chegada das imagens reais por letra.

### Contrato

- Sem alterações no `contracts/openapi.yaml`; o conteúdo do jogo continua modelado como `mediaType=game`, `gameType=alphabet` e `gameConfig`.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `.agents/state/handoffs/TASK-164.md`
- `.agents/state/handoffs/TASK-163.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `proposta.md` | definição do jogo | confirmar comportamento base do alfabeto |
| `contracts/openapi.yaml` | API | validar que o conteúdo existente suportava o jogo sem novo campo |
| `backend/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md` | backend | bootstrap do catálogo |
| `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | front-end | seção de cards na biblioteca |
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | manter linguagem visual da biblioteca |

### Contexto evitado

- `design-system/mobile/` e `mobile/docs/ai/` não foram carregados porque a execução mobile do jogo já estava entregue.

## Handoff

- Caminho: `.agents/state/handoffs/TASK-165.md`
- Próximo contexto recomendado: reusar a task 165 e a feature de games mobile se a próxima etapa adicionar imagens por letra ou novos jogos.

## Arquivos alterados

### Backend

- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.module.ts`

### Front-end

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/libraryGames.ts`

### Governança

- `tasks/change-requests/165-bootstrap-do-primeiro-jogo-e-card-na-biblioteca.md`
- `tasks/slices/029-catalogo-inicial-jogos-terapeuticos.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-165.md`

## Validacoes executadas

- `cd backend && npm run lint` — ok
- `cd backend && npm run test` — ok (`18 suites`, `68 tests`)
- `cd front-end && npm run lint` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok

## Aderencia ao design system

- A biblioteca manteve filtros no topo, tabela/lista limpa e ações no fim.
- A nova seção de jogos usa card simples, cantos arredondados e visual acolhedor sem criar fluxo paralelo.

## Acessibilidade aplicada

- A seção “Conheça o alfabeto” usa heading próprio e estrutura semântica de `section`.
- O card clicável do master foi implementado como `button` com nome acessível.
- No modo read-only, o profissional recebe card não interativo com identificação textual.

## Pendencias pos-task

- Imagens reais por letra ainda não foram adicionadas; o card usa placeholder textual.
- Se o produto quiser persistir “Conheça o alfabeto” como categoria de domínio, isso exigirá nova task e possível extensão de contrato.

## Status final

done
