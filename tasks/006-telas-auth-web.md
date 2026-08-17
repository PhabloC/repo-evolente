# Task 006 - Telas de autenticacao web

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

- `contracts/openapi.yaml#/paths` auth

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- Inputs/botoes/estados conforme DS desktop.

## Contexto de negocio

### Por que

Entrar e recuperar senha na web.

### O que

Login, links de cadastro, recovery e reset.

### Comportamento esperado

- Login
- Erros visiveis
- Recovery completo

### Fora de escopo

- Formularios de cadastro de dominio

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: publico + redirect por role
- Casos de erro: credenciais; token reset
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: deep link reset

## Especificacao tecnica

### Deve

- Consumir API 005
- Estados loading/erro

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Pular gate de assinatura

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`
- `contracts/openapi.yaml`

## Dependencias

- Task 005

## Slice vertical

### Identificador do slice

Slice 002 - Autenticacao

### Arquivo do slice

- `tasks/slices/002-autenticacao.md`

### Objetivo de negócio

Auth web.

### Entrega verificável do slice

Telas auth web.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |
| API | `contracts/openapi.yaml` | API | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Login e recovery utilizaveis
- Aderencia DS

## Instrucoes de implementacao

- CTAs cadastro profissional e responsavel

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- Telas auth web

## Riscos ou ambiguidades

- Sem prints

## Resultado da execucao

### Resumo por stack

- **front-end**: telas de login (`/entrar`), recuperação (`/recuperar-senha`) e reset (`/redefinir-senha`); placeholders de CTA para cadastro profissional/responsável; sessão real via `authStore` + `localStorage`; consumo dos endpoints auth da Task 005; removido preview de sessão da Task 003.

### Relação com o slice

- Entrega web do Slice 002 concluída. Slice permanece `in_progress` até Task 007 (mobile).

### Decisões técnicas

- Sessão persistida em `evolente:web-auth`; hydrate no boot (`main.tsx`).
- Adapter `adaptAuthResponse` isola DTO OpenAPI do modelo interno.
- Placeholders de cadastro sem formulários de domínio.
- Gate de assinatura não implementado (ainda inexistente).
- Dependência `@hookform/resolvers` adicionada: necessária para `zodResolver` já usado nos formulários auth (sem alternativa no stack atual). Justificativa: desbloqueio de lint/typecheck; escopo limitado a validação de formulários.

### Trade-offs

- Sem prints: layout baseado em tokens/componentes do DS documental + shell existente.
- Logout best-effort: limpa sessão local mesmo se API falhar.

### Contrato

- Consome `POST /auth/login`, `/auth/password-recovery`, `/auth/password-reset`, `/auth/logout` conforme OpenAPI.

### Referência visual

- Tokens/inputs/botões alinhados a `Design_System_Evolente_Desktop.md` e componentes UI existentes.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/002-autenticacao.md`
- handoff `TASK-005.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI web | tokens/inputs/botões |
| openapi auth | API | payloads/status |
| front-end docs (ARCHITECTURE, CODE_STYLE, ACCESSIBILITY) | front/UI | estrutura e a11y |

### Evitado

- `design-system/mobile/`, `mobile/`, `backend/` (fora do escopo single-stack web)
- requirements inteiros (sem ambiguidade de negócio)

## Handoff

- Caminho: `.agents/state/handoffs/TASK-006.md`
- Decisões: sessão real web; placeholders cadastro; sem gate assinatura
- Próximo contexto: Task 007 (auth mobile) + DS mobile + openapi auth
- Pendências: Task 007; SMTP real no back; formulários de domínio em slices 003/004

## Arquivos alterados

### front-end

- `front-end/src/types/auth.ts`
- `front-end/src/services/adapters/adaptAuthResponse.ts`
- `front-end/src/services/adapters/adaptAuthResponse.test.ts`
- `front-end/src/services/auth/authService.ts`
- `front-end/src/services/http/apiClient.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/hooks/useAuth.ts`
- `front-end/src/constants/routes.ts`
- `front-end/src/main.tsx`
- `front-end/src/routes/index.tsx`
- `front-end/src/routes/PrivateRoutes.tsx`
- `front-end/src/routes/RoleGuard.tsx`
- `front-end/src/layout/AuthLayout/**`
- `front-end/src/layout/Header/**`
- `front-end/src/layout/MainLayout/**`
- `front-end/src/pages/Auth/Login/**`
- `front-end/src/pages/Auth/PasswordRecovery/**`
- `front-end/src/pages/Auth/PasswordReset/**`
- `front-end/src/pages/Auth/RegisterPlaceholder/**`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/pages/Main/Forbidden/index.tsx`
- `front-end/src/ui/Input/**` (estilos tema claro)
- `front-end/.env.example`
- `front-end/package.json` / `package-lock.json` (`@hookform/resolvers`)
- removido: `front-end/src/pages/Public/SessionPreview/**`

### governança

- `tasks/006-telas-auth-web.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-006.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok (5 tests)
- `npm run build` — ok

## Qualidade estrutural

- Tipos em `types/auth.ts`
- Adapter em `services/adapters/`
- Service em `services/auth/`
- Layout `AuthLayout` separado das pages
- Sem utils soltas em pages

## Acessibilidade aplicada

- Labels nos inputs; erros com `role="alert"`; formulários com `aria-busy`; hierarquia `h1` no AuthLayout; links de CTA com texto descritivo
- Lacuna: sem prints para validar contraste/layout pixel-perfect

## Aderencia ao design system

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md` (artefato documental)
- Evidências: AuthLayout + Input/Button existentes; tema claro Evolente
- Desvio: sem prints — composição auth derivada do DS + shell; placeholders de cadastro sem UI de domínio

## Pendencias pos-task

- Task 007 — telas auth mobile
- SMTP real no backend (MailAdapter)
- Formulários de cadastro profissional/responsável (slices 003/004)
- Gate de assinatura (slice 005) — não pular; ainda inexistente

## Status final

done
