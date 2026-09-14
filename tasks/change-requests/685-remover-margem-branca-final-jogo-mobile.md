## Status

done

## Título

Remover margem branca no final do jogo da memória mobile

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- mobile: sim

## Contrato

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/032-jogo-memoria.md`

## Objetivo

Fazer o scroll do jogo terminar próximo ao último controle, sem faixa branca extra.

## Entrega verificável

O final do conteúdo usa o fundo do jogo e possui apenas espaçamento curto após o botão.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Contexto sob demanda

- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`: composição dos controles finais.

## Orçamento de contexto

Baixo; container de scroll e tela do jogo.

## Resultado da execucao

Removido o padding inferior excessivo de 120px e aplicado fundo de jogo ao conteúdo rolável.

## Contexto utilizado

- Estilos do scroll e composição da tela de atividade.

## Handoff

Final do jogo sem margem branca artificial.

## Arquivos alterados

- `mobile/src/features/trail/screens/styles.ts`
- `tasks/change-requests/685-remover-margem-branca-final-jogo-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-685.md`

## Validacoes executadas

- Revisão estática dos estilos.

## Pendencias pos-task

- Nenhuma.

## Status final

done
