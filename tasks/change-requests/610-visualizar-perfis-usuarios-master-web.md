# Task 610 - Visualizar perfis de usuários no master web

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

- Não exige endpoint novo. Reutiliza os dados já carregados pela listagem de usuários e pela árvore de pacientes.

## Modo de execução

single-stack

## Slice vertical

- Slice 009 — `tasks/slices/009-administracao-master.md`

## Objetivo

Permitir que o master abra um perfil de consulta para cada pessoa exibida nas abas Profissionais, Pacientes e Admins, sem disponibilizar edição de dados.

## Dependências

- Task 183 — done (tela de usuários por abas)
- Task 450 — done (padrão visual de modal do master)

## Contexto mínimo

- esta task
- `tasks/slices/009-administracao-master.md`
- `front-end/src/pages/Main/AdminUsers/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/types/admin.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI do master | print fornecido pelo usuário nesta conversa e `design-system/front/Design_System_Evolente_Desktop.md` | manter a linguagem de abas, tabela e ações discretas. |
| Acessibilidade | `front-end/docs/ai/{ACCESSIBILITY,CODE_STYLE,QA}.md` | botão com nome acessível, modal acionável por teclado e sem controles de edição. |
| Dados existentes | `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx` e `front-end/src/services/users/userService.ts` | confirmar que a visualização reaproveita dados carregados e não faz atualização. |

## Orçamento de contexto

- baixo
- estratégia: adicionar estado local e modal somente-leitura na página existente; sem alterar API, permissões, formulários ou rotas.

## Critérios de aceite

- [x] Cada linha das abas Profissionais, Pacientes e Admins possui uma ação clara para visualizar o perfil.
- [x] O modal mostra identificação e dados disponíveis da pessoa, de acordo com a categoria.
- [x] O modal não contém campos editáveis, botão de salvar ou chamadas de atualização.
- [x] A ação de inativar usuários continua separada e inalterada.
- [x] O fluxo é acessível por teclado e tem teste de regressão.

## Referência visual

- Print da página de Usuários do ambiente master fornecido pelo usuário nesta conversa: abas, tabela e coluna Ação governam o ponto de entrada.
- Fonte complementar: `design-system/front/Design_System_Evolente_Desktop.md`.

## Resultado da execução

- Adicionado um ícone de olho na coluna Ação de Profissionais, Pacientes e Admins.
- O ícone abre um modal de perfil somente-leitura: usuários mostram contato, perfil, status, datas e, para profissionais, contagem de pacientes; pacientes mostram código, profissional vinculado e status do vínculo.
- A ação de inativar/reativar permanece separada do novo controle e nenhuma chamada de atualização foi acrescentada.

## Contexto utilizado

- Task 610 e Slice 009.
- Página, estilos e testes de `AdminUsers`, dados `AdminUser`, workspace do master e cliente de usuários.
- Print fornecido pelo usuário, design system front e guias de acessibilidade, estilo e QA do front-end.

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `tasks/change-requests/610-visualizar-perfis-usuarios-master-web.md`
- `tasks/000-index.md`
- `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-610.md`

## Validações executadas

- `npm run test -- --run src/pages/Main/AdminUsers` — concluído sem mensagens de erro (o ambiente não exibiu o resumo final do Vitest).
- `npm run lint` — concluído sem mensagens de erro (o ambiente não exibiu o resumo final do ESLint).
- `npm run build` — concluído sem mensagens de erro (o ambiente não exibiu o resumo final).
- `git diff --check` — aprovado.

## Pendências pós-task

- Conferir manualmente o modal em navegador, incluindo o retorno do foco ao ícone de olho depois de fechá-lo.

## Handoff

- `.agents/state/handoffs/TASK-610.md`

## Status final

done
