# Task 158 - Execucao mobile do jogo alfabeto falado

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

- `contracts/openapi.yaml#/paths` trails/progress/contents

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

- Atividade do dia no app atual, sem gamificacao e sem exigir uma area infantil separada.

## Contexto de negocio

### Por que

Sem uma superfície de execução no app, o profissional até consegue enviar o jogo, mas o paciente não consegue usá-lo.

### O que

Implementar a abertura e a execução do jogo "Alfabeto falado" dentro do fluxo mobile atual do responsavel.

### Comportamento esperado

- Responsavel abre a atividade interativa a partir da trilha
- Tela mostra letras do alfabeto
- Toque em cada letra reproduz a fala correspondente
- Conclusao da atividade continua registrando progresso no fluxo atual

### Fora de escopo

- Novos minigames alem do alfabeto
- Gamificacao
- Perfil/login infantil
- Gravar estatistica detalhada por letra

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: responsavel executa, sem edição
- Casos de erro: recurso de voz indisponivel; atividade sem config valida
- Decisoes humanas confirmadas: jogo inicial = alfabeto; sem gamificacao; fluxo no app atual
- Casos de borda: dispositivo sem voz PT-BR; trilha mista com audio/video/jogo

## Especificacao tecnica

### Deve

- preservar o fluxo atual de trilha
- abrir renderer específico para `alphabet`
- manter fallback simples se a voz do dispositivo não estiver disponível

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao reescrever a feature inteira de trilha
- nao introduzir pontuacao, medalhas ou ranking

## Entradas

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/`
- `contracts/openapi.yaml`
- `requirements/001-escopo-produto.md`

## Dependencias

- Task 156
- Task 020

## Slice vertical

### Identificador do slice

Slice 026 - Jogos terapeuticos

### Arquivo do slice

- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

### Objetivo de negócio

Execução do primeiro jogo terapêutico no app.

### Entrega verificável do slice

Responsavel consegue abrir e usar o alfabeto falado.

### Fora do slice

- Web

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
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | fluxo da atividade interativa | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | implementação mobile | sim |
| API | `contracts/openapi.yaml` | leitura da trilha e conclusão | sim |
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | validar atores e execução | sim |

## Orçamento de contexto

- Risco medio
- Estrategia de reducao: limitar a mudança à feature de trilha e ao renderer do jogo do alfabeto, sem reabrir home, perfil ou notificações

## Criterios de conclusao

- Atividade `alphabet` abre no app
- Toque nas letras aciona a fala
- Conclusao continua registrando progresso
- Testes mobile cobrindo adaptação/renderer básico

## Instrucoes de implementacao

- Preferir TTS do dispositivo se a stack já suportar sem nova dependência; se isso não for viável, registrar bloqueio técnico ou fallback permitido na task
- Manter a mesma linguagem visual serena da trilha atual

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Entregaveis esperados

- renderer mobile do jogo alfabeto
- integração com a trilha existente
- testes da stack mobile

## Riscos ou ambiguidades

- Expo atual não traz engine de fala instalada; a task pode exigir fallback técnico ou autorização para dependência de TTS

## Resultado da execucao

### Resumo por stack

- **mobile**: a trilha do responsavel agora reconhece conteúdos `game/alphabet`, abre um renderer próprio com grade de letras e usa TTS do dispositivo via `expo-speech`, com fallback textual quando a voz ou a config não estiverem disponíveis.

### Relação com o slice

- Slice 026 foi concluído na camada mobile: o jogo do alfabeto já pode ser cadastrado, distribuído e executado no fluxo atual da trilha.

### Decisões técnicas

- Reuso da `TrailActivityScreen` com switch por `mediaType`, preservando o fluxo de áudio e vídeo.
- Introdução do componente `AlphabetGameRenderer` apenas para `gameType=alphabet`.
- Encapsulamento do TTS em `trailSpeechService`, evitando acoplamento direto da tela ao SDK do Expo.
- Fallback para voz padrão do dispositivo quando a locale específica não estiver disponível.
- Fallback textual para `voiceMode=recorded` e para configs inválidas, sem bloquear a conclusão da atividade.

### Trade-offs

- O jogo não tenta persistir telemetria por letra, porque isso está fora do escopo do slice.
- O app aceita `voiceMode=recorded`, mas nesta fase só entrega fallback guiado por texto, já que não existe pipeline de áudio gravado para jogos.

### Contrato

- Consumo adaptado ao contrato já estendido na Task 156 (`mediaType=game`, `gameType`, `gameConfig` com `letters`, `locale` e `voiceMode`).

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-157.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | manter atividade serena, toque claro e feedback imediato |
| `mobile/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | implementação mobile | organizar renderer, tipos e service |
| `contracts/openapi.yaml` | API | refletir `mediaType=game`, `gameType` e `gameConfig` |
| `requirements/001-escopo-produto.md`, `002-regras-de-negocio.md` | regras | validar ator responsavel e continuidade do fluxo de evolução |

### Contexto evitado

- `design-system/front/` e `front-end/docs/ai/` não foram carregados porque a task é exclusivamente mobile.
- `mobile/docs/ai/ACCESSIBILITY.md` foi declarado na task, mas o arquivo não existe na stack; a execução seguiu com as diretrizes de acessibilidade do design system mobile e com os padrões compartilhados já usados no app.

## Handoff

- Caminho: `.agents/state/handoffs/TASK-158.md`
- Próximo contexto recomendado: nenhum obrigatório para o slice 026; próximas mudanças em jogos devem partir de novo change request.

## Arquivos alterados

### Mobile

- `mobile/package.json`
- `mobile/package-lock.json`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/trail/adapters/adaptDayTrail.ts`
- `mobile/src/features/trail/adapters/adaptDayTrail.test.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/features/trail/services/trailSpeechService.ts`
- `mobile/src/features/trail/utils/alphabetGame.ts`
- `mobile/src/features/trail/utils/alphabetGame.test.ts`
- `mobile/src/features/trail/components/AlphabetGameRenderer/index.tsx`
- `mobile/src/features/trail/components/AlphabetGameRenderer/styles.ts`
- `mobile/src/features/trail/components/AlphabetGameRenderer/index.test.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

### Governança

- `tasks/change-requests/158-execucao-mobile-do-jogo-alfabeto-falado.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-158.md`

## Validacoes executadas

- `cd mobile && npm run lint` — ok
- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm run test` — ok (`14 suites`, `36 tests`)

## Aderencia ao design system

- A atividade permaneceu no fluxo atual do responsavel, sem gamificação, com linguagem calma e feedback imediato por toque.
- A grade de letras usa alvos grandes, contraste alto e reforço visual simples, coerentes com o DS mobile.

## Acessibilidade aplicada

- Botões de letra com `accessibilityRole="button"` e `accessibilityLabel` por letra.
- Alvos de toque acima do mínimo recomendado.
- Feedback de fala em região viva (`accessibilityLiveRegion="polite"`).
- Fallback textual preservado quando a voz do dispositivo não está disponível.

## Pendencias pos-task

- Nenhuma bloqueante dentro do slice 026.
- Se o produto quiser `voiceMode=recorded` real no futuro, será preciso abrir nova task para modelar assets e distribuição de áudio por letra.
- A stack mobile continua sem `mobile/docs/ai/ACCESSIBILITY.md`; vale criar esse documento em task futura para alinhar a malha documental ao padrão do scaffold.

## Status final

done
