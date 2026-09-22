# Task 716 - Centralizar formulário e boas-vindas no login tablet

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

- nao se aplica (refinamento visual sem API)

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Refinar o layout de login em tablets para centralizar vertical e horizontalmente a marca, a mensagem de boas-vindas e o formulário, ocultando a ilustração da menina nessa variação.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/716-centralizar-login-tablet-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/MOBILE_PATTERNS.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`

## Orcamento de contexto

- 9 fontes
- estrategia de reducao: alterar somente a composição tablet do login e seus estilos; preservar o caminho de telefone.

## Referencia visual

- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- decisão desta task: no tablet, logo, boas-vindas e formulário ficam centralizados; a imagem da menina fica oculta.

## Criterios de aceite

- Tablet exibe logo e copy de boas-vindas centralizados.
- Formulário fica centralizado abaixo da boas-vindas.
- Imagem da menina não é renderizada no tablet.
- Telefones não sofrem alteração visual.
- Login, biometria, recovery, teclado e modal de erro continuam funcionais.

## Dependencias

- Task 715 (layout tablet em duas colunas)

## Fora de escopo

- Recuperação de senha
- API e autenticação
- Novos assets

## Status final

done

## Resultado da execucao

- O layout tablet passou de duas colunas para uma composição vertical centralizada.
- Logo, mensagem “Bem-vindo(a)!” e subtítulo ficam alinhados ao centro.
- A imagem da menina não é renderizada no tablet.
- O formulário permanece centralizado abaixo da boas-vindas, com o card e os estados de autenticação preservados.
- A composição de telefones não foi alterada.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, Task 716 e Slice 002.
- Contexto sob demanda: design system mobile, guias AI mobile e tela/estilos de login.
- Handoff da Task 715 usado para preservar o breakpoint e a separação entre tablet e telefone.

## Handoff

- `.agents/state/handoffs/TASK-716.md`
- Decisão: tablet usa composição centralizada sem ilustração; telefone preserva a composição anterior.
- Próximo contexto recomendado: validar portrait/landscape e teclado em tablet.

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/716-centralizar-login-tablet-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-716.md`

## Validacoes executadas

- `git -C mobile diff --check`: concluído sem erros.
- Revisão do diff: concluída, com alteração restrita à composição tablet e seus estilos.
- Validação visual em emulador/dispositivo tablet: não executada nesta sessão.

## Pendencias pos-task

- Confirmar visualmente o espaçamento final em tablet portrait e landscape, incluindo teclado aberto.
