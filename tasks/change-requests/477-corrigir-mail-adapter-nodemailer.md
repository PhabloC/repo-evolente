# Task 477 - Corrigir MailAdapter: nodemailer e imports

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/002-autenticacao.md` (recuperação de senha / e-mail)

## Objetivo

Corrigir `mailAdapter.ts`: instalar `nodemailer` e importar `Transporter` + `createTransport`.

## Contexto mínimo

- `backend/src/patterns/adapters/mailAdapter.ts`
- `mailAdapter.spec.ts`

## Orçamento de contexto

- risco: baixo

## Criterios de aceite

- [x] Import + dependência `nodemailer`
- [x] Spec `mailAdapter.spec.ts` passa
- [x] Sem erros de lint/TS no arquivo

## Resultado da execucao

Instalados `nodemailer` e `@types/nodemailer`; imports nomeados; mock do Jest alinhado.

## Handoff

- `.agents/state/handoffs/TASK-477.md`

## Arquivos alterados

- `backend/src/patterns/adapters/mailAdapter.ts`
- `backend/src/patterns/adapters/mailAdapter.spec.ts`
- `backend/package.json`
- `backend/package-lock.json`

## Validacoes executadas

- `jest mailAdapter.spec` PASS
- `eslint mailAdapter.ts` exit 0

## Status final

done
