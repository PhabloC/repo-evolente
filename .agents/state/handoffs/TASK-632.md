# Handoff — Task 632

- **Título:** Ajustar área segura da tab bar mobile.
- **Slice:** `tasks/slices/058-area-segura-tab-bar-mobile.md`.
- **Status final:** done.
- **Decisões preservadas:** remover `marginBottom: -bottomOverlap` dos três shells preserva o padding seguro existente e sobe a tab bar acima da navegação Android.
- **Contexto mínimo lido:** governança da raiz, índice, task e Slice 058.
- **Contexto sob demanda carregado:** referência de navegação mobile, diretrizes locais e os componentes de shell/tab bar.
- **Arquivos alterados:** os três consumidores da ShellTabBar e os arquivos de rastreabilidade da task.
- **Validações executadas:** lint aprovado; typecheck e testes completos têm falhas preexistentes fora do escopo da tab bar; builds EAS Android/iOS 5 iniciadas.
- **Pendências:** baixar as builds concluídas e distribuí-las pelos canais de teste.
- **Próxima ação sugerida:** publicar o AAB Android 5 no teste interno e enviar o IPA iOS 5 ao App Store Connect.
- **Próximo contexto recomendado:** shells mobile e `useAndroidBottomOverlap`.
- **Contexto que não deve ser carregado:** API, backend, web, contrato e telas sem a tab bar.
