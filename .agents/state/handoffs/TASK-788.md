# Handoff - Task 788

## Task

- identificador: 788
- título: Botão criar conta no login mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002 - Autenticacao e recuperacao de senha
- objetivo de negócio: login no app; cadastro do responsável no site
- entrega verificável: “Criar conta” abre `https://evolente.com.br/cadastro/responsavel`

## Decisões preservadas

- decisão: CTA web, sem cadastro in-app
- motivo: pedido explícito; destino já existe no Slice 049
- impacto: desvio documentado do print `login-mobile.png` (Task 094)

- decisão: URL fixa de produção no helper/constante
- motivo: domínio oficial confirmado pelo usuário
- impacto: staging usaria a mesma URL até haver env dedicado

- decisão: `Button` ghost abaixo do formulário
- motivo: não competir com Entrar; reusar componente compartilhado
- impacto: `Button` agora aceita `accessibilityHint`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/788-botao-criar-conta-login-mobile.md`
- `tasks/slices/002-autenticacao.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `mobile/src/features/auth/screens/SignInScreen.tsx` | inserir CTA | posição do botão |
| `mobile/src/features/auth/screens/styles.ts` | espaçamento | `createAccountButton` |
| `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI | tokens/botões |
| `mobile/src/features/trail/utils/openTrailMedia.ts` | Linking | padrão `canOpenURL`/`openURL` |
| `mobile/docs/ai/COMPONENT_REUSE.md` | Button | reuso |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `front-end/` / `contracts/openapi.yaml` | sem mudança web/API |
| `requirements/` | URL e CTA já explícitos |
| Slice 049 inteiro | só o destino do link |
| Asaas / `APP_PUBLIC_URL` | fora de escopo |

## Resultado por stack

- front-end ou next-js: não alterado
- backend: não alterado
- mobile: CTA “Criar conta” no login abre o cadastro web do responsável

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/constants.ts`
- `mobile/src/features/auth/utils/openResponsibleSignup.ts`
- `mobile/src/features/auth/utils/openResponsibleSignup.test.ts`
- `mobile/src/shared/components/Button/index.tsx`
- `tasks/change-requests/788-botao-criar-conta-login-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-788.md`

## Validações executadas

- validação: eslint dos arquivos mobile alterados — passou
- validação: jest `openResponsibleSignup.test.ts` — 2 passaram
- validação: UI em dispositivo — não exercitada

## Pendências ou bloqueios

- conferir toque no app e publicar build se necessário

## Próxima ação sugerida

- abrir o login no Expo e tocar em “Criar conta”

## Próximo contexto recomendado

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/utils/openResponsibleSignup.ts`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `contracts/openapi.yaml`
- motivo: sem contrato
- fonte: Asaas / webhook
- motivo: fora desta task
