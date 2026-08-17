# Handoff - Task 369

## Task

- identificador: 369
- título: Abrir lista e download de relatórios a partir do perfil mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 011

## Decisões preservadas

- decisão: manter o card de relatórios no perfil apenas como entrada para a nova tela
- motivo: o download agora precisa de um fluxo explícito por item, sem disparar ação acidental no card-resumo
- impacto: o perfil continua calmo e previsível, enquanto a tela dedicada concentra lista e CTA de download

- decisão: implementar o download autenticado na `reportsService`
- motivo: o endpoint `/reports/{reportId}/download` exige bearer token e integração com armazenamento do dispositivo
- impacto: a tela só coordena estado visual, enquanto rede e abertura do arquivo ficam encapsuladas no domínio de relatórios

## Contexto utilizado

- handoff `TASK-357`
- `tasks/change-requests/357-adicionar-card-de-relatorios-no-perfil-mobile.md`
- `contracts/openapi.yaml#/paths/~1reports/get`
- `contracts/openapi.yaml#/paths/~1reports~1{reportId}~1download/get`
- `mobile/src/features/reports/**`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/routes/RootNavigator.tsx`

## Arquivos alterados

- `mobile/src/features/reports/types/report.ts`
- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/features/reports/hooks/useGuardianReports.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/shell/screens/guardianReportsStyles.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/routes/params.ts`
- `tasks/change-requests/369-abrir-lista-e-download-de-relatorios-a-partir-do-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-369.md`

## Validações executadas

- `cd mobile && npm run lint` — falhou por erros preexistentes fora do escopo
- `cd mobile && npm run typecheck` — falhou por erros preexistentes fora do escopo
- `cd mobile && npm run test` — passou (`27` suítes, `95` testes)

## Pendências ou bloqueios

- erros preexistentes de lint e typecheck no mobile continuam abertos
- a abertura do arquivo baixado depende do suporte do dispositivo ao arquivo salvo

## Próxima ação sugerida

- se o usuário quiser refinar a experiência, tratar feedback pós-download e possíveis estados de arquivo não suportado no dispositivo

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-369.md`
- `mobile/src/features/reports/**`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
