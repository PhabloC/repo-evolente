## Status

done

## Título

Visualizar atividade na Biblioteca da trilha mobile

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica. A biblioteca já carrega os resumos e a visualização usa os dados existentes.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Objetivo

Permitir que o usuário abra e visualize uma atividade diretamente pelo catálogo da Biblioteca no perfil mobile do paciente/responsável.

## Entrega verificável

Cada card da Biblioteca possui ação de visualização que abre a tela existente da atividade, preservando a ação de seleção para adicionar à trilha quando o usuário puder gerenciar.

## Fora de escopo

- Criar novo player ou novo endpoint.
- Alterar permissões de edição da trilha.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`
- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`: UI mobile e estados da ação.
- `mobile/docs/ai/ACCESSIBILITY.md`: critérios de acessibilidade para o novo botão.
- `mobile/src/navigation`: registro da rota existente, se necessário.

## Orçamento de contexto

Baixo; carregar somente os arquivos listados e os testes focados do módulo.

## Dependências

- A tela/rota `TrailActivity` existente.

## Resultado da execucao

A Biblioteca ganhou ação “Visualizar” em cada atividade. A ação abre `TrailActivity` em modo de pré-visualização, sem permitir conclusão ou mutação da trilha.

## Contexto utilizado

Task, Slice 047, navegação mobile, tela de atividade, biblioteca mobile, design system mobile e documentação local disponível.

## Handoff

Fluxo concluído; para novos refinamentos, retomar pela Biblioteca e pela tela `TrailActivityScreen`.

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailLibraryScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/routes/params.ts`

Correção posterior: o wrapper do card passou a preservar `libraryPosterCell` (48% da grade), mantendo o botão de visualização dentro da mesma coluna.

Refinamento posterior: botão de visualização recebeu pill com ícone de olho, contraste e área de toque mobile.

## Validacoes executadas

- `npm run typecheck` — falhou por erros preexistentes em arquivos administrativos/jogos/styles e por incompatibilidade preexistente de `ContentCoverThumb`; não há erro novo de sintaxe no fluxo alterado após a correção.

## Pendencias pos-task

- Corrigir os erros globais de typecheck já existentes em task separada.

## Status final

done
