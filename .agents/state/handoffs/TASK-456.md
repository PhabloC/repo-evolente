# Handoff TASK-456

## Task

Template de e-mail de recuperação de senha com logo S3

## Status final

done

## Decisões preservadas

- Logo por URL pública S3: `…/branding/logo-completa.webp` (override `MAIL_BRAND_LOGO_URL`)
- SMTP via nodemailer quando `MAIL_SMTP_HOST` está preenchido; senão só log
- Template HTML responsivo com CTA laranja e texto alternativo

## Arquivos-chave

- `backend/src/patterns/mail/password-recovery-email.template.ts`
- `backend/src/patterns/adapters/mailAdapter.ts`
- `backend/scripts/upload-branding-logo.mjs`

## Validações

- logo enviada ao bucket
- 12 testes passando (auth + mail)

## Próxima ação

- disparar recuperação de senha em ambiente com SMTP e conferir o e-mail recebido
