# Task 428 - Capa e vidro nas telas auth de cadastro e recovery

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

- sem alteração

## Modo de execução

single-stack

## Slice vertical

- Slice 014 - Template auth unificado web
- `tasks/slices/014-template-auth-unificado.md`

## Objetivo

Reutilizar a capa `capa-tela-login.webp` com efeito de vidro nas páginas de criar conta e esqueci minha senha (e reset), alinhadas ao login.

## Contexto mínimo

- `AGENTS.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- handoffs 426/427

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Prop já existente | `AuthLayout` `coverBackground` | ativar nas telas |
| Cadastro | `RegisterProfessional`, `RegisterGuardian` | criar conta |
| Recovery | `PasswordRecovery`, `PasswordReset` | esqueci senha |

## Orçamento de contexto

- baixo

## Critérios de conclusão

- [x] criar conta profissional e responsável com capa + vidro
- [x] recovery e reset com capa + vidro
- [x] gate de assinatura com capa + vidro
- [x] sem alterar markup além da prop

## Resultado da execucao

- `coverBackground` ativado em RegisterProfessional, RegisterGuardian, PasswordRecovery, PasswordReset e SubscriptionGate.

## Contexto utilizado

- AuthLayout prop das Tasks 426/427; páginas auth listadas

## Handoff

- `.agents/state/handoffs/TASK-428.md`

## Arquivos alterados

- `front-end/src/pages/Auth/RegisterProfessional/index.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/index.tsx`
- `front-end/src/pages/Auth/PasswordRecovery/index.tsx`
- `front-end/src/pages/Auth/PasswordReset/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `tasks/change-requests/428-capa-vidro-auth-cadastro-recovery.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-428.md`

## Validacoes executadas

- prop reutilizada; sem mudança de CSS

## Pendencias pos-task

- nenhuma

## Status final

done

## Dependências

- Tasks 426 e 427
