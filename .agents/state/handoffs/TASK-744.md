# Handoff Task 744

- Slice: `tasks/slices/060-one-signal-push-mobile.md`
- Status final: `done`
- Decisão: manter `logo-seal-original.webp` intacto e usar sua conversão PNG nos campos nativos processados pelo Expo/OneSignal; remover a propriedade raiz `notification`, incompatível com Expo 57.
- Validações: `npx expo prebuild --no-install --platform android` passou; builds EAS Android e iOS foram iniciados com a configuração corrigida.
- Pendência: acompanhar a conclusão dos builds EAS Android `08c...` e iOS `145...`.
