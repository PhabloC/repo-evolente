# Task 030 - Politica de senha forte e confirmacao no reset

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/components/schemas` — password em RegisterProfessionalRequest, GuardianRegistrationData, PasswordResetRequest (e CreateUser se aplicavel)
- LoginRequest: manter apenas minLength (nao aplicar pattern forte no login)

## Modo de execucao

cross-stack

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- Telas auth existentes (sem redesign)

### Regra de aderencia visual

- Manter layout AuthLayout; apenas mensagens de validacao e campos ja existentes no reset.

## Origem da solicitacao

Pedido do usuario: senha em criacao de conta e recuperacao deve ter no minimo 8 caracteres, numero, letra maiuscula e caractere especial; no reset, inputs de nova senha e confirmacao devem coincidir.

## Objetivo

Padronizar validacao de senha forte no cadastro e na redefinicao, com confirmacao de senha no reset, alinhando front, backend e OpenAPI.

## Escopo

- Util compartilhado de validacao de senha no front (`utils/`) e regra equivalente no backend.
- Aplicar nos schemas/forms de cadastro profissional, cadastro responsavel e (se houver) criacao de conta em AddPatient.
- Em PasswordReset: manter/garantir campos Nova senha + Confirmar senha; exigir igualdade; aplicar politica forte na nova senha.
- Backend: DTOs de create/register e password-reset com a mesma politica.
- OpenAPI: documentar `minLength: 8` + `pattern` (ou description) da politica nos schemas de criacao/reset.
- Atualizar testes front/back afetados (senhas de fixture devem cumprir a politica).

## Fora de escopo

- Mobile
- Redesign visual
- Forcar reset em usuarios existentes
- Aplicar pattern forte no LoginRequest (apenas comprimento)

## Entradas

- Forms: `RegisterProfessional`, `RegisterGuardian`, `PasswordReset`, `AddPatient` (senha)
- DTOs: `create-user`, `register-professional`, `register-guardian`, `password-reset`
- `contracts/openapi.yaml` schemas de password
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`
- `backend/docs/ai/` essenciais se necessario

## Dependencias

- Task 006/009/011 (auth e cadastros web) — done
- Task 005 (API auth) — done
- Task 028 (template auth) — done

## Slice vertical

### Identificador do slice

Slice 016 - Politica de senha forte (web)

### Arquivo do slice

- `tasks/slices/016-politica-senha-forte-web.md`

### Objetivo de negocio

Senhas novas seguras e reset com confirmacao.

### Entrega verificavel do slice

Cadastro e reset rejeitam senha fraca; reset exige confirmacao igual.

### Fora do slice

- Mobile, redesign, login forte

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/016-politica-senha-forte-web.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Contrato | `contracts/openapi.yaml` (schemas password) | alinhar | sim |
| Front forms | Register*/PasswordReset/AddPatient | schemas | sim |
| Back DTOs | modules users/auth/professionals/guardians | validacao | sim |
| Docs | front-end/backend docs/ai essenciais | padroes | sim |

## Orçamento de contexto

- Fontes obrigatorias estimadas: 6
- Fontes sob demanda estimadas: 6
- Risco: baixo/medio
- Estrategia: nao carregar mobile, design-system, requirements; carregar so schemas/DTOs/forms de senha

## Criterios de conclusao

- [x] Politica: >=8, numero, maiuscula, especial — mensagem clara no front
- [x] Cadastro profissional e responsavel usam a politica
- [x] PasswordReset: nova + confirmar iguais + politica na nova senha
- [x] Backend rejeita senha fraca em create/register/reset
- [x] OpenAPI atualizado nos schemas de criacao/reset
- [x] Testes atualizados; lint/test/build (front) e lint/test (back) ok

## Instrucoes de implementacao

