# Task 572 - Reproduzir composição do perfil profissional no perfil do filho

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

- `GET /guardians/me/children/{childId}`

## Modo de execucao

single-stack

## Slice vertical

- Slice 050 — `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Contexto mínimo

- Governança raiz, índice, esta task, Slice 050, handoff Task 571.

## Contexto sob demanda

- Perfil profissional e perfil do filho; `ACCESSIBILITY.md` para preservar semântica.

## Orçamento de contexto

- médio; limitar aos dois módulos de perfil.

## Dependencias

- Task 571 (done)

## Resultado

- O perfil do filho agora usa a mesma composição do perfil profissional: hero, indicadores, radar, grade de conteúdo, cards e painel lateral.
- As ações e informações exclusivas do profissional continuam fora da área do responsável.

## Contexto utilizado

- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Guardian/ChildProfile/index.tsx`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Arquivos alterados

- `front-end/src/pages/Main/Guardian/ChildProfile/index.tsx`
- `front-end/src/pages/Main/Guardian/ChildProfile/index.test.tsx`
- Rastreabilidade desta task, Slice 050, índice e handoff.

## Validações

- `npm run test -- src/pages/Main/Guardian/ChildProfile/index.test.tsx --run` — ok (2 testes).
- `npx eslint src/pages/Main/Guardian/ChildProfile/index.tsx src/pages/Main/Guardian/ChildProfile/index.test.tsx --max-warnings=0` — ok.
- `git diff --check` — ok.

## Pendências

- Nenhuma.

## Handoff

- `.agents/state/handoffs/TASK-572.md`

## Status final

done
