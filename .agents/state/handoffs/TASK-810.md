# Handoff - Task 810

## Task

- identificador: Task 810
- título: Limite de três filhos por responsável
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 074
- objetivo de negócio: o responsável cadastra no máximo três filhos na web e no app
- entrega verificável: API, web e mobile recusam o quarto filho e mantêm os já cadastrados

## Decisões preservadas

- decisão: teto de 3 por conta do responsável, aplicado em `createMyChild`
- motivo: o cliente sozinho seria contornável
- impacto: contas que já tinham mais de três filhos permanecem assim e não cadastram outro
- decisão: a frase única é "Cada responsável pode cadastrar no máximo 3 filhos."

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/810-limite-tres-filhos-responsavel.md`
- `tasks/slices/074-limite-tres-filhos-responsavel.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` path `/guardians/me/children` | contrato do cadastro | descrever o teto e o 400 |
| `backend/src/modules/guardians/guardians.service.ts` | regra no servidor | recusar o quarto filho |
| páginas `Guardian/Children` e `Guardian/ChildRegister` | UI web | esconder o atalho e o formulário |
| `SelectChildScreen`, `CreateChildScreen`, `resolveSelectChildViewState` | UI mobile | esconder o atalho e o formulário |
| `front-end/docs/ai/ACCESSIBILITY.md` | texto de estado | `role="status"` e aviso em texto |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` e design system completo | a tela reutiliza status e botões já existentes; não houve print novo |
| trilha, pagamento e dashboard analítico | fora do ponto de bloqueio |

## Resultado por stack

- front-end: lista e rota de cadastro param no terceiro filho
- backend: `POST /guardians/me/children` responde 400 no quarto
- mobile: seletor e tela de cadastro param no terceiro filho; demo também

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/guardian-children-limit.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `front-end/src/constants/guardianChildrenLimit.ts`
- `front-end/src/pages/Main/Guardian/Children/index.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.test.tsx`
- `front-end/src/pages/Main/Guardian/ChildRegister/index.tsx`
- `front-end/src/pages/Main/Guardian/ChildRegister/index.test.tsx`
- `mobile/src/features/children/constants/guardianChildrenLimit.ts`
- `mobile/src/features/children/screens/CreateChildScreen.tsx`
- `mobile/src/features/children/screens/SelectChildScreen.tsx`
- `mobile/src/features/children/services/childrenService.ts`
- `mobile/src/features/children/utils/resolveSelectChildViewState.ts`
- `mobile/src/features/children/utils/resolveSelectChildViewState.test.ts`

## Validações executadas

- Jest do `GuardiansService`: passou, com recusa do quarto filho
- Vitest de Filhos e Cadastrar filho: passou
- Jest de `resolveSelectChildViewState`: passou
- ESLint dos arquivos alterados: passou

## Pendências ou bloqueios

- Fluxo logado no navegador com uma conta de três filhos não foi percorrido

## Próxima ação sugerida

- Nenhuma task aberta neste slice. Conferir no navegador com uma conta que já tenha três filhos, se quiser validar o texto na página real.

## Próximo contexto recomendado

- `tasks/change-requests/810-limite-tres-filhos-responsavel.md`
- `.agents/state/handoffs/TASK-810.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: trilha, jogos, pagamento e design system completo
- motivo: não participam do teto de filhos
