# Task 606 - Paciente cancelado com ações restritas na web profissional

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

- Depende da Task 605: listagem com estado de paciente cancelado e remoção/inativação do vínculo.

## Modo de execução

single-stack

## Slice vertical

- Slice 054 — `tasks/slices/054-cancelamento-conta-responsavel-acesso-profissional.md`

## Objetivo

Refletir no painel do profissional que um paciente foi cancelado junto com a conta do responsável: impedir navegação ao perfil e ocultar todas as ações clínicas/trilhas, deixando visível somente **Remover vínculo**.

## Dependências

- Task 605 — done
- Task 604 — done

## Contexto mínimo

- esta task
- Slice 054 e Task 605
- `.agents/state/handoffs/TASK-604.md`
- listagem, perfil, tipos e serviço de pacientes no `front-end`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Estado e ações do perfil | `front-end/src/pages/Main/Patients/PatientProfile/` | remover CTAs clínicos/trilha e tratar tentativa de rota direta |
| Lista de pacientes | página, card/tabela e mapeadores de `Patients` | exibir estado cancelado e ação exclusiva de remoção |
| Ação destrutiva | componente de confirmação existente | confirmar remoção do vínculo e atualizar a lista |
| Acessibilidade/UI | `front-end/docs/ai/ACCESSIBILITY.md` e `design-system/front/Design_System_Evolente_Desktop.md` | rótulo textual, foco e confirmação acessível |
| Cobertura | testes de lista/perfil de pacientes | garantir que não existam CTAs ocultos acessíveis por teclado ou rota |

## Orçamento de contexto

- baixo
- estratégia: limitar à listagem/perfil de pacientes e componentes de confirmação; não alterar dashboard, configurações, checkout ou área do responsável.

## Critérios de aceite

- [x] A lista identifica explicitamente o paciente cancelado e não oferece link/navegação para o perfil clínico.
- [x] Uma rota direta ao perfil de paciente cancelado não expõe conteúdo clínico; apresenta estado restrito e somente **Remover vínculo**, ou retorna à lista com mensagem clara quando a API negar o acesso.
- [x] Para paciente cancelado, não são renderizadas ações de editar, inativar/reativar, avatar, consultas, evolução, relatórios ou montar/editar trilha.
- [x] **Remover vínculo** pede confirmação, chama a operação permitida pela Task 605 e remove/atualiza o item sem reativar o paciente.
- [x] Estado e confirmação têm texto explícito e foco acessível; testes focados cobrem renderização e tentativas de ação.

## Fora de escopo

- Alterar o processamento de assinatura/cancelamento.
- Criar reativação de conta/paciente.
- Mudanças no app mobile.

## Referência visual

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md`.
- Sem print específico; reutilizar os padrões existentes de status e confirmação de ação destrutiva, sempre com texto além de cor.

## Resultado da execucao

- O tipo de vínculo passou a reconhecer `canceled`.
- A lista identifica o estado como **Conta cancelada**, não abre o perfil pelo menu e exibe somente **Remover vínculo**.
- A remoção usa a confirmação acessível existente e envia a inativação permitida pela API; o texto confirma que ela não reativa a conta.
- A lista não requisita progresso para vínculos cancelados. Uma rota direta cujo acesso seja negado pela API mantém apenas a mensagem de erro e o botão de retorno, sem renderizar ações clínicas ou de trilha.

## Contexto utilizado

- Task 606, Slice 054, handoffs 604/605, tipos e serviço de pacientes, lista/perfil web, checklist de acessibilidade e Design System desktop.

## Handoff

- `.agents/state/handoffs/TASK-606.md`

## Arquivos alterados

- `front-end/src/types/patient.ts`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`

## Validacoes executadas

- `npx eslint` nos arquivos alterados — passou.
- `npx vitest run src/pages/Main/Patients/index.test.tsx --pool=threads --maxWorkers=1` — 7 testes passaram.
- `npx vitest run src/pages/Main/Patients/PatientProfile/index.test.tsx --pool=threads --maxWorkers=1` — 7 testes passaram.
- `npm run build` — bloqueado por erros preexistentes de mocks de `guardian`/`PatientDetail` em testes de Pacientes e Planos; nenhum erro nos componentes funcionais alterados nesta task.
- `git diff --check` — sem erros de whitespace.

## Acessibilidade aplicada

- O estado cancelado é textual, não depende apenas de cor.
- A ação destrutiva usa botão semântico, rótulo explícito e modal de confirmação com foco já gerenciado pelo componente reutilizado.
- A recusa de rota direta permanece anunciada com `role="alert"`.

## Pendencias pos-task

- Corrigir os mocks legados de `PatientGuardian`/`PatientDetail` em uma task de manutenção separada para desbloquear o build global.

## Status final

done
