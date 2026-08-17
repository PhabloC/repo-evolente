# Task 123 - Aproximar a home do responsavel do print de referencia

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

- nao se aplica (reuso das queries existentes de perfil e notificacoes; sem endpoint novo)

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas

### Fonte primaria visual

- `design-system/mobile/prints/home-responsavel-referencia.png`

### Telas e estados que o print governa

- Composicao geral da home: cabecalho com saudacao e avatar em tile arredondado; banner hero laranja com titulo e CTA em pilula; fileira de atalhos em tiles pastel com icone e rotulo; secao de cards de recomendacao/aviso em fundo creme
- Linguagem visual: fundo quente claro, cards com cantos bem arredondados, pastilhas de icone em tints suaves, CTAs em pilula, titulos bold

### Lacunas do print (estados nao cobertos)

- Estado de carregamento: manter indicador integrado ao layout atual
- Card "Acesso limitado": nao existe no print; manter como card de aviso no tom coral suave seguindo a mesma linguagem de card
- Estado sem crianca vinculada / zero avisos: cobrir com as mesmas copies atuais dentro do novo layout
- Mascote/ilustracoes do print (girafa) pertencem a outra marca: nao copiar assets; usar formas decorativas simples (circulos) e icones Lucide

## Restricao explicita do usuario

- Nao alterar a tab bar inferior (`ShellTabBar`) nem o mecanismo de troca de abas do `ResponsavelShellNavigator`

## Objetivo

Recompor a home do responsavel para ficar bem proxima ao print de referencia: saudacao com avatar-tile, banner hero laranja da trilha do dia com CTA em pilula, atalhos pastel (Trilha, Avisos com badge, Perfil) e secao de avisos em card, preservando tokens e o tom calmo da area do responsavel.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/123-home-responsavel-fiel-ao-print-referencia.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-122.md`

## Contexto sob demanda

- `design-system/mobile/prints/home-responsavel-referencia.png`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/components/`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx` (somente para passar novo callback de aba)
- `mobile/src/shared/theme/tokens.ts`

## Orcamento de contexto

- ~12 fontes
- estrategia de reducao: alterar apenas a home do responsavel e componentes locais da feature shell; navigator so ganha repasse de callback; nao tocar ShellTabBar, Trilha, Perfil, Avisos, auth nem backend

## Criterios de aceite

- Cabecalho: saudacao bold a esquerda e avatar em tile arredondado (rounded square) a direita, como no print
- Banner hero laranja (Trilha do dia) com titulo em branco, formas decorativas suaves e CTA em pilula clara "Ver trilha"
- Fileira de 3 atalhos em tiles pastel com icone e rotulo: Trilha (laranja), Avisos (azul, com badge de nao lidos), Perfil (rosa); troca de aba via callbacks do navigator
- Secao "Avisos" com cabecalho de secao (titulo + acao "Ver todos") e card no estilo do print (pastilha de icone + texto), pressable para a aba Avisos
- Card "Acesso limitado" mantido, seguindo a mesma linguagem visual (coral suave)
- Botao "Sair" discreto no rodape mantido
- `ShellTabBar` sem nenhuma alteracao
- Icones exclusivamente via `lucide-react-native`; sem novas dependencias; sem copiar assets ilustrados do print
- Estilos em `styles.ts` locais com `createStyles` e tokens; alvos de toque >= 44px; labels/roles de acessibilidade preservados

## Fora de escopo

- Tab bar inferior e navegacao entre abas
- Telas Trilha, Perfil e Avisos
- Backend e contrato OpenAPI
- Home do master
- Pacote de fonte Nunito

## Dependencias

- Task 122 (redesign anterior da home do responsavel)
- Task 095 (Lucide como padrao de icones mobile)

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Cabecalho refeito no padrao do print: saudacao em extrabold a esquerda ("Bem-vindo de volta" + "Ola, {nome}") e avatar em tile arredondado amarelo suave a direita; o sino saiu do header e virou atalho
- Novo `HomeHeroBanner`: banner laranja com cantos bem arredondados, formas decorativas (circulo amarelo translucido e circulo branco), eyebrow "Trilha do dia", titulo branco extrabold com o nome da crianca e CTA em pilula branca "Ver trilha"
- Novo `HomeShortcutTile`: fileira de 3 atalhos pastel no estilo Story/Video/Music do print — Trilha (laranja), Avisos (azul, com badge de nao lidos) e Perfil (rosa), cada um com pastilha branca de icone e rotulo
- Secao "Avisos" com cabecalho de secao (titulo + "Ver todos") e card pressable reutilizando `HomeActionCard`
- Card "Acesso limitado" mantido em coral suave, mesma linguagem de card
- `ResponsavelShellNavigator` apenas repassa `onOpenProfile` para a home; `ShellTabBar` intocado
- Sem novas dependencias e sem copiar assets ilustrados do print (mascote de outra marca)

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md` e handoff `TASK-122`
- Contexto sob demanda carregado: `design-system/mobile/prints/home-responsavel-referencia.png` (fonte primaria), tokens do tema, componentes da home criados na Task 122, navigator do responsavel
- Fontes evitadas: `requirements/`, `contracts/openapi.yaml`, stacks web/backend, telas Trilha/Perfil/Avisos, `ShellTabBar`

## Handoff

- `.agents/state/handoffs/TASK-123.md`
- Decisoes preservadas: print governa composicao e linguagem, cores vem dos tokens Evolente (nao do amarelo exato do print); sino removido do header em favor do atalho pastel; `onOpenProfile` novo callback do navigator
- Proximo contexto recomendado: `mobile/src/features/shell/components/` para novos refinos da home

## Arquivos alterados

- `design-system/mobile/prints/home-responsavel-referencia.png` (novo, referencia visual)
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx` (novo)
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts` (novo)
- `mobile/src/features/shell/components/HomeShortcutTile/index.tsx` (novo)
- `mobile/src/features/shell/components/HomeShortcutTile/styles.ts` (novo)
- `mobile/src/features/shell/components/HomeHeader/index.tsx` (restilizado: avatar-tile, sem sino)
- `mobile/src/features/shell/components/HomeHeader/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts` (`sectionHeader`, `sectionTitle`, `shortcutRow`)
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx` (repasse de `onOpenProfile`)
- `tasks/change-requests/123-home-responsavel-fiel-ao-print-referencia.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-123.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok (apos trocar `StyleSheet.absoluteFillObject` por posicionamento absoluto explicito)
- `npm run test` - ok (9 suites, 19 testes)

## Aderencia ao print e desvios registrados

- Composicao seguida: header saudacao+avatar-tile, banner hero com CTA em pilula, atalhos pastel com icone, secao de cards com cabecalho "Ver todos"
- Desvio 1: paleta usa os tokens Evolente (laranja `#FF8A00`, bege `#F3E4C2`) em vez do amarelo/pessego exatos do print — o DS documental governa cores
- Desvio 2: sem mascote/ilustracoes (girafa e de outra marca); formas decorativas simples no banner
- Desvio 3: conteudos do print (musica/cursos) mapeados para o dominio Evolente (trilha, avisos, perfil)
- Lacunas de estado cobertas com a linguagem atual: loading integrado, acesso limitado em coral suave, zero avisos com copy existente

## Pendencias pos-task

- Validar visual em dispositivo fisico/Expo Go
- Avaliar fonte Nunito (dependencia ainda nao autorizada) para aproximar a tipografia bold do print

## Status final

done
