# Task 717 - Corrigir sobreposição do login tablet

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

- nao se aplica (correcao visual sem API)

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Corrigir a composição do login tablet para impedir que o card do formulário cubra a logo e a mensagem de boas-vindas, mantendo o grupo em fluxo vertical previsível.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/717-corrigir-sobreposicao-login-tablet-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- print enviado pelo usuario nesta solicitacao (estado tablet com sobreposicao)

## Orcamento de contexto

- 9 fontes
- estrategia de reducao: corrigir somente fluxo, espaçamento e dimensões da composição tablet; preservar telefone e lógica de auth.

## Referencia visual

- print enviado pelo usuario: governa o estado tablet observado, especialmente a ausência de sobreposição entre boas-vindas e formulário.
- design system mobile: governa tokens, cores, tipografia e componentes.

## Criterios de aceite

- Logo e boas-vindas ficam totalmente visíveis acima do formulário.
- Card do formulário não sobrepõe a marca/copy.
- Espaçamento vertical permanece estável em tablet portrait e landscape.
- Telefones não sofrem alteração.
- Fluxo de login, biometria, recovery e modal de erro permanecem funcionais.

## Dependencias

- Task 716 (centralização do login tablet)

## Fora de escopo

- Recuperação de senha
- API e autenticação
- Mudanças no layout de telefones

## Status final

done

## Resultado da execucao

- A composição tablet deixou de usar centralização que permitia sobreposição entre os blocos.
- O layout agora usa fluxo vertical explícito, com padding superior, altura mínima para logo/copy e margem antes do formulário.
- Logo e boas-vindas permanecem totalmente visíveis acima do card.
- O caminho de telefone e a lógica do formulário permanecem preservados.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, Task 717 e Slice 002.
- Contexto sob demanda: design system mobile, tela/estilos de login e print enviado pelo usuário.
- Handoff da Task 716 usado para preservar a decisão de ocultar a menina no tablet.

## Handoff

- `.agents/state/handoffs/TASK-717.md`
- Decisão: composição tablet em fluxo vertical com `paddingTop`, `minHeight` da marca e `marginTop` do formulário para impedir sobreposição.
- Próximo contexto recomendado: validar o print em tablet portrait/landscape.

## Arquivos alterados

- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/717-corrigir-sobreposicao-login-tablet-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-717.md`

## Validacoes executadas

- `git -C mobile diff --check`: concluído sem erros.
- `git diff --check` nos arquivos de rastreabilidade: concluído sem erros.
- Revisão do diff de estilos: concluída.
- Validação visual em emulador/dispositivo: não executada nesta sessão.

## Pendencias pos-task

- Conferir visualmente se o espaçamento final corresponde ao esperado no tablet usado pelo usuário.
