# Handoff - Task 558

## Task

- identificador: `558`
- título: Wizard web: cadastro só do responsável e redirect ao pagamento
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 049
- objetivo de negócio: cadastro público só do responsável
- entrega verificável: wizard `/cadastro/responsavel` só com dados do responsável e redirect para `/assinatura`
- status do slice: done

## Decisões preservadas

- Duas etapas: identidade + acesso; submit só `{ guardian }`
- Sem parentesco, criança, anamnese e sem `setSession`
- Redirect `/assinatura` com `audience: 'responsavel'`, e-mail e `fromRegistration`; sem `patientCode`
- Schemas de criança/anamnese ficaram no arquivo para a Task 560

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/558-wizard-cadastro-so-responsavel-web.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `.agents/state/handoffs/TASK-557.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI | tokens/auth |
| `front-end/src/pages/Auth/RegisterGuardian/**` | wizard | etapas |
| `front-end/src/services/guardians/guardianService.ts` | payload | register |
| `contracts/openapi.yaml` RegisterGuardian* | contrato | tipos |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile | fora da task |
| dashboard responsável | Task 559 |
| backend | já fechado na 557 |

## Resultado por stack

- front-end: wizard público só do responsável
- backend: não alterado nesta task
- mobile: não alterado

## Arquivos alterados

- `front-end/src/pages/Auth/RegisterGuardian/index.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/index.test.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`
- `front-end/src/constants/guardianOptions.ts`
- `front-end/src/types/guardian.ts`
- `front-end/src/services/adapters/adaptGuardianRegistration.ts`

## Validações executadas

- eslint dos arquivos do wizard: passou
- vitest RegisterGuardian: 3 testes passaram
- vite build: passou

## Pendências ou bloqueios

- nenhuma no Slice 049

## Próxima ação sugerida

- executar Task 559 (área web do responsável — Slice 050)

## Próximo contexto recomendado

- `tasks/change-requests/559-area-web-responsavel-shell-dashboard.md`
- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`
- `front-end/src/utils/resolvePostAuthPath.ts`
- `front-end/src/pages/Auth/GuardianAppGate/**`
- shell/rotas autenticadas do front-end

## Contexto que não deve ser carregado na próxima etapa

- wizard público de cadastro (já fechado)
- cadastro autenticado de filho (Task 560), salvo o que o shell precisar apontar
- mobile (Task 561)
