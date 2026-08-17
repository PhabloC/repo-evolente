# Handoff - Task 553

## Task

- identificador: TASK-553
- título: Bootstrap: preservar intro/conclusão personalizados
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 048
- objetivo de negócio: áudios de intro/conclusão no catálogo sem wipe no bootstrap
- entrega verificável: URL customizado sobrevive ao bootstrap com storage público configurado

## Decisões preservadas

- decisão: `preferNonEmpty(current, built)` em intro/finish
- motivo: com `publicBaseUrl`, `built ?? current` fazia o URL gerado vencer sempre
- impacto: áudio persistido não vazio permanece; vazio cai no gerado

- decisão: mesma precedência em `attachSharedFeedbackAudioUrls` (`fromCurrent || fromBuilt`)
- motivo: o arquivo tinha o mesmo anti-padrão nos feedbacks; a CR ampliou o escopo só neste arquivo
- impacto: praise custom vence; retry vazio recebe o gerado

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 553, slice 048

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `game-session-audio-assets.ts` | precedência | intro/finish + feedbacks |
| `catalog-config-merge.ts` | helper | `preferNonEmpty` |
| `game-session-audio-assets.spec.ts` | regressão | custom vs gerado |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| runtime mobile/web | só bootstrap |

## Resultado por stack

- backend: precedência invertida no attach de áudio de sessão
- front-end / mobile: fora de escopo

## Arquivos alterados

- `backend/src/modules/contents/game-session-audio-assets.ts`
- `backend/src/modules/contents/game-session-audio-assets.spec.ts`

## Validações executadas

- validação: Jest `game-session-audio-assets.spec.ts` — PASS
- validação: eslint arquivo + spec — 0 erros

## Pendências ou bloqueios

- smoke bootstrap com `publicBaseUrl` e intro custom no admin

## Próxima ação sugerida

- validar no ambiente com storage; não reabrir UI nesta CR

## Próximo contexto recomendado

- `game-session-audio-assets.ts` `attachGameSessionAudioUrls`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `design-system/`
- motivo: sem UI
