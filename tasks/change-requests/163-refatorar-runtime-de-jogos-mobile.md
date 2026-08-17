# Task 163 - Refatorar runtime de jogos mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` trails/contents/progress

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- O refactor não deve alterar a experiência visual ou o fluxo de atividade do responsável.

## Contexto de negocio

### Por que

Os próximos jogos seguirão o mesmo fluxo de catálogo → trilha → execução mobile, então o app precisa de uma camada dedicada de runtime para não acumular lógica de jogos dentro da feature de trilha.

### O que

Extrair o runtime do jogo do alfabeto para `features/games`, mantendo a trilha como ponto de entrada e conclusão.

### Comportamento esperado

- Atividade `game/alphabet` continua abrindo normalmente
- Áudio e vídeo continuam funcionando sem regressão
- Runtime do jogo fica isolado em feature própria, pronto para novos `gameType`

### Fora de escopo

- Criar novos jogos
- Alterar contrato
- Mudar biblioteca web ou planejamentos
- Adicionar telemetria, ranking ou gamificação

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: sem mudança; o refactor é interno ao mobile
- Casos de erro: jogo não suportado; config inválida; regressão em mídia existente
- Decisoes humanas confirmadas: jogo continua como conteúdo do catálogo; trilha continua como entrada
- Casos de borda: item `audio`/`video` misturado com `game`; renderer desconhecido

## Especificacao tecnica

### Deve

- criar uma feature dedicada `games` no mobile
- mover renderers e serviços de execução de jogo para essa feature
- manter a feature `trail` responsável apenas por carregar a atividade e concluir progresso
- preservar comportamento atual do jogo do alfabeto

### Nao deve

- nao alterar contrato backend/web
- nao espalhar abstrações genéricas sem uso real
- nao mexer no fluxo de auth, home, perfil ou notificações

## Entradas

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/`
- `contracts/openapi.yaml`

## Dependencias

- Task 158

## Slice vertical

### Identificador do slice

Slice 028 - Runtime de jogos mobile extensivel

### Arquivo do slice

- `tasks/slices/028-runtime-jogos-mobile-extensivel.md`

### Objetivo de negócio

Endurecer a base mobile para crescimento de jogos sem mudar o produto entregue.

### Entrega verificável do slice

O runtime do alfabeto é executado via `features/games` e a trilha fica desacoplada da implementação do jogo.

### Fora do slice

- Web e backend

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/028-runtime-jogos-mobile-extensivel.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | confirmar preservação visual | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | implementação mobile | sim |
| API | `contracts/openapi.yaml` | confirmar shape de jogo | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: restringir a mudança às features `trail` e `games`, sem reabrir outras áreas do app

## Criterios de conclusao

- Runtime do jogo extraído para `features/games`
- `TrailActivityScreen` sem lógica específica do alfabeto
- Testes atualizados e passando
- `audio`, `video` e `game/alphabet` continuam funcionando

## Instrucoes de implementacao

- Preferir extração incremental, sem reescrever comportamento já validado
- Introduzir apenas abstrações que já sejam usadas pelo alfabeto e pelo ponto de entrada da trilha

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Entregaveis esperados

- feature `games` no mobile
- trilha desacoplada do renderer do alfabeto
- testes ajustados

## Riscos ou ambiguidades

- a extração não deve degradar a clareza atual da tela nem reintroduzir dependência cruzada entre `trail` e `games`

## Resultado da execucao

### Resumo por stack

- **mobile**: o runtime do jogo do alfabeto foi extraído para a nova feature `games`, com renderer dedicado, utilitários e serviço de voz próprios; a trilha permaneceu responsável apenas por entrada da atividade e conclusão do progresso.

### Relação com o slice

- Slice 028 foi concluído: a base mobile agora está pronta para receber novos `gameType` sem acoplar a implementação de cada jogo à feature de trilha.

### Decisões técnicas

- Criação da feature `mobile/src/features/games/` com `components`, `renderers`, `services` e `utils`.
- Introdução de `GameActivityRenderer` como dispatcher por `gameType`.
- Extração de `AlphabetGameRenderer`, `gameSpeechService` e utilitários do alfabeto para a nova feature.
- `TrailActivityScreen` manteve apenas lógica genérica para mídia/jogo, hero e conclusão da atividade.
- Labels e copy específicas de jogo foram centralizadas em utilitário de metadata.

### Trade-offs

- O runtime de jogos ainda consome `TrailActivityItem` da feature `trail`, porque a trilha continua sendo a fronteira de entrada do conteúdo no app.
- A arquitetura foi endurecida só até o ponto já exercido pelo alfabeto; não foi criado um engine genérico prematuro.

### Contrato

- Sem alterações no `contracts/openapi.yaml`; o refactor preserva `mediaType=game`, `gameType` e `gameConfig` já consolidados.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/028-runtime-jogos-mobile-extensivel.md`
- `.agents/state/handoffs/TASK-158.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | preservar o fluxo visual da atividade |
| `mobile/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | implementação mobile | organizar a extração para feature dedicada |
| `contracts/openapi.yaml` | API | confirmar que o refactor não exigia mudança de contrato |

### Contexto evitado

- `design-system/front/`, `front-end/docs/ai/` e `backend/docs/ai/` não foram carregados porque o refactor é restrito ao mobile.
- `mobile/docs/ai/ACCESSIBILITY.md` segue ausente na stack; a execução manteve as regras já aplicadas pelo DS mobile e pelos componentes existentes.

## Handoff

- Caminho: `.agents/state/handoffs/TASK-163.md`
- Próximo contexto recomendado: reutilizar `features/games/` como base da próxima task de novo jogo mobile.

## Arquivos alterados

### Mobile

- `mobile/src/features/games/components/AlphabetGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetGameRenderer/styles.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.test.tsx`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/utils/alphabetGame.ts`
- `mobile/src/features/games/utils/alphabetGame.test.ts`
- `mobile/src/features/games/utils/gameMetadata.ts`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- remoção de arquivos equivalentes antes localizados em `mobile/src/features/trail/components`, `services` e `utils`

### Governança

- `tasks/change-requests/163-refatorar-runtime-de-jogos-mobile.md`
- `tasks/slices/028-runtime-jogos-mobile-extensivel.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-163.md`

## Validacoes executadas

- `cd mobile && npm run lint` — ok
- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm run test` — ok (`14 suites`, `36 tests`)

## Aderencia ao design system

- O refactor preservou a mesma experiência visual entregue na Task 158, sem alterar linguagem, fluxo ou densidade da atividade do responsável.

## Acessibilidade aplicada

- Os mesmos alvos, labels e feedbacks vivos do jogo do alfabeto foram preservados após a extração.
- O dispatcher de jogos não removeu nenhuma proteção já aplicada na UI anterior.

## Pendencias pos-task

- Nenhuma bloqueante para a base de jogos mobile.
- Se entrar novo `gameType`, o próximo passo natural é adicionar um novo renderer em `features/games/renderers` e seus serviços/utilitários específicos.
- A documentação `mobile/docs/ai/ACCESSIBILITY.md` continua pendente como lacuna da stack, fora deste escopo.

## Status final

done
