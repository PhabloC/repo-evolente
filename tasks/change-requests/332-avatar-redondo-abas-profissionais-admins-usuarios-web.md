# Task 332 - Avatar redondo nas abas profissionais e admins da página de usuários web

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

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

- front-end

### Tipo de referencia visual

artefato documental

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- manter a composição atual da tabela de usuários, alterando apenas o raio do avatar exibido nas abas `Profissionais` e `Admins`

## Contexto de negocio

### Por que

As fotos de perfil nas abas `Profissionais` e `Admins` da página de usuários ainda aparecem com cantos arredondados, mas não totalmente redondos.

### O que

Deixar o avatar dessas duas abas com borda totalmente redonda.

### Comportamento esperado

1. foto de perfil em `Profissionais` aparece circular
2. foto de perfil em `Admins` aparece circular
3. aba `Pacientes` mantém o avatar próprio já ajustado na task 331

### Fora de escopo

- mudança de payload
- redesign da tabela
- ajustes de avatar em outras telas

## Slice vertical

### Identificador do slice

Slice 027 - Fotos de perfil em bucket

### Arquivo do slice

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Dependencias

- Task 182 - done
- Task 183 - done
- Task 331 - done

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-182.md`
- `.agents/state/handoffs/TASK-331.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Stack front | `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | ajuste visual local com reuso do módulo admin | sim |
| Página usuários | `front-end/src/pages/Main/AdminUsers/**` | validar impacto das abas `Profissionais` e `Admins` | sim |
| Workspace admin | `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx` | confirmar render compartilhado do avatar | sim |
| Estilo admin | `front-end/src/pages/Main/Admin/styles.module.css` | aplicar o raio redondo do avatar | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar a mudança ao CSS compartilhado do avatar de usuário no módulo admin

## Criterios de conclusao

- avatar da aba `Profissionais` fica circular
- avatar da aba `Admins` fica circular
- testes relevantes da página continuam passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: o avatar exibido nas abas `Profissionais` e `Admins` da página de usuários passou a usar borda totalmente redonda.

### Relação com o slice

- refina o Slice 027 na superfície administrativa já existente, sem alterar payloads ou regras de upload.

### Decisões técnicas

- o ajuste foi concentrado em `front-end/src/pages/Main/Admin/styles.module.css`, no estilo compartilhado `userAvatar`
- a aba `Pacientes` não foi alterada porque já usa um avatar próprio definido na task 331

### Trade-offs

- o raio circular passa a valer para os usos do avatar compartilhado do módulo admin que reaproveitam `userAvatar`

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-182.md`
- `.agents/state/handoffs/TASK-331.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,COMPONENT_REUSE.md,ACCESSIBILITY.md}` | ajuste visual local | confirmar reuso do módulo |
| `front-end/src/pages/Main/AdminUsers/**` | página usuários | validar impacto nas abas |
| `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx` | render compartilhado | confirmar aba `Admins` |
| `front-end/src/pages/Main/Admin/styles.module.css` | estilo admin | aplicar avatar circular |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-332.md`

## Arquivos alterados

- `front-end/src/pages/Main/Admin/styles.module.css`
- `tasks/change-requests/332-avatar-redondo-abas-profissionais-admins-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-332.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
