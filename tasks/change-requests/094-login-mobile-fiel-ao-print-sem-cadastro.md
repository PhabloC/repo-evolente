# Task 094 - Login mobile fiel ao print sem CTA de cadastro

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

- nao se aplica; refino visual da tela de login mobile sem mudanca de integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas + assets locais

### Fonte primaria visual

- `C:\Users\phabl\Downloads\Evolente\login-mobile.png`
- `mobile/assets/girl.png`
- `mobile/assets/nuvem_evolente_mobile_svg.svg`
- `mobile/assets/logo-completa.webp`

### Regra de aderencia visual

- reproduzir o layout do print na tela de login mobile com alta fidelidade, removendo apenas a opcao de cadastro conforme pedido do usuario

## Objetivo

Deixar a tela de login mobile alinhada ao print enviado, usando os assets locais reais e sem exibir CTA de criar conta.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-093.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Fidelidade visual login | `C:\Users\phabl\Downloads\Evolente\login-mobile.png` | reproduzir composicao, espacamentos e hierarquia da tela | sim |
| Assets da tela | `mobile/assets/girl.png`, `mobile/assets/nuvem_evolente_mobile_svg.svg`, `mobile/assets/logo-completa.webp` | montar hero e base decorativa da tela | sim |
| UI auth mobile | `mobile/AGENTS.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md` | manter organizacao e reuso corretos | sim |
| Implementacao atual | `mobile/src/features/auth/**`, `mobile/src/shared/components/TextField/**`, `mobile/src/shared/components/Button/**`, `mobile/src/shared/components/Screen/**` | adaptar a tela e componentes compartilhados ao print | sim |
| DS mobile documental | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | manter cores e tom quando o print nao cobrir algum detalhe | opcional |

## Orçamento de contexto

- baixo
- estrategia: restringir a execucao ao login mobile e aos componentes base usados por essa tela; nao reabrir recovery, contrato ou shell

## Criterios de conclusao

- [x] login mobile reproduz a composicao principal do print com logo, texto, menina e base em nuvem
- [x] formulario segue o print com labels, placeholders e CTA principal
- [x] CTA de cadastro nao aparece na tela
- [x] fluxo de recuperar senha permanece acessivel
- [x] validacoes locais da stack mobile executadas

## Dependencias

- Task 007 - done
- Task 093 - done

## Resultado da execucao

- a tela de login mobile foi reconstruida a partir do print anexado, com layout vertical dedicado, logo grande centralizada, copy lateral, ilustracao da menina e base em nuvem separando hero e formulario
- os campos passaram a seguir a composicao do print com labels menores, placeholders `seu@email.com` e `Digite sua senha`, icones laterais de e-mail/cadeado e botao principal alto em destaque
- o link `Esqueci minha senha` foi mantido e o bloco de cadastro foi removido integralmente da tela
- como a stack nao possui pipeline de renderizacao SVG configurada, a nuvem foi reproduzida na UI com formas nativas equivalentes guiadas pelo arquivo `nuvem_evolente_mobile_svg.svg`, sem adicionar dependencia nova

## Contexto utilizado

### Minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-093.md`

### Sob demanda

- `C:\Users\phabl\Downloads\Evolente\login-mobile.png`
- `mobile/assets/girl.png`
- `mobile/assets/nuvem_evolente_mobile_svg.svg`
- `mobile/assets/logo-completa.webp`
- `mobile/AGENTS.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/src/features/auth/**`
- `mobile/src/shared/components/TextField/**`
- `mobile/src/shared/components/Button/**`
- `mobile/src/shared/components/Screen/**`
- `mobile/src/shared/components/AppText/**`

### Contexto evitado

- `contracts/openapi.yaml` e backend: sem alteracao de integracao
- `design-system/front/`: task mobile com print governando a tela
- recovery/reset alem da compatibilidade de stylesheet: sem redesign solicitado

## Handoff

- `.agents/state/handoffs/TASK-094.md`

## Arquivos alterados

- `mobile/src/features/auth/components/AuthFieldIcon.tsx`
- `mobile/src/features/auth/components/AuthFieldIcon.styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/components/styles.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/shared/components/AppText/index.tsx`
- `mobile/src/shared/components/Button/index.tsx`
- `mobile/src/shared/components/TextField/index.tsx`
- `tasks/change-requests/094-login-mobile-fiel-ao-print-sem-cadastro.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-094.md`

## Validacoes executadas

- `cd mobile && npm run lint` - ok
- `cd mobile && npm run typecheck` - ok
- `cd mobile && npm run test` - ok (6 suites, 8 testes)

## Pendencias pos-task

- se a stack receber suporte oficial a SVG no futuro, a nuvem pode passar a usar o asset diretamente em vez da reproducao com formas nativas

## Status final

done
