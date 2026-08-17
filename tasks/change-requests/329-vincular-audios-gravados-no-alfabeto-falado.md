# Task 329 - Vincular audios gravados no alfabeto falado

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

- `nao se aplica`

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

- O comportamento do jogo deve permanecer igual na UI, mudando apenas a origem do áudio quando existir arquivo gravado para a letra.

## Contexto de negocio

### Por que

O catálogo já possui a atividade `Alfabeto falado`, mas agora algumas letras têm áudio gravado e devem usar esse material em vez de depender sempre da voz sintética.

### O que

Subir os arquivos da pasta `audios-atividades/` para o bucket, vincular as URLs na configuração do jogo `Alfabeto falado` e fazer web/mobile tocarem o áudio gravado por letra quando ele existir.

### Comportamento esperado

- letras com áudio gravado tocam o arquivo correspondente
- letras sem áudio gravado continuam usando o comportamento atual
- a atividade `Alfabeto falado` existente é atualizada sem perder capa nem imagens

### Fora de escopo

- gravação de novos áudios pela interface
- edição manual de áudio por letra na biblioteca
- mudanças nos outros jogos

## Dependencias

- Task 156
- Task 157
- Task 159
- Task 160
- Task 324
- Task 327

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-327.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Bucket real | `backend/.env.local`, `backend/scripts/` | subir os áudios para o storage configurado | sim |
| Config do jogo | `backend/src/modules/contents/` | estender e persistir mapa de áudio por letra | sim |
| Preview web | `front-end/src/pages/Main/Library/` | tocar áudio gravado no preview do alfabeto | sim |
| Renderer mobile | `mobile/src/features/games/` | tocar áudio gravado no jogo real e manter fallback | sim |

## Orçamento de contexto

- Risco médio
- Estratégia de redução: limitar a mudança ao jogo `alphabet`, reaproveitando o `gameConfig` existente e criando script dedicado para upload e vínculo

## Criterios de conclusao

- áudios da pasta local sobem para o bucket configurado
- `Alfabeto falado` recebe mapa de URLs por letra no `gameConfig`
- preview web toca áudio gravado quando existir
- renderer mobile toca áudio gravado quando existir
- letras sem arquivo continuam em TTS

## Validacao esperada

- `cd backend && npm run test -- contents.service.spec.ts`
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx`
- `cd mobile && npm test -- --runInBand src/features/games/services/gameSpeechService.test.ts src/features/games/components/AlphabetGameRenderer/index.test.tsx src/features/games/utils/alphabetGame.test.ts`
- `cd backend && npm run upload:alphabet-letter-audios`

## Resultado da execucao

### Resumo por stack

- **backend**: o `AlphabetGameConfig` passou a aceitar `letterAudioUrls`, o bootstrap preserva esse mapa quando o conteúdo já existe e foi criado um script dedicado para subir os `.mp4` e atualizar o jogo `Alfabeto falado` no banco.
- **front-end**: a prévia web do `Alfabeto falado` passou a tocar o áudio gravado da letra quando houver URL configurada, com fallback automático para a voz do navegador.
- **mobile**: o renderer real do jogo passou a tocar o áudio remoto por letra via `expo-audio`, mantendo fallback para TTS nas letras sem arquivo ou em falha de playback.

### Relação com o slice

- O Slice 006 passa a usar assets de áudio reais por letra no jogo de alfabeto, sem quebrar a experiência atual das letras ainda não gravadas.

### Decisões técnicas

- o novo mapa foi adicionado como `letterAudioUrls` dentro do `gameConfig` do jogo `alphabet`
- o `voiceMode` do conteúdo foi atualizado para `recorded`
- o fallback permanece por letra, e não por jogo inteiro
- o script de upload tratou também o arquivo `audio_letro_o.mp4`, vinculando corretamente à letra `O`

### Upload executado

- bucket/key prefix efetivo: `dev/games/alphabet/audio/`
- letras vinculadas com áudio gravado: `A`, `E`, `I`, `O`, `U`
- conteúdo atualizado: `1f34a5ec-b02f-4cd2-aacb-3eaac0074ed0`

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-327.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `backend/.env.local`, `backend/.env` | execução real | storage e banco |
| `backend/scripts/` | upload real | script dedicado de upload + vínculo |
| `backend/src/modules/contents/` | domínio do jogo | validação, bootstrap e tipos |
| `front-end/src/pages/Main/Library/` | preview web | playback gravado com fallback |
| `mobile/src/features/games/` | jogo real | playback gravado com fallback |

### Contexto evitado

- outras áreas do catálogo não relacionadas ao jogo `alphabet`

## Handoff

- Caminho: `.agents/state/handoffs/TASK-329.md`
- Próximo contexto recomendado: reutilizar esta task se novas letras gravadas precisarem ser subidas ou se o produto quiser editar esse mapa pela interface.

## Arquivos alterados

### Backend

- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents.service.spec.ts`
- `backend/scripts/upload-alphabet-letter-audios.mjs`
- `backend/package.json`

### Front-end

- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/pages/Main/Library/libraryGameSpeech.ts`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`

### Mobile

- `mobile/package.json`
- `mobile/package-lock.json`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/alphabetGame.ts`
- `mobile/src/features/games/utils/alphabetGame.test.ts`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetGameRenderer/index.test.tsx`

### Governança

- `tasks/change-requests/329-vincular-audios-gravados-no-alfabeto-falado.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-329.md`

## Validacoes executadas

- `cd backend && npm run test -- contents.service.spec.ts` — ok em **quarta-feira, 29 de julho de 2026**
- `cd front-end && npx vitest run src/pages/Main/Library/index.test.tsx` — ok em **quarta-feira, 29 de julho de 2026**
- `cd mobile && npm test -- --runInBand src/features/games/services/gameSpeechService.test.ts src/features/games/components/AlphabetGameRenderer/index.test.tsx src/features/games/utils/alphabetGame.test.ts` — ok em **quarta-feira, 29 de julho de 2026**
- `cd backend && npm run upload:alphabet-letter-audios` — ok em **quarta-feira, 29 de julho de 2026**

## Pendencias pos-task

- novas letras gravadas podem ser adicionadas reaproveitando o mesmo script
- edição manual de `letterAudioUrls` pela biblioteca continua fora do escopo

## Status final

done
