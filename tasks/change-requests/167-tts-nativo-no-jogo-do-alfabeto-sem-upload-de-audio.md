# Task 167 - TTS nativo no jogo do alfabeto sem upload de audio

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

- A mudanca nao deve alterar o layout do jogo; apenas endurecer o comportamento de voz ao tocar nas letras.

## Contexto de negocio

### Por que

O jogo do alfabeto precisa falar as letras sem depender de upload manual de audio por letra no catalogo.

### O que

Usar a voz nativa do dispositivo como fallback operacional do jogo, inclusive quando a configuracao vier como `recorded`.

### Comportamento esperado

- Toque na letra continua acionando voz no mobile
- O jogo nao depende de audio gravado para funcionar
- Quando a voz do dispositivo estiver disponivel, o app fala a letra mesmo sem upload de audio

### Fora de escopo

- Novo contrato backend
- Novo jogo
- Mudancas visuais amplas na tela da atividade

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: sem mudanca; fluxo continua no app do responsavel
- Casos de erro: voz indisponivel no dispositivo; locale sem match exato; conteudo marcado como `recorded`
- Decisoes humanas confirmadas: evitar upload de audio e preferir voz do dispositivo
- Casos de borda: fallback para voz padrao e feedback amigavel quando a fala falhar

## Especificacao tecnica

### Deve

- usar TTS nativo do dispositivo ao tocar nas letras
- tratar `voiceMode=recorded` como fallback para TTS quando nao houver audio embarcado
- preservar a API atual do renderer do jogo
- cobrir o comportamento com testes

### Nao deve

- nao exigir upload de audio por letra
- nao alterar contrato
- nao acoplar Expo Speech diretamente na tela

## Entradas

- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `contracts/openapi.yaml`

## Dependencias

- Task 158
- Task 163

## Slice vertical

### Identificador do slice

Slice 028 - Runtime de jogos mobile extensivel

### Arquivo do slice

- `tasks/slices/028-runtime-jogos-mobile-extensivel.md`

### Objetivo de negócio

Endurecer a execucao mobile do jogo para nao depender de audio gravado.

### Entrega verificável do slice

O jogo do alfabeto segue falando as letras com TTS nativo mesmo sem upload de audio.

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
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | implementacao do runtime | sim |
| API | `contracts/openapi.yaml` | confirmar shape de `gameConfig` | sim |
| Handoff | `.agents/state/handoffs/TASK-158.md e TASK-163.md` | preservar decisoes do jogo e do runtime | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a mudanca a `features/games` no mobile, sem reabrir trilha, web ou backend

## Criterios de conclusao

- TTS nativo continua falando a letra no toque
- `voiceMode=recorded` nao bloqueia mais a voz do jogo
- testes do runtime mobile atualizados e passando

## Instrucoes de implementacao

- Preferir endurecimento localizado no service de fala
- Reaproveitar o feedback existente do renderer quando houver fallback

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test -- gameSpeechService AlphabetGameRenderer`

## Entregaveis esperados

- ajuste do service de fala do jogo
- testes cobrindo fallback de `recorded` para TTS

## Riscos ou ambiguidades

- alguns dispositivos podem nao ter a voz/localidade ideal; nesses casos o app deve cair para a voz padrao do sistema ou para feedback textual

## Resultado da execucao

### Resumo por stack

- **mobile**: o service do jogo do alfabeto passou a tentar TTS nativo mesmo quando o conteúdo vier marcado como `recorded`, eliminando a dependência de upload manual de áudio por letra.

### Relação com o slice

- Slice 028 foi endurecido sem reabrir web ou backend: o runtime mobile continua o mesmo visualmente, mas a fala agora é mais resiliente e operacional.

### Decisões técnicas

- remoção do bloqueio antecipado de `voiceMode=recorded` no `gameSpeechService`
- manutenção do mesmo renderer e do mesmo fluxo de toque por letra
- preservação do feedback atual do componente quando a voz usada é fallback do dispositivo
- adição de testes dedicados para fallback de `recorded` para TTS e fallback para voz padrão do sistema

### Contrato

- sem alterações em `contracts/openapi.yaml`; a mudança é apenas de comportamento interno do app ao consumir `gameConfig`

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/028-runtime-jogos-mobile-extensivel.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `.agents/state/handoffs/TASK-158.md` | continuidade do jogo | preservar a decisão original de usar `expo-speech` |
| `.agents/state/handoffs/TASK-163.md` | continuidade do runtime | manter a mudança isolada em `features/games` |
| `mobile/docs/ai/ARCHITECTURE.md` | implementação mobile | manter integração encapsulada em service |
| `mobile/docs/ai/CODE_STYLE.md` | implementação mobile | respeitar organização e testes da stack |
| `contracts/openapi.yaml` | contrato | confirmar que não há mudança de shape em `gameConfig` |

### Contexto evitado

- `design-system/front/`, `front-end/docs/ai/` e `backend/docs/ai/` não foram carregados porque a mudança é restrita ao mobile.
- `mobile/docs/ai/ACCESSIBILITY.md` segue ausente na stack; a alteração preservou labels e feedbacks existentes.

## Handoff

- Caminho: `.agents/state/handoffs/TASK-167.md`
- Próximo contexto recomendado: `mobile/src/features/games/services/gameSpeechService.ts` e `mobile/src/features/games/components/AlphabetGameRenderer/`

## Arquivos alterados

### Mobile

- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.test.tsx`

### Governança

- `tasks/change-requests/167-tts-nativo-no-jogo-do-alfabeto-sem-upload-de-audio.md`
- `tasks/slices/028-runtime-jogos-mobile-extensivel.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-167.md`

## Validacoes executadas

- `cd mobile && npm run lint` — ok
- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm run test -- gameSpeechService AlphabetGameRenderer` — ok

## Aderencia ao design system

- sem mudança visual; o comportamento de voz foi endurecido mantendo a experiência atual da atividade

## Acessibilidade aplicada

- preservados `accessibilityLabel` dos botões de letra e `accessibilityLiveRegion` do feedback
- a atividade continua oferecendo orientação textual quando a voz do dispositivo falha

## Pendencias pos-task

- se no futuro houver áudio gravado embarcado por letra, isso deve entrar como otimização opcional, não como requisito para a fala básica
- alguns dispositivos podem variar a qualidade ou o timbre da voz por depender da engine nativa instalada

## Status final

done
