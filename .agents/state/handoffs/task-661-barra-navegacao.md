# Handoff — Task 661

- Slice: 010 — shell mobile do responsável
- Status final: done
- Decisão: configurar `expo-navigation-bar` em modo claro com botões escuros; o SDK atual não expõe configuração JS de cor de fundo.
- Arquivos alterados: `mobile/src/app/AppGate.tsx`, `mobile/app.json` e `mobile/src/features/shell/navigators/styles.ts`.
- Correção posterior: `androidNavFill` passou de `colors.primary` para `colors.background`, removendo o laranja visível sob a navegação nativa.
- Pendências: nenhuma.
