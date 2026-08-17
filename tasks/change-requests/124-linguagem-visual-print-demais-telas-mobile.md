# Task 124 - Aplicar linguagem visual do print nas demais telas mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica (mudanca puramente visual; queries e services existentes)

## Modo de execucao

single-stack

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas

### Fonte primaria visual

- `design-system/mobile/prints/home-responsavel-referencia.png`

### Telas e estados que o print governa

- Linguagem transversal: cabecalho com eyebrow + titulo extrabold, cards brancos de cantos bem arredondados, pastilhas de icone em tints suaves (estilo lista "Popular"/"Recommend"), tags/pills de status pequenas, CTAs em pilula
- Lista de itens com thumbnail arredondado + titulo + subtitulo (aplicar em avisos e atividades da trilha)
- Card de perfil "Personal" (avatar + nome + dados) como base do perfil do responsavel

### Lacunas do print (estados nao cobertos)

- Estados de erro, vazio, carregando e "ja concluida": manter copies atuais dentro da nova linguagem
- Tela master: print nao cobre area administrativa; aplicar somente a linguagem (cabecalho, cards, pastilhas)
- Sem mascote/ilustracoes (marca de terceiros); usar icones Lucide e tints

## Restricao explicita do usuario

- Nao alterar a tab bar inferior (`ShellTabBar`) nem o mecanismo de troca de abas

## Objetivo

Estender a linguagem visual da home (Task 123) para as demais telas do app: Trilha do dia (lista), Atividade da trilha, Perfil do responsavel, Avisos e telas master (home e placeholder), com componentes compartilhados de cabecalho e pastilha de icone.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/124-linguagem-visual-print-demais-telas-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-123.md`

## Contexto sob demanda

- `design-system/mobile/prints/home-responsavel-referencia.png`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/CODE_STYLE.md` e `COMPONENT_REUSE.md`
- `mobile/src/features/shell/screens/` (Avisos, Perfil, Master)
- `mobile/src/features/trail/screens/` (TrailToday, TrailActivity)
- `mobile/src/shared/theme/tokens.ts` e `mobile/src/shared/components/`

## Orcamento de contexto

- ~13 fontes
- estrategia de reducao: mudanca restrita a estilo/composicao das telas alvo e componentes shared novos; sem tocar hooks, services, navigators (exceto nada), auth, home ja entregue e ShellTabBar

## Criterios de aceite

- Componente shared `ScreenHeader` (eyebrow + titulo extrabold + descricao opcional) usado nas telas alvo
- Componente shared `IconPill` (pastilha de icone com tint suave) agnostico de dominio
- Avisos: cards brancos arredondados com pastilha de icone (sino, azul), titulo bold, corpo, data e badge/dot de nao lido; vazio em card creme com pastilha
- Trilha do dia: cards de atividade com pastilha de icone por tipo de midia (audio/video), pills de status (pendente azul suave, concluida verde suave) e CTAs atuais
- Atividade: card de midia com pastilha, feedback de sucesso em card verde suave, estado "ja concluida" como pill
- Perfil: card principal estilo "Personal" do print (avatar-tile com inicial, nome, e-mail, parentesco) com pills de status de acesso/assinatura; criancas como itens de lista com pastilha
- Master home e placeholder: mesmo cabecalho e cards com pastilha
- `ShellTabBar` e navigators sem alteracao de comportamento
- Icones exclusivamente `lucide-react-native`; sem novas dependencias
- Estilos em `styles.ts` com `createStyles` e tokens; alvos de toque >= 44px; acessibilidade preservada

## Fora de escopo

- Tab bar inferior e navegacao
- Telas de auth e splash
- Home do responsavel (Tasks 122/123)
- Backend, contrato, comportamento das queries

## Dependencias

