# Handoff - Task 567

## Task

- identificador: `567`
- título: Balão de download do app na sidebar do responsável
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 050
- status do slice: done

## Decisões preservadas

- O balão é exclusivo do papel `responsavel` e fica acima do bloco de perfil da sidebar.
- A forma do balão é CSS (borda, raio e ponta inferior); os logos de App Store e Google Play reutilizam assets locais.
- Como não há links oficiais de loja configurados, os dois controles levam a `/baixar-app`.

## Contexto efetivamente usado

- Task 567, Slice 050, Sidebar/MainLayout, GuardianAppGate, rotas, logos locais e acessibilidade.

## Arquivos alterados

- Sidebar, seus estilos/testes e MainLayout.
- task, slice e índice.

## Validações executadas

- prettier e eslint focados: ok.
- `git diff --check`: ok.

## Pendências ou bloqueios

- Links externos das lojas ainda não foram fornecidos.

## Próximo contexto recomendado

- Nenhum, salvo disponibilização dos links oficiais de App Store e Google Play.
