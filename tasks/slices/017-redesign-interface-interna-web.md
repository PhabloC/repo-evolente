# Slice 017 - Redesign da interface interna web

## Status

done

## Objetivo de negocio

Elevar a qualidade visual e a consistencia de toda a area autenticada web da Evolente, preservando os fluxos e reforcando acolhimento, clareza e confianca clinica.

## Entrega verificavel

- Shell compartilhado, dashboard e paginas internas usam a mesma linguagem visual responsiva.
- Pacientes, planejamentos, biblioteca, relatorios, administracao e configuracoes possuem hierarquia e estados coerentes.
- O auth permanece sem ilustracoes ou formas decorativas no fundo.

## Fora de escopo

- Alteracoes de API, regras de negocio ou mobile.
- Redesign das telas publicas alem da remocao do fundo.

## Tasks relacionadas

- Task 035 - remover fundo auth
- Task 036 - fundacao visual, shell e dashboard
- Task 037 - pacientes e planejamentos
- Task 038 - biblioteca e relatorios
- Task 039 - administracao e configuracoes
- `tasks/change-requests/052-refinar-perfil-usuario-configuracoes-web.md` - refino visual incremental do perfil do usuario em configuracoes
- `tasks/change-requests/077-refinar-usuarios-admin-web.md` - refino visual incremental da pagina dedicada de usuarios do admin
- `tasks/change-requests/078-paginacao-usuarios-admin-web.md` - paginação incremental da tabela de usuarios do admin
- `tasks/change-requests/079-remover-scroll-externo-shell-web.md` - correção do scroll externo do shell autenticado
- `tasks/change-requests/080-confirmacao-inativar-usuarios-admin-web.md` - confirmação antes de inativar usuários no admin
- `tasks/change-requests/081-limpar-textos-superiores-tabela-usuarios-admin.md` - remoção de textos redundantes acima da tabela de usuários
- `tasks/change-requests/082-refinar-card-profissionais-vinculos-admin-web.md` - refino visual incremental do bloco de profissionais e vínculos no admin
- `tasks/change-requests/083-estruturar-central-relatorios-master-web.md` - estruturação da central de relatórios do master com prioridades e exportações ideais
- `tasks/change-requests/084-ajustar-texto-hero-relatorios-master-web.md` - ajuste textual do hero da central de relatórios do master
- `tasks/change-requests/085-exportacoes-csv-relatorios-master-web-e-api.md` - exportações CSV reais para a central de relatórios do master
- `tasks/change-requests/086-ajustar-grade-exportacoes-relatorios-master-web.md` - simplificação visual da grade de exportações na central do master
- `tasks/change-requests/087-ajustar-grade-catalogo-relatorios-master-web.md` - ajuste da grade do catálogo ideal de relatórios para duas colunas
- `tasks/change-requests/454-enxugar-pagina-relatorios-admin-web.md` - remover catálogo/planejamento e deixar só exportações CSV — **done**
- `tasks/change-requests/455-exportacoes-csv-laranja-e-pdf-relatorios-admin.md` - CSV laranja + exportação PDF com logo — **done**
- `tasks/change-requests/459-melhorar-layout-modal-nova-atividade-biblioteca.md` - layout do modal Nova atividade — **done**
- `tasks/change-requests/088-clareza-e-paginacao-tabela-logs-admin-web.md` - clareza textual e paginação da tabela de logs do admin
- `tasks/change-requests/089-corrigir-page-size-users-nos-logs-admin-web.md` - correção do pageSize excedente no carregamento auxiliar dos logs
- `tasks/change-requests/152-hardening-shell-admin-web-frontend.md` - hardening comportamental do shell autenticado e do admin web
- `tasks/change-requests/153-otimizar-logs-paginacao-e-exportacoes-admin-web.md` - otimização incremental de logs, paginação e exportações concorrentes no admin web
- `tasks/change-requests/154-restaurar-bloqueio-scroll-externo-shell-web.md` - restauração do bloqueio de scroll externo do documento no shell autenticado
- `tasks/change-requests/155-criar-usuario-master-na-pagina-de-usuarios-web.md` - criação operacional de outro login master na rota dedicada de usuários
- `tasks/change-requests/182-avatar-sidebar-e-pagina-usuarios-web.md` - avatar no sidebar e na listagem de usuários
- `tasks/change-requests/183-redesign-pagina-usuarios-admin-web.md` - redesign da página de usuários com abas, badges e filtro dropdown
- `tasks/change-requests/184-botao-filtro-icone-circular-usuarios-web.md` - botão de filtro só ícone circular
- `tasks/change-requests/185-icones-abas-pagina-usuarios-web.md` - ícones Lucide nas abas de usuários
- `tasks/change-requests/186-border-radius-8px-modais-web.md` - border-radius 8px nos modais
- `tasks/change-requests/187-botao-inativar-icone-usuarios-web.md` - botão inativar só ícone
- `tasks/change-requests/188-refinar-modal-confirmacao-inativacao-usuarios.md` - refino do modal de confirmação de inativação
- `tasks/change-requests/189-footer-modal-inativacao-botoes-lado-a-lado.md` - botões lado a lado e fundo no footer
- `tasks/change-requests/190-largura-e-footer-modal-inativacao.md` - largura maior e footer cinza full-bleed
- `tasks/change-requests/191-corrigir-footer-modal-inativacao.md` - scroll, gap e margens do footer
- `tasks/change-requests/192-colunas-vinculo-profissional-paciente-usuarios.md` - colunas de vínculo profissional-paciente
- `tasks/change-requests/193-refinar-coluna-profissional-tabela-pacientes.md` - refino visual da coluna profissional
- `tasks/change-requests/194-bolinha-esquerda-badge-status-usuarios.md` - bolinha à esquerda no badge de status
- `tasks/change-requests/195-abrir-pacientes-vinculados-ao-clicar-profissional.md` - modal de pacientes ao clicar no profissional
- `tasks/change-requests/196-icone-save-plus-botao-novo-usuario.md` - ícone SavePlus no botão Novo usuário
- `tasks/change-requests/197-icone-save-plus-criar-usuario-master.md` - ícone SavePlus no botão criar usuário master
- `tasks/change-requests/258-normalizar-telefone-no-criar-usuario-master-web.md` - validação e normalização do telefone no modal de criar usuário master
- `tasks/change-requests/333-refinar-feedback-e-mascara-no-criar-usuario-master-web.md` - banner de sucesso e máscara no telefone do modal de criar usuário master
- `tasks/change-requests/297-unificar-design-dos-ctas-de-dashboard-pacientes-e-planejamentos-web.md` - unificação visual dos principais CTAs operacionais dessas três páginas
- `tasks/change-requests/298-corrigir-busca-expansivel-no-header-web.md` - correção comportamental da busca expansível no header compartilhado
- `tasks/change-requests/299-scroll-horizontal-na-grade-semanal-do-planejamento-web.md` - rolagem horizontal na grade semanal para evitar compressão dos cards
- `tasks/change-requests/300-arraste-com-maozinha-na-grade-semanal-do-planejamento-web.md` - arraste horizontal com cursor de mão na grade semanal
- `tasks/change-requests/301-corrigir-overflow-e-arraste-da-grade-semanal-web.md` - correção do vazamento à direita e do arraste real da grade semanal
- `tasks/change-requests/302-refinar-secao-de-evolucao-da-trilha-web.md` - redesign da seção de progresso/evolução da trilha do paciente
- `tasks/change-requests/303-corrigir-renderizacao-do-grafico-de-evolucao-web.md` - correção da renderização do gráfico de evolução na trilha
- `tasks/change-requests/304-scroll-no-card-de-historico-recente-web.md` - scroll interno no card de histórico recente da trilha
- `tasks/change-requests/305-evitar-deslocamento-do-subtitulo-ao-abrir-busca-web.md` - estabilidade do header ao abrir a busca compartilhada
- `tasks/change-requests/306-corrigir-header-da-trilha-da-crianca-ao-abrir-busca-web.md` - correção da regressão remanescente do header na página da trilha com ações no topo
- `tasks/change-requests/307-limitar-largura-do-heading-no-header-da-trilha-web.md` - restauração do layout original do header com limitação de largura do texto à esquerda
- `tasks/change-requests/308-limitar-largura-maxima-das-acoes-do-header-web.md` - limitação de largura máxima do bloco da direita do header compartilhado
- `tasks/change-requests/309-manter-sugestao-da-anamnese-como-rascunho-ate-salvar-trilha-web.md` - sugestão da anamnese apenas em rascunho local até o salvamento explícito da semana
- `tasks/change-requests/310-refinar-card-de-status-e-sugestao-da-trilha-web.md` - refino visual do bloco de status e feedback da sugestão na trilha
- `tasks/change-requests/311-mover-feedback-da-sugestao-para-baixo-dos-botoes-da-trilha-web.md` - reposicionamento do feedback da sugestão para baixo dos botões da semana
- `tasks/change-requests/312-adicionar-confirmacao-antes-de-salvar-semana-na-trilha-web.md` - confirmação explícita em modal antes de persistir a semana
- `tasks/change-requests/313-unificar-componente-global-de-tabelas-web.md` - consolidacao do layout e cabecalho das tabelas no componente global `Table`
- `tasks/change-requests/347-reposicionar-ctas-de-pacientes-e-planejamentos-abaixo-do-header.md` - reposicionamento dos CTAs principais das páginas de pacientes e planejamentos abaixo do heading
- `tasks/change-requests/348-reposicionar-acoes-do-perfil-do-paciente-abaixo-do-header.md` - reposicionamento das ações do perfil do paciente abaixo do heading
- `tasks/change-requests/349-reposicionar-acoes-da-trilha-do-paciente-abaixo-do-header.md` - reposicionamento das ações da trilha do paciente abaixo do heading
- `tasks/change-requests/351-refinar-botoes-e-resumo-da-semana-na-trilha-web.md` - refinamento visual dos botões azuis e do resumo semanal na trilha do paciente
- `tasks/change-requests/352-remover-gradientes-dos-botoes-do-sistema-web.md` - padronização global dos botões web para fundos sólidos sem gradiente
- `tasks/change-requests/353-varredura-final-de-controles-interativos-com-gradiente-web.md` - fechamento da varredura residual de controles interativos ainda com gradiente
- `tasks/change-requests/354-refinar-subtitulo-do-dashboard-web.md` - melhoria de hierarquia visual e semântica no subtítulo do dashboard profissional
- `tasks/change-requests/355-adicionar-acao-de-visualizar-na-tabela-editorial-da-biblioteca-web.md` - exposição do ícone de preview na tabela editorial também para o modo leitura
- `tasks/change-requests/356-refinar-hover-e-badge-dos-cards-de-jogos-no-modo-profissional-web.md` - ajuste visual dos cards de jogos vistos pelo profissional
- `tasks/change-requests/401-atualizar-abas-e-objetivo-da-biblioteca-web.md` - atualização das abas e do bloco de objetivo da seção `Conteúdos` da biblioteca web
- `tasks/change-requests/402-restaurar-aba-todas-na-biblioteca-web.md` - restauração da aba `Todas` como primeira entrada da seção `Conteúdos`
- `tasks/change-requests/403-alinhar-dropdown-categorias-biblioteca-web.md` - alinhamento do dropdown `Categoria` do modal da biblioteca às categorias definidas no chat
- `tasks/change-requests/404-adicionar-botao-salvar-conteudo-no-topo-do-modal.md` - ação visível de `Salvar conteúdo` no topo do modal da biblioteca
- `tasks/change-requests/091-ajustar-subtitulo-e-placeholders-modal-conteudo-web.md` - ajuste textual e de placeholders no modal de conteúdo da biblioteca
- `tasks/change-requests/181-icones-lucide-em-todos-os-botoes-front.md` - ícones Lucide em todos os botões textuais do front-end
- Task 044 - refinamento visual dos modais compartilhados
- Task 047 - refinamento visual da tela de relatórios por referência de chat
- Task 048 - refinamento visual da tabela de planejamentos por referência de chat

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- task em execucao e handoff imediatamente anterior deste slice

