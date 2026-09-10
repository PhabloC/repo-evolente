# Task 610 - Responsividade da pagina de login para tablet no mobile

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

- nao se aplica (ajuste visual e de layout)

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Ajustar a pagina de login do aplicativo mobile para aproveitar corretamente larguras e alturas de tablets, preservando o layout atual em telefones.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/610-responsividade-login-tablet-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md` (tokens e comportamento visual do login)
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/styles.ts`

## Orcamento de contexto

- 12 fontes
- estrategia de reducao: limitar a análise ao SignIn e estilos diretamente usados; não reabrir recovery, API ou outras telas.

## Criterios de aceite

- Login se adapta a tablets em orientações suportadas sem conteúdo cortado ou espaçamentos desproporcionais.
- Composição visual atual e comportamento em telefones permanecem preservados.
- Formulário continua utilizável com teclado e respeita áreas seguras.
- Não há overflow horizontal nem dependência de dimensões fixas inadequadas para tablet.
- Lint, typecheck e testes existentes passam.

## Dependencias

- Task 007 (telas auth mobile)
- Tasks 114–116 e 495–496 (comportamento de teclado do login)

## Fora de escopo

- Recuperação de senha
- Alterações de API, autenticação ou contrato
- Redesign visual do login

## Status final

done

## Resultado da execucao

- Detectado tablet a partir de 600 dp com `useWindowDimensions`.
- Referência máxima de viewport ajustada para `1024 × 1366 dp`, conforme iPad Pro informado.
- Hero e painel do formulário passaram a ter largura máxima de 560 dp e permanecem centralizados.
- Ilustração e logo recebem ajustes específicos para tablet, preservando os estilos de telefone.
- No tablet, o cluster é reposicionado para o centro vertical; a nuvem ocupa a largura total e o formulário permanece centralizado com limite próprio.
- A animação de recolhimento/elevação ao abrir o teclado fica desativada no tablet no login e na recuperação de senha.
- O painel do formulário no tablet ocupa 100% da largura e preenche o espaço restante até o final da tela.
- A imagem da menina com a nuvem usa dimensionamento de largura total no tablet.
- O painel mantém o comportamento de teclado existente.

## Contexto utilizado

- Contexto mínimo: arquivos globais, índice, Task 610 e Slice 002.
- Contexto sob demanda: design system mobile, guias AI mobile e arquivos da tela/estilos de login.
- Não foram carregados contrato, requirements ou stacks não envolvidas.

## Handoff

- `.agents/state/handoffs/TASK-610.md`
- Decisão: breakpoint de tablet em 600 dp; conteúdo limitado a 560 dp para evitar expansão desproporcional.
- Próximo contexto recomendado: validar visualmente em tablet portrait/landscape e teclado aberto.

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/hooks/useAuthKeyboardLift.ts`
- `tasks/change-requests/610-responsividade-login-tablet-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-610.md`

## Validacoes executadas

- Verificação de diff e status do submódulo mobile: alterações restritas à tela e estilos de login.
- `npm run lint`, `npx tsc --noEmit` e `npm run test -- --runInBand`: iniciados, mas o ambiente Expo/npm não concluiu durante a sessão.

## Pendencias pos-task

- Validação visual em dispositivo/emulador tablet permanece recomendada.

## Status final

done
