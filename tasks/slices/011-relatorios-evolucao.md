# Slice 011 - Relatorios de evolucao

## Status

done

## Objetivo de negocio

Profissional gera PDF e disponibiliza ao responsavel.

## Entrega verificavel

Export PDF; responsavel so acessa apos disponibilizacao.

## Fora de escopo

- Gamificacao
- Viewer mobile dedicado

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- front-end
- backend
- mobile

## Contrato

- `contracts/openapi.yaml#/paths` de reports

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md` (historico/relatorios)

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (área do responsável)

## Permissoes e atores

- Profissional gera
- Responsavel le liberados

## Casos de erro e borda

- Sem dados
- Falha geracao
- 403 nao liberado

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito
- PDF sem lib externa (task sem autorizacao de dependencia)

## Tasks relacionadas

- `tasks/025-relatorios-pdf-csv.md` - API+UI relatorios — **done**
- `tasks/change-requests/314-estruturar-conteudo-do-relatorio-da-crianca.md` - estruturar o conteúdo prioritário do relatório da criança — **done**
- `tasks/change-requests/315-ajustar-botao-baixar-na-tabela-de-relatorios-web.md` - diferenciar o CTA `Baixar` e alinhar a coluna de ações — **done**
- `tasks/change-requests/316-extrair-variant-info-do-botao-e-aplicar-no-baixar-relatorios.md` - aderir o CTA `Baixar` ao azul oficial do design system e extrair variant reutilizável — **done**
- `tasks/change-requests/317-excluir-relatorios-gerados-na-tela-de-relatorios.md` - permitir exclusão de relatórios gerados com confirmação explícita — **done**
- `tasks/change-requests/318-reduzir-acao-de-excluir-para-icone-na-tabela-de-relatorios.md` - reduzir a ação de exclusão para ícone de lixeira mantendo o modal — **done**
- `tasks/change-requests/319-reordenar-acao-disponibilizar-na-tabela-de-relatorios.md` - mover `Disponibilizar` para a primeira posição da fileira de ações — **done**
- `tasks/change-requests/320-restaurar-acentuacao-nos-relatorios-pdf.md` - corrigir acentuação do conteúdo emitido nos PDFs de relatório — **done**
- `tasks/change-requests/321-migrar-geracao-de-pdf-para-puppeteer-com-layout-personalizado.md` - substituir o PDF textual por geração com Puppeteer e layout estruturado — **done**
- `tasks/change-requests/322-formatar-datas-do-pdf-em-dd-mm-aaaa.md` - exibir datas do PDF no formato `dd/mm/aaaa` — **done**
- `tasks/change-requests/323-adicionar-confirmacao-ao-disponibilizar-relatorio.md` - exigir confirmação antes de disponibilizar relatório ao responsável — **done**
- `tasks/change-requests/362-refinar-feedback-de-sucesso-ao-disponibilizar-relatorio-web.md` - refinar o feedback visual exibido após disponibilizar o relatório ao responsável — **done**
- `tasks/change-requests/364-separar-criacao-de-relatorio-da-filtragem-na-pagina-web.md` - separar geração de relatório e filtragem do histórico na página web — **done**
- `tasks/change-requests/365-refinar-filtro-no-topo-e-por-datas-na-pagina-de-relatorios-web.md` - mover o filtro para o topo, adicionar datas e refinar a copy da página — **done**
- `tasks/change-requests/366-aumentar-espaco-entre-gerar-relatorio-e-tabela-web.md` - aumentar o respiro entre o bloco de geração e a tabela de histórico — **done**
- `tasks/change-requests/363-transformar-gerado-em-em-badge-na-tabela-de-relatorios-web.md` - transformar a coluna `Gerado em` em badge na tabela de relatórios — **done**
- `tasks/change-requests/358-notificar-paciente-ao-disponibilizar-relatorio.md` - notificar o responsável quando o relatório for disponibilizado — **done**
- `tasks/change-requests/369-abrir-lista-e-download-de-relatorios-a-partir-do-perfil-mobile.md` - abrir lista e download de relatórios a partir do perfil mobile — **done**
- `tasks/change-requests/370-exibir-tab-bar-do-responsavel-nas-edicoes-de-perfil-e-relatorios-mobile.md` - exibir tab bar do responsável na tela mobile de relatórios — **done**
- `tasks/change-requests/371-corrigir-abertura-do-arquivo-baixado-nos-relatorios-mobile-android.md` - corrigir abertura do arquivo baixado no Android — **done**
- `tasks/change-requests/372-agrupar-relatorios-por-mes-na-tela-mobile-do-responsavel.md` - agrupar relatórios por mês na tela mobile do responsável — **done**
- `tasks/change-requests/373-remover-criacao-de-relatorio-csv-e-manter-apenas-pdf.md` - remover a criação de relatórios CSV e manter apenas PDF no fluxo novo — **done**
- `tasks/change-requests/387-preservar-renovacao-de-token-no-download-de-relatorios-mobile.md` - preservar renovação de token e validar status no download mobile — **done**
- `tasks/change-requests/389-tratar-periodo-do-relatorio-como-data-civil-no-mobile.md` - exibir o período do relatório sem deslocamento de fuso — **done**
- `tasks/change-requests/390-alinhar-agrupamento-mensal-dos-relatorios-mobile-ao-fuso-local.md` - alinhar chave e rótulo do agrupamento mensal ao fuso local — **done**
- `tasks/change-requests/391-filtrar-relatorios-indisponiveis-no-perfil-do-responsavel-mobile.md` - unificar o filtro de relatórios disponíveis entre perfil e lista — **done**
- `tasks/change-requests/395-preservar-filtro-ao-atualizar-relatorios-web.md` - preservar o filtro visível ao atualizar o histórico web — **done**
- `tasks/change-requests/396-filtrar-atividades-planejadas-por-data-no-relatorio.md` - calcular atividades previstas pela data planejada de cada item — **done**
- `tasks/change-requests/442-alinhar-botao-gerar-relatorio-mesma-linha-filtros.md` - botão Gerar relatório na mesma linha dos filtros Paciente/De/Até — **done**
- `tasks/change-requests/443-foto-paciente-tabela-relatorios-web.md` - foto do paciente na coluna Paciente da tabela — **done**
- `tasks/change-requests/444-alinhar-filtros-acoes-historico-relatorios-mesma-linha.md` - filtros e ações do histórico na mesma linha — **done**
- `tasks/change-requests/453-enxugar-layout-pagina-relatorios-web.md` - tentativa em `/relatorios` profissional — **cancelled/reverted** (pedido era admin)

## Dependencias do slice

- Slice 008

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` | regras do slice | sim |
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim se UI web |
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim se UI mobile |
| API | `contracts/openapi.yaml` | API | sim se API |
| Front-end | `front-end/docs/ai/` | front envolvido | sim se front |
| Backend | `backend/docs/ai/` | back envolvido | sim se back |
| Mobile | `mobile/docs/ai/` | mobile envolvido | sim se mobile |

