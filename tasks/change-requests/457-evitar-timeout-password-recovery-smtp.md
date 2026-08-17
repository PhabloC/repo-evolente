# Task 457 - Evitar timeout no password-recovery por SMTP lento

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Contrato

- preserva `POST /auth/password-recovery` e resposta generica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/002-autenticacao.md`

## Objetivo

A API de recuperacao de senha nao deve esperar o SMTP concluir; o e-mail segue em background com timeout de conexao.

## Criterios de conclusao

- [x] `requestPasswordRecovery` retorna sem await do SMTP
- [x] falhas de envio sao logadas
- [x] transporter SMTP tem timeouts
- [x] testes de auth continuam passando

## Resultado da execucao

- Envio de e-mail em background (`void` + `.catch`)
- Timeouts SMTP: connection/greeting 10s, socket 20s
- Causa do timeout do front: SMTP Hostinger ~24s > axios 10s

## Status final

done
