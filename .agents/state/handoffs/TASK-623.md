# Handoff - Task 623

## Task

- identificador: `623`
- título: Refinar formulário de cadastro de filho mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- Slice 055 — cadastro de filho no perfil mobile
- status: done

## Decisões preservadas

- A data é mostrada como `DD/MM/AAAA`, mas é convertida para ISO somente no envio do payload.
- O CPF é mostrado mascarado e enviado apenas com dígitos.
- Placeholders seguem sendo pistas visuais; os labels continuam como o nome acessível dos campos.

## Contexto efetivamente usado

- Task/Slice, handoff 621, tela de cadastro de filho, componentes de campo e botão, design system mobile e docs locais de implementação.

## Arquivos alterados

- Tela, estilos e utilitário/teste de máscara em `mobile/src/features/children`.
- Task 623, Slice 055, índice e este handoff.

## Validações executadas

- Teste Jest da máscara: 1 suíte / 2 testes passaram.
- Typecheck e lint do escopo passaram.
- `git diff --check` passou.

## Pendências ou bloqueios

- Nenhuma.

## Próximo contexto recomendado

- Nenhum, salvo novo refinamento do cadastro de filho mobile.
