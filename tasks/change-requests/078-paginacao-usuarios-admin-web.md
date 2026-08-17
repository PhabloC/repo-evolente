# Task 078 - Adicionar paginação na tabela de usuários do admin web

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

- nao altera contrato; reutiliza a paginação já suportada por `GET /users`

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

padrao ja consolidado na tabela de pacientes

### Fonte primaria visual

- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css}`

### Lacunas

- sem print dedicado para a paginação do admin
- decisao: aplicar o mesmo rodape compacto de paginação usado em `Pacientes`, preservando a linguagem do modulo

## Objetivo

Adicionar paginação na tabela de usuários do admin para reduzir densidade visual e permitir navegação consistente em listas maiores.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-077.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css}` | espelhar o padrão de paginação compacto | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | preservar `nav`, `aria-live` e estado de página atual | sim |
| Implementação atual | `front-end/src/pages/Main/Admin/{sections.tsx,useAdminWorkspace.tsx,styles.module.css}` | aplicar a paginação na listagem de usuários | sim |
| Rota alvo | `front-end/src/pages/Main/AdminUsers/index.tsx` | validar a integração final da página | sim |
| Service | `front-end/src/services/users/userService.ts` e `front-end/src/types/admin.ts` | reutilizar paginação real do endpoint `/users` | sim |
| Teste | `front-end/src/pages/Main/AdminUsers/index.test.tsx` | cobrir troca de página e faixa exibida | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à listagem de usuários do admin, sem tocar overview, planos, logs ou backend

## Criterios de conclusao

- [x] tabela de usuários passa a paginar em lotes consistentes
- [x] troca de filtro reseta para a primeira página
- [x] resumo da faixa exibida e navegação por página ficam visíveis e acessíveis
- [x] teste da rota e validações do front-end aprovados

## Dependencias

- Task 045 - done
- Task 071 - done
- Task 077 - done

## Resultado da execucao

- a listagem de usuários do admin passou a usar paginação real do endpoint `/users`, em lotes de 10 itens
- a seção ganhou rodapé com resumo da faixa exibida e navegação compacta por páginas, alinhada ao padrão de `Pacientes`
- mudanças de filtro resetam para a primeira página e a tela corrige automaticamente a página atual quando o total muda
- foi adicionado teste cobrindo a navegação da primeira para a segunda página

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-077.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css}`
- `front-end/src/pages/Main/Admin/{sections.tsx,useAdminWorkspace.tsx,styles.module.css}`
- `front-end/src/pages/Main/AdminUsers/{index.tsx,index.test.tsx}`
- `front-end/src/services/users/userService.ts`
- `front-end/src/types/admin.ts`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver mudança de contrato
- backend, mobile e outras rotas do admin por nao participarem da listagem de usuários

## Handoff

- `.agents/state/handoffs/TASK-078.md`

## Arquivos alterados

- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `tasks/change-requests/078-paginacao-usuarios-admin-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-078.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx` - ok
- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
