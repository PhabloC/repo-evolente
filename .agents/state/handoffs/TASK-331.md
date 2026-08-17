# Handoff - Task 331

## Task

- identificador: 331
- titulo: Vincular foto do paciente na aba de usuários web
- tipo: shared
- modo de execucao: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 027 - Fotos de perfil em bucket
- objetivo de negocio: refletir a foto do paciente também na árvore administrativa exibida na página de usuários
- entrega verificavel: a aba `Pacientes` de `/usuarios` e o modal de vínculos exibem a foto real quando houver `avatarUrl`
- status do slice: done

## Decisoes preservadas

- a rota `/admin/professionals-tree` agora inclui `avatarUrl` e `sex` em `AdminProfessionalPatientNode`
- `AdminUsers` reaproveita `PatientAvatar` para manter o mesmo fallback nativo por sexo já consolidado nas tabelas `/pacientes` e `/planejamentos`
- a estrutura `PatientRow` local passou a carregar `avatarUrl` e `sex` tanto para a aba `Pacientes` quanto para o modal de pacientes vinculados

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/331-vincular-foto-paciente-na-aba-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-182.md`
- `.agents/state/handoffs/TASK-295.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | contrato admin | schema da árvore |
| `backend/src/modules/admin/**` | backend admin | payload + teste |
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | stack front e UI | reuso do avatar e a11y |
| `front-end/src/pages/Main/AdminUsers/**` | página usuários | renderização da aba e do modal |
| `front-end/src/components/PatientAvatar/**` | fallback consolidado | componente reutilizado |
| `front-end/src/types/admin.ts` | tipagem | sincronização do payload |

## Resultado por stack

- backend: a árvore admin agora retorna `avatarUrl` e `sex` para cada paciente vinculado
- front-end: a aba `Pacientes` e o modal de vínculos exibem a foto do paciente com `PatientAvatar`

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

## Validacoes executadas

- `cd backend && npm run test -- admin.service.spec.ts`: ok
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx src/components/PatientAvatar/resolvePatientAvatarSource.test.ts`: ok
- `cd front-end && npm run build`: falhou por erro pré-existente em `src/pages/Main/Library/GamePreviewModal.tsx`

## Pendencias ou bloqueios

- sem bloqueio para esta task
- build global do front-end segue pendente por erro fora do escopo em `src/pages/Main/Library/GamePreviewModal.tsx`

## Proxima acao sugerida

- corrigir o typing de `GamePreviewModal` e reexecutar `npm run build` do front-end quando essa dívida entrar em escopo

## Proximo contexto recomendado

- `src/pages/Main/AdminUsers/index.tsx`
- `src/components/PatientAvatar/index.tsx`
- `backend/src/modules/admin/admin.service.ts`
