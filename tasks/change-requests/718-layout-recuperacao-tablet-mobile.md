# Task 718 - Aplicar layout tablet na recuperação de senha mobile

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

Aplicar à tela de recuperação de senha o mesmo layout tablet do login: logo e copy centralizados, formulário abaixo em card e ilustração da menina ocultada.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/718-layout-recuperacao-tablet-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/PasswordRecoveryForm.tsx`

## Orcamento de contexto

- 9 fontes
- estrategia de reducao: reutilizar estilos tablet existentes do login e alterar somente a composição da recuperação; preservar telefone e API.

## Referencia visual

- referência primária: composição tablet definida nas Tasks 716 e 717.
- design system mobile governa tokens, tipografia, cores e estados.

## Criterios de aceite

- Recuperação tablet usa logo/copy centralizados e formulário abaixo.
- Ilustração da menina não aparece no tablet.
- Telefone mantém o layout atual.
- Erro, sucesso, retorno ao login, teclado e áreas seguras continuam funcionais.

## Dependencias

- Task 717 (fluxo vertical sem sobreposição)

## Fora de escopo

- Login tablet
- API e regras de recuperação
- Novos assets

## Status final

done

## Resultado da execucao

- A recuperação de senha passou a usar no tablet a mesma composição vertical do login.
- Logo, título, descrição e formulário ficam centralizados, sem a imagem da menina.
- O formulário de recuperação e o link “Voltar ao login” foram compartilhados entre tablet e telefone.
- O comportamento de telefone, teclado, erro e sucesso foi preservado.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, Task 718 e Slice 002.
- Contexto sob demanda: design system mobile, `PasswordRecoveryScreen.tsx`, estilos compartilhados e formulário de recuperação.
- Tasks 716 e 717 usadas como referência do layout tablet aprovado.

## Handoff

- `.agents/state/handoffs/TASK-718.md`
- Decisão: recuperação tablet usa fluxo vertical centralizado, sem ilustração; telefone preserva a composição anterior.
- Próximo contexto recomendado: validar login e recuperação juntos em tablet portrait/landscape.

## Arquivos alterados

- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/718-layout-recuperacao-tablet-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-718.md`

## Validacoes executadas

- `git -C mobile diff --check`: concluído sem erros.
- `git diff --check` nos arquivos de rastreabilidade: concluído sem erros.
- Revisão do diff: concluída.
- Validação visual em emulador/dispositivo tablet: não executada nesta sessão.

## Pendencias pos-task

- Confirmar visualmente os estados inicial, erro e sucesso em tablet portrait e landscape.
