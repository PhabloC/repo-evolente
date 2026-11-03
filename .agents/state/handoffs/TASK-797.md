# Handoff — Task 797

- **Título:** Apontar o mobile para api.evolente.com.br após teste no Chrome.
- **Slice:** `tasks/slices/057-configuracao-api-publica-mobile.md`.
- **Status final:** done.
- **Decisões preservadas:** EAS production e OTA 1.0.3 apontam para `https://api.evolente.com.br/api`. Chrome mostrando JSON foi o gatilho; o cliente nativo ainda pode falhar se a Cloudflare tratar OkHttp diferente do navegador.
- **Contexto mínimo lido:** governança, índice, task e Slice 057.
- **Contexto sob demanda carregado:** EAS production.
- **Arquivos alterados:** só rastreabilidade.
- **Validações executadas:** env set; OTA Android `04b5c590-5616-4303-8d2a-d406e92ea461` e iOS `54d94927-07a0-4b40-9e40-8d2d3cc4c5dd`; bundle com `api.evolente.com.br`.
- **Pendências:** usuário precisa fechar o app duas vezes e testar login.
- **Próxima ação sugerida:** se o login falhar, reverter de novo (padrão da Task 796) e tratar WAF/Bot Fight para o cliente nativo.
- **Próximo contexto recomendado:** feedback de login no aparelho.
- **Contexto que não deve ser carregado:** design-system, OpenAPI, UI.
