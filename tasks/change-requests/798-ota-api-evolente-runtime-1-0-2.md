# Task 798 - Publicar OTA da API nova no runtime 1.0.2

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

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 057 — `tasks/slices/057-configuracao-api-publica-mobile.md`

## Objetivo

Os OTAs 795–797 foram publicados só no runtime `1.0.3`. O Android da loja está em `1.0.2` e não recebe esse update. Publicar o mesmo apontamento `https://api.evolente.com.br/api` no runtime `1.0.2`.

## Fora de escopo

- Build de loja
- Mudar `expo.version` permanente

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 057

## Contexto sob demanda

- `mobile/app.json` `runtimeVersion`
- EAS production

## Orçamento de contexto

- Fontes obrigatórias: 6

## Criterios de aceite

- [x] OTA Android 1.0.2 publicado com `api.evolente.com.br`
- [x] `app.json` volta para `runtimeVersion.policy = appVersion`

## Resultado da execucao

- `runtimeVersion` temporário `1.0.2` só para o export
- OTA Android runtime `1.0.2`: `134b3cec-09d7-4361-83cb-8699b2622b63`
- `app.json` restaurado para `policy: appVersion`

## Contexto utilizado

- EAS production, `mobile/app.json`

## Handoff

- `.agents/state/handoffs/TASK-798.md`

## Arquivos alterados

- `tasks/change-requests/798-ota-api-evolente-runtime-1-0-2.md`
- `tasks/slices/057-configuracao-api-publica-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-798.md`

## Validacoes executadas

- `eas update` Android concluiu com Runtime version 1.0.2

## Pendencias pos-task

- Fechar o app Android duas vezes
- Task 799 altera o texto da versão no login; precisa de OTA extra

## Status final

done