## Risco de contexto

- medio
- estrategia: carregar apenas secoes/paths citados nas tasks

## Observacoes de rastreabilidade

- Entrega Task 025: `/reports` + UI `/relatorios`; 403 pré-share; audit `report.shared`.
- Change request 314 reabre o slice para enriquecer a estrutura do conteúdo do relatório da criança em PDF/CSV.
- Change request 314 concluída: PDF/CSV agora nascem de um modelo estruturado de relatório, com resumo, métricas, evolução por área, linha do tempo, alertas, orientações e próximos passos.
- Change request 315 refinou a tabela de relatórios com CTA `Baixar` diferenciado e alinhamento da coluna de ações.
- Change request 316 promoveu o estilo azul do CTA `Baixar` para o `ui/Button`, aderindo explicitamente à cor `Confianca` do design system e removendo skin local da página.
- Change request 317 adicionou exclusão de relatórios no contrato/backend e na UI web, com confirmação destrutiva e auditoria `report.deleted`.
- Change request 318 compactou a ação de exclusão da tabela para ícone-only, preservando o modal de confirmação e o nome acessível do botão.
- Change request 319 reordenou a coluna de ações para priorizar `Disponibilizar` como primeiro CTA quando o relatório ainda está privado.
- Change request 320 restaurou a acentuação do conteúdo gerado no PDF e ajustou a serialização do arquivo para preservar caracteres latinos.
- Change request 321 substituiu o PDF textual por geração com Puppeteer, com layout HTML estruturado em tabela e logo da Evolente no topo quando o asset está disponível.
- Change request 322 padronizou as datas exibidas no PDF para `dd/mm/aaaa`, incluindo período, emissão e linha do tempo.
- Change request 323 adicionou modal de confirmação antes do `Disponibilizar`, mantendo o padrão visual e acessível dos modais da tela de relatórios.
- Change request 362 substituiu o texto simples de sucesso por um card de feedback com hierarquia visual e texto de apoio mais claro após o compartilhamento do relatório.
- Change request 364 separou semanticamente a geração do relatório e a filtragem do histórico em blocos distintos na página.
- Change request 365 promoveu o filtro para o topo, adicionou recorte por datas na tabela e refinou os textos de orientação da página.
- Change request 366 ampliou o espaçamento vertical entre o bloco de geração e a tabela de histórico.
- Change request 363 transformou a data da coluna `Gerado em` em badge para aumentar destaque e escaneabilidade na tabela.
- Change request 358 passou a emitir notificação `report_shared` ao responsável na primeira disponibilização do relatório, reaproveitando a central in-app de avisos já existente no mobile.
- Change request 369 abriu no app mobile uma tela dedicada de relatórios para o responsável, ligada ao card do perfil, com listagem dos arquivos compartilhados e download autenticado via `/reports/{reportId}/download`.
- Change request 370 fez a tela mobile de relatórios reaproveitar a mesma tab bar do responsável usada no shell principal, mantendo a navegação lateral consistente com o restante da área do responsável.
- Change request 371 ajustou a abertura pós-download no Android, convertendo o arquivo local baixado em `content://...` antes de chamar `Linking.openURL`.
- Change request 372 agrupou a lista mobile de relatórios por mês, mantendo os arquivos mais novos no topo e separando os antigos em blocos mensais.
- Change request 373 removeu o formato CSV do fluxo de criação web/API, manteve a emissão nova fixada em PDF e preservou compatibilidade de leitura/download para arquivos CSV legados.
- Change request 387 alinhou o download mobile ao fluxo de refresh do `apiClient`, renovando o token em resposta 401, validando o status HTTP antes de abrir o arquivo e descartando downloads que retornaram erro.
- Change request 389 passou a tratar `periodFrom`/`periodTo` como datas civis na tela mobile, com utilitário compartilhado de data, evitando exibir o dia anterior em fusos negativos.
- Change request 390 unificou o parse de datas da tela mobile em `parseDisplayDate`, fazendo chave e rótulo do agrupamento mensal saírem da mesma data local.
- Change request 391 moveu o filtro `availableToGuardian` para o `select` de `useGuardianReportsQuery`, alinhando o resumo do perfil à lista de relatórios do responsável.
- Change request 395 separou o filtro do histórico do paciente selecionado para criação, preservando a listagem visível após gerar, disponibilizar ou excluir.
- Change request 396 passou a filtrar cada atividade planejada por `weekStartDate + weekday - 1`, corrigindo totais e taxa de adesão quando o período corta uma semana.

## Status final

done
