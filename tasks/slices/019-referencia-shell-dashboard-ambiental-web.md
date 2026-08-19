# Slice 019 - Reproducao de shell dashboard por referencia externa

## Status

done

## Objetivo de negocio

Elevar a fidelidade visual da home autenticada web com base em uma nova referencia aprovada pelo usuario, reforcando impacto visual e hierarquia do shell.

## Entrega verificavel

- shell autenticado adota moldura externa escura com sidebar integrada
- painel principal branco interno reproduz a percepcao de conteudo encaixado dentro do shell
- dashboard inicial segue a composicao da referencia com metricas, paineis e CTA

## Fora de escopo

- novos endpoints, dados clinicos ficticios, mobile ou mudancas nas telas de auth

## Tasks relacionadas

- Task 041 - reproduzir shell e dashboard por nova referencia
- `tasks/change-requests/053-refinar-dashboard-profissional-web.md` - refino visual incremental do dashboard profissional
- `tasks/change-requests/055-refinar-home-dashboard-profissional-operacional.md` - recorte operacional do conteudo da home do profissional
- `tasks/change-requests/056-dashboard-profissional-dados-reais.md` - integracao da home profissional com dados reais
- `tasks/change-requests/057-refinar-alinhamento-card-prioridades-dashboard.md` - ajuste visual do card de prioridades
- `tasks/change-requests/058-dashboard-duas-colunas-apos-metricas.md` - ajuste da grade dos cards abaixo das metricas
- `tasks/change-requests/059-centralizar-icone-alerta-card-prioridades.md` - correcao de alinhamento do icone no destaque de prioridades
- `tasks/change-requests/060-centralizar-svg-do-sino-no-badge.md` - correcao residual do SVG do sino no badge de prioridades
- `tasks/change-requests/061-alinhar-atalhos-card-prioridades-dashboard.md` - ajuste de composicao dos atalhos do card de prioridades
- `tasks/change-requests/062-reposicionar-card-cadencia-dashboard.md` - reposicionamento pontual do card de cadencia na grade principal
- `tasks/change-requests/063-equalizar-largura-cta-cadencia-dashboard.md` - equalizacao do CTA do card de cadencia com os demais botoes do dashboard
- `tasks/change-requests/064-reduzir-altura-cta-cadencia-dashboard.md` - reducao pontual da altura do CTA do card de cadencia
- `tasks/change-requests/065-adicionar-icone-cta-planejamentos-dashboard.md` - adicao de icone ao CTA de planejamentos no card de prioridades
- `tasks/change-requests/070-textura-animada-suave-sidebar-web.md` - adicao de textura animada suave ao fundo do sidebar autenticado
- `tasks/change-requests/075-reduzir-pressao-no-dashboard-e-higienizar-sidebar.md` - limitacao de concorrencia no summary e limpeza segura do sidebar persistente
- `tasks/change-requests/090-sincronizar-dropdowns-sidebar-web.md` - exclusao mutua entre Configuracoes e o menu do usuario no sidebar
- `tasks/change-requests/346-reposicionar-cta-do-dashboard-profissional-abaixo-do-header.md` - reposicionamento do CTA do header do dashboard profissional
- `tasks/change-requests/439-redesenhar-dashboard-profissional-web.md` - redesenho do conteudo do dashboard profissional (graficos, atividades de hoje, carrossel e relatorios)
- `tasks/change-requests/440-melhorar-metricas-cards-dashboard-profissional.md` - troca das metricas dos 4 cards superiores por indicadores operacionais
- `tasks/change-requests/441-reorganizar-grade-atividades-relatorios-carrossel-dashboard.md` - grade inferior: atividades+relatorios / carrossel
- `tasks/change-requests/554-grafico-evolucao-diaria-dashboard-profissional.md` - grafico diario agregado da carteira — **done**

## Contexto mínimo

- fontes globais, Task 041, handoff 040 e este slice

## Contexto sob demanda

- imagem enviada pelo usuario no chat
- shell e dashboard inicial do `front-end`

## Risco de contexto

- medio; escopo restrito a uma tela e ao layout compartilhado autenticado

## Resultado

- composicao do shell/dashboard inicial aproximada da nova referencia, preservando o dominio do produto
- Task 053 enxugou o dashboard profissional e reforcou o foco em informacoes operacionais realmente uteis.
- Task 055 aprofunda esse recorte ao manter apenas os paineis que apoiam o uso diario do profissional.
- Task 056 substitui os mocks restantes por dados reais das APIs ja existentes, sem inventar indicadores sem fonte.
- Task 061 alinha os dois atalhos principais do card de prioridades em colunas equivalentes, mantendo responsividade.
- Task 062 move o card de cadencia recente para a grade principal, eliminando o vazio visual ao lado do acompanhamento clinico.
- Task 063 ajusta o CTA do card de cadencia para ocupar largura equivalente aos demais botoes principais.
- Task 064 reduz a altura do CTA do card de cadencia para manter a proporcao visual apos a largura total.
- Task 065 adiciona um ícone ao CTA de planejamentos para reforcar consistencia com os demais atalhos do dashboard.
- Task 070 adiciona uma textura animada bem suave ao sidebar para enriquecer o shell sem disputar atenção com a navegação.
- Task 075 reduziu a pressao de requisições no dashboard e melhorou o isolamento do sidebar persistente em testes.
- Task 090 sincroniza o estado dos menus do sidebar para impedir que Configuracoes e o menu do usuario fiquem abertos ao mesmo tempo.
- Task 346 move o CTA principal do dashboard profissional para uma segunda linha abaixo do heading, preservando busca e notificacoes no topo.
- Task 439 substitui o conteudo operacional por metricas limpas, grafico de evolucao, pizza por area, atividades de hoje, carrossel de progresso e relatorios semanais.
- Task 440 troca os 4 cards superiores por indicadores operacionais (atividades de hoje, engajamento e relatorios pendentes).
- Task 554 adiciona o grafico diario da carteira (planejado vs concluido vs adesao nos ultimos 7 dias), reusando trails/progress ja carregados.
