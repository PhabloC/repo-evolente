# Task 456 - Template de e-mail de recuperação de senha com logo S3

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Contrato

- nao altera paths OpenAPI; preserva `POST /auth/password-recovery`

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/002-autenticacao.md`

## Objetivo

Enviar o e-mail de recuperacao de senha com template HTML visual (marca Evolente) e logo carregada da URL publica do S3, usando SMTP quando configurado.

## Criterios de conclusao

- [x] template HTML de recuperacao com logo S3 no topo
- [x] envio SMTP real quando `MAIL_SMTP_HOST` estiver configurado
- [x] fallback de log quando SMTP nao estiver configurado
- [x] script/upload da logo em `branding/` no S3
- [x] testes do template e adapter

## Resultado da execucao

- Template HTML table-based com logo, faixa de marca, CTA laranja e fallback texto
- `MailAdapter` envia via nodemailer quando SMTP existe
- Logo publica: `STORAGE_S3_PUBLIC_BASE_URL/branding/logo-completa.webp`
- Script `npm run upload:branding-logo` executado com sucesso

## Contexto utilizado

- mailAdapter, auth.service, app.config, S3 public base

## Handoff

- `.agents/state/handoffs/TASK-456.md`

## Arquivos alterados

- `backend/src/patterns/mail/password-recovery-email.template.ts`
- `backend/src/patterns/adapters/mailAdapter.ts`
- `backend/src/config/app.config.ts`
- `backend/src/modules/auth/auth.service.ts`
- `backend/scripts/upload-branding-logo.mjs`
- `backend/.env.example`
- `backend/package.json`
- testes relacionados

## Validacoes executadas

- upload branding logo OK
- jest mailAdapter + template + auth.service: 12 passed

## Pendencias pos-task

- nenhuma

## Status final

done
