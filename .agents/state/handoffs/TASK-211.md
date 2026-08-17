# Handoff - Task 211

## Task

- identificador: 211
- título: Header do perfil: voltar, título central e sem textos extras
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010
- entrega verificável: header do perfil simplificado

## Decisões preservadas

- decisão: barra custom no perfil (não alterar ScreenHeader global)
- motivo: layout centrado com ações laterais diferente do padrão eyebrow/title
- impacto: voltar → home; Perfil central; logout à direita

## Contexto utilizado

- task 211, `ResponsavelProfileScreen`, `ResponsavelShellNavigator`, padrão `TrailActivityScreen` topBar

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `tasks/change-requests/211-header-perfil-voltar-titulo-central-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-211.md`

## Validações executadas

- `npm run typecheck` — ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma
