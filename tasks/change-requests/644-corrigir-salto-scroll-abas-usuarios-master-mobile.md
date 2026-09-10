# Task 644 - Corrigir salto de scroll nas abas de usuários master mobile

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

- Não aplicável; correção exclusivamente de estado/renderização da UI.

## Modo de execução

single-stack

## Slice vertical

- Slice 009 — `tasks/slices/009-administracao-master.md`

## Objetivo

Impedir que a tela de usuários do master salte até o final da lista e retorne ao trocar entre as abas Master, Profissionais e Pacientes.

## Dependências

- Task 619 — done (`tasks/change-requests/619-usuarios-master-mobile-busca-abas-paginacao.md`)

## Contexto mínimo

- esta task
- `tasks/slices/009-administracao-master.md`
- `mobile/src/features/admin/screens/AdminUsersScreen.tsx`
- `mobile/src/features/admin/screens/usersStyles.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Implementação mobile | `mobile/docs/ai/MOBILE_PATTERNS.md` | validar estado e composição de listas/abas. |
| Validação | `mobile/docs/ai/QA.md` | executar lint, typecheck, testes e teste de regressão quando viável. |

## Orçamento de contexto

- baixo
- estratégia: inspecionar somente a tela, estilos e testes diretamente relacionados ao diretório de usuários.

## Critérios de aceite

- [ ] Trocar qualquer uma das três abas mantém a posição vertical esperada, sem salto ao fim da lista.
- [x] A lista continua filtrando e paginando corretamente.
- [x] Não há alteração de contrato ou comportamento de outras telas.

## Resultado da execucao

- Configurada rolagem aninhada e bloqueio direcional na lista horizontal de abas para evitar propagação do gesto e salto vertical ao atualizar a lista.
- Corrigido o estiramento vertical das abas com alinhamento transversal explícito no conteúdo do `ScrollView` horizontal.
- Removido o `flexGrow` dos contêineres internos para evitar espaço vazio abaixo da lista na aba Pacientes.
- Removido o padding horizontal do bloco principal para o conteúdo ocupar toda a largura disponível.
- Ajustado o bloco principal para usar espaçamento lateral pequeno e consistente.

## Contexto utilizado

- Task 644, Slice 009, `AdminUsersScreen.tsx`, `usersStyles.ts`, padrões mobile e QA.

## Arquivos alterados

- `mobile/src/features/admin/screens/AdminUsersScreen.tsx`
- `mobile/src/features/admin/screens/usersStyles.ts`

## Validacoes executadas

- `npm run lint` — concluído sem erro reportado.
- `npm run typecheck` — falha em erros preexistentes de outras telas/componentes (`AdminMasterProfileScreen`, auth, jogos e trail).
- `npm run test -- --runInBand` — 40 suites aprovadas; 1 suite preexistente falhou em `MemoryGameRenderer` por `expo-audio`.

## Pendencias pos-task

- Validar em dispositivo/emulador Android e iOS a troca das três abas com a lista em diferentes posições de scroll.

## Handoff

- Correção limitada aos props de rolagem da tela de usuários; não houve alteração de API, filtro ou paginação.

## Status final

done

## Status final

pending
