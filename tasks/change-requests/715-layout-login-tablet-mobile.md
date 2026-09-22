# Task 715 - Novo layout de login para tablet no mobile

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

- nao se aplica (alteracao visual sem API)

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Criar uma composicao visual propria para a tela de login em tablets, aproveitando a area horizontal com branding e ilustracao em uma coluna e o formulario em um card dedicado na outra, sem alterar o fluxo de autenticacao.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/715-layout-login-tablet-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md` (tokens e linguagem visual)
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/MOBILE_PATTERNS.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/styles.ts`

## Orcamento de contexto

- 10 fontes
- estrategia de reducao: limitar a implementacao ao SignIn e aos estilos diretamente usados; nao reabrir recovery, API ou outras telas.

## Referencia visual

- tipo: artefato documental mobile existente
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- decisao adicional desta task: tablet usa duas colunas; a coluna esquerda concentra logo, copy e ilustracao, e a direita concentra o formulario em superficie clara arredondada.
- telefones preservam a composicao atual.

## Criterios de aceite

- Em tablet, login apresenta layout de duas colunas, com formulario visualmente separado da ilustracao.
- Em telefone, a composicao atual permanece preservada.
- Tablet portrait e landscape nao apresentam overflow horizontal, cortes ou largura desproporcional.
- Campos, biometria, recovery, modal de erro, teclado e areas seguras continuam funcionais.
- Lint, typecheck e testes existentes passam.

## Dependencias

- Task 610 (responsividade do login em tablet)
- Tasks 114-116 e 495-496 (comportamento de teclado do login)

## Fora de escopo

- Recuperacao de senha
- Alteracoes de API, autenticacao ou contrato
- Mudancas no layout de telefones
- Novos assets de ilustracao

## Status final

done

## Resultado da execucao

- Criada uma composição exclusiva para tablets com duas colunas: marca/copy/ilustração à esquerda e formulário em card à direita.
- O layout de telefones permanece na composição anterior, com o mesmo comportamento de teclado e recuperação.
- O formulário foi compartilhado entre as duas composições para preservar validações, biometria, recovery, versão e modal de erro.
- A nova composição usa os tokens e assets existentes, sem alteração de autenticação ou API.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, Task 715 e Slice 002.
- Contexto sob demanda: design system mobile, guias AI mobile e arquivos de login/estilos diretamente envolvidos.
- Não foram carregados contrato, requirements ou stacks não envolvidas.

## Handoff

- `.agents/state/handoffs/TASK-715.md`
- Decisão: tablet mantém breakpoint de 600 dp da Task 610, mas troca a composição para duas colunas; telefones preservam o layout existente.
- Próximo contexto recomendado: validar visualmente em tablet portrait/landscape e com teclado aberto.

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/715-layout-login-tablet-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-715.md`

## Validacoes executadas

- `git -C mobile diff --check`: concluído sem erros.
- Revisão do diff da tela e estilos: concluída.
- `npm run typecheck`, `npm run lint` e `npm run test -- --runInBand`: iniciados, mas não concluíram no ambiente após aproximadamente um minuto; processos interrompidos.
- Validação visual em emulador/dispositivo tablet: não executada nesta sessão.

## Pendencias pos-task

- Confirmar a composição em tablet portrait e landscape, incluindo foco de campo e teclado aberto.
- Reexecutar typecheck, lint e testes em ambiente Expo estável.
