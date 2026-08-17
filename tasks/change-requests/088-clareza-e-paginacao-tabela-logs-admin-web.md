# Task 088 - Clareza e paginação da tabela de logs do admin web

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

- nao se aplica; refino de apresentação sobre dados já disponíveis no módulo master

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

print de tela enviado no chat

### Fonte primaria visual

- `front-end/src/pages/Main/AdminLogs/index.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/sections.tsx`

### Lacunas

- sem novo layout externo; decisao: manter a tabela existente e refinar apenas clareza textual e paginação

## Objetivo

Deixar a tabela de logs do admin mais compreensível, exibindo ação e recurso em linguagem clara, mostrando nomes no lugar de IDs e adicionando paginação de 6 itens por página.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-087.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Logs admin | `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx` | enriquecer ação, recurso e ator; aplicar paginação local | sim |
| UI da tabela | `front-end/src/pages/Main/Admin/sections.tsx` | renderizar rodapé de paginação da seção de logs | sim |
| Página de logs | `front-end/src/pages/Main/AdminLogs/index.tsx` | repassar estado de paginação para a seção | sim |
| Tipos admin | `front-end/src/types/admin.ts` | reutilizar tipos atuais do log e assinaturas | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | garantir semântica e navegação da paginação | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao fluxo de logs do admin, sem alterar backend ou contrato

## Criterios de conclusao

- [x] coluna `Ação` fica em linguagem clara
- [x] coluna `Recurso` não exibe IDs brutos quando houver nome resolvível
- [x] coluna `Ator` mostra nome quando existir usuário associado
- [x] paginação local de 6 itens por página implementada
- [x] lint e build do front-end aprovados

## Dependencias

- Task 085 - done

## Resultado da execucao

- a coluna `Ação` foi traduzida para linguagem mais clara, incluindo status de usuário e assinatura
- a coluna `Recurso` passou a mostrar nomes resolvidos em vez de IDs quando o dado já existe no módulo admin
- a coluna `Ator` agora mostra nome do usuário quando houver correspondência; caso contrário, mantém `Sistema`
- a seção de logs ganhou paginação local de 6 itens por página com o mesmo padrão visual das demais tabelas do admin

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-087.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/AdminLogs/index.tsx`

### Contexto evitado

- backend, contrato OpenAPI e módulo clínico de relatórios por nao participarem deste refino de apresentação

## Handoff

- `.agents/state/handoffs/TASK-088.md`

## Arquivos alterados

- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/AdminLogs/index.tsx`
- `tasks/change-requests/088-clareza-e-paginacao-tabela-logs-admin-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-088.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
