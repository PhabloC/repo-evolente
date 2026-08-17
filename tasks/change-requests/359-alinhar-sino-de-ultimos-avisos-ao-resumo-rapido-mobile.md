# Task 359 - Alinhar sino de Ultimos avisos ao Resumo rapido mobile

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

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

ajuste incremental solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/assets/bell.webp`

## Objetivo

Deixar o sino do card/lista "Ultimos avisos" com o mesmo tratamento visual usado no "Resumo rápido".

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-283.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Composição visual do sino na lista | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | alinhar o item não lido ao padrão do resumo | sim |
| Referência do tratamento visual | `mobile/src/features/shell/components/HomeActionCard/index.tsx` | reproduzir a pastilha/escala usada no resumo rápido | sim |
| Estilos locais | `mobile/src/features/shell/screens/styles.ts` | criar apenas o estilo necessário para a nova pastilha | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter organização e registrar validações | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar o ajuste ao ícone do estado não lido em "Ultimos avisos", sem reabrir copy, status ou comportamento da tela

## Criterios de conclusao

- [x] o sino do item não lido em "Ultimos avisos" usa o mesmo asset `bell.webp`
- [x] a pastilha visual do sino fica alinhada ao padrão do "Resumo rápido"
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 268 - done
- Task 282 - done
- Task 283 - done

## Resultado da execucao

- o item não lido de "Ultimos avisos" passou a renderizar o sino em uma pastilha circular com `orangeSoft`, espelhando o acabamento usado no card "Resumo rápido"
- o estado lido continua usando o tratamento atual com `check.webp`

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-283.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-359.md`

## Arquivos alterados

- `tasks/change-requests/359-alinhar-sino-de-ultimos-avisos-ao-resumo-rapido-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-359.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`

## Validacoes executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo em `WordSearchGameRenderer`, `EditChildProfileScreen`, `EditGuardianProfileScreen`, `HomeHeader`, `AppBackgroundBubbles` e `Screen`
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` - ok (`26` suites, `90` testes)

## Pendencias pos-task

- `npm run lint` do mobile segue com débitos preexistentes fora do escopo desta mudança
- `npm run typecheck` do mobile segue com débitos preexistentes fora do escopo desta mudança

## Status final

done
