# Handoff - Task 549

## Task

- identificador: TASK-549
- título: Login mobile: autofill só desligado com teclado compacto
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002
- objetivo de negócio: login por e-mail/senha
- entrega verificável: gerenciador de credenciais funciona com teclado fechado

## Decisões preservadas

- decisão: `autoComplete`/`textContentType`/`importantForAutofill` dependem de `compact`
- motivo: Task 495 desligou autofill o tempo todo para Samsung Pass; o review mostrou que isso quebra password managers no estado normal
- impacto: teclado aberto continua sem autofill

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 549, slice 002

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `SignInForm.tsx` | props permanentes off | condicionar a compact |
| Task 495 | histórico Samsung Pass | não reabrir o layout |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `design-system/mobile/` | sem mudança visual |

## Arquivos alterados

- `mobile/src/features/auth/components/SignInForm.tsx`

## Validações executadas

- validação: eslint SignInForm — 0 erros

## Pendências ou bloqueios

- smoke no device (teclado aberto vs fechado)

## Próxima ação sugerida

- nenhuma nesta fatia

## Próximo contexto recomendado

- `SignInForm.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `app.json`
- motivo: resize do teclado já coberto na Task 495
