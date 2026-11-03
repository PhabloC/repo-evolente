# Task 787 - Aviso quando senhas não coincidem no cadastro web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim (fora de escopo desta task)

## Contrato

- n/a (validação apenas no cliente; API continua recebendo um único `password`)

## Modo de execucao

single-stack

## Slice vertical

- Slice 016 — `tasks/slices/016-politica-senha-forte-web.md`

## Objetivo

Nos formulários de criar conta do profissional e do responsável, exigir confirmação de senha e exibir aviso claro quando as senhas não coincidem.

## Criterios de aceite

- [x] Cadastro profissional tem campo "Confirmar senha" e exibe "As senhas não coincidem." quando divergem
- [x] Cadastro responsável tem o mesmo comportamento
- [x] Mensagem reutiliza o padrão já usado em `PasswordReset`
- [x] Submit/avanço de etapa bloqueado enquanto as senhas não coincidirem
- [x] Testes dos dois formulários cobrem o aviso de divergência

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/016-politica-senha-forte-web.md`

## Contexto sob demanda

| Gatilho | Fonte | Decisão |
|---|---|---|
| Forms de cadastro | `front-end/src/pages/Auth/RegisterProfessional/`, `RegisterGuardian/` | adicionar `confirmPassword` + refine |
| Padrão existente | `front-end/src/pages/Auth/PasswordReset/index.tsx` | copiar mensagem e validação |
| Política de senha | `front-end/src/utils/password.ts` | manter `strongPasswordSchema` no campo senha |

## Orçamento de contexto

baixo — só forms auth web; sem design-system amplo, sem mobile, sem OpenAPI

## Estrategia de reducao

- Não reler requirements nem design-system
- Não alterar backend/contrato
- Espelhar apenas o refine de `PasswordReset`

## Dependencias

- Task 030 (política de senha forte) — done

## Fora de escopo

- Mobile
- Backend / OpenAPI
- Login e recuperação (pedido de link)
- Redesign visual das telas

## Resultado da execucao

- Campo "Confirmar senha" nos cadastros de profissional e responsável.
- Mensagem `As senhas não coincidem.` alinhada ao reset de senha.
- No wizard do profissional, checagem explícita no `goNext` porque `trigger(campos)` do RHF não aplica o `refine` do Zod.

## Contexto utilizado

- Contexto mínimo da task + forms auth + PasswordReset como referência de mensagem.

## Handoff

- `.agents/state/handoffs/TASK-787.md`

## Arquivos alterados

- `front-end/src/pages/Auth/RegisterProfessional/index.tsx`
- `front-end/src/pages/Auth/RegisterProfessional/index.test.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/index.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`
- `front-end/src/pages/Auth/RegisterGuardian/index.test.tsx`
- `tasks/slices/016-politica-senha-forte-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx vitest run --pool=threads --no-file-parallelism src/pages/Auth/RegisterProfessional/index.test.tsx src/pages/Auth/RegisterGuardian/index.test.tsx` — 6 passed

## Pendencias pos-task

- Nenhuma

## Status final

done
