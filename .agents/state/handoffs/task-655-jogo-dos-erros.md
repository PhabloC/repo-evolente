# Handoff — Task 655

- Slice: 035 — Jogo dos erros (articulação)
- Status final: done
- Decisões: dica destaca a primeira diferença pendente sem marcar acerto; “Avançar” entra no exercício da rodada; título atualizado para exercícios de articulação/articulatórios.
- Contexto usado: prévia web, runtime mobile, estilos, metadados mobile e acessibilidade web.
- Arquivos alterados: componentes/estilos do jogo em `front-end` e `mobile`, além de metadados mobile.
- Validações: ESLint direcionado web e `git diff --check` passaram; typechecks completos interrompidos por duração.
- Pendências: nenhuma funcional; repetir typechecks completos em CI/janela dedicada.
- Próximo contexto: somente se houver ajuste visual ou revisão de UX da dica/avanço.
- Ajuste posterior: marcador da dica agora usa as coordenadas do hotspot, em vez do centro da imagem, nas duas stacks.
