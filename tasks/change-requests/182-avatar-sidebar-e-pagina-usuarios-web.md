# Task 182 - Avatar no sidebar e na página de usuários web

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

- `contracts/openapi.yaml#/components/schemas/User` (`avatarUrl` já exposto)
- `contracts/openapi.yaml#/paths/~1users` (listagem já retorna `User`)

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

- reutilizar o padrão visual já consolidado de avatar circular com fallback por inicial nas páginas de perfil

## Contexto de negocio

### Por que

A foto de perfil já é persistida e aparece em Configurações, mas o rodapé do sidebar e a listagem de usuários ainda mostram apenas a inicial.

### O que

Exibir `avatarUrl` no rodapé do sidebar (usuário autenticado) e na coluna de identidade da página de usuários master.

### Comportamento esperado

- com foto: sidebar e página de usuários renderizam a imagem
- sem foto: mantêm a inicial como fallback
- após upload em Configurações, o sidebar reflete a nova foto sem relogin (via `authStore`)

### Fora de escopo

- upload/remoção/crop de foto
- avatar no mobile
- foto de pacientes em outras listagens
- alterações de API/backend (já retorna `avatarUrl`)

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissões: não se aplica (somente leitura de URL já autorizada na sessão/listagem)
- Casos de borda: `avatarUrl` nulo/ausente → inicial; imagem quebrada pode cair no fallback visual se tratado
- Dependência: Task 162 já entregou upload e `avatarUrl` no contrato/API

## Especificacao tecnica

### Deve

- passar `avatarUrl` do `authStore`/`useAuth` para o `Sidebar`
- renderizar imagem no footer do sidebar quando houver URL
- tipar `AdminUser` com `avatarUrl` e renderizar na coluna Usuário
- manter fallback por inicial

### Nao deve

- não alterar endpoints
- não alterar upload de foto
- não mudar layout geral do shell além do avatar

## Entradas

- `.agents/state/handoffs/TASK-162.md`
- `front-end/src/layout/Sidebar/**`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`

## Dependencias

- Task 162

## Slice vertical

### Identificador do slice

Slice 027 - Fotos de perfil em bucket

### Arquivo do slice

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

### Objetivo de negócio

Refletir a foto de perfil já persistida nos pontos de identidade do shell e da gestão de usuários.

### Entrega verificável do slice

Sidebar e página de usuários exibem `avatarUrl` com fallback por inicial.

### Fora do slice

- mobile
- edição de foto nestas telas

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-162.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Sidebar | `front-end/src/layout/Sidebar/**`, `MainLayout` | renderizar avatar do usuário logado | sim |
| Página usuários | `front-end/src/pages/Main/Admin/**`, `AdminUsers/**` | renderizar avatar na tabela | sim |
| Tipos | `front-end/src/types/admin.ts`, `useAuth` | tipagem e prop | sim |
| Front docs | `front-end/docs/ai/CODE_STYLE.md`, `ACCESSIBILITY.md` | a11y de imagem | sob demanda |

## Orçamento de contexto

- Risco baixo
- Estratégia de redução: só UI de sidebar + coluna de usuários; API já cobre `avatarUrl`

## Criterios de conclusao

- sidebar mostra foto quando `user.avatarUrl` existe
- página de usuários mostra foto quando o item tem `avatarUrl`
- fallback por inicial preservado
- lint e testes relevantes passam

## Instrucoes de implementacao

- usar `object-fit: cover` em avatares circulares
- `alt` descritivo com o nome do usuário
- tipar `avatarUrl` em `AdminUser` como `string | null` opcional/compatível com a API

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/layout/Sidebar src/pages/Main/AdminUsers`
- `cd front-end && npm run build`

## Entregaveis esperados

- Sidebar com avatar real
- Página de usuários com avatar real
- Task/slice/índice/handoff atualizados

## Resultado da execucao

### Resumo por stack

- **front-end**: o rodapé do sidebar e a coluna Usuário da página de usuários passam a renderizar `avatarUrl` com fallback por inicial.

### Relação com o slice

- Completa a exibição da foto já persistida (Task 162) nos pontos de identidade do shell e da gestão master.

### Decisões técnicas

- Sem mudança de API: a listagem `/users` e a sessão já expõem `avatarUrl`.
- `MainLayout` repassa `user?.avatarUrl` do `authStore` para o `Sidebar`.
- `AdminUser` ganhou `avatarUrl?: string | null` para tipar a listagem.

### Trade-offs

- Sem tratamento especial de imagem quebrada além do `alt` descritivo.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-162.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/layout/Sidebar/**`, `MainLayout` | sidebar | prop e renderização |
| `front-end/src/pages/Main/Admin/**`, `AdminUsers/**` | listagem | coluna Usuário |
| `front-end/src/types/admin.ts` | tipagem | `avatarUrl` em `AdminUser` |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-182.md`
- Próximo contexto recomendado: mobile/responsável apenas se a foto precisar aparecer no app

## Arquivos alterados

### Front-end

- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/styles.module.css`
- `front-end/src/layout/Sidebar/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/types/admin.ts`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

### Governança

- `tasks/change-requests/182-avatar-sidebar-e-pagina-usuarios-web.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-182.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npm run test -- --run src/layout/Sidebar src/pages/Main/AdminUsers` — ok (reexecução AdminUsers ok; falhas anteriores foram timeout flaky sob carga)
- `cd front-end && npm run build` — ok

## Aderencia ao design system

- Mantido avatar circular/arredondado com `object-fit: cover` e fallback por inicial.

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
