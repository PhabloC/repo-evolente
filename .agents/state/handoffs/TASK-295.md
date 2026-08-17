# Handoff - Task 295

## Task

- identificador: 295
- titulo: Foto e fallback nativo nas tabelas de pacientes e planejamentos web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 027 - Fotos de perfil em bucket
- objetivo de negocio: refletir a foto persistida do paciente tambem nas tabelas operacionais da web
- entrega verificavel: pacientes e planejamentos exibem foto real quando houver `avatarUrl` e fallback nativo por sexo quando nao houver

## Decisoes preservadas

- a web passou a espelhar a regra do mobile para paciente: `avatarUrl` tem prioridade; sem foto usa fallback local por `masculino`, `feminino` ou `neutro`
- a regra ficou encapsulada em `PatientAvatar` + `resolvePatientAvatarSource` para evitar divergencia entre `/pacientes` e `/planejamentos`
- se a imagem remota falhar ao carregar, o componente cai para o fallback nativo em vez de quebrar a célula

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/295-foto-e-fallback-nativo-nas-tabelas-de-pacientes-e-planejamentos-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-182.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `COMPONENT_REUSE.md`, `ACCESSIBILITY.md` | stack front e UI | orientar componentizacao e a11y |
| `front-end/src/pages/Main/Patients/**` | tabela de pacientes | ligar foto real e fallback |
| `front-end/src/pages/Main/Plans/**` | tabela de planejamentos | ligar foto real e fallback |
| `front-end/src/types/guardian.ts` | tipagem | reusar `sex` e `avatarUrl` |
| `mobile/src/features/profile/utils/resolveChildAvatarSource.ts` | comportamento existente no mobile | espelhar fallback por sexo |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | contrato ja cobria `avatarUrl` e `sex` |
| `backend/` | nenhuma alteracao de API/storage |
| outras rotas web com avatar | fora do escopo pedido |

## Resultado por stack

- front-end: tabelas de pacientes e planejamentos exibem foto real ou fallback nativo por sexo
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/public/avatars/child-masculino.png`
- `front-end/public/avatars/child-feminino.png`
- `front-end/public/avatars/child-neutro.png`
- `front-end/src/components/PatientAvatar/index.tsx`
- `front-end/src/components/PatientAvatar/resolvePatientAvatarSource.ts`
- `front-end/src/components/PatientAvatar/resolvePatientAvatarSource.test.ts`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Plans/index.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/295-foto-e-fallback-nativo-nas-tabelas-de-pacientes-e-planejamentos-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.test.tsx src/components/PatientAvatar/resolvePatientAvatarSource.test.ts`: ok
- `cd front-end && npm run lint`: sem retorno util no ambiente
- `cd front-end && npx eslint ...arquivos alterados`: sem retorno util no ambiente

## Pendencias ou bloqueios

- nenhuma bloqueante
- investigar separadamente por que o lint ficou sem saida neste ambiente, caso esse sintoma se repita

## Proxima acao sugerida

- seguir apenas se quiser levar o mesmo fallback nativo por sexo para outras listagens web de pacientes

## Proximo contexto recomendado

- `front-end/src/components/PatientAvatar/index.tsx`
- `front-end/src/components/PatientAvatar/resolvePatientAvatarSource.ts`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Plans/index.tsx`
