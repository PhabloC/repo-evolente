# Task 560 - Cadastro autenticado de filho na web (perfil, anamnese, código, trilha)

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

- `POST /guardians/me/children`
- `GET /guardians/me/children`
- `GET /guardians/me/children/{childId}` (aditivo nesta task: a lista não traz anamnese)
- `PATCH /guardians/me/children/{childId}` já existente para edição básica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- reuso do wizard de anamnese extraído de `front-end/src/pages/Auth/RegisterGuardian/**` (etapas Criança / Motivo / Perfil)

### Regra de aderencia visual

- Formulário interno no shell autenticado (não no `AuthLayout` público)
- Pergunta 6: mesmas 9 categorias da biblioteca (`guardianOptions` / Task 545)
- Lacuna: sem print do cadastro interno de filho

## Contexto de negocio

### Por que

Criança e anamnese saíram do cadastro público e precisam existir dentro da plataforma, para um ou mais filhos.

### O que

Na área Filhos, o responsável cadastra cada filho (dados + anamnese). O backend devolve código único e categorias de trilha daquele filho. Há tela de perfil por filho.

### Comportamento esperado

- CTA “Cadastrar filho” no empty state e na listagem
- Wizard interno: dados da criança (nome, nascimento, CPF, sexo, parentesco) → anamnese Q1–8
- Submit `POST /guardians/me/children`
- Sucesso mostra o `patientCode` e leva ao perfil do filho
- Perfil do filho: dados, código, anamnese resumida, categorias sugeridas da trilha
- É possível cadastrar o segundo filho sem novo pagamento
- CPF da criança ≠ CPF do responsável (validação no front, reforço da API)

### Fora de escopo

- Montar/editar a grade semanal na web
- Cadastro de filho no mobile
- Criar filho sem anamnese

## Slice vertical

### Identificador do slice

Slice 050 - Área web do responsável e cadastro de filhos

### Arquivo do slice

- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`

## Permissoes

- `responsavel` com `accessGranted`

## Casos de erro mapeados

- Validação por etapa (CPF, anamnese, pergunta 6)
- 409 CPF duplicado
- 403 sem assinatura
- Falha de submit

## Decisoes humanas confirmadas

- Cadastro do filho dentro da plataforma
- N filhos, cada um com perfil, trilha individualizada e código único

## Premissas adotadas pela IA

- Parentesco no filho
- Após criar, a trilha semanal ainda é montada no mobile (self-serve); a web só persiste anamnese + categorias sugeridas
- Reusar schemas Zod da anamnese do RegisterGuardian, movendo-os para módulo compartilhado se necessário

## Criterios de aceite

- [x] Responsável cria o primeiro e o segundo filho pela web
- [x] Cada filho recebe `patientCode` visível
- [x] Anamnese completa persistida; pergunta 6 com ≥1 área
- [x] Perfil individual por filho
- [x] Empty state some depois do primeiro cadastro
- [x] Lint, testes do fluxo e build ok
- [x] Acessibilidade do wizard interno (etapas, erros, radiogroup)

## Casos de borda

- Voltar etapa
- Dois filhos
- Conta antiga já com um filho: listagem + novo cadastro

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 050, Tasks 556/557/559
- `front-end/docs/ai/ACCESSIBILITY.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Wizard legado | `front-end/src/pages/Auth/RegisterGuardian/**`, `schemas.ts`, `guardianOptions.ts` | reuso anamnese | sim |
| Contrato | schema `CreateGuardianChildRequest` | payload | sim |
| Perfil paciente profissional | `front-end/src/pages/Main/Patients/PatientProfile/**` | o que reusar vs não copiar | nao |

## Orçamento de contexto

- medio
- estrategia de reducao: reusar anamnese existente; não abrir jogos nem planejamento profissional

## Dependencias

- Task 557
- Task 559

## Resultado da execucao

### Resumo por stack

