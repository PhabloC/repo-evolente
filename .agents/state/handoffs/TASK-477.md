# Handoff — Task 477

## Identificador

- task: 477
- slice: 002
- status final: done

## Decisões

- Dependências: `nodemailer` + `@types/nodemailer` (dev)
- Import: `import { createTransport, type Transporter } from 'nodemailer'`
- Mock Jest exporta `createTransport` nomeado (não default)

## Validações

- Spec e eslint do `mailAdapter` OK

## Próxima ação

Se o `start:dev` já estava rodando, deixar o hot-reload aplicar; confirmar env SMTP se quiser envio real.
