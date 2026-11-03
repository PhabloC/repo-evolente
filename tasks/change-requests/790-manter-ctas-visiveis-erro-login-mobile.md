# Task 790 - Manter CTAs visíveis quando o login mostra erro de campo

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

- preservar CTAs Entrar, Criar conta e Esqueci minha senha
- textos vermelhos de validação continuam abaixo dos inputs
- o bloco superior (logo/hero/nuvem) sobe ou comprime; os CTAs de baixo não podem sumir

## Origem da solicitacao

Com os avisos de e-mail/senha, **Criar conta** e **Esqueci minha senha** desaparecem (cortados pelo overflow do login após Task 789).

## Objetivo

Quando os HelperTexts vermelhos aparecem, o conteúdo de cima cede espaço e os CTAs abaixo dos campos permanecem visíveis.

## Escopo

- Layout do `SignInScreen` / estilos do login
- Expor estado de erro de campo do `useSignInForm` se precisar comprimir o topo

## Fora de escopo

- Copy das mensagens de validação
- Backend, web, Asaas

## Slice vertical

### Identificador do slice

Slice 002 - Autenticacao e recuperacao de senha

### Arquivo do slice

- `tasks/slices/002-autenticacao.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Overflow do login | `SignInScreen.tsx`, `screens/styles.ts` | empilhar pelo fundo | sim |
| Erros de campo | `useSignInForm.ts`, `TextField` | altura extra | sim |
| Handoff 789 | `.agents/state/handoffs/TASK-789.md` | rodapé da versão | nao |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Risco: baixo
- Estratégia: só login mobile

## Dependencias

- Task 789 (versão no rodapé + `overflow: hidden` no `mainColumn`)
- Task 788 (CTA Criar conta)

## Criterios de conclusao

- [x] Com erro em e-mail e/ou senha, Criar conta e Esqueci minha senha continuam visíveis
- [x] Versão permanece no rodapé
- [x] Hero/nuvem cedem espaço para cima

## Instrucoes de implementacao

- Empilhar o `mainColumn` pelo fundo (`justifyContent: 'flex-end'`) para o overflow cortar o topo, não os CTAs
- Comprimir hero/nuvem quando houver erro de campo
- Não esconder os CTAs dentro do cluster que estoura

## Validacao esperada

- lint dos arquivos alterados

## Resultado da execucao

- `mainColumn` passou a empilhar pelo fundo e o cluster do formulário não encolhe; o overflow corta logo/nuvem, não os CTAs.
- Com erro de e-mail/senha, hero e nuvem diminuem (320→120 e 200→64) para caber os HelperTexts.
- `useSignInForm` expõe `hasFieldErrors`.

## Contexto utilizado

- Task 790, Slice 002, `SignInScreen`, `styles`, `useSignInForm`, `TextField`

## Handoff

- `.agents/state/handoffs/TASK-790.md`

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/hooks/useSignInForm.ts`
- `tasks/change-requests/790-manter-ctas-visiveis-erro-login-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-790.md`

## Validacoes executadas

- eslint dos arquivos alterados — passou
- UI em dispositivo não exercitada nesta sessão

## Pendencias pos-task

- Recarregar o Expo, submeter o login vazio e confirmar que Criar conta e Esqueci minha senha continuam visíveis

## Status final

done