- **front-end**: `/filhos/cadastrar` virou wizard interno (Criança → Motivo → Perfil). Submit em `POST /guardians/me/children`. Sucesso navega ao perfil com `patientCode`. Perfil carrega `GET /guardians/me/children/{childId}` com dados, código, anamnese resumida e chips de categorias sugeridas. Listagem deixa o empty state após o primeiro filho e mantém o CTA para o segundo.
- **backend**: `GET /guardians/me/children/:childId` devolve filho + anamnese (403 se não for dono). Necessário porque a listagem não inclui anamnese.
- **contrato**: path GET de detalhe + schema `GuardianChildDetailResponse` (aditivo, anamnese nullable).

### Relação com o slice

- Fecha o Slice 050 (559 já estava done). Cadastro autenticado de N filhos na web está entregue.

### Decisões técnicas

- Reuso dos schemas Zod de `RegisterGuardian/schemas.ts` (com `kinship` no passo da criança).
- Parentesco no filho; CPF da criança comparado ao `GET /guardians/me` antes de avançar.
- Continuar da identidade fica desabilitado até o perfil do responsável carregar, para a checagem de CPF não correr em falso.
- Não monta trilha na web; só persiste anamnese e `suggestedTrailCategories`.
- GET de detalhe foi adicionado ao contrato porque o critério de aceite pede resumo de anamnese no perfil.

### Relação com o contrato

- `POST /guardians/me/children` já existia na 557.
- `GET /guardians/me/children/{childId}` é aditivo desta task.

### Relação com a referência visual

- Shell autenticado (`MainLayout`), tokens, empty/sucesso/erro do DS desktop.
- Lacuna: sem print do cadastro interno de filho; wizard reusa o padrão de etapas da anamnese pública, fora do `AuthLayout`.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 050, handoff 559
- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | botões, cards, empty, sucesso |
| `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`, `guardianOptions.ts` | wizard | anamnese Q1–8 e pergunta 6 |
| `contracts/openapi.yaml` `POST/GET /guardians/me/children` | API | payload e detalhe |

### Evitado

- mobile seletor de filho (561)
- montagem de trilha / jogos / dashboard profissional

## Handoff

- Caminho: `.agents/state/handoffs/TASK-560.md`
- Próximo contexto: Task 561 (seletor de filho no mobile), se o usuário pedir

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.controller.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `front-end/src/constants/guardianOptions.ts`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`
- `front-end/src/types/guardian.ts`
- `front-end/src/services/guardians/guardianService.ts`
- `front-end/src/pages/Main/Guardian/styles.module.css`
- `front-end/src/pages/Main/Guardian/ChildRegister/index.tsx`
- `front-end/src/pages/Main/Guardian/ChildRegister/index.test.tsx`
- `front-end/src/pages/Main/Guardian/ChildProfile/index.tsx`
- `front-end/src/pages/Main/Guardian/ChildProfile/index.test.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.test.tsx`
- `tasks/change-requests/560-cadastro-filho-autenticado-web.md`
- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-560.md`

## Validacoes executadas

- eslint dos arquivos do wizard/perfil/listagem — passou
- vitest: ChildRegister, ChildProfile, Children — 7 testes passaram
- jest: `guardians.service.spec.ts` — passou (inclui GET detalhe e 403 de outra conta)
- `npx vite build` — passou

## Qualidade estrutural

- Tipos de create/detail em `types/guardian.ts`; chamadas em `guardianService.ts`
- Schemas de criança/anamnese reutilizados de `RegisterGuardian/schemas.ts`
- Pendência residual: o wizard em `ChildRegister/index.tsx` ainda concentra as 3 etapas no mesmo arquivo (reuso deliberado, sem extrair componentes nesta task)

## Aderencia ao design system

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md` (artefato)
- Formulário interno no shell, não no AuthLayout
- Sucesso em verde; erros em texto; empty state da listagem já existente
- Lacuna: sem print do cadastro interno; não foi inventado um produto visual novo

## Acessibilidade aplicada

- `ol` com `aria-label` nas etapas e `aria-current="step"`
- Labels associados; `fieldset`/`legend`; `radiogroup` nas perguntas de escolha única
- Erros com `role="alert"`; envio com `aria-busy`; banner de sucesso com `role="status"`
- Continuar da identidade desabilitado até o CPF do responsável estar disponível

## Pendencias pos-task

- Task 561: seletor de filho no mobile após login; empty state aponta para a web

## Status final

done
