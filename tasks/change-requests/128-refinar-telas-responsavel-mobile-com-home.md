# Task 128 - Refinar atividades, perfil e avisos do responsavel com a linguagem da home

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

- nao se aplica (mudanca puramente visual e reposicionamento de acao existente)

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

- Hero laranja com CTA em pilula, composicao com blocos maiores e hierarquia mais proxima da home entregue
- Pastilhas/atalhos com icone e cards em tons suaves como apoio visual para listas e secoes
- Card principal de perfil com linguagem acolhedora da home, mantendo dados reais e estados existentes

### Lacunas do print (estados nao cobertos)

- Erro, loading, vazio e sucesso continuam com a linguagem atual do app
- O print nao cobre botao de sair no perfil; mover a acao da home para o perfil sem alterar o fluxo de logout

## Restricao explicita do usuario

- Deixar as paginas de atividades, perfil e avisos mais parecidas com a home do app
- Remover o botao de sair da home e colocá-lo dentro da tela de perfil

## Objetivo

Reforcar nas telas de atividades, perfil e avisos a mesma composicao visual da home do responsavel, com blocos mais proximos do hero/atalhos/cards da home, e reposicionar a acao de sair para dentro do perfil.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/128-refinar-telas-responsavel-mobile-com-home.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-124.md`

## Contexto sob demanda

- `design-system/mobile/prints/home-responsavel-referencia.png`
- `mobile/docs/ai/CODE_STYLE.md` e `COMPONENT_REUSE.md`
- `mobile/src/features/shell/components/` (HomeHeroBanner, HomeActionCard, HomeShortcutTile, HomeHeader)
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`

## Orcamento de contexto

- ~12 fontes
- estrategia de reducao: limitar a mudanca a composicao visual e reposicionamento do logout; sem tocar queries, services, navigators, tab bar ou contrato

## Criterios de aceite

- Home do responsavel deixa de exibir o botao `Sair`
- Perfil passa a concentrar a acao `Sair` em bloco consistente com a linguagem da home
- Avisos recebe composicao mais proxima da home, com destaque inicial e lista de cards/atalhos sem alterar a leitura e o marcar como lido
- Atividades (lista e detalhe) recebem composicao mais proxima da home, incluindo destaque inicial, agrupamentos mais claros e CTAs em pilula
- Mantem `lucide-react-native`, tokens atuais e comportamento funcional das telas
- Sem alteracao na `ShellTabBar` nem na navegacao

## Fora de escopo

- Home do responsavel alem da remocao do botao `Sair`
- Auth, splash, tab bar e navegacao
- Mudancas de API, contrato, hooks, services ou regras de negocio

## Dependencias

- Task 123 (home do responsavel fiel ao print)
- Task 124 (linguagem visual do print nas demais telas mobile)

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Home do responsavel deixou de exibir o botao `Sair`, preservando a hero, os atalhos e os cards do dia
- Perfil ganhou um bloco hero laranja alinhado a home, resumo de conta com cards de apoio e um card dedicado para `Sair`
- Avisos ganhou hero de resumo, bloco de apoio com contagem de nao lidos e hierarquia de secoes mais proxima da home
- Atividades ganhou hero de abertura na lista e no detalhe, com CTA em pilula e composicao mais proxima do destaque da home
- Nenhuma query, service, navigator ou `ShellTabBar` foi alterado

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, `tasks/slices/022-linguagem-visual-print-telas-mobile.md` e handoff `TASK-124`
- Contexto sob demanda carregado: print `home-responsavel-referencia`, `CODE_STYLE.md`, `COMPONENT_REUSE.md`, home components, telas `ResponsavelHome`, `ResponsavelProfile`, `ResponsavelNotifications`, `TrailToday`, `TrailActivity` e estilos locais
- Fonte ausente registrada: `mobile/docs/ai/ACCESSIBILITY.md` nao existe; mantidas as praticas ja adotadas de labels, live regions e ocultacao de icones decorativos

## Handoff

- `.agents/state/handoffs/TASK-128.md`
- Decisoes preservadas: logout do responsavel fica no perfil; composicao hero laranja passa a ser o reforco visual padrao para telas internas ligadas a home
- Proximo contexto recomendado: `mobile/src/features/shell/screens/` e `mobile/src/features/trail/screens/` para futuros refinos da experiencia do responsavel

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `tasks/change-requests/128-refinar-telas-responsavel-mobile-com-home.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-128.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar visual em dispositivo fisico/Expo Go para calibrar espacamento dos novos blocos hero

## Status final

done
