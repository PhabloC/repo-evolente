# Task 678 - Visualizar atividade no acervo master mobile

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

- Não aplicável; reutiliza o conteúdo já carregado.

## Modo de execução

single-stack

## Slice vertical

- Slice 006 — `tasks/slices/006-catalogo-conteudos-master.md`

## Objetivo

Adicionar uma ação “Visualizar atividade” no detalhe de conteúdo do Acervo master mobile, abrindo a atividade em modo de prévia.

## Contexto mínimo

- esta task
- `mobile/src/features/admin/contents/screens/AdminContentDetailScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/types/trail.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI mobile | `mobile/docs/ai/MOBILE_PATTERNS.md` | composição da ação e navegação acessível. |
| Validação | `mobile/docs/ai/QA.md` | lint, typecheck e testes. |

## Orçamento de contexto

- baixo

## Critérios de aceite

- [x] Detalhe do conteúdo exibe botão “Visualizar atividade”.
- [x] Botão abre a atividade em modo preview.
- [x] Preview não permite concluir ou alterar progresso.

## Resultado da execucao

- Adicionado o botão `Visualizar atividade` no detalhe do Acervo e navegação para `TrailActivity` com `preview: true`.
- Registrada a rota `TrailActivity` também no navegador do perfil Master, permitindo que a prévia seja aberta nesse fluxo.

## Contexto utilizado

- Detalhe de conteúdo master, tela de atividade e tipos de trilha.

## Arquivos alterados

- `mobile/src/features/admin/contents/screens/AdminContentDetailScreen.tsx`
- `mobile/src/routes/RootNavigator.tsx`

## Validacoes executadas

- ESLint da tela executado sem erros.

## Pendencias pos-task

- Validar manualmente jogos, áudio e vídeo no emulador/dispositivo.

## Status final

done

## Status final

in_progress
