# Task 775 - Remover card Outro filho do perfil mobile

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

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- nao se aplica

### Regra de aderencia visual

- nao se aplica

## Origem da solicitacao

Pedido do usuário: remover o card "Outro filho" do perfil mobile.

## Objetivo

Remover o atalho "Outro filho" da tela de perfil do responsável.

## Escopo

- Remover o `HomeActionCard` com título `Outro filho` em `ResponsavelProfileScreen`
- Limpar import não usado (`CirclePlus`) se aplicável

## Fora de escopo

- Remover cadastro de filho quando não há crianças (`Criança` / CreateChild)
- Card `Trocar filho`
- Fluxo web de cadastro de filhos

## Entradas

- pedido explícito do usuário
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Slice vertical

### Identificador do slice

Slice 010 - App do responsavel: home, perfil e notificacoes

### Arquivo do slice

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

### Objetivo de negocio

Simplificar o perfil removendo o atalho de cadastrar outro filho.

### Entrega verificavel do slice

Card "Outro filho" não aparece no perfil.

### Fora do slice

- redesenho do fluxo de cadastro de filhos

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Perfil | `ResponsavelProfileScreen.tsx` | remover card | sim |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 1
- Risco de contexto excessivo: baixo
- Estratégia: só a tela de perfil

## Dependencias

- nenhuma bloqueante

## Criterios de conclusao

- [x] Card "Outro filho" removido do perfil
- [x] Cadastro inicial (sem filhos) permanece
- [x] Card "Trocar filho" permanece

## Instrucoes de implementacao

- Remover o bloco JSX do card "Outro filho"
- Remover `CirclePlus` do import se ficar órfão

## Validacao esperada

- eslint na tela do perfil

## Entregaveis esperados

- perfil sem card Outro filho
- task, índice, slice e handoff

## Resultado da execucao

- Card "Outro filho" removido do perfil.
- Import `CirclePlus` removido.
- Card "Criança" (sem filhos) e "Trocar filho" mantidos.

## Contexto utilizado

- Task 775, Slice 010, `ResponsavelProfileScreen.tsx`.

## Handoff

- `.agents/state/handoffs/TASK-775.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/775-remover-card-outro-filho-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-775.md`

## Validacoes executadas

- `npx eslint src/features/shell/screens/ResponsavelProfileScreen.tsx` — passou.

## Pendencias pos-task

- Com filhos já cadastrados, o atalho mobile para incluir outro filho no perfil deixa de existir (cadastro inicial sem filhos permanece).

## Status final

done
