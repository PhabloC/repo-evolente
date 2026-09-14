# Handoff Task 679

- Slice: `tasks/slices/030-escrita-guiada-de-letras.md`
- Status final: done
- Decisão: desabilitar `ScrollView` apenas para `alphabet-writing`, preservando os demais jogos.
- Contexto usado: governança raiz, Slice 030, guias mobile e telas `TrailActivityScreen`/`AlphabetWritingGameRenderer`.
- Arquivo alterado: `mobile/src/features/trail/screens/TrailActivityScreen.tsx`.
- Validações: ESLint direcionado sem erro reportado; typecheck e teste direcionado não concluíram no ambiente.
- Pendência: smoke manual em Android/iOS.
- Próximo contexto: nenhum adicional necessário; apenas validação em dispositivo se disponível.
