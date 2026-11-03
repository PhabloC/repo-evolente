# Handoff - Task 787

## Task

- identificador: 787
- título: Aviso quando senhas não coincidem no cadastro web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 016
- objetivo de negócio: política de senha forte e confirmação
- entrega verificável: cadastro profissional/responsável avisam quando senhas divergem

## Decisões preservadas

- decisão: reutilizar mensagem `As senhas não coincidem.` do PasswordReset
- motivo: consistência UX entre fluxos de criação/redefinição
- impacto: campo `confirmPassword` só no cliente; API segue com um `password`

- decisão: no cadastro profissional, checar mismatch no `goNext` com `setError`
- motivo: `trigger(listaDeCampos)` do RHF+zodResolver não aplica `refine` de objeto
- impacto: responsável continua confiando no `handleSubmit` + refine do schema

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/787-aviso-senhas-nao-coincidem-cadastro-web.md`
- `tasks/slices/016-politica-senha-forte-web.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `RegisterProfessional/index.tsx` | UI cadastro | campo + validação |
| `RegisterGuardian/index.tsx` + `schemas.ts` | UI cadastro | campo + refine |
| `PasswordReset/index.tsx` | padrão de mensagem | copy e refine |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | API não muda |
| `mobile/` | fora de escopo |
| `design-system/` | sem redesign |

## Resultado por stack

- front-end: done
- backend: n/a
- mobile: n/a

## Arquivos alterados

- `front-end/src/pages/Auth/RegisterProfessional/index.tsx`
- `front-end/src/pages/Auth/RegisterProfessional/index.test.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/index.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`
- `front-end/src/pages/Auth/RegisterGuardian/index.test.tsx`

## Validações executadas

- vitest RegisterProfessional + RegisterGuardian: 6 passed

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente nos formulários de criar conta

## Próximo contexto recomendado

- apenas os forms auth alterados, se houver ajuste de copy/UX

## Contexto que não deve ser carregado na próxima etapa

- backend, OpenAPI, mobile — sem impacto
