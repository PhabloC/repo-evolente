# Handoff - Task 560

## Task

- identificador: `560`
- título: Cadastro autenticado de filho na web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 050
- objetivo de negócio: área web do responsável e cadastro de filhos
- entrega verificável: wizard autenticado + perfil com anamnese e código único
- status do slice: done

## Decisões preservadas

- Cadastro de filho só depois do pagamento, no shell autenticado (não no AuthLayout)
- Parentesco canônico em `Child.kinship`
- CPF da criança ≠ CPF do responsável (front + API)
- `GET /guardians/me/children/{childId}` foi aditivo: a lista não traz anamnese
- Web não monta trilha; só persiste anamnese e `suggestedTrailCategories`
- Segundo filho reusa o mesmo CTA da listagem, sem novo pagamento

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/change-requests/560-cadastro-filho-autenticado-web.md`
- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`
- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`
- `.agents/state/handoffs/TASK-559.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS desktop | UI | tokens, empty, sucesso |
| `RegisterGuardian/schemas.ts`, `guardianOptions.ts` | anamnese | Q1–8 e pergunta 6 |
| OpenAPI children | API | POST create + GET detalhe |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile | Task 561 |
| trilha/jogos/dashboard profissional | fora de escopo |

## Resultado por stack

- front-end: wizard interno e perfil com anamnese
- backend: GET de detalhe do filho do responsável
- mobile: não alterado

## Arquivos alterados

- contrato OpenAPI GET detalhe
- `backend/.../guardians.service.ts` / controller / spec
- `front-end/.../Guardian/ChildRegister/**`
- `front-end/.../Guardian/ChildProfile/**`
- `front-end/.../guardianService.ts`, `types/guardian.ts`

## Validações executadas

- eslint wizard/perfil: passou
- vitest ChildRegister/ChildProfile/Children: passou
- jest guardians.service.spec: passou
- vite build: passou

## Pendências ou bloqueios

- nenhuma desta task; Slice 050 fechado

## Próxima ação sugerida

- Task 561: seletor de filho no mobile após login (empty state aponta para a web)

## Próximo contexto recomendado

- `tasks/change-requests/561-seletor-filho-pos-login-mobile.md`
- `tasks/slices/051-seletor-filho-mobile.md`
- contrato de listagem de filhos já existente

## Contexto que não deve ser carregado na próxima etapa

- wizard web de anamnese
- dashboard profissional
- jogos / biblioteca
