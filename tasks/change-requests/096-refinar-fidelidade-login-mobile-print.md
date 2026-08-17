# Task 096 - Refinar fidelidade visual do login mobile ao print

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

- nao se aplica; refino visual da tela de login mobile sem mudanca de integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas + assets locais

### Fonte primaria visual

- `design-system/mobile/prints/login-mobile.png` (governa composicao, hierarquia, decoracoes, form e ausencia de cadastro)
- `mobile/assets/girl.png`
- `mobile/assets/nuvem_evolente_mobile_svg.svg`
- `mobile/assets/logo-completa.webp`

### Telas e estados cobertos pelo print

- Login: hero (logo, saudacao, menina), separador nuvem, campos e-mail/senha, CTA Entrar, link recuperar senha, shapes decorativos
- Nao cobre: estados de loading/erro de submit, recovery/reset, teclado aberto

### Lacunas do print

- Sem estados de erro/loading — manter comportamento atual
- Bloco "Ainda nao tem conta? / Criar conta" aparece no print — **remover** conforme pedido do usuario

### Regra de aderencia visual

- alta fidelidade ao print; unica exclusao deliberada e o CTA de cadastro

## Origem da solicitacao

Usuario reenviou o print e pediu login igual a imagem, sem opcao de cadastro, com assets `girl.png`, `nuvem_evolente_mobile_svg.svg` e `logo-completa.webp`. Continuidade da Task 094 + Lucide (095) para usar a nuvem SVG real.

## Objetivo

Elevar a fidelidade do login mobile ao print oficial, usando a nuvem SVG real (agora viavel com `react-native-svg`) e removendo qualquer residuo de cadastro.

## Escopo

- Copiar/consolidar print em `design-system/mobile/prints/login-mobile.png`
- Renderizar nuvem a partir do path do asset SVG (via `react-native-svg`)
- Ajustar hierarquia: logo, "Bem-vindo(a)! 👋", copy, menina sobre a nuvem
- Refinar shapes decorativos top/bottom e form (inputs, botao, link)
- Confirmar ausencia de CTA de cadastro
- Validar lint/typecheck/test

## Fora de escopo

- Cadastro de conta
- Recovery/reset alem do link ja existente
- Instalar fontes (Nunito) sem autorizacao dedicada
- Backend / contrato / web

## Dependencias

- Task 094 — done
- Task 095 — done (`react-native-svg` + Lucide)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-095.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Fidelidade visual | `design-system/mobile/prints/login-mobile.png` | layout | sim |
| Assets | `mobile/assets/girl.png`, `nuvem_evolente_mobile_svg.svg`, `logo-completa.webp` | hero/nuvem | sim |
| Implementacao | `mobile/src/features/auth/screens/SignInScreen.tsx` e estilos/form relacionados | refino | sim |

## Orçamento de contexto

- Risco: baixo
- Estrategia: nao reabrir recovery, openapi, front-end

## Criterios de conclusao

- [x] print oficial versionado em `design-system/mobile/prints/login-mobile.png`
- [x] nuvem renderizada a partir do SVG (nao apenas circulos View)
- [x] layout alinhado ao print sem CTA de cadastro
- [x] Lucide permanece nos icones de campo
- [x] lint/typecheck/test ok

## Instrucoes de implementacao

1. Usar `react-native-svg` com os paths do asset `nuvem_evolente_mobile_svg.svg`
2. Posicionar a menina sobrepondo a borda superior da nuvem
3. Titulo com emoji de aceno; copy em um unico bloco
4. Formulario e superficie da nuvem com fill `#FFF9F1`
5. Nao reintroduzir cadastro

## Validacao esperada

- `cd mobile && npm run lint`
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Entregaveis esperados

- Login mobile mais fiel + handoff TASK-096

## Resultado da execucao

### Resumo por stack

- **mobile**: login refinado com nuvem SVG real (`SignInCloud`), hierarquia do print (logo, saudacao com emoji, copy unica, menina sobre a nuvem), form arredondado com Lucide, sem CTA de cadastro; print versionado em `design-system/mobile/prints/login-mobile.png`.

### Relação com o slice

- Slice 002 permanece done; CR adicional de fidelidade visual mobile.

### Decisões técnicas

- Paths do SVG embutidos em `SignInCloud` (source of truth = asset local) via `react-native-svg`.
- Cadastro ausente de proposito (excecao ao print).
- Tipografia Nunito nao instalada (dependencia nao autorizada nesta task).
- Estilos compartilhados de recovery/reset preservados no mesmo `styles.ts`.

### Trade-offs

- Shapes decorativos continuam aproximados com Views nativas (print nao entrega assets individuais dos confetes).

## Contexto utilizado

### Contexto mínimo

- AGENTS, GUIDE, context-map, index, esta task, slice 002, handoff 095

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| print login-mobile | fidelidade | composicao |
| assets girl/nuvem/logo | hero | montagem visual |
| SignInScreen + form styles | implementacao | refino |

### Evitado

- openapi, backend, front-end, recovery UI ampla

## Handoff

- Caminho: `.agents/state/handoffs/TASK-096.md`

## Arquivos alterados

- `design-system/mobile/prints/login-mobile.png`
- `mobile/src/features/auth/components/SignInCloud.tsx`
- `mobile/src/features/auth/components/SignInCloud.styles.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/styles.ts`
- `tasks/change-requests/096-refinar-fidelidade-login-mobile-print.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-096.md`

## Validacoes executadas

- lint ok
- typecheck ok
- test ok

## Pendencias pos-task

- Nenhuma obrigatoria; se tipografia Nunito for exigida, abrir CR dedicada de fonte

## Status final

done
