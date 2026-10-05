# Task 753 - Corrigir layout dos botões do cabeçalho Filhos

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

Não se aplica.

## Modo de execucao

single-stack

## Slice vertical

- Slice 063 — `tasks/slices/063-diretorio-profissionais-responsavel-web.md`

## Referencia de design system

- Stack: front-end
- Tipo: captura do usuário na conversa + shell atual do header
- Fonte: `front-end/src/layout/Header/`, `front-end/src/pages/Main/Guardian/Children/`

## Origem da solicitacao

Pedido humano com print: botões “Encontrar profissionais” e “Cadastrar filho” ficaram empilhados, desalinhados e sobrepondo o card de filhos.

## Comportamento esperado

- Os dois botões ficam lado a lado no desktop, alinhados e sem sobrepor o conteúdo abaixo.
- Em telas estreitas, empilham de forma controlada sem cortar nem invadir o card.
- Ações e navegação permanecem iguais.

## Fora de escopo

- Alterar copy, rotas ou a página de profissionais.
- Redesign geral do header.

## Criterios de aceite

- [x] Botões não sobrepõem o card “filho cadastrado”.
- [x] Alinhamento horizontal coerente no desktop.
- [x] Teste focado da página Filhos passa.

## Contexto mínimo

- esta task, Slice 063, handoff TASK-752
- Header e página Filhos

## Contexto sob demanda

| Gatilho | Fonte | Decisão | Obrigatório? |
|---|---|---|---|
| Layout header | `front-end/src/layout/Header/styles.module.css` | remover overflow absoluto | sim |
| Página | `Children/index.tsx` + estilos Guardian | grupo de ações | sim |

## Orçamento de contexto

- baixo

## Dependências

- Task 752 — done

## Resultado da execucao

- Removido `position: absolute` das ações below-heading; o header passa a reservar altura no fluxo.
- Grupo `headerActions` alinha os dois botões em linha com wrap controlado.

## Contexto utilizado

- Header CSS, página Filhos, captura do usuário.

## Handoff

- `.agents/state/handoffs/TASK-753.md`

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/pages/Main/Guardian/Children/index.tsx`
- `front-end/src/pages/Main/Guardian/styles.module.css`
- `tasks/slices/063-diretorio-profissionais-responsavel-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx vitest run src/pages/Main/Guardian/Children/index.test.tsx` — ok

## Pendencias pos-task

- Nenhuma

## Status final

done
