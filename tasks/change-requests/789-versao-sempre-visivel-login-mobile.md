# Task 789 - Versão sempre visível no login mobile

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

- `design-system/mobile/prints/login-mobile.png`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- preservar login, CTAs e copy
- o número da versão (Task 660) deve permanecer visível no rodapé
- se o conteúdo crescer, comprimir/subir o bloco superior — não esconder a versão

## Origem da solicitacao

Após o botão “Criar conta” (Task 788), a versão ficou cortada na parte de baixo da tela. Pedido: ela deve aparecer sempre; o conteúdo sobe para caber.

## Objetivo

Reservar o rodapé do login para a versão do app, com safe area inferior, e ajustar o restante para cima.

## Escopo

- Layout do `SignInScreen` (telefone e tablet)
- Estilos do rodapé da versão e compactação do conteúdo acima

## Fora de escopo

- Alterar o valor da versão em `app.json`
- Cadastro, Asaas, backend, web

## Entradas

- pedido explícito nesta conversa
- handoff `TASK-788.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/shared/components/Screen/index.tsx` (safe area sem edge `bottom`)

## Slice vertical

### Identificador do slice

Slice 002 - Autenticacao e recuperacao de senha

### Arquivo do slice

- `tasks/slices/002-autenticacao.md`

### Objetivo de negocio

Identificar a build no login sem a versão sumir atrás da borda ou do home indicator.

### Entrega verificavel do slice

“Versão X.Y.Z” visível no rodapé do login; conteúdo acima se ajusta.

### Fora do slice

- incremento de versão de release

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
| Layout atual | `SignInScreen.tsx` + `screens/styles.ts` | reposicionar versão | sim |
| Safe area inferior | `mobile/src/shared/components/Screen/index.tsx` | padding do rodapé | sim |
| Handoff do CTA | `.agents/state/handoffs/TASK-788.md` | causa do overflow | nao |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 7
- Fontes sob demanda estimadas: 2
- Risco de contexto excessivo: baixo
- Estratégia: só login mobile; sem front/back

## Dependencias

- Task 660 (exibir versão)
- Task 788 (botão criar conta aumentou a altura)

## Criterios de conclusao

- [x] Versão visível no rodapé com teclado fechado
- [x] Conteúdo acima sobe/comprime em vez de cobrir a versão
- [x] Safe area inferior respeitada (`Screen` não aplica edge bottom)
- [x] Telefone e tablet

## Instrucoes de implementacao

- Tirar a versão de dentro do `loginForm`
- Reservar footer `flexShrink: 0` no `contentLayer`
- Aplicar `useSafeAreaInsets().bottom` no padding do rodapé
- Reduzir espaçamento superior (logo/hero/form) o suficiente para caber o bloco

## Validacao esperada

- lint dos arquivos alterados
- revisão de layout: versão fora do cluster que estoura

## Entregaveis esperados

- `SignInScreen` + estilos
- task, índice, slice e handoff

## Resultado da execucao

- A versão saiu do `loginForm` e passou a um rodapé `flexShrink: 0` no telefone e no tablet.
- O bloco superior (`mainColumn`) ocupa o espaço restante e pode comprimir; o canvas não corta mais a versão.
- Padding inferior usa `useSafeAreaInsets().bottom` (mínimo 8), porque o `Screen` não aplica edge `bottom`.
- Logo e hero subiram (marginTop 80→48 e 20→12) para caber o botão “Criar conta” sem esconder a versão.

## Contexto utilizado

- Task 789, Slice 002, handoff 788
- `SignInScreen.tsx`, `screens/styles.ts`, `Screen/index.tsx`

## Handoff

- `.agents/state/handoffs/TASK-789.md`

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/789-versao-sempre-visivel-login-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-789.md`

## Validacoes executadas

- `npx eslint src/features/auth/screens/SignInScreen.tsx src/features/auth/screens/styles.ts` — passou
- UI em dispositivo não exercitada nesta sessão

## Pendencias pos-task

- Recarregar o Expo e conferir a versão acima da home indicator no telefone

## Status final

done
