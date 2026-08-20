# Task 591 - Isolar carregamento de vinculos no perfil do filho web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Sem alteracao de contrato; usa endpoints existentes de detalhe do filho e vinculos.

## Modo de execucao

single-stack

## Slice vertical

- Slice 053 - `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Contexto mínimo

- Indice, Slice 053, perfil web do filho e teste associado.

## Contexto sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`, para o feedback dinâmico do painel.

## Orçamento de contexto

- baixo; somente perfil e seus mocks.

## Estratégia de redução

- Manter carregamento do perfil separado do painel secundario de vinculos.

## Resultado da execucao

- O perfil e a anamnese continuam visiveis quando a consulta de vinculos falha; o painel afetado informa o erro.
- O mock do teste passou a fornecer todas as funcoes importadas pela pagina.

## Contexto utilizado

- Perfil do filho, service de vinculos, teste e guia de acessibilidade web.

## Handoff

- `.agents/state/handoffs/TASK-591.md`

## Arquivos alterados

- `front-end/src/pages/Main/Guardian/ChildProfile/index.tsx`
- `front-end/src/pages/Main/Guardian/ChildProfile/index.test.tsx`

## Validacoes executadas

- Vitest direcionado e build do front-end.

## Pendencias pos-task

- Nenhuma.

## Status final

done
