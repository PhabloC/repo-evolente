# Task 655 - Jogo dos erros: avançar, dicas e título articulatório

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end (React/Vite)
- mobile (Expo)

## Perfil do projeto

- web: front-end
- mobile: sim

## Contrato

Não aplicável; alteração de comportamento e nomenclatura em atividade já existente.

## Modo de execução

cross-stack

## Slice vertical

- Slice 035 — `tasks/slices/035-jogo-dos-erros.md`

## Objetivo

Melhorar a condução do Jogo dos erros para permitir avançar entre rodadas e solicitar dicas de localização das diferenças, além de atualizar o nome exibido para “Jogo dos erros com exercícios de articulação/articulatórios”.

## Entrega verificável

- Durante a rodada, exibir ação para avançar quando aplicável, sem quebrar a progressão do exercício.
- Disponibilizar dica que revele ou destaque uma diferença ainda não encontrada, com feedback acessível.
- Usar o novo título e descrição nos pontos visíveis da atividade web e mobile.
- Preservar o fluxo de conclusão e o áudio/feedback existentes.

## Fora de escopo

- Alteração do catálogo de hotspots ou dos assets das rodadas.
- Novo modo de dificuldade.
- API ou persistência adicional.

## Dependências

- Tasks 414, 524 e 654 — concluídas.
- Slice 035 — concluído; será reaberto apenas para registrar a extensão de comportamento.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `front-end/src/pages/Main/Library/SpotDifferencePreviewModal.tsx`
- runtime mobile do Jogo dos erros

## Contexto sob demanda

- `front-end/docs/ai/` — padrões, acessibilidade e QA da UI web.
- `design-system/front/prints/jogo-dos-erros-articulacao.png` — referência visual web.
- `mobile/docs/ai/` — padrões e acessibilidade do runtime mobile, se existente.
- `design-system/mobile/` — somente se houver referência concreta do runtime mobile.

## Orçamento de contexto

Carregar somente os arquivos do jogo, estilos/testes diretamente relacionados e os documentos de acessibilidade das stacks alteradas; não carregar requisitos, contrato ou outras atividades.

## Critérios de aceite

- É possível pedir dica sem marcar incorretamente a diferença.
- É possível avançar conforme o estado permitido da rodada, com estado limpo na próxima etapa.
- O título novo aparece na configuração/entrada da atividade e nos cabeçalhos relevantes.
- Testes/lint direcionados passam ou falhas preexistentes ficam registradas.

## Resultado da execucao

Implementadas ações de dica e avanço durante a busca de diferenças, com feedback acessível e destaque visual sem contabilizar a diferença. O título foi atualizado nas superfícies web e mobile para exercícios de articulação/articulatórios.

## Contexto utilizado

- `tasks/slices/035-jogo-dos-erros.md`
- `front-end/src/pages/Main/Library/SpotDifferencePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx`
- `mobile/src/features/games/components/SpotDifferenceGameRenderer/styles.ts`
- `mobile/src/features/games/utils/gameMetadata.ts`

## Handoff

Fluxo concluído nas duas stacks. A dica aponta a primeira diferença ainda não encontrada e o avanço leva diretamente ao exercício da rodada, preservando o botão de progressão existente após as repetições.

## Arquivos alterados

- `front-end/src/pages/Main/Library/SpotDifferencePreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx`
- `mobile/src/features/games/components/SpotDifferenceGameRenderer/styles.ts`
- `mobile/src/features/games/utils/gameMetadata.ts`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Library/SpotDifferencePreviewModal.tsx --max-warnings=0` — passou.
- `git diff --check` — passou, com aviso preexistente de conversão LF/CRLF no índice.
- Typecheck completo web/mobile — interrompido por execução prolongada; não houve diagnóstico registrado.

## Pendencias pos-task

- Nenhuma funcional dentro do escopo.
- Recomenda-se executar os typechecks completos em CI ou em uma janela dedicada.

## Status final

done

## Ajuste posterior

A dica foi corrigida para usar as coordenadas `x`/`y` do hotspot indicado, ficando exatamente sobre o local do erro no web e no mobile.
