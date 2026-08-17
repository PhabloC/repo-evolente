# Task 098 - Ajustar nuvem, input de e-mail e shapes do login mobile

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

feedback visual do usuario + print

### Fonte primaria visual

- screenshot atual enviado pelo usuario
- `design-system/mobile/prints/login-mobile.png`

## Objetivo

Subir a nuvem, impedir corte do input de e-mail, remover emoji da saudacao e manter shapes geometricos longe do texto de boas-vindas.

## Escopo

- Subir nuvem (overlap com menina mantido)
- Corrigir empilhamento/padding para o campo e-mail nao ser cortado
- Remover 👋 de "Bem-vindo(a)!"
- Reposicionar shapes do topo fora da area do texto
- lint/typecheck

## Fora de escopo

- Cadastro, recovery, tipografia, novos assets

## Dependencias

- Task 097 — done

## Contexto mínimo

- esta task, SignInScreen + styles + SignInCloud styles + SignInForm styles

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] nuvem um pouco mais alta
- [x] input e-mail visivel por completo
- [x] sem emoji na saudacao
- [x] shapes nao sobrepoem o texto de bem-vindo
- [x] lint/typecheck ok

## Resultado da execucao

### Resumo por stack

- **mobile**: nuvem sobe (`marginTop: -64`); form acima do SVG da nuvem com `paddingTop: 36` para o e-mail nao cortar; emoji removido; losango azul e pontos saíram da coluna do texto.

### Decisões técnicas

- Empilhamento: menina `zIndex 1` < nuvem `2` < form `3`; copy/logo `6` acima dos shapes.
- Causa do corte do e-mail: nuvem com zIndex maior que o form; corrigido + padding.

## Handoff

- `.agents/state/handoffs/TASK-098.md`

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInCloud.styles.ts`
- `tasks/change-requests/098-ajustar-nuvem-input-e-shapes-login-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-098.md`

## Validacoes executadas

- lint ok
- typecheck ok

## Pendencias pos-task

- Nenhuma

## Status final

done
