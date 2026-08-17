# Task 466 - Alinhar modal de excluir relatório ao modal de inativar

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/011-relatorios-evolucao.md`

## Objetivo

Deixar o modal de excluir relatório (perfil profissional) com o mesmo layout split do modal de inativar usuário (master).

## Criterios de conclusao

- [x] rail de alerta + painel de confirmação
- [x] card do relatório com paciente/arquivo/formato
- [x] CTA de perigo e cancelar preservados
- [x] modal de disponibilizar relatório inalterado

## Resultado da execucao

- Modal delete com `hideHeader`, rail vermelho e painel direito no padrão AdminUsers
- Classes `deleteConfirm*` em Reports para não afetar o modal de share

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/000-index.md`

## Status final

done
