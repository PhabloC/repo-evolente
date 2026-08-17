# Slice 010 - App do responsavel: home, perfil e notificacoes

## Status

done

## Objetivo de negocio

Completar mobile do responsavel com home, perfil e base de notificacoes (provedor a definir).

## Entrega verificavel

Home/conta, perfil e notificacoes in-app de trilha.

## Fora de escopo

- Gamificacao
- Area administrativa
- Login da crianca

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- mobile
- backend

## Contrato

- `contracts/openapi.yaml#/paths` de profile/notifications

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `nao se aplica`

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md` (area do responsavel)

## Permissoes e atores

- Responsavel com assinatura

## Casos de erro e borda

- Perfil incompleto
- Push indisponivel
- Sessao expirada

## Decisoes humanas confirmadas

- Stack web: React/Vite; Mobile: sim; Profissional multi-especialidade; Inativar (nao excluir); Gamificacao/jogos fora do escopo

## Premissas adotadas

- Gateway, valores e push a definir — abstrair
- DS documental governa tokens; sem prints nesta fase
- Conflito DS mobile (gamificacao/UI crianca) vs requisitos — prevalece requisito

## Tasks relacionadas

- `tasks/024-app-responsavel-home-perfil-notificacoes.md` - Home/perfil/notificacoes — **done**
- `tasks/change-requests/122-melhorar-design-home-responsavel-mobile.md` - Melhorar design da home do responsavel — **done**
- `tasks/change-requests/123-home-responsavel-fiel-ao-print-referencia.md` - Home do responsavel fiel ao print de referencia — **done**
- `tasks/change-requests/260-limpar-avisos-na-tela-mobile.md` - Limpar avisos visíveis na central mobile — **done**
- `tasks/change-requests/261-persistir-limpeza-de-avisos-mobile.md` - Persistir avisos limpos no storage local — **done**
- `tasks/change-requests/262-usar-assets-bell-e-check-nos-avisos-mobile.md` - Trocar sino e check da lista de avisos por assets locais — **done**
- `tasks/change-requests/264-usar-bell-off-no-estado-de-avisos-limpos-mobile.md` - Usar bell-off no estado de avisos limpos — **done**
- `tasks/change-requests/265-corrigir-path-dos-assets-de-avisos-mobile.md` - Corrigir resolução dos assets locais na tela de avisos — **done**
- `tasks/change-requests/268-usar-bell-na-home-com-asset-local-mobile.md` - Aplicar bell.webp no sino da home — **done**
- `tasks/change-requests/273-refinar-card-de-avisos-da-home-mobile-com-bg-e-status.md` - Refinar card de avisos da home com shadow, bg e status — **done**
- `tasks/change-requests/274-refinar-tipografia-e-profundidade-do-card-de-avisos-home-mobile.md` - Refinar tipografia e profundidade do card de avisos da home — **done**
- `tasks/change-requests/275-corrigir-renderizacao-do-bg-trilha-no-card-de-avisos-home-mobile.md` - Corrigir renderização do bg trilha no card de avisos da home — **done**
- `tasks/change-requests/276-corrigir-bg-e-sombra-do-card-de-avisos-home-mobile.md` - Corrigir bg e sombra do card de avisos da home — **done**
- `tasks/change-requests/277-forcar-trilha-webp-100-porcento-no-bg-do-card-de-avisos-home-mobile.md` - Forçar trilha.webp 100% no bg do card de avisos da home — **done**
- `tasks/change-requests/278-profundidade-e-bg-trilha-card-avisos-home-mobile.md` - Profundidade e bg trilha no card de avisos da home — **done**
- `tasks/change-requests/279-reduzir-tamanho-bg-trilha-card-avisos-home-mobile.md` - Reduzir tamanho do bg trilha no card de avisos da home — **done**
- `tasks/change-requests/280-corrigir-sombra-quadrada-e-bg-trilha-card-avisos-home-mobile.md` - Corrigir sombra quadrada e bg trilha no card de avisos da home — **done**
- `tasks/change-requests/281-remover-bg-trilha-e-mover-sombra-para-card-avisos-home-mobile.md` - Remover bg trilha e mover sombra para o card de avisos da home — **done**
- `tasks/change-requests/282-alinhar-cards-pagina-avisos-ao-estilo-home-mobile.md` - Alinhar cards da página de avisos ao estilo do card da home — **done**
- `tasks/change-requests/283-icones-status-em-dia-e-limpos-pagina-avisos-mobile.md` - Ícones nos status Em dia e Limpos da página de avisos — **done**
- `tasks/change-requests/359-alinhar-sino-de-ultimos-avisos-ao-resumo-rapido-mobile.md` - Alinhar sino de Últimos avisos ao Resumo rápido — **done**
- `tasks/change-requests/360-deixar-branco-o-bg-do-sino-em-ultimos-avisos-mobile.md` - Deixar branco o bg do sino em Últimos avisos — **done**
- `tasks/change-requests/284-alinhar-cards-pagina-perfil-ao-estilo-home-mobile.md` - Alinhar cards da página de perfil ao estilo do card da home — **done**
- `tasks/change-requests/285-refinar-metadados-card-responsavel-perfil-mobile.md` - Refinar metadados do card de responsável no perfil — **done**
- `tasks/change-requests/286-refinar-card-crianca-perfil-mobile.md` - Refinar card da criança no perfil — **done**
- `tasks/change-requests/287-foto-perfil-cards-responsavel-crianca-perfil-mobile.md` - Foto de perfil nos cards de responsável e criança — **done**
- `tasks/change-requests/288-fundo-bolhas-telas-edicao-perfil-mobile.md` - Fundo de bolhas nas telas de edição de perfil — **done**
- `tasks/change-requests/289-sombra-cards-e-icone-salvar-edicao-perfil-mobile.md` - Sombra nos cards e ícone no salvar das edições de perfil — **done**
- `tasks/change-requests/290-revelar-bolhas-stack-edicao-perfil-mobile.md` - Revelar bolhas no stack das telas de edição de perfil — **done**
- `tasks/change-requests/291-icone-telefone-input-edicao-responsavel-mobile.md` - Ícone de telefone no input da edição do responsável — **done**
- `tasks/change-requests/292-melhorar-design-intro-edicoes-perfil-mobile.md` - Melhorar design da seção intro das edições de perfil — **done**
- `tasks/change-requests/357-adicionar-card-de-relatorios-no-perfil-mobile.md` - Card de relatórios compartilhados no perfil do responsável — **done**
- `tasks/change-requests/369-abrir-lista-e-download-de-relatorios-a-partir-do-perfil-mobile.md` - Abrir tela e download dos relatórios a partir do perfil do responsável — **done**
- `tasks/change-requests/370-exibir-tab-bar-do-responsavel-nas-edicoes-de-perfil-e-relatorios-mobile.md` - Exibir tab bar do responsável nas edições de perfil e relatórios — **done**
- `tasks/change-requests/388-consumir-parametro-de-aba-inicial-no-shell-do-responsavel-mobile.md` - Consumir e limpar `initialTab` no shell do responsável — **done**

## Dependencias do slice

- Slices 005 e 008

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

- Push TBD: in-app + `NoopPushNotificationAdapter` entregues na Task 024.
- Entrega: `GET/PATCH /notifications`, `GET /guardians/me`, telas Home/Perfil/Avisos.
- Task 122: redesign da home do responsavel (HomeHeader + HomeActionCard, tints suaves nos tokens), sem mudanca de API.
- Task 123: home fiel ao print `design-system/mobile/prints/home-responsavel-referencia.png` (HomeHeroBanner + HomeShortcutTile); ShellTabBar preservado.
- Task 253: edição do responsável preserva estado local ao trocar avatar e aceita limpeza explícita do telefone com `null`.
- Task 208: header da home com "Olá", avatar à esquerda, lupa e sino à direita.
- Task 209: lupa abre busca local de atividades da trilha e avisos.
- Task 210: ícone log-out no topo direito do perfil; botão Sair removido do rodapé.
- Task 211: header do perfil com voltar à esquerda, título central e sem eyebrow/description.
- Task 213: home com ícone usuário no topo e campo de busca em largura total abaixo.
- Task 214: removidos cards de atalho Trilha/Avisos/Perfil da home.
- Task 215: busca inline na home (teclado nativo, sem modal).
- Task 219: cabeçalho de Atividades e Avisos igual ao Perfil (sem logout).
- Task 260: central de avisos ganhou ação local "Limpar avisos" no cabeçalho da lista, sem endpoint novo.
- Task 261: ids dispensados passaram a persistir no storage local para não reaparecerem após remontar a tela.
- Task 262: cards de avisos passaram a usar `bell.webp` e `check.webp` na pastilha visual dos estados não lido/lido.
- Task 264: o estado “Avisos limpos da tela” passou a usar `bell-off.webp`, preservando o estado vazio padrão.
- Task 265: corrigidos os `require(...)` dos assets locais de avisos para subir até `mobile/assets`.
- Task 268: o quadro "Avisos da trilha" da home passou a usar `bell.webp`, e o header voltou ao sino vetorial anterior.
- Task 273: o card "Avisos da trilha" ganhou shadow, fundo `trilha.webp`, status com ícone de carta, sem barra lateral e com pastilha principal circular.
- Task 274: o texto descritivo do card "Avisos da trilha" foi reduzido e a sombra reforçada para dar mais profundidade.
- Task 275: o `trilha.webp` passou a usar uma camada absoluta dedicada, maior e com `resizeMode="contain"` para aparecer de forma consistente no card.
- Task 276: a sombra foi movida para um container externo sem clipping e o `trilha.webp` ficou maior, mais opaco e com `resizeMode="cover"` para aparecer melhor.
- Task 277: o `trilha.webp` passou a preencher 100% do card com opacidade total e `resizeMode="stretch"` para garantir presença visual integral.
- Task 278: sombra do card de avisos reequilibrada para profundidade real (incluindo elevation no Android) e `trilha.webp` como background com `cover` + scrim leve para legibilidade.
- Task 279: o `trilha.webp` passou a um carimbo 112x112 com `contain` à esquerda, sem preencher/esticar o card.
- Task 280: sombra movida para `View` host (fora do `Pressable`) com elevation mais baixa; carimbo da trilha 168x168 com opacidade 0.7.
- Task 281: removido o background `trilha.webp` e a sombra passou a ficar no próprio card (sem wrapper pai).
- Task 282: cards de resumo rápido e estado vazio da página de avisos passaram a usar `HomeActionCard` no estilo da home.
- Task 283: status "Em dia" e "Limpos" ganharam ícone `CheckCircle2` ao lado do texto.
- Task 359: o sino do item não lido em "Últimos avisos" passou a usar a mesma pastilha circular e o mesmo `bell.webp` do card "Resumo rápido".
- Task 360: a pastilha do sino em "Últimos avisos" passou a usar fundo branco, preservando o `bell.webp`.
- Task 284: cards de responsável e criança na página de perfil passaram a usar `HomeActionCard` no estilo da home.
- Task 285: card do responsável ganhou ícones em e-mail/parentesco e pastilha de assinatura com bolinha verde.
- Task 286: removido o cabeçalho agregado "Criança"; cada criança é um card com calendário no nascimento e código em linha própria.
- Task 287: cards de responsável e criança passam a exibir foto de perfil, com fallback provisório (inicial / avatar por sexo).
- Task 288: telas de edição de responsável e criança passam a revelar o fundo de bolhas global (Screen transparente).
- Task 289: cards das edições ganharam box-shadow; botão Salvar alterações ganhou ícone `Save`.
- Task 290: removido o `contentStyle` bege das rotas de edição no stack — bolhas globais passam a aparecer.
- Task 291: input de telefone na edição do responsável ganhou ícone `Phone` à esquerda.
- Task 292: intro das edições virou card com pastilha de ícone, tipografia reforçada e sombra.
- Task 357: perfil do responsável ganhou card de relatórios compartilhados pelo profissional, consumindo `GET /reports` e resumindo quantidade + último envio sem abrir viewer/download no app.
- Task 358: a central de avisos do responsável passou a receber também notificações `report_shared` quando o profissional disponibiliza um relatório pela primeira vez.
- Task 369: o card de relatórios do perfil passou a abrir uma tela dedicada com a lista de arquivos compartilhados e botão de download por item.
- Task 370: as telas de editar responsável, editar criança e relatórios passaram a exibir a mesma tab bar do responsável fora do shell principal.
- Task 388: o shell do responsável passou a aplicar e limpar `initialTab`, devolvendo o controle da aba visível ao estado local e restaurando o efeito do `Voltar` em trilha, perfil e avisos.

## Status final

done