## Contexto sob demanda

- `design-system/front/Design_System_Evolente_Desktop.md`
- arquivos do shell e apenas das paginas cobertas pela task atual
- docs locais de acessibilidade e componentes

## Risco de contexto

- Alto se executado como uma unica task; mitigado pela divisao em quatro entregas internas sequenciais.

## Resultado

- Auth sem conteudo de fundo e area interna redesenhada de ponta a ponta nas Tasks 035-039.
- Shell, dashboards, pacientes, planejamentos, biblioteca, relatorios, administracao, configuracoes, estados auxiliares e modais compartilhados concluídos.
- Task 052 refinou o perfil do usuario em configuracoes com hero, resumo de conta e preferencias mais fortes.
- Task 077 refinou a pagina dedicada de usuarios do admin com hero operacional, tabela mais hierarquica e arvore de vinculos mais legivel.
- Task 078 adicionou paginação real na tabela de usuarios do admin, com rodape alinhado ao padrão de pacientes.
- Task 079 removeu o scroll externo do shell autenticado no desktop, preservando apenas o scroll interno do conteúdo.
- Task 080 adicionou modal de confirmação antes de inativar usuários na tabela do admin.
- Task 081 removeu textos redundantes acima da tabela de usuários, mantendo o contexto de paginação apenas no rodapé.
- Task 082 refinou o card de profissionais e vínculos com hierarquia visual mais forte para profissional, paciente e status.
- Task 083 transformou a rota de relatórios do master em uma central operacional com catálogo ideal, recortes e governança explícita.
- Task 084 refinou a cópia do hero em relatórios do master para uma comunicação mais informativa.
- Task 085 conectou a central do master a exportações CSV reais de usuários, vínculos, assinaturas e logs.
- Task 086 removeu o card lateral da seção de exportações e reorganizou os cards em duas colunas por linha.
- Task 087 reorganizou o catálogo ideal de relatórios em duas colunas por linha no desktop.
- Task 088 deixou a tabela de logs mais clara, com nomes no lugar de IDs e paginação de 6 itens por página.
- Task 089 corrigiu o carregamento auxiliar de usuários na página de logs para respeitar o limite máximo aceito pela API.
- Task 152 endurece o shell autenticado contra corrida de bloqueio de scroll e reforça a resiliência operacional do módulo admin web.
- Task 153 substituiu a varredura total de usuários dos logs por lookup seletivo, compactou a paginação da base de usuários e bloqueou exportações concorrentes na central de relatórios.
- Task 154 restaurou o bloqueio de scroll externo no documento raiz do shell autenticado, preservando apenas o scroll interno do conteúdo após regressão recente.
- Task 155 adicionou criação de outro usuário master na rota dedicada de usuários, com modal validado, refresh da listagem e contrato OpenAPI documentado.
- Task 047 refinou especificamente a tela de relatórios com nova referência visual enviada no chat.
- Task 048 refinou especificamente a tabela da página de planejamentos com nova referência visual enviada no chat.
- Task 091 refinou o modal de conteúdo da biblioteca com subtítulo mais direto e placeholders nos campos textuais do formulário.
- Task 181 padronizou ícones Lucide na prop `icon` de todos os CTAs textuais do componente `Button` (auth + área logada + modais).
- Task 183 redesenhou a página de usuários com abas por categoria, badges de contagem, tabela zebra e filtro dropdown com `FunnelPlus`.
- Task 184 deixou o botão de filtro só com ícone circular.
- Task 185 adicionou ícones Lucide em cada aba da página de usuários.
- Task 186 padronizou o border-radius dos modais web para 8px.
- Task 187 deixou o botão Inativar/Reativar da tabela de usuários só com ícone.
- Task 188 refinou o modal de confirmação de inativação com card do usuário e tom de alerta.
- Task 189 colocou os botões do modal de inativação lado a lado com fundo distinto no footer.
- Task 190 aumentou a largura do modal e deixou o footer cinza claro sem padding lateral/inferior.
- Task 191 removeu o scroll horizontal, adicionou gap entre botões e ajustou margens do footer.
- Task 192 adicionou colunas de quantidade de pacientes (profissionais) e vínculo de profissional (pacientes).
- Task 193 refinou a coluna profissional na tabela de pacientes (inicial + nome / sem vínculo).
- Task 194 colocou a bolinha do badge de status à esquerda do texto.
- Task 195 permite clicar no profissional e abrir o modal com pacientes vinculados.
- Task 196 trocou o ícone do botão Novo usuário para SavePlus.
- Task 197 trocou o ícone do CTA criar usuário master para SavePlus.
- Task 258 passou a validar telefone opcional no modal de criação de usuário master e a enviar o valor normalizado para a API.
- Task 333 refinou o feedback de sucesso da criação de usuário master com um banner local e aplicou máscara de telefone durante a digitação no modal.
- Task 297 unificou o design dos CTAs operacionais de dashboard, pacientes e planejamentos com um componente compartilhado.
- Task 298 corrigiu a busca expansível do header para manter o campo aberto durante a digitação e fechar por um ícone dedicado.
- Task 299 adicionou scroll horizontal na grade semanal do planejamento para preservar a largura dos cards diários.
- Task 300 adicionou arraste com cursor de mão na grade semanal para reforçar a usabilidade do scroll horizontal.
- Task 301 corrigiu o vazamento visual da grade semanal à direita e reimplementou o arraste horizontal com `pointer events`.
- Task 302 redesenhou a seção de evolução da trilha com resumo visual, gráfico semanal mais forte e histórico recente organizado.
- Task 303 corrigiu a renderização do gráfico de evolução ao dar altura real ao contêiner do Recharts.
- Task 304 adicionou scroll interno ao card de histórico recente da seção de evolução da trilha.
- Task 305 estabilizou o layout do header para a abertura da busca não deslocar o subtítulo das páginas.
- Task 306 separou heading e ações no header quando a página injeta CTAs no topo, eliminando a regressão remanescente na trilha da criança.
- Task 307 reverteu a solução estrutural da Task 306 e limitou a largura máxima do heading para manter o layout original sem deslocar o texto.
- Task 308 limitou a largura máxima do bloco de ações/busca do header para reduzir a pressão horizontal sobre o heading.
- Task 309 passou a tratar a sugestão da anamnese como rascunho local até o salvamento explícito e adicionou dirty state real ao botão de salvar semana.
- Task 310 refinou o bloco de status e feedback da trilha com um callout visual mais forte para a sugestão da anamnese.
- Task 311 moveu o callout da sugestão para baixo dos botões operacionais da semana.
- Task 312 adicionou um modal de confirmação antes do salvamento da semana na trilha.
- Task 313 consolidou o layout e o cabecalho das tabelas no componente global `Table`, removendo skins locais em pacientes, planejamentos e relatorios.
- Task 347 passou a renderizar os CTAs principais de pacientes e planejamentos em uma segunda linha abaixo do heading, reduzindo a pressão horizontal no header dessas rotas.
- Task 348 passou a renderizar as ações do perfil do paciente em uma segunda linha abaixo do heading, evitando a compressão do título e subtítulo dessa tela.
- Task 349 passou a renderizar as ações da trilha do paciente em uma segunda linha abaixo do heading, evitando a compressão do título e subtítulo dessa tela.
- Task 351 refinou os CTAs da trilha com azul sólido e deu mais hierarquia visual ao resumo do período semanal no card principal.
- Task 352 removeu gradientes dos botões compartilhados e dos principais CTAs locais do sistema web, consolidando fundos sólidos.
- Task 353 removeu os últimos gradientes residuais em controles interativos do header e da biblioteca, encerrando a varredura pedida pelo usuário.
- Task 354 refinou o subtítulo do dashboard com contexto principal e atualização destacados, além de abrir o header para subtítulos ricos sem markup inválido.
- Task 355 adicionou a ação de visualizar na tabela editorial da biblioteca para o profissional, mantendo edição e mutações restritas ao master.
- Task 356 moveu a badge para baixo do título e trocou o botão fixo por overlay de preview no hover/focus apenas nos cards de jogos do profissional.
- Task 401 substituiu o conjunto de abas da seção `Conteúdos` da biblioteca pelas nove áreas definidas no chat e adicionou o objetivo da aba ativa logo abaixo das tabs.
- Task 402 restaurou `Todas` como primeira aba da biblioteca para exibir o acervo completo, mantendo as demais abas como recortes por categorias vinculadas.
- Task 403 alinhou o dropdown `Categoria` do modal da biblioteca às categorias novas da seção `Conteúdos`, removendo os labels antigos do select sem reabrir a API.
- Task 404 adicionou um botão `Salvar conteúdo` no header do modal de edição da biblioteca e passou a habilitá-lo somente após mudanças reais no formulário.
