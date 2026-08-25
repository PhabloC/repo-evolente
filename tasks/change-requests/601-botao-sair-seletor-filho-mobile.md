# Task 601 - Adicionar botão sair ao seletor de filho mobile

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

- não se aplica; reutiliza o logout local existente

## Modo de execucao

single-stack

## Slice vertical

- Slice 051 - Seletor de filho no mobile
- `tasks/slices/051-seletor-filho-mobile.md`

## Objetivo

Disponibilizar um botão `Sair` no fim da página em que o responsável escolhe o filho que vai gerenciar, para encerrar a sessão sem precisar entrar no shell.

## Dependências

- Task 561 — done

## Contexto mínimo

- esta task
- `tasks/slices/051-seletor-filho-mobile.md`
- `.agents/state/handoffs/TASK-561.md`
- `mobile/src/features/children/screens/SelectChildScreen.tsx`
- `mobile/src/features/children/hooks/useSelectChildScreen.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Ação de sair | `mobile/src/features/auth/services/authService.ts`, `useSessionStore` | reutilizar o encerramento de sessão existente |
| Composição visual | `design-system/mobile/Design_System_Evolente_App_Mobile.md` (navegação e componentes) | manter botão claro e curto no rodapé |
| Padrões locais | `mobile/docs/ai/ARCHITECTURE.md`, `COMPONENT_REUSE.md` | manter a ação no hook de feature e usar `Button` compartilhado |

## Orçamento de contexto

- baixo
- estratégia: restringir à tela, hook e logout existente; sem mudanças em API, seleção persistida ou shell.

## Critérios de aceite

- [x] O seletor de filho exibe um botão `Sair` após o conteúdo da página.
- [x] Ao tocar em `Sair`, a sessão é encerrada e o usuário volta ao fluxo de autenticação.
- [x] A seleção de filho e todos os estados de lista permanecem inalterados.

## Fora de escopo

- Alterar login, cadastro de filhos, a lista de filhos ou o backend.

## Referência visual

### Mobile

- Fonte: `design-system/mobile/Design_System_Evolente_App_Mobile.md`.
- Sem print específico do seletor; usar o `Button` compartilhado, texto curto e ação clara no fim do conteúdo.

## Resultado da execucao

- Adicionado o botão `Sair`, com ícone e rótulo acessível, após o conteúdo do seletor de filho.
- A ação reutiliza `authService.signOut`, limpa a seleção de filho, a sessão e o cache de queries.

## Contexto utilizado

- Task 601, Slice 051, handoff da Task 561, seletor de filho, logout existente, design system mobile e guias locais de arquitetura/reutilização.

## Handoff

- `.agents/state/handoffs/TASK-601.md`

## Arquivos alterados

- `mobile/src/features/children/screens/SelectChildScreen.tsx`
- `mobile/src/features/children/screens/styles.ts`
- `mobile/src/features/children/hooks/useSelectChildScreen.ts`
- `tasks/change-requests/601-botao-sair-seletor-filho-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/051-seletor-filho-mobile.md`
- `.agents/state/handoffs/TASK-601.md`

## Validacoes executadas

- `npx eslint src/features/children/screens/SelectChildScreen.tsx src/features/children/screens/styles.ts src/features/children/hooks/useSelectChildScreen.ts` — passou
- `npx jest src/features/children --runInBand` — passou

## Pendencias pos-task

- Nenhuma.

## Status final

done
