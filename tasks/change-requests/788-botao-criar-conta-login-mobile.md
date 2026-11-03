# Task 788 - Botão criar conta no login mobile

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

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas + artefato documental

### Fonte primaria visual

- `design-system/mobile/prints/login-mobile.png` (layout atual do login)
- `design-system/mobile/Design_System_Evolente_App_Mobile.md` (botões, tokens, hit target)

### Regra de aderencia visual

- preservar layout, copy de boas-vindas, campos, botão Entrar, biometria, “Esqueci minha senha” e versão
- o print **não** tem CTA de cadastro (Task 094 removeu de propósito)
- lacuna registrada: inserir botão secundário “Criar conta” abaixo do formulário, sem cadastro in-app
- usar `Button` ghost existente; não reinterpretar o restante da tela

## Origem da solicitacao

Pedido explícito: no login mobile, adicionar botão “Criar conta” que abre `https://evolente.com.br/cadastro/responsavel`.

## Objetivo

Permitir que o responsável inicie o cadastro no site de produção a partir da tela de login do app, sem implementar onboarding no mobile.

## Escopo

- CTA “Criar conta” na tela de login mobile (telefone e tablet)
- Abrir o navegador/site em `https://evolente.com.br/cadastro/responsavel`
- Acessibilidade mínima do botão (role, label, área de toque)

## Fora de escopo

- Cadastro in-app
- Cadastro de profissional
- Backend, front-end, contrato OpenAPI
- Alterar webhook/Asaas ou `APP_PUBLIC_URL`
- Copy de pagamento/assinatura (manter neutro; só “Criar conta”)

## Entradas

- pedido explícito do usuário nesta conversa
- URL oficial: `https://evolente.com.br/cadastro/responsavel`
- `mobile/src/features/auth/screens/SignInScreen.tsx`

## Slice vertical

### Identificador do slice

Slice 002 - Autenticacao e recuperacao de senha

### Arquivo do slice

- `tasks/slices/002-autenticacao.md`

### Objetivo de negocio

Login mobile continua autenticando no app; quem não tem conta vai ao cadastro web do responsável.

### Entrega verificavel do slice

Toque em “Criar conta” no login abre `https://evolente.com.br/cadastro/responsavel`.

### Fora do slice

- wizard de cadastro no app

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Layout e CTAs do login | `mobile/src/features/auth/screens/SignInScreen.tsx` | inserir botão | sim |
| Estilos do login | `mobile/src/features/auth/screens/styles.ts` | espaçamento do CTA | sim |
| Tokens/botões mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI | sim |
| Print do login | `design-system/mobile/prints/login-mobile.png` | registrar lacuna do CTA | nao |
| Padrão de abrir URL | `mobile/src/features/trail/utils/openTrailMedia.ts` | Linking | sim |
| Button compartilhado | `mobile/docs/ai/COMPONENT_REUSE.md` | reusar `Button` | nao |
| Acessibilidade | `mobile/docs/ai/ACCESSIBILITY.md` | UI | nao — arquivo inexistente na stack |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 7
- Fontes sob demanda estimadas: 4
- Risco de contexto excessivo: baixo
- Estratégia para reduzir contexto: só login mobile e helper de URL; sem front-end, Asaas ou slice 049 inteiro

## Dependencias

- Task 094 (login sem cadastro in-app) — esta task adiciona apenas deep-link web
- Slice 049 (cadastro público só do responsável na web) — destino do link já existe

## Criterios de conclusao

- [x] Login mobile exibe botão “Criar conta” em telefone e tablet
- [x] Toque abre `https://evolente.com.br/cadastro/responsavel`
- [x] Não há fluxo de cadastro dentro do app
- [x] Copy não menciona pagamento, assinatura ou checkout
- [x] Print do login permanece a base visual; desvio do CTA documentado

## Instrucoes de implementacao

- Reusar `Button` `variant="ghost"` abaixo do `SignInForm` e acima de “Esqueci minha senha”
- Extrair URL e `Linking` para `features/auth/utils/`
- URL fixa de produção do cadastro do responsável
- `accessibilityRole="button"` e label “Criar conta”; hint de que abre o site

## Validacao esperada

- teste unitário do helper de abertura de URL
- lint dos arquivos alterados no mobile

## Entregaveis esperados

- CTA no `SignInScreen`
- helper + teste
- task, índice, slice e handoff atualizados

## Resultado da execucao

- Botão ghost “Criar conta” entrou no `loginForm` compartilhado (telefone e tablet), entre Entrar/biometria e “Esqueci minha senha”.
- Toque chama `openResponsibleSignup`, que abre `https://evolente.com.br/cadastro/responsavel`.
- Desvio do print `login-mobile.png` registrado: CTA web, sem cadastro in-app.
- `Button` passou a encaminhar `accessibilityHint`.
- Acessibilidade aplicada: role button (via `Button`), label “Criar conta”, hint “Abre o cadastro no site Evolente”, `minHeight` 52.

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/002-autenticacao.md`
- `SignInScreen.tsx`, `screens/styles.ts`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `openTrailMedia.ts` (padrão Linking)
- `mobile/docs/ai/COMPONENT_REUSE.md`

## Handoff

- `.agents/state/handoffs/TASK-788.md`

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

## Validacoes executadas

- `npx eslint` nos arquivos mobile alterados — passou
- `npx jest src/features/auth/utils/openResponsibleSignup.test.ts --runInBand` — 2 testes passaram
- UI no dispositivo/emulador não foi exercitada nesta sessão

## Pendencias pos-task

- Conferir no app (telefone e tablet) que o toque abre o site
- Publicar nova build se o login em loja/TestFlight precisar do CTA

## Status final

done