1. Definir regra unica (regex/util) e mensagem amigavel em PT-BR.
2. Front: `passwordSchema` Zod reutilizavel em `utils/` (ou schemas compartilhados de auth).
3. Aplicar em RegisterProfessional, RegisterGuardian/schemas, PasswordReset; AddPatient se criar senha.
4. PasswordReset: garantir dois inputs e `.refine` de igualdade (ja existe — reforcar politica).
5. Backend: decorator Matches ou validator compartilhado em `common/`; aplicar nos DTOs de senha de criacao/reset (nao no login).
6. OpenAPI: pattern + description nos passwords de registro/reset.
7. Atualizar fixtures de teste que usam senhas fracas (`senha12345`, `password123`, etc.).

## Validacao esperada

- `cd front-end && npm run test -- --run` (ou suites auth/register/reset afetadas)
- `cd front-end && npm run lint && npm run build`
- `cd backend && npm run test -- --testPathPattern="auth|users|professionals|guardians" ` (ou suite afetada)
- `cd backend && npm run lint`

## Entregaveis esperados

- Util/schema de senha forte
- Forms e DTOs atualizados
- OpenAPI alinhado
- Handoff `.agents/state/handoffs/TASK-030.md`

## Riscos ou ambiguidades

- Contas antigas com senha fraca continuam logando (desejavel)
- Definicao de "caractere especial": qualquer nao alfanumerico

## Resultado da execucao

### Resumo por stack

- **front-end**: `strongPasswordSchema` em cadastro profissional/responsavel (e AddPatient via schema) e PasswordReset; reset mantém nova + confirmar iguais.
- **backend**: decorator `IsStrongPasswordField`, `assertStrongPassword` em create/update/updatePassword; DTOs de register/create/reset atualizados.
- **contracts**: pattern + description nos passwords de registro e PasswordResetRequest; LoginRequest sem pattern forte.

### Relação com o slice

- Slice 016 concluído nesta task.

### Decisões técnicas

- Caractere especial = qualquer não alfanumérico.
- Login permanece só com minLength 8.
- Fixtures de teste: `SenhaForte1!` / `NovaSenha1!`.

### Trade-offs

- Contas antigas com senha fraca ainda fazem login (desejável nesta fase).

### Contrato

- OpenAPI alinhado nos schemas de criação/reset.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, index, CR-030, slice 016

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| openapi password | contrato | pattern |
| forms/DTOs auth | implementacao | politica |
| docs/ai (minimo) | padroes | utils/ |

### Evitado

- mobile/, design-system, requirements

## Handoff

- Caminho: `.agents/state/handoffs/TASK-030.md`
- Decisões: politica unica front/back/contrato; login sem pattern forte
- Pendências: mobile opcional

## Arquivos alterados

### raiz / governanca

- `tasks/change-requests/030-politica-senha-forte-web.md`
- `tasks/slices/016-politica-senha-forte-web.md`
- `tasks/000-index.md`
- `contracts/openapi.yaml`
- `.agents/state/handoffs/TASK-030.md`

### front-end

- `front-end/src/utils/password.ts`
- `front-end/src/utils/password.test.ts`
- `front-end/src/pages/Auth/RegisterProfessional/index.tsx`
- `front-end/src/pages/Auth/RegisterProfessional/index.test.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts`
- `front-end/src/pages/Auth/RegisterGuardian/index.tsx`
- `front-end/src/pages/Auth/PasswordReset/index.tsx`

### backend

- `backend/src/common/utils/password.util.ts`
- `backend/src/common/decorators/is-strong-password.decorator.ts`
- `backend/src/modules/users/dto/create-user.dto.ts`
- `backend/src/modules/users/dto/update-user.dto.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/auth/dto/password-reset.dto.ts`
- `backend/src/modules/professionals/dto/register-professional.dto.ts`
- `backend/src/modules/guardians/dto/register-guardian.dto.ts`
- specs atualizados com senhas fortes

## Validacoes executadas

- front: password tests, RegisterProfessional, lint, build — ok
- back: jest auth|users|professionals|guardians — ok; lint — ok

## Pendencias pos-task

- Aplicar mesma politica no mobile (fora de escopo)
- Contas antigas com senha fraca continuam logando

## Status final

done
