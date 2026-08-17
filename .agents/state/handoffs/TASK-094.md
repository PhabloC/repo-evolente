# Handoff - Task 094

## Task

- identificador: 094
- título: Login mobile fiel ao print sem CTA de cadastro
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002 - Autenticacao
- objetivo de negócio: alinhar a tela de login mobile ao print concreto enviado pelo usuario sem mudar o fluxo auth
- entrega verificável: login mobile com layout fiel ao print, assets reais e sem criar conta
- status do slice: done

## Decisões preservadas

- decisão: substituir o hero generico por uma tela de login dedicada ao print
- motivo: a referencia visual agora e concreta e governa composicao e hierarquia
- impacto: `SignInScreen` ganhou layout proprio e deixou de reutilizar o hero genérico anterior

- decisão: estender `TextField` e `Button` com props visuais opcionais
- motivo: suportar o layout do print sem hardcode da tela dentro dos componentes compartilhados
- impacto: inputs aceitam adornos/estilos locais e o botao aceita estilo por tela

- decisão: reproduzir a nuvem com formas nativas
- motivo: o app nao possui pipeline SVG configurada para usar o asset diretamente
- impacto: fidelidade visual mantida sem dependencia nova

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/094-login-mobile-fiel-ao-print-sem-cadastro.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-093.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `login-mobile.png` | print concreto | reproduzir hierarquia, espacamentos e ausência do cadastro |
| `girl.png`, `logo-completa.webp`, `nuvem_evolente_mobile_svg.svg` | assets da tela | montar hero e base decorativa |
| mobile docs AI | guardrails da stack | manter reuse e code style |
| `features/auth/**` + componentes shared usados | implementacao | refino da tela e dos inputs/botao |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| OpenAPI / backend | sem mudanca de contrato |
| design-system front | task estritamente mobile |
| recovery/reset alem do stylesheet compartilhado | pedido focado em login |

## Resultado por stack

- mobile: login mobile redesenhado conforme print, sem CTA de cadastro, mantendo link de recovery
- front/back: n/a

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

## Validações executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (6 suites, 8 testes)

## Pendências ou bloqueios

- sem bloqueios tecnicos
- oportunidade futura: usar o asset SVG da nuvem diretamente se a stack receber suporte oficial

## Próxima ação sugerida

- validar a tela em device real ou Expo web para calibrar os ultimos milimetros de espacamento contra o print, se voce quiser uma segunda rodada de fidelidade

## Próximo contexto recomendado

- `mobile/src/features/auth/screens/SignInScreen.tsx` + o mesmo print de referencia

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend/openapi/recovery/reset
- motivo: o pedido atual nao alterou fluxo auth nem telas secundarias
