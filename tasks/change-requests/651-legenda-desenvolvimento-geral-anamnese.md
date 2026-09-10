# Task 651 - Informar extremos da escala de desenvolvimento geral

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- mobile

## Contrato

- Não altera contrato.

## Modo de execucao

cross-stack

## Slice vertical

- Slice 060 - Multisseleção na anamnese do filho
- `tasks/slices/060-multisselecao-anamnese-filho.md`

## Objetivo

Informar claramente que a escala de desenvolvimento geral vai de 1 (ruim) a 5 (ótimo).

## Critérios de aceite

- [ ] Web exibe `1 = Ruim` e `5 = Ótimo` junto à escala.
- [ ] Mobile exibe `1 = Ruim` e `5 = Ótimo` junto à escala.
- [ ] Valor e payload da escala permanecem inalterados.

## Resultado da execucao

- A legenda `1 = Ruim · 5 = Ótimo` foi adicionada ao formulário web e ao mobile.
- A escala e o payload não foram alterados.

## Validacoes executadas

- `git diff --check` — passou.
- Build web continua com erros preexistentes fora do escopo em Patients/Plans.

## Status final

done

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e Slice 060

## Contexto sob demanda

- Formulário web em `front-end/src/pages/Main/Guardian/ChildRegister/**`.
- Formulário mobile em `mobile/src/features/children/screens/CreateChildScreen.tsx`.
- Documentação de acessibilidade e design system das duas stacks.

## Orçamento de contexto

- baixo; alterar somente textos auxiliares da escala.
