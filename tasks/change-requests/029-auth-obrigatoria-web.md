# Task 029 - Reativar autenticacao obrigatoria web

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

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- Layout de login ja entregue na Task 026 (sem redesign)

### Regra de aderencia visual

- Nao redesenhar `/login`; apenas remover hint/CTA de acesso livre e restaurar protecao de rotas.

## Origem da solicitacao

Pedido do usuario: a partir de agora o sistema precisa de senha (autenticacao obrigatoria), encerrando o acesso livre temporario da Task 026.

## Objetivo

Reverter o bypass de `PrivateRoutes`/`RoleGuard` e exigir sessao autenticada (e-mail/senha) para acessar a area principal web.

## Escopo

- Restaurar redirect para `/login` em `PrivateRoutes` quando `!isAuthenticated`.
- Restaurar exigencia de perfil autenticado em `RoleGuard`.
- Remover CTA/hint "explorar o dashboard" / acesso livre da LoginPage.
- Remover navegacao guest (sidebar como profissional sem sessao) em `getNavigationForRole`.
- Atualizar testes afetados (LoginPage e, se houver, guards).

## Fora de escopo

- Backend/API
- Mobile
- Redesign visual do login
- Cadastro, recovery, gate de assinatura (exceto impacto indireto do redirect)

## Entradas

- `tasks/change-requests/026-login-visual-acesso-livre-web.md` (origem do bypass)
- `.agents/state/handoffs/TASK-026.md` (instrucoes de reversao)
- codigo: `PrivateRoutes`, `RoleGuard`, `navigation.ts`, `LoginPage`

## Dependencias

- Task 026 (login visual + acesso livre) — done

## Slice vertical

### Identificador do slice

Slice 015 - Autenticacao obrigatoria web

### Arquivo do slice

- `tasks/slices/015-auth-obrigatoria-web.md`

### Objetivo de negocio

Exigir login com senha para area principal web.

### Entrega verificavel do slice

Sem sessao, area principal inacessivel; login real continua o unico caminho de entrada.

### Fora do slice

- Mobile, API, redesign visual

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/015-auth-obrigatoria-web.md`
- `.agents/state/handoffs/TASK-026.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Bypass atual | `front-end/src/routes/PrivateRoutes.tsx`, `RoleGuard.tsx`, `constants/navigation.ts`, `pages/Auth/Login/**` | reverter | sim |
| Padroes front | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md` | implementar | sim |
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | se UI do login mudar | sim se UI |

## Orçamento de contexto

- Fontes obrigatorias estimadas: 7
- Fontes sob demanda estimadas: 4
- Risco: baixo
- Estrategia de reducao: nao carregar mobile, backend, openapi, design-system, requirements; nao redesenhar login

## Criterios de conclusao

- [x] Sem sessao, rotas privadas redirecionam para `/login`
- [x] RoleGuard nao libera rota sem autenticacao
- [x] Hint/CTA de acesso livre removido da LoginPage
- [x] Sidebar sem navegacao guest profissional
- [x] Testes atualizados e passando
- [x] lint/test/build ok no front-end

## Instrucoes de implementacao

1. Em `PrivateRoutes`: se `!isAuthenticated`, `Navigate` para `routePaths.login` (remover early-return com `<Outlet />`).
2. Em `RoleGuard`: se `!isAuthenticated`, redirecionar para login (ou forbidden consistente com o padrao anterior ao bypass); nao liberar Outlet.
3. Em `getNavigationForRole(null)`: retornar array vazio (ou equivalente seguro), nao itens de profissional.
4. Remover bloco `guestHint` / link "explorar o dashboard" da LoginPage e estilos associados se ficarem orfaos.
5. Atualizar `LoginPage` tests (remover expectativa do link explorar).
6. Manter formulario de login e fluxo real de API intactos.

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Auth/Login`
- `cd front-end && npm run lint`
- `cd front-end && npm run build`

## Entregaveis esperados

- Guards restaurados
- Login sem CTA de acesso livre
- Testes atualizados
- Handoff `.agents/state/handoffs/TASK-029.md`

## Riscos ou ambiguidades

- Gate de assinatura continua valendo apos autenticacao (nao alterar nesta task)
- Mobile permanece fora de escopo

## Resultado da execucao

### Resumo por stack

- **front-end**: bypass de acesso livre revertido; area principal exige sessao; CTA guest removido da LoginPage.

### Relação com o slice

- Slice 015 concluído nesta task.

### Decisões técnicas

- `PrivateRoutes` e `RoleGuard` redirecionam para `/login` sem sessão.
- `getNavigationForRole(null)` retorna `[]`.
- Removidos hint guest e estilo `.guestHint`.
- Teste de Login deixa de esperar footer LGPD (removido no AuthLayout da Task 028).

### Trade-offs

- Nenhum relevante; restaura comportamento de produção esperado.

### Contrato

- nao se aplica

### Referência visual

- Sem redesign; apenas remoção do hint de acesso livre.

### Acessibilidade

- Remoção de link guest; formulário de login e labels permanecem intactos.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/015-auth-obrigatoria-web.md`
- `.agents/state/handoffs/TASK-026.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| PrivateRoutes / RoleGuard / navigation / Login | reverter bypass | implementação |
| ARCHITECTURE.md | padroes front | confirmação de proteção de rotas |

### Evitado

- mobile/, backend/, openapi, design-system, requirements

## Handoff

- Caminho: `.agents/state/handoffs/TASK-029.md`
- Decisões: guards restaurados; nav guest removida; CTA explorar removido
- Próximo contexto: validar login real com usuário master
- Pendências: nenhuma de bypass web

## Arquivos alterados

### raiz / governanca

- `tasks/change-requests/029-auth-obrigatoria-web.md`
- `tasks/slices/015-auth-obrigatoria-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-029.md`

### front-end

- `front-end/src/routes/PrivateRoutes.tsx`
- `front-end/src/routes/RoleGuard.tsx`
- `front-end/src/constants/navigation.ts`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/Login/styles.module.css`
- `front-end/src/pages/Auth/Login/index.test.tsx`

## Validacoes executadas

- `npm run test -- --run src/pages/Auth/Login` — ok
- `npm run lint` — ok
- `npm run build` — ok

## Pendencias pos-task

- Nenhuma pendência de bypass web
- Mobile permanece fora deste escopo

## Status final

done
