# Task 295 - Foto e fallback nativo nas tabelas de pacientes e planejamentos web

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

- nao se aplica; `avatarUrl` e `sex` ja estao presentes no payload de pacientes

## Modo de execucao

single-stack

## Slice vertical

- Slice 027 - Fotos de perfil em bucket
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Referencia visual

### Tipo

comportamento existente no mobile + padrao visual ja consolidado nas tabelas web

### Cobertura

- tabela da pagina `/pacientes`
- tabela da pagina `/planejamentos`

### Lacunas

- sem novo print dedicado; a composicao atual das tabelas deve ser preservada

## Objetivo

Exibir a foto real do paciente nas tabelas de pacientes e planejamentos quando `avatarUrl` existir e, quando nao existir, usar o mesmo fallback nativo por sexo ja consolidado no mobile em vez de iniciais.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-182.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Stack front | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | organizar componente reutilizavel e a11y | sim |
| Tabela pacientes | `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}` | ligar avatar real na listagem de pacientes | sim |
| Tabela planejamentos | `front-end/src/pages/Main/Plans/{index.tsx,index.test.tsx,styles.module.css}` | ligar avatar real na listagem de planejamentos | sim |
| Regra de fallback | `mobile/src/features/profile/utils/resolveChildAvatarSource.ts` | espelhar fallback nativo por sexo | sim |
| Tipos | `front-end/src/types/guardian.ts` | reusar `sex` e `avatarUrl` do paciente | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a mudanca a exibição web dos avatares do paciente, sem reabrir upload, backend ou mobile fora da regra de fallback

## Criterios de conclusao

- [x] tabela de pacientes mostra foto real quando `avatarUrl` existir
- [x] tabela de planejamentos mostra foto real quando `avatarUrl` existir
- [x] ausencia de foto cai em fallback nativo por sexo, sem voltar para iniciais
- [x] testes cobrindo pelo menos um caso com foto real e um com fallback

## Dependencias

- Task 162 - done
- Task 182 - done
- Task 212 - done
- Task 294 - done

## Resultado da execucao

- as tabelas de pacientes e planejamentos passaram a renderizar `avatarUrl` quando existir
- quando a foto estiver ausente ou falhar ao carregar, a web cai no mesmo fallback nativo por sexo usado no mobile (`masculino`, `feminino`, `neutro`)
- a regra de avatar foi isolada em um componente `PatientAvatar` com resolver reutilizavel para evitar duplicacao entre as duas paginas

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-182.md`

### Sob demanda

- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/pages/Main/Plans/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/components/PatientAvatar/{index.tsx,resolvePatientAvatarSource.ts,resolvePatientAvatarSource.test.ts}`
- `front-end/src/types/guardian.ts`
- `mobile/src/features/profile/utils/resolveChildAvatarSource.ts`

### Contexto evitado

- `contracts/openapi.yaml`, porque `avatarUrl` e `sex` ja estavam expostos e nao exigiram mudanca de contrato
- `backend/`, porque a entrega ficou restrita a exibição no front-end
- outras paginas web com avatar, porque o escopo pedido foi apenas pacientes e planejamentos

## Handoff

- `.agents/state/handoffs/TASK-295.md`

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
- `.agents/state/handoffs/TASK-295.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.test.tsx src/components/PatientAvatar/resolvePatientAvatarSource.test.ts` - ok
- `cd front-end && npm run lint` - sem retorno util no ambiente durante esta execucao
- `cd front-end && npx eslint src/components/PatientAvatar/index.tsx src/components/PatientAvatar/resolvePatientAvatarSource.ts src/components/PatientAvatar/resolvePatientAvatarSource.test.ts src/pages/Main/Patients/index.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.tsx src/pages/Main/Plans/index.test.tsx` - sem retorno util no ambiente durante esta execucao

## Pendencias pos-task

- nenhuma bloqueante; se quiser, vale investigar depois por que o lint ficou sem saida neste ambiente

## Status final

done
