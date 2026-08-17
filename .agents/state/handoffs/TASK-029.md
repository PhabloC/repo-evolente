# Handoff - Task 029

## Task

- identificador: 029
- título: Reativar autenticacao obrigatoria web
- tipo: front
- modo de execução: single-stack
- status final: done
- arquivo: `tasks/change-requests/029-auth-obrigatoria-web.md`

## Slice vertical

- identificador: Slice 015 - Autenticacao obrigatoria web
- objetivo de negócio: exigir login com senha na área principal web
- entrega verificável: guards restaurados; sem CTA de acesso livre
- status do slice: done

## Decisões preservadas

- decisão: `PrivateRoutes` e `RoleGuard` redirecionam para `/login` sem sessão
- motivo: encerrar bypass temporário da Task 026
- impacto: área principal inacessível sem autenticação

- decisão: `getNavigationForRole(null)` retorna `[]`
- motivo: não expor sidebar guest como profissional
- impacto: navegação só com role autenticado

- decisão: remover hint/CTA "explorar o dashboard" da LoginPage
- motivo: acesso livre não é mais permitido
- impacto: login real é o único caminho de entrada

- decisão: teste de Login deixa de exigir footer LGPD
- motivo: footer foi removido no AuthLayout unificado (Task 028); asserção órfã
- impacto: teste alinhado ao DOM atual

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, CR-029, slice 015, handoff TASK-026

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| PrivateRoutes / RoleGuard / navigation / Login | reverter bypass | implementação |
| ARCHITECTURE.md | padroes front | confirmação de fluxo de rotas |

### Evitado

- mobile/, backend/, openapi, design-system, requirements

## Arquivos alterados

- `front-end/src/routes/PrivateRoutes.tsx`
- `front-end/src/routes/RoleGuard.tsx`
- `front-end/src/constants/navigation.ts`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/Login/styles.module.css`
- `front-end/src/pages/Auth/Login/index.test.tsx`
- governança: slice 015, CR-029, index, este handoff

## Validações executadas

- `npm run test -- --run src/pages/Auth/Login` — ok
- `npm run lint` — ok
- `npm run build` — ok

## Pendências

- Nenhuma pendência de bypass web
- Mobile auth permanece no escopo do próprio app (fora desta task)

## Próxima ação sugerida

- Validar login real com o usuário master criado (`phablo@fasters.com.br`)

## Próximo contexto recomendado

- Handoff desta task; não recarregar Task 026 inteira

## Contexto que não deve ser carregado

- `mobile/`, `backend/`, `contracts/openapi.yaml`, requirements inteiros (salvo nova demanda)
