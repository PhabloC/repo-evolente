# Task 331 - Vincular foto do paciente na aba de usuários web

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1admin~1professionals-tree`
- `contracts/openapi.yaml#/components/schemas/AdminProfessionalPatientNode`

## Modo de execucao

cross-stack

## Referencia de design system

### Stack de referencia visual

- front-end

### Tipo de referencia visual

artefato documental

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar a composicao atual da tabela de usuários e reutilizar o padrão de avatar/fallback já consolidado nas tabelas web de pacientes

## Contexto de negocio

### Por que

Na aba `Pacientes` da página de usuários, a criança ainda aparece só com inicial mesmo quando já possui foto de perfil enviada.

### O que

Fazer a rota `/admin/professionals-tree` expor `avatarUrl` do paciente e ligar a coluna `Usuário` da aba `Pacientes` para renderizar essa foto com o fallback nativo já adotado na web.

### Comportamento esperado

1. paciente com foto aparece com a imagem real na aba `Pacientes` da página `/usuarios`
2. paciente sem foto continua com fallback nativo já usado nas tabelas `/pacientes` e `/planejamentos`
3. modal de pacientes vinculados do profissional segue consistente com a mesma regra visual

### Fora de escopo

- upload/remoção de foto
- mudanças no mobile
- redesign da tabela de usuários

## Slice vertical

### Identificador do slice

Slice 027 - Fotos de perfil em bucket

### Arquivo do slice

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Dependencias

- Task 162 - done
- Task 182 - done
- Task 183 - done
- Task 192 - done
- Task 193 - done
- Task 295 - done

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-182.md`
- `.agents/state/handoffs/TASK-295.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Contrato admin | `contracts/openapi.yaml` | validar schema da árvore admin | sim |
| Backend admin | `backend/src/modules/admin/**` | expor `avatarUrl` na árvore de profissionais/pacientes | sim |
| Stack front | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | reaproveitar componente/avatar com a11y | sim |
| Página usuários | `front-end/src/pages/Main/AdminUsers/**` | renderizar foto do paciente na aba `Pacientes` e no modal de vínculos | sim |
| Avatar reutilizável | `front-end/src/components/PatientAvatar/**` | manter o mesmo fallback nativo por sexo | sim |
| Tipos admin | `front-end/src/types/admin.ts` | tipagem da árvore admin | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar a mudança ao payload da árvore admin e à renderização da aba `Pacientes`, sem reabrir outros fluxos de upload ou listagens

## Criterios de conclusao

- `avatarUrl` do paciente passa a existir no contrato e no retorno da árvore admin
- aba `Pacientes` da página de usuários renderiza foto real quando houver
- ausência de foto usa o mesmo fallback nativo já consolidado na web
- testes de backend e front-end cobrindo o novo campo/visual passam

## Validacao esperada

- `cd backend && npm run test -- admin.service.spec.ts`
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx src/components/PatientAvatar/resolvePatientAvatarSource.test.ts`
- `cd front-end && npm run build`

## Resultado da execucao

### Resumo por stack

- **backend**: a rota `/admin/professionals-tree` passou a expor `avatarUrl` e `sex` em cada paciente vinculado.
- **front-end**: a aba `Pacientes` da página de usuários e o modal de pacientes vinculados passaram a renderizar a foto real do paciente com `PatientAvatar`.

### Relação com o slice

- estende o Slice 027 para cobrir também a árvore administrativa de vínculos, que ainda não refletia a foto do paciente mesmo após as entregas anteriores de avatar.

### Decisões técnicas

- o contrato `AdminProfessionalPatientNode` foi ampliado com `avatarUrl` e `sex` para alinhar a árvore admin ao padrão já usado nas tabelas `/pacientes` e `/planejamentos`
- a UI de `AdminUsers` reaproveita `PatientAvatar` em vez de manter fallback por inicial só nessa tela
- o modal de pacientes vinculados do profissional usa a mesma estrutura de `PatientRow` para evitar divergência visual

### Trade-offs

- o `build` do front-end continua falhando por erro pré-existente em `src/pages/Main/Library/GamePreviewModal.tsx`, fora do escopo desta task

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-182.md`
- `.agents/state/handoffs/TASK-295.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | contrato admin | expor `avatarUrl` e `sex` na árvore |
| `backend/src/modules/admin/**` | backend admin | mapear novos campos e validar com teste |
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | stack front com UI | orientar reuso do avatar e a11y |
| `front-end/src/pages/Main/AdminUsers/**` | página usuários | renderizar foto na aba `Pacientes` e no modal |
| `front-end/src/components/PatientAvatar/**` | fallback consolidado | reaproveitar regra de avatar do paciente |
| `front-end/src/types/admin.ts` | tipagem | alinhar a árvore admin ao novo payload |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-331.md`

## Arquivos alterados

- `backend/src/modules/admin/admin.service.ts`
- `backend/src/modules/admin/admin.service.spec.ts`
- `contracts/openapi.yaml`
- `front-end/src/types/admin.ts`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `tasks/change-requests/331-vincular-foto-paciente-na-aba-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-331.md`

## Validacoes executadas

- `cd backend && npm run test -- admin.service.spec.ts` — ok
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx src/components/PatientAvatar/resolvePatientAvatarSource.test.ts` — ok
- `cd front-end && npm run build` — falhou por erro pré-existente em `src/pages/Main/Library/GamePreviewModal.tsx` (`content.gameConfig` possivelmente nulo e `voiceMode` ausente em parte do union)

## Pendencias pos-task

- revalidar o `build` do front-end depois de corrigir o erro pré-existente em `src/pages/Main/Library/GamePreviewModal.tsx`

## Status final

done
