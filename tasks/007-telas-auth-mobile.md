# Task 007 - Telas de autenticacao mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` auth

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- Login mobile sem fluxo infantil/gamificado.

## Contexto de negocio

### Por que

Master e responsavel acessam o app.

### O que

Login e recovery no mobile.

### Comportamento esperado

- Login
- Recovery
- Redirect master/responsavel

### Fora de escopo

- Cadastro multi-etapa no mobile

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master e responsavel
- Casos de erro: credenciais; inativo
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: profissional no mobile

## Especificacao tecnica

### Deve

- Toque >= 44px

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Cadastro completo no mobile

## Entradas

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/`
- `contracts/openapi.yaml`

## Dependencias

- Task 005

## Slice vertical

### Identificador do slice

Slice 002 - Autenticacao

### Arquivo do slice

- `tasks/slices/002-autenticacao.md`

### Objetivo de negócio

Auth mobile.

### Entrega verificável do slice

Telas auth mobile.

### Fora do slice

- Web

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
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | mobile | sim |
| API | `contracts/openapi.yaml` | API | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Login master/responsavel

## Instrucoes de implementacao

- Orientar profissional ao web

## Validacao esperada

- npm run lint
- npm run typecheck
- npm run test

## Entregaveis esperados

- Telas auth mobile

## Riscos ou ambiguidades



## Resultado da execucao

### Resumo por stack

- **mobile**: login real (OpenAPI AuthResponse), recovery e reset; remoção do preview de role da Task 004; redirect master/responsável via shell existente; profissional → `UnsupportedRoleScreen` (“Use a web”).

### Relação com o slice

- Entrega mobile do Slice 002 concluída. Slice 002 → **done** (005 + 006 + 007).

### Decisões técnicas

- Adapter alinhado ao contrato camelCase (`user` + `tokens.accessToken`), não snake_case legado.
- Demo data (sem API) autentica como `responsavel` sem chips de preview.
- Bearer via interceptor do `apiClient` a partir do `useSessionStore`.
- Deep link `redefinir-senha` com param `token`.
- Nenhuma dependência nova.

### Trade-offs

- Sem prints: UI baseada em tokens DS + componentes shell existentes.
- Logout best-effort na API antes de limpar SecureStore.

### Contrato

- Consome `POST /auth/login`, `/auth/password-recovery`, `/auth/password-reset`, `/auth/logout`.

### Referência visual

- DS mobile documental; sem gamificação/fluxo infantil; alvos de toque ≥ 44px (botões 48, inputs 52, links 44).

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/002-autenticacao.md`
- handoff `TASK-006.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Mobile | UI | toque ≥44px; sem gamificação |
| openapi auth | API | payloads AuthResponse |
| ARCHITECTURE + CODE_STYLE | mobile | Screen→Hook→Service→Adapter |

### Evitado

- `design-system/front/`, `front-end/`, `backend/` (single-stack mobile)
- requirements inteiros

## Handoff

- Caminho: `.agents/state/handoffs/TASK-007.md`
- Decisões: auth real mobile; profissional → web; Slice 002 fechado
- Próximo contexto: Task 008 (API cadastro profissional) ou próxima do index
- Pendências: SMTP real; cadastros domínio

## Arquivos alterados

### mobile

- `mobile/src/features/auth/types/session.ts`
- `mobile/src/features/auth/adapters/adaptSession.ts`
- `mobile/src/features/auth/adapters/adaptSession.test.ts`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/hooks/useSignInForm.ts`
- `mobile/src/features/auth/hooks/usePasswordRecoveryForm.ts`
- `mobile/src/features/auth/hooks/usePasswordResetForm.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/components/styles.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/PasswordResetScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/shared/network/apiClient.ts`
- `mobile/src/routes/params.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/config/linking.ts`
- `mobile/.env.example`

### governança

- `tasks/007-telas-auth-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-007.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run typecheck` — ok
- `npm run test` — ok (5 tests)

## Qualidade estrutural

- Tipos em `features/auth/types/`
- Adapter + service + hooks por responsabilidade
- Screens novas colocalizadas em `features/auth/screens/`

## Aderencia ao design system

- Fonte: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (artefato documental)
- Evidências: sem gamificação; copy orienta profissional à web; toque ≥44px
- Lacuna: sem prints de login

## Pendencias pos-task

- SMTP real no backend
- Cadastros de domínio (slices 003/004)
- Próxima task do backlog (ex.: 008 API cadastro profissional)

## Status final

done
