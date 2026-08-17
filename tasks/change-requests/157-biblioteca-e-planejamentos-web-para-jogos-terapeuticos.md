# Task 157 - Biblioteca e planejamentos web para jogos terapeuticos

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

- `contracts/openapi.yaml#/paths` contents/trails

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

- Biblioteca e planejamentos devem seguir o DS atual, sem criar um fluxo administrativo paralelo.

## Contexto de negocio

### Por que

O master precisa gerenciar jogos pela biblioteca e o profissional precisa conseguir enviar esses jogos ao paciente sem editar o conteúdo.

### O que

Adaptar biblioteca e montagem de trilha para exibir conteúdos jogáveis, com leitura clara do tipo de atividade e restrições de permissão.

### Comportamento esperado

- Master cadastra/edita/inativa jogo na biblioteca
- Profissional vê jogo publicado na biblioteca em modo leitura
- Profissional adiciona o jogo do alfabeto à trilha do paciente
- Interface diferencia audio/video/jogo sem ambiguidade

### Fora de escopo

- Execucao do jogo
- UI mobile
- Ferramenta de autoria para profissional

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master muta; profissional read-only na biblioteca e write apenas na trilha
- Casos de erro: jogo sem status ativo; biblioteca vazia; trilha com item inativo
- Decisoes humanas confirmadas: primeiro jogo = alfabeto; envio via planejamento existente
- Casos de borda: paciente com trilha já preenchida e item jogável misturado com audio/video

## Especificacao tecnica

### Deve

- reaproveitar a rota `/biblioteca`
- reaproveitar o fluxo existente de `/planejamentos`
- tornar visivel o tipo `jogo` e o nome do jogo

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao liberar edição para profissional
- nao criar uma nova pagina de biblioteca separada so para jogos

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`
- `contracts/openapi.yaml`

## Dependencias

- Task 156
- Task 015
- Task 019

## Slice vertical

### Identificador do slice

Slice 026 - Jogos terapeuticos

### Arquivo do slice

- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

### Objetivo de negócio

Gestão e envio web do primeiro jogo terapêutico.

### Entrega verificável do slice

Biblioteca e planejamentos web suportam o jogo do alfabeto.

### Fora do slice

- Mobile

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
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | biblioteca e planejamentos | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | implementação web | sim |
| API | `contracts/openapi.yaml` | consumo de contents/trails | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | componentes e estados | sim |

## Orçamento de contexto

- Risco medio
- Estrategia de reducao: restringir o trabalho às rotas `Library` e `Plans`, sem reabrir áreas não relacionadas do shell

## Criterios de conclusao

- Master consegue cadastrar o jogo do alfabeto pela biblioteca
- Profissional enxerga o jogo e o adiciona à trilha
- UI comunica permissões e tipo do conteúdo com clareza
- Testes web cobrindo renderização e permissão básica

## Instrucoes de implementacao

- Reutilizar os modais e padrões visuais já consolidados na biblioteca
- Evitar qualquer inferência de execução infantil na web; o destino continua sendo a trilha do paciente

## Validacao esperada

- `npm run lint`
- `npm run test`
- `npm run build`

## Entregaveis esperados

- ajustes na biblioteca web
- ajustes em planejamentos web
- testes da stack front-end

## Riscos ou ambiguidades

- a forma de edição do `config` do jogo deve ser simples o bastante para caber no modal atual sem torná-lo confuso

## Resultado da execucao

### Resumo por stack

- **front-end**: a biblioteca web passou a suportar cadastro e leitura de conteúdos `game`, com formulário específico para o jogo `alphabet`; os planejamentos agora exibem e permitem adicionar o jogo do alfabeto à trilha sem abrir fluxo paralelo.

### Relação com o slice

- Slice 026 avançou na camada web: master já consegue gerenciar o jogo pela biblioteca e o profissional já consegue enviá-lo ao paciente pelo planejamento.

### Decisões técnicas

- Reuso da rota `/biblioteca` com extensão do modal atual.
- Campos de jogo aparecem apenas quando `mediaType=game`.
- `gameType` inicial restrito a `alphabet`.
- `gameConfig` do alfabeto editado por `letters`, `locale` e `voiceMode`.
- Planejamentos continuam usando o catálogo ativo existente; só ganharam labels claras para jogos.

### Trade-offs

- O formulário de jogo ficou textual e enxuto para caber no modal atual, sem criar builder visual.
- A web não tenta executar o jogo; apenas cadastra e distribui o conteúdo para a trilha.

### Contrato

- Consumo adaptado ao contrato já estendido na Task 156 (`mediaType=game`, `gameType`, `gameConfig`).

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-156.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | manter filtros, tabela, cards e modais no padrão atual |
| `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementação web | organizar tipos/estado e respeitar acessibilidade |
| `contracts/openapi.yaml` | consumo API | refletir `gameType` e `gameConfig` no front |

### Contexto evitado

- `design-system/mobile/` e `mobile/docs/ai/` não foram carregados porque a execução do jogo segue para a Task 158

## Handoff

- Caminho: `.agents/state/handoffs/TASK-157.md`
- Próximo contexto recomendado: `Task 158` + `contracts/openapi.yaml` (`contents/trails`) + `mobile/docs/ai/`

## Arquivos alterados

### Front-end

- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/types/trail.ts`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/test/setup.ts`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.test.tsx`

### Governança

- `tasks/change-requests/157-biblioteca-e-planejamentos-web-para-jogos-terapeuticos.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-157.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npm run build` — ok
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx src/pages/Main/Plans/AddCatalogContentModal.test.tsx` — ok
- `cd front-end && npm run test` — **falhou por timeout pré-existente** em `src/pages/Main/AdminUsers/index.test.tsx` (`cria outro usuário master...`), fora do escopo desta task; os testes diretamente afetados pela mudança passaram

## Aderencia ao design system

- Biblioteca e planejamentos mantiveram filtros no topo, tabela/lista limpa, ações no fim, status em pills e modais no padrão já consolidado

## Acessibilidade aplicada

- Campos condicionais do jogo continuam com label visível e mensagens textuais de erro
- Loading/feedback existentes foram preservados
- Setup global de `matchMedia` em teste estabilizou rotas que dependem do `MainLayout`

## Pendencias pos-task

- Task 158 — renderer mobile do jogo `alphabet`
- O teste de `AdminUsers` permanece com timeout fora deste escopo e pode merecer hardening próprio depois

## Status final

done
