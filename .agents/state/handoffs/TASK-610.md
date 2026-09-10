# Handoff Task 610

- Slice: `tasks/slices/002-autenticacao.md`
- Status final: done
- Decisão: tablet a partir de 600 dp; hero e formulário centralizados com largura máxima de 560 dp.
- Referência máxima: viewport de iPad Pro em `1024 × 1366 dp`.
- Tablet: cluster sobe para a região central, nuvem usa largura total e formulário mantém `maxWidth: 560` centralizado.
- O lift/animacao de teclado é desativado no tablet para SignIn e PasswordRecovery via parâmetro do hook.
- Contexto usado: design system mobile, guias AI mobile e tela/estilos do SignIn.
- Arquivos alterados: `mobile/src/features/auth/screens/SignInScreen.tsx`, `mobile/src/features/auth/screens/styles.ts`.
- Validações: comandos Expo/npm iniciados, sem conclusão no ambiente; diff revisado.
- Pendência: validar portrait/landscape e teclado em tablet.
- Próximo contexto: execução visual em tablet.
