# Handoff Task 712

- Slice: 034 - Jogo da memória de articulação
- Status final: done
- Decisão: usar `exerciseInstructionAudioUrl` e aguardar `announcePraise()` antes de `announceExerciseInstruction()`.
- Contexto usado: Task 527, script de upload de áudios, bootstrap de catálogo, runtime mobile e prévia web.
- Arquivos alterados: script de upload, tipos/configuração de memória, bootstrap, serviço de áudio mobile, renderer mobile, preview web e teste do helper de storage.
- Validações: upload S3 + atualização do banco passaram; teste backend isolado passou. Checks globais têm falhas preexistentes; teste mobile não inicia por mock nativo existente do `expo-audio`.
- Pendência: smoke manual no app e na prévia web.
- Próximo contexto: verificar manualmente um acerto com áudio gravado e confirmar que não há sobreposição.
