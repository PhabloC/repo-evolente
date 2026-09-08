# Slice 058 - Área segura da tab bar mobile

## Objetivo de negócio

Garantir que os controles de navegação do app permaneçam acessíveis em aparelhos Android com barra de navegação do sistema.

## Entrega verificável

A tab bar respeita o inset inferior seguro e não se sobrepõe aos botões nativos de voltar, início e apps recentes.

## Fora de escopo

- Alterar rotas, itens ou comportamento da navegação.
- Redesenhar telas ou alterar a API.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/632-ajustar-area-segura-tab-bar-mobile.md`

## Contexto sob demanda

- `mobile/src/`: localizar a tab bar compartilhada e aplicar o inset inferior.
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`: preservar os tokens e a composição visual da navegação.
- `mobile/docs/ai/`: padrões de implementação e QA da stack móvel.

## Risco de contexto

Baixo: alteração localizada na navegação inferior compartilhada, sem API ou mudança de fluxo.

## Status

done