- Task 123 (linguagem visual da home)

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Novos componentes shared agnosticos de dominio: `ScreenHeader` (eyebrow suave + titulo extrabold + descricao opcional) e `IconPill` (pastilha de icone com 6 tints suaves)
- Avisos: cada notificacao virou card branco arredondado com pastilha de sino (laranja quando nao lida, azul quando lida), titulo, corpo, data e dot de nao lida; estado vazio em card creme com `BellOff`
- Perfil: card principal no estilo "Personal" do print (avatar-tile amarelo com inicial, nome, e-mail, parentesco) e status de acesso/assinatura como pills coloridas (verde suave positivo, amarelo suave pendente); criancas listadas com pastilha `Baby` rosa
- Trilha do dia: cards de atividade com pastilha de midia (`Headphones`/`Video` em laranja), status como pill arredondada (azul suave pendente, verde suave concluida), feedback de conclusao em card verde com `CheckCircle2`; estados vazios com pastilhas `UserX`/`CalendarX2`
- Atividade da trilha: cabecalho padrao, card de midia com pastilha, feedback verde com pastilha e estado "Ja concluida" como pill verde
- Master: home e placeholders com o mesmo cabecalho e cards com pastilha (`LayoutDashboard`, `Hourglass`); "Sair" no rodape
- Token novo `greenSoft` substituiu rgba hardcoded nos status da trilha
- `ShellTabBar` e navigators intocados

### Correcao pos-entrega (mesma task)

- Identificado que o `MasterShellNavigator` usa `AdminHomeScreen` e `AdminUsersScreen` (feature `admin`), nao o `MasterHomeScreen`; as abas "Inicio" e "Usuarios" do master haviam ficado sem o redesign
- `AdminHomeScreen`: cabecalho padrao, metricas com valor em extrabold, logs como cards brancos com pastilha `FileClock` azul, "Sair" no rodape
- `AdminUsersScreen`: cabecalho padrao, cards de usuario com pastilha `UserRound` (laranja ativo, coral inativo), status como pill arredondada, feedback verde com `CheckCircle2`, vazio com `UsersRound`
- `admin/screens/styles.ts` migrado para tokens (`greenSoft`, `coralSoft`) e pills arredondadas

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, `tasks/slices/022-linguagem-visual-print-telas-mobile.md` e handoff `TASK-123`
- Contexto sob demanda carregado: print de referencia, tokens, `CODE_STYLE.md`/`COMPONENT_REUSE.md`, telas alvo em `features/shell/screens/` e `features/trail/screens/`
- Fontes evitadas: `requirements/`, `contracts/openapi.yaml`, stacks web/backend, auth/splash, hooks e services (sem mudanca de comportamento)

## Handoff

- `.agents/state/handoffs/TASK-124.md`
- Decisoes preservadas: `ScreenHeader` e `IconPill` sao os blocos padrao da linguagem interna; tints suaves nos tokens; sem mascote de terceiros
- Proximo contexto recomendado: `mobile/src/shared/components/` para qualquer nova tela seguir o mesmo padrao

## Arquivos alterados

- `mobile/src/shared/theme/tokens.ts` (`greenSoft`)
- `mobile/src/shared/components/ScreenHeader/{index.tsx,styles.ts}` (novos)
- `mobile/src/shared/components/IconPill/{index.tsx,styles.ts}` (novos)
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/MasterHomeScreen.tsx`
- `mobile/src/features/shell/screens/MasterPlaceholderScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts` (avatar-tile, cardRow/cardBody, pills de status)
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts` (cardRow/cardBody, pills arredondadas com tokens)
- `mobile/src/features/admin/screens/AdminHomeScreen.tsx` (correcao pos-entrega)
- `mobile/src/features/admin/screens/AdminUsersScreen.tsx` (correcao pos-entrega)
- `mobile/src/features/admin/screens/styles.ts` (correcao pos-entrega)
- `tasks/change-requests/124-linguagem-visual-print-demais-telas-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-124.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (9 suites, 19 testes)

## Aderencia ao print e desvios registrados

- Linguagem aplicada: cabecalho eyebrow+titulo extrabold, cards brancos arredondados, pastilhas de icone em tints, pills de status, itens de lista com thumbnail+titulo+subtitulo
- Desvio 1: paleta segue os tokens Evolente, nao as cores exatas do print (DS documental governa)
- Desvio 2: sem ilustracoes/mascote (marca de terceiros); icones Lucide
- Desvio 3: area master nao existe no print; recebeu apenas a linguagem transversal
- Acessibilidade: pastilhas decorativas ocultas de leitores de tela; labels/hints e live regions preservados; alvos >= 44px

## Pendencias pos-task

- Validar visual em dispositivo fisico/Expo Go
- Fonte Nunito segue como pendencia de dependencia

## Status final

done
