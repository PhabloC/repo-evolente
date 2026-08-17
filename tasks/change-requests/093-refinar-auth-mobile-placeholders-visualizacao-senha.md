# Task 093 - Refinar telas auth mobile com placeholders e visualizacao de senha

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

- nao se aplica; refino visual nas telas auth mobile existentes sem mudanca de integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system + assets locais

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/assets/logo-completa.webp`
- `mobile/assets/logo-seal.webp`

### Regra de aderencia visual

- manter auth mobile acolhedora, clara e sem fluxo infantil/gamificado

## Objetivo

Melhorar o design das telas de login e recuperar senha no app mobile, adicionando placeholders nos inputs e visualizacao de senha no login.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-007.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI auth mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | definir direcao visual e acessibilidade minima | sim |
| Regras locais mobile | `mobile/AGENTS.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md` | ajustar composicao e componente compartilhado | sim |
| Implementacao auth atual | `mobile/src/features/auth/**` | refinar layout e copy das telas | sim |
| Input compartilhado | `mobile/src/shared/components/TextField/**` | suportar toggle de senha sem duplicacao | sim |
| Logos locais | `mobile/assets/logo-completa.webp`, `mobile/assets/logo-seal.webp` | branding nas telas auth | opcional |

## Orçamento de contexto

- baixo
- estrategia: limitar a execucao ao fluxo auth mobile, sem reabrir API, shell autenticado ou outras features

## Criterios de conclusao

- [x] tela de login com visual refinado e branding mobile
- [x] tela de recuperar senha com visual refinado e consistente com login
- [x] placeholders adicionados aos inputs envolvidos
- [x] campo de senha do login com acao de mostrar/ocultar senha
- [x] validacoes locais da stack mobile executadas

## Dependencias

- Task 007 - done

## Resultado da execucao

- login e recuperar senha ganharam composicao visual mais intencional com branding da Evolente, cards em camadas e copy mais clara para acesso mobile
- os inputs de login e recovery agora exibem placeholders; o campo de senha do login passou a ter acao de mostrar/ocultar com icone nativo desenhado sem dependencias extras
- o `TextField` compartilhado foi ajustado para aceitar adorno a direita, preservando reutilizacao horizontal sem acoplar a feature auth
- as logos `logo-completa.webp` e `logo-seal.webp` foram incorporadas ao header compartilhado das telas auth mobile

## Contexto utilizado

### Minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-007.md`

### Sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/AGENTS.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/src/features/auth/**`
- `mobile/src/shared/components/TextField/**`
- `mobile/assets/logo-completa.webp`
- `mobile/assets/logo-seal.webp`

### Contexto evitado

- `contracts/openapi.yaml`, backend e shell autenticado: sem mudanca de integracao ou regra de sessao
- `design-system/front/`: task estritamente mobile
- `mobile/docs/ai/ACCESSIBILITY.md`: arquivo inexistente; foram aplicadas as regras de toque do design system mobile e os alvos minimos ja mantidos pelos componentes

## Handoff

- `.agents/state/handoffs/TASK-093.md`

## Arquivos alterados

- `mobile/src/features/auth/components/AuthHero.tsx`
- `mobile/src/features/auth/components/AuthHero.styles.ts`
- `mobile/src/features/auth/components/PasswordVisibilityIcon.tsx`
- `mobile/src/features/auth/components/PasswordVisibilityIcon.styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/components/styles.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/shared/components/TextField/index.tsx`
- `mobile/src/shared/components/TextField/styles.ts`
- `tasks/change-requests/093-refinar-auth-mobile-placeholders-visualizacao-senha.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-093.md`

## Validacoes executadas

- `cd mobile && npm run lint` - ok
- `cd mobile && npm run typecheck` - ok
- `cd mobile && npm run test` - ok (6 suites, 8 testes)

## Pendencias pos-task

- sem bloqueios tecnicos abertos nesta CR
- se houver nova referencia visual especifica para auth mobile, o proximo refino deve partir dela em vez de reinterpretacao livre do DS documental

## Status final

done
