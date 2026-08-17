# Slice 022 - Linguagem visual do print aplicada as telas mobile

## Status

done

## Objetivo de negocio

Estender a linguagem visual consolidada na home do responsavel (Task 123, print de referencia) para as demais telas internas do app mobile, criando uma experiencia coesa e acolhedora em todo o produto.

## Entrega verificavel

Telas de Trilha (lista e atividade), Perfil, Avisos e area master com a mesma linguagem: cabecalho com eyebrow + titulo extrabold, cards brancos de cantos bem arredondados com pastilhas de icone em tints suaves, pills de status e CTAs em pilula.

## Fora de escopo

- Tab bar inferior (`ShellTabBar`) e mecanismo de navegacao
- Telas de auth (login/recuperacao seguem o print proprio do Slice 002)
- Home do responsavel (ja entregue nas Tasks 122/123)
- Mudancas de comportamento, API ou contrato
- Gamificacao

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- mobile

## Contrato

- nao se aplica

## Referencia visual por stack

### Mobile

- tipo: prints de telas
- fonte primaria: `design-system/mobile/prints/home-responsavel-referencia.png`
- apoio documental: `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Tasks relacionadas

- `tasks/change-requests/124-linguagem-visual-print-demais-telas-mobile.md` - Aplicar linguagem visual do print nas demais telas — **done**
- `tasks/change-requests/128-refinar-telas-responsavel-mobile-com-home.md` - Refinar atividades, perfil e avisos com composicao mais proxima da home — **done**
- `tasks/change-requests/129-aplicar-fundo-estrelinha-hero-home-responsavel-mobile.md` - Aplicar `fundo_estrelinha.svg` no hero da home do responsavel — **done**
- `tasks/change-requests/131-remover-folga-do-svg-no-hero-home-mobile.md` - Remover folga do SVG no hero da home — **done**
- `tasks/change-requests/132-aplicar-fundos-svg-nas-telas-responsavel-mobile.md` - Aplicar fundos SVG dedicados em atividades, perfil e avisos — **done**
- `tasks/change-requests/133-expandir-fundos-svg-para-preenchimento-total-mobile.md` - Expandir fundos SVG para preenchimento total nos heroes mobile — **done**
- `tasks/change-requests/134-remover-inset-do-card-hero-svg-mobile.md` - Remover inset residual do card hero com SVG — **done**
- `tasks/change-requests/135-restaurar-balao-e-ajustar-home-e-copy-trilha-mobile.md` - Restaurar balão, corrigir home e ajustar copy da trilha — **done**
- `tasks/change-requests/136-quebrar-copy-do-hero-perfil-mobile.md` - Quebrar copy do hero de perfil — **done**
- `tasks/change-requests/137-quebrar-copy-do-hero-avisos-mobile.md` - Quebrar copy do hero de avisos — **done**
- `tasks/change-requests/138-cachear-svgs-dos-heroes-mobile.md` - Cachear os SVGs dos heroes mobile — **done**
- `tasks/change-requests/139-aplicar-selo-com-icone-nos-heroes-mobile.md` - Aplicar selo com icone nos heroes mobile — **done**
- `tasks/change-requests/140-deixar-eyebrows-dos-headers-em-laranja-mobile.md` - Deixar em laranja os eyebrows dos headers das paginas mobile — **done**
- `tasks/change-requests/141-aumentar-titulo-dos-headers-das-paginas-mobile.md` - Aumentar o tamanho dos titulos dos headers das paginas mobile — **done**
- `tasks/change-requests/142-corrigir-cache-dos-svgs-dos-heroes-no-android-mobile.md` - Corrigir leitura em cache dos SVGs dos heroes no Android mobile — **done**
- `tasks/change-requests/143-usar-cover-nos-svgs-de-background-dos-heroes-mobile.md` - Usar cover nos SVGs de background dos heroes mobile — **done**
- `tasks/change-requests/144-refinar-card-principal-do-perfil-mobile-por-print.md` - Refinar card principal do perfil mobile por print — **done**
- `tasks/change-requests/145-corrigir-overflow-da-pill-de-assinatura-no-perfil-mobile.md` - Corrigir overflow da pill de assinatura no perfil mobile — **done**
- `tasks/change-requests/146-adicionar-icones-nos-botoes-do-auth-mobile.md` - Adicionar icones nos botoes do auth mobile — **done**
- `tasks/change-requests/147-tentar-ocultar-barra-de-navegacao-nativa-no-android-mobile.md` - Tentar ocultar a barra de navegacao nativa no Android mobile — **done**
- `tasks/change-requests/148-remover-folga-inferior-da-tabbar-apos-ocultar-nav-bar-mobile.md` - Remover folga inferior da tabbar apos ocultar nav bar mobile — **done**
- `tasks/change-requests/149-eliminar-faixa-branca-nav-bar-android-abaixo-da-tabbar-mobile.md` - Eliminar faixa branca da nav bar Android abaixo da tabbar mobile — **done**
- `tasks/change-requests/384-restaurar-botoes-nativos-da-nav-bar-android-mobile.md` - Restaurar botões nativos da nav bar Android — **done**
- `tasks/change-requests/267-remover-borda-das-imagens-na-icon-pill-mobile.md` - Remover borda das imagens renderizadas pela IconPill — **done**
- `tasks/change-requests/269-remover-canto-arredondado-das-imagens-da-icon-pill-mobile.md` - Remover canto arredondado das imagens renderizadas pela IconPill — **done**
- `tasks/change-requests/270-aumentar-radius-dos-heroes-mobile-com-bg-ilustrado.md` - Aumentar arredondamento dos heroes ilustrados — **done**
- `tasks/change-requests/271-aumentar-ainda-mais-o-radius-dos-heroes-mobile.md` - Aumentar ainda mais o arredondamento dos heroes ilustrados — **done**
- `tasks/change-requests/272-alinhar-ctas-dos-heroes-home-e-trilha-mobile.md` - Alinhar CTAs dos heroes da home e trilha — **done**

## Observacoes de rastreabilidade

- Task 267 removeu o contorno residual das imagens renderizadas pela `IconPill`, preservando o fallback vetorial e a linguagem visual consolidada das telas mobile.
- Task 269 removeu também o canto arredondado residual das imagens renderizadas pela `IconPill`.
- Task 270 aumentou o radius dos heroes ilustrados da home, shell e trilha sem alterar os demais cards.
- Task 271 elevou esse radius dos heroes ilustrados para `32`, mantendo os demais cards inalterados.
- Task 272 alinhou o CTA do hero da trilha ao padrão da home e adicionou seta à direita nos dois heroes.
- Task 384 reverte a ocultação global da nav bar nativa no Android para voltar a exibir os botões do sistema.

## Dependencias do slice

- Slice 010 (home do responsavel) e Task 123

## Contexto minimo recomendado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, este slice, task atual

## Contexto sob demanda recomendado

- print de referencia e DS mobile documental (UI)
- `mobile/docs/ai/CODE_STYLE.md` e `COMPONENT_REUSE.md`
- telas alvo em `mobile/src/features/{shell,trail}/screens/`

## Risco de contexto

- medio; estrategia: reusar componentes/tokens das Tasks 122/123 e limitar a mudanca a estilo/composicao das telas alvo

## Status final

done
