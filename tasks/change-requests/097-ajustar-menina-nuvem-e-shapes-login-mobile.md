# Task 097 - Ajustar menina atras da nuvem e espaçar shapes do login mobile

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

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas + feedback visual do usuario

### Fonte primaria visual

- `design-system/mobile/prints/login-mobile.png`
- screenshot atual do login enviado pelo usuario nesta solicitacao

## Objetivo

Colocar a parte inferior do corpo da menina sutilmente atras da nuvem e espaçar melhor os elementos geometricos do topo e da base.

## Escopo

- Empilhar a nuvem acima do corpo da menina (zIndex) com overlap sutil
- Reposicionar shapes top/bottom para ficarem mais separados
- Validar typecheck/lint

## Fora de escopo

- Mudar formulario, copy, cadastro, assets ou tipografia
- Recovery/reset

## Dependencias

- Task 096 — done

## Contexto mínimo

- esta task, slice 002, handoff TASK-096, SignInScreen + styles + SignInCloud

## Contexto sob demanda

| Gatilho | Fonte | Obrigatorio? |
|---|---|---|
| Layout atual | `mobile/src/features/auth/screens/**` | sim |
| Print | `design-system/mobile/prints/login-mobile.png` | opcional |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] corpo inferior da menina atras da nuvem (overlap sutil)
- [x] shapes do topo e da base mais separados
- [x] lint/typecheck ok

## Validacao esperada

- `cd mobile && npm run lint`
- `cd mobile && npm run typecheck`

## Resultado da execucao

### Resumo por stack

- **mobile**: menina com overlap sutil atras da nuvem (zIndex + marginBottom); shapes top/bottom redistribuidos com maior separacao.

### Decisões técnicas

- Nuvem `zIndex: 5` sobre a menina `zIndex: 1`; texto/logo permanecem acima.
- Overlay sutil (parte inferior do corpo), conforme escolha do usuario.
- Shapes da base espalhados na horizontal; canvas com mais padding inferior.

## Contexto utilizado

- task, styles do SignIn + SignInCloud, feedback visual do screenshot

## Handoff

- `.agents/state/handoffs/TASK-097.md`

## Arquivos alterados

- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInCloud.styles.ts`
- `tasks/change-requests/097-ajustar-menina-nuvem-e-shapes-login-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-097.md`

## Validacoes executadas

- lint ok
- typecheck ok

## Pendencias pos-task

- Nenhuma

## Status final

done
