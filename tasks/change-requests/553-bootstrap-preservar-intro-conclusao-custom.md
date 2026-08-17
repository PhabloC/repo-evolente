# Task 553 - Bootstrap: preservar intro/conclusão personalizados

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora de escopo)

## Referencia de design system

### Stack de referencia visual

nao se aplica

## Origem da solicitacao

Code review em `ajustes_backend.md` item 3: com URL pública do storage, `attachGameSessionAudioUrls` prefere o URL gerado e sobrescreve intro/conclusão personalizados.

## Objetivo

Usar o áudio persistido quando não vazio; URL gerado só como fallback (`preferNonEmpty`).

## Escopo

- `attachGameSessionAudioUrls` (intro/finish)
- Mesma precedência em `attachSharedFeedbackAudioUrls` (mesmo anti-padrão no arquivo)
- Teste de regressão

## Fora de escopo

- UI de upload de áudio
- Mobile/web runtime

## Slice vertical

### Identificador do slice

Slice 048 - Narração intro/conclusão dos jogos

### Arquivo do slice

- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

### Objetivo de negocio

Áudios de intro/conclusão no catálogo sem wipe no bootstrap.

### Entrega verificavel do slice

URL customizado de intro/finish sobrevive ao bootstrap quando o storage público está configurado.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 048

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Implementação | `game-session-audio-assets.ts` | precedência | sim |
| Merge | `catalog-config-merge.ts` | `preferNonEmpty` | sim |

## Orçamento de contexto

- baixo; um arquivo + teste

## Dependencias

- Task 538, Task 488 (done)

## Criterios de conclusao

- `current.introAudioUrl` não vazio vence o URL gerado
- Ausente/vazio cai no URL gerado
- Feedbacks curtos seguem a mesma precedência

## Instrucoes de implementacao

- Inverter `built ?? current` para `preferNonEmpty(current, built)`
- Idem `fromCurrent || fromBuilt` nos feedbacks

## Validacao esperada

- Jest
- Lint

## Entregaveis esperados

- Assets + teste + handoff

## Resultado da execucao

- `attachGameSessionAudioUrls` usa `preferNonEmpty(current, built)` em intro/finish
- `attachSharedFeedbackAudioUrls` usa `fromCurrent || fromBuilt` (mesmo anti-padrão no arquivo)
- Teste: custom vence URL gerado; vazio cai no gerado; praise custom + retry gerado
- Slice 048 permanece done

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 048

### Contexto sob demanda carregado

- `game-session-audio-assets.ts` — precedência
- `catalog-config-merge.ts` — `preferNonEmpty`
- `game-session-audio-assets.spec.ts` — regressão

### Contexto não carregado

- UI de upload, runtime mobile/web — só bootstrap

## Handoff

- `.agents/state/handoffs/TASK-553.md`
- Próximo contexto: smoke bootstrap com `publicBaseUrl` e intro custom persistido

## Arquivos alterados

- `backend/src/modules/contents/game-session-audio-assets.ts`
- `backend/src/modules/contents/game-session-audio-assets.spec.ts`
- `tasks/change-requests/553-bootstrap-preservar-intro-conclusao-custom.md`
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest `game-session-audio-assets.spec.ts`: PASS
- eslint do arquivo e spec: 0 erros

## Pendencias pos-task

- Smoke: bootstrap com storage público configurado não deve sobrescrever intro/finish editados no admin

## Status final

done
