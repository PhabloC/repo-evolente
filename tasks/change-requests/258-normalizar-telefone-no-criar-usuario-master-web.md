# Task 258 - Normalizar telefone no criar usuário master web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1users/post`

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste incremental solicitado via code review

### Fonte primaria visual

- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`

## Objetivo

Garantir que o modal de criação de usuário master valide telefone no mesmo padrão do restante do produto e envie o valor normalizado para a API.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-155.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Padrão de telefone já adotado | `front-end/src/utils/phone.ts` | reutilizar normalização e validação existentes | sim |
| Fluxo do modal | `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx` | ajustar schema e payload do submit | sim |
| Cobertura do fluxo | `front-end/src/pages/Main/AdminUsers/index.test.tsx` | validar máscara + bloqueio de valor inválido | sim |
| Padrões da stack | `front-end/docs/ai/CODE_STYLE.md`, `ACCESSIBILITY.md` | manter consistência da implementação | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao modal `CreateMasterUserModal` e ao teste da página `AdminUsers`

## Criterios de conclusao

- [x] schema rejeita telefone arbitrário no modal de criação
- [x] submit envia telefone normalizado sem máscara
- [x] teste cobre telefone mascarado válido e telefone inválido

## Dependencias

- Task 155 - done

## Resultado da execucao

- o schema do modal passou a aceitar telefone opcional apenas quando o valor tem 10 ou 11 dígitos válidos
- o submit agora usa `normalizePhone` antes de chamar `createUser`
- o teste de criação foi ajustado para simular entrada mascarada e validar payload normalizado
- um teste adicional cobre o bloqueio de telefone inválido

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-155.md`

### Sob demanda

- `front-end/src/utils/phone.ts`
- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Handoff

- `.agents/state/handoffs/TASK-258.md`

## Arquivos alterados

- `tasks/change-requests/258-normalizar-telefone-no-criar-usuario-master-web.md`
- `front-end/src/pages/Main/AdminUsers/CreateMasterUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-258.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/AdminUsers/index.test.tsx` - ok
- `cd front-end && npm run lint` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
