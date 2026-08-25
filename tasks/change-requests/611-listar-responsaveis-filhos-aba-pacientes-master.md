# Task 611 - Listar responsáveis e filhos na aba Pacientes do master

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Adicionar `GET /admin/guardians-tree` em `contracts/openapi.yaml`.
- Resposta somente-leitura: responsáveis autenticáveis e seus filhos cadastrados.

## Modo de execução

cross-stack

## Slice vertical

- Slice 009 — `tasks/slices/009-administracao-master.md`

## Objetivo

Na aba Pacientes da página de Usuários do master, listar responsáveis em vez de crianças isoladas e permitir expandir cada responsável para ver, logo abaixo, os filhos que cadastrou.

## Dependências

- Task 610 — done (consulta somente-leitura na página de usuários)
- Task 557 — done (cadastro de responsável e filhos)
- Task 561 — done (modelo de seleção de filhos)

## Contexto mínimo

- esta task
- `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-610.md`
- `front-end/src/pages/Main/AdminUsers/{index.tsx,index.test.tsx,styles.module.css}`
- `backend/src/modules/admin/{admin.controller.ts,admin.service.ts}`
- `contracts/openapi.yaml` no bloco `/admin`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Novo endpoint administrativo | `backend/src/modules/guardians/{guardians.repository.ts,entities/child.entity.ts}` | obter filhos por responsável sem permitir alteração. |
| Cliente web | `front-end/src/services/admin/adminService.ts` e `front-end/src/types/admin.ts` | tipar e consumir a árvore administrativa. |
| UI web | print da página fornecido pelo usuário e `design-system/front/Design_System_Evolente_Desktop.md` | preservar tabela, badges e ações discretas. |
| Acessibilidade/qualidade | `front-end/docs/ai/{ACCESSIBILITY,CODE_STYLE,QA}.md` e `backend/docs/ai/{AGENTS,CODE_STYLE,QA}.md` | manter expansão por botão acessível e validar contrato e implementações. |

## Orçamento de contexto

- médio
- estratégia: acrescentar uma única consulta administrativa somente-leitura e reutilizar a tabela/modal existentes; sem mudanças em cadastro, vínculo profissional, assinatura ou edição de perfis.

## Critérios de aceite

- [x] A aba Pacientes lista responsáveis, com contato, status e quantidade de filhos cadastrados.
- [x] Cada responsável tem um botão acessível para expandir/recolher seus filhos dentro da tabela.
- [x] Os filhos aparecem imediatamente abaixo do responsável selecionado, com identificação, código e status de vínculo quando disponível.
- [x] Master pode somente consultar; não há controles de editar/criar/inativar nessa aba.
- [x] Endpoint é exclusivo de master e está documentado no OpenAPI.
- [x] Backend e front-end contam com testes de regressão aplicáveis.

## Referência visual

- Print da página de Usuários do ambiente master fornecido pelo usuário nesta conversa: a aba Pacientes e a tabela são a referência de entrada.
- Fonte complementar web: `design-system/front/Design_System_Evolente_Desktop.md`.

## Resultado da execução

- O backend expõe `GET /admin/guardians-tree`, disponível apenas ao master, com cada responsável e seus filhos. O retorno não inclui CPF, data de nascimento ou outros dados sensíveis da criança.
- A aba Pacientes agora lista responsáveis. O botão de seta expande/recolhe os filhos do responsável dentro da própria tabela; cada filho mostra nome, código e status agregado de vínculo profissional.
- Os controles de olho mantêm a consulta de perfil em modo somente-leitura. A aba não ganhou criação, edição, inativação ou alteração de vínculos.

## Contexto utilizado

- Task 611, Slice 009 e handoff da Task 610.
- Contrato OpenAPI, AdminController/AdminService e repositórios de responsáveis no backend.
- AdminUsers, serviço admin e tipos compartilhados no front-end, além da referência visual e guias locais de acessibilidade/qualidade.

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/admin/admin.controller.ts`
- `backend/src/modules/admin/admin.service.ts`
- `backend/src/modules/admin/admin.service.spec.ts`
- `backend/src/modules/guardians/{guardians.repository.ts,guardians.in-memory.repository.ts,guardians.typeorm.repository.ts}`
- `front-end/src/types/admin.ts`
- `front-end/src/services/admin/adminService.ts`
- `front-end/src/pages/Main/AdminUsers/{index.tsx,index.test.tsx,styles.module.css}`
- `tasks/change-requests/611-listar-responsaveis-filhos-aba-pacientes-master.md`
- `tasks/000-index.md`
- `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-611.md`

## Validações executadas

- Backend: `npm run test -- --runInBand src/modules/admin/admin.service.spec.ts` — aprovado (10 testes).
- Backend: `npm run typecheck` — aprovado.
- Front-end: `npm run test -- --run src/pages/Main/AdminUsers` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final do Vitest).
- Front-end: `npm run build` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final).
- Front-end: `npm run lint` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final do ESLint).
- `git diff --check` — aprovado.

## Pendências pós-task

- Conferir em navegador com uma conta responsável sem filhos, uma com um filho e uma com múltiplos filhos; validar expansão por teclado e retorno de foco.

## Handoff

- `.agents/state/handoffs/TASK-611.md`

## Status final

done
