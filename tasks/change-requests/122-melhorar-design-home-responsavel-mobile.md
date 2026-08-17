# Task 122 - Melhorar design da home do responsavel no mobile

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

artefato de design system (documental; sem prints para esta tela)

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- Area do responsavel calma, objetiva e informativa, com menos ornamentacao
- Tokens existentes de `mobile/src/shared/theme/tokens.ts` (bege fundo, laranja principal, azul informacao)
- Sem gamificacao (medalhas, pontos, confetes)

## Objetivo

Elevar a qualidade visual da home do responsavel (`ResponsavelHomeScreen`), que hoje e uma pilha de textos e cards genericos, para uma composicao mais acolhedora e organizada: cabecalho de saudacao com identidade, atalho de avisos com badge de nao lidos, card de destaque da trilha do dia com icone e CTA, e estados (carregando, acesso limitado) integrados ao layout.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/122-melhorar-design-home-responsavel-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/ACCESSIBILITY.md` (se existir; senao checklist do DS)
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/shared/theme/tokens.ts`
- `mobile/src/shared/components/` (AppText, Button, Screen)

## Orcamento de contexto

- ~12 fontes
- estrategia de reducao: alterar apenas a home do responsavel e componentes novos locais da feature shell; nao tocar Trilha, Perfil, Avisos, auth nem backend

## Criterios de aceite

- Cabecalho de saudacao com avatar (inicial do nome), "Ola, {nome}" e atalho de avisos com badge numerico de nao lidos no topo
- Card de destaque "Trilha do dia" com pastilha de icone (`Route`), texto contextual com o nome da crianca quando disponivel e CTA "Ver trilha"
- Card "Avisos" pressable com icone (`Bell`), contagem de nao lidos e affordance de navegacao (chevron)
- Card de "Acesso limitado" com tom de aviso suave (amarelo/laranja em fundo calmo), exibido apenas quando `subscriptionAccessGranted === false`
- Estado de carregamento integrado (skeleton simples ou indicador dentro do layout, sem "pular" a tela)
- Botao "Sair" discreto no rodape (ghost), mantido funcional
- Icones exclusivamente via `lucide-react-native`, decorativos marcados como ocultos para acessibilidade
- Estilos em `styles.ts` locais com `createStyles` e tokens; nenhum `StyleSheet.create` inline no componente
- Componentizacao por responsabilidade: header e cards de acao extraidos para `mobile/src/features/shell/components/`
- Alvos de toque com minimo de 44px; labels e roles de acessibilidade preservados/melhorados
- Sem novas dependencias

## Fora de escopo

- Telas Trilha, Perfil e Avisos
- Backend e contrato OpenAPI
- Push notifications
- Home do master
- Pacote de fonte Nunito (desvio ja documentado)

## Dependencias

- Task 024 (home/perfil/notificacoes do responsavel)
- Task 095 (Lucide como padrao de icones mobile)

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Home do responsavel recomposta com cabecalho de identidade: avatar circular com inicial do nome (tint rosa do DS), saudacao "Ola, {nome}" com eyebrow "Bem-vindo de volta" e atalho circular de avisos com sino e badge de nao lidos
- Novo componente `HomeActionCard` (pastilha de icone com tint suave, titulo, badge opcional, descricao, chevron quando pressable e slot para CTA) usado nos tres cards da tela
- Card "Trilha do dia" com icone `Route` em tint laranja e CTA primario "Ver trilha"
- Card "Avisos" pressable com icone `Bell` em tint azul, contagem de nao lidos e chevron de navegacao
- Card "Acesso limitado" com icone `AlertCircle` em tint coral (atencao com cuidado, conforme DS), exibido apenas quando a assinatura nao libera acesso
- Estado de carregamento integrado ao layout (indicador + texto "Carregando seu dia...")
- Botao "Sair" ghost movido para o rodape da tela (`marginTop: auto`)
- Tokens de tint suave adicionados ao tema (`orangeSoft`, `pinkSoft`, `blueSoft`, `yellowSoft`, `coralSoft`)

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/010-app-responsavel-home-notificacoes.md`
- Contexto sob demanda carregado: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`, `ResponsavelHomeScreen.tsx`, `styles.ts` da shell, `ResponsavelShellNavigator.tsx`, `tokens.ts`, shared components (AppText/Button/Screen/ShellTabBar) e hooks de perfil/notificacoes
- Fontes evitadas: `requirements/`, `contracts/openapi.yaml`, stacks web/backend, telas Trilha/Perfil/Avisos
- `mobile/docs/ai/ACCESSIBILITY.md` nao existe na stack; usado o checklist de acessibilidade do DS mobile (secao 7)

## Handoff

- `.agents/state/handoffs/TASK-122.md`
- Decisoes preservadas: cards da home compostos via `HomeActionCard`; tints suaves como tokens compartilhados; "Sair" no rodape; sino do header e a via principal para avisos, card mantem redundancia acessivel
- Proximo contexto recomendado: `mobile/src/features/shell/components/` se houver novo refino da home ou reuso dos cards na home do master

## Arquivos alterados

- `mobile/src/shared/theme/tokens.ts` (tints suaves)
- `mobile/src/features/shell/components/HomeHeader/index.tsx` (novo)
- `mobile/src/features/shell/components/HomeHeader/styles.ts` (novo)
- `mobile/src/features/shell/components/HomeActionCard/index.tsx` (novo)
- `mobile/src/features/shell/components/HomeActionCard/styles.ts` (novo)
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts` (`feedbackRow`, `footer`)
- `mobile/src/shared/components/ShellTabBar/index.tsx` (correcao de lint pre-existente `react-hooks/refs`, fora do escopo visual mas necessaria para a validacao passar)
- `tasks/change-requests/122-melhorar-design-home-responsavel-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-122.md`

## Validacoes executadas

- `npm run lint` - ok (apos correcao do erro pre-existente no ShellTabBar)
- `npm run typecheck` - ok
- `npm run test` - ok (9 suites, 19 testes)

## Aderencia ao design system

- Area do responsavel calma: fundo bege, cards brancos com respiro, sem gamificacao
- Cores por papel do DS: laranja (acao/trilha), azul (informacao/avisos), coral (atencao com cuidado), rosa (acolhimento/avatar)
- Alvos de toque >= 44px (sino 48px, pastilhas 44px, cards inteiros pressables)
- Acessibilidade: `accessibilityRole="button"` e labels com contagem de nao lidos; icones decorativos ocultos de leitores de tela
- Desvio ja documentado: tipografia Nunito segue sem pacote de fonte (fonte do sistema)

## Pendencias pos-task

- Avaliar reuso do `HomeActionCard` na home do master (CR futuro, se desejado)
- Validar visual em dispositivo fisico/Expo Go

## Status final

done
